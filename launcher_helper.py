#!/usr/bin/env python3
"""GraphPlot V4.4.5 Windows launcher helper.

Goals
-----
* Start the same Python interpreter that successfully ran this helper.
* Reuse an already-running V4.4.3 server instead of starting a duplicate.
* Detect an older/stale GraphPlot process that owns port 8800.
* Ask before stopping a stale GraphPlot process.
* Never force-kill an unknown/non-GraphPlot process.
* Keep Stable / Hidden / Debug launch behavior consistent.
"""
from __future__ import annotations

import argparse
import ctypes
import json
import ipaddress
import os
import re
import socket
import subprocess
import sys
import time
import urllib.request
import webbrowser
from pathlib import Path
from typing import Any

APP_FILENAME = "Graphplot_webserv_v4_4_5.py"
EXPECTED_VERSION = "V4.4.5.2026"
APP_TITLE_PREFIX = "CSV Data Plotter"
DEFAULT_PORT = 8800
LOG_FILENAME = "GraphPlot_launcher.log"


def root_dir() -> Path:
    return Path(__file__).resolve().parent


def log_line(message: str) -> None:
    try:
        with (root_dir() / LOG_FILENAME).open("a", encoding="utf-8") as log:
            log.write(time.strftime("%Y-%m-%d %H:%M:%S ") + message.rstrip() + "\n")
    except Exception:
        pass


def health_url(port: int) -> str:
    return f"http://127.0.0.1:{port}/api/health"


def get_lan_ip() -> str:
    """Return the most useful non-loopback IPv4 address for LAN browsing."""
    candidates: list[str] = []

    # First ask the OS routing table which local address it would use for a
    # normal outbound IPv4 connection. No packet needs to be sent.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("8.8.8.8", 80))
        candidates.append(sock.getsockname()[0])
    except Exception:
        pass
    finally:
        sock.close()

    # Add addresses registered for the computer name as fallbacks.
    try:
        candidates.extend(socket.gethostbyname_ex(socket.gethostname())[2])
    except Exception:
        pass
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET, socket.SOCK_STREAM):
            candidates.append(info[4][0])
    except Exception:
        pass

    unique: list[str] = []
    for value in candidates:
        value = str(value or "").strip()
        if value and value not in unique and not value.startswith("127.") and not value.startswith("169.254."):
            unique.append(value)

    # Prefer RFC1918/private addresses over VPN/public-style adapter addresses.
    for value in unique:
        try:
            if ipaddress.ip_address(value).is_private:
                return value
        except ValueError:
            continue
    return unique[0] if unique else "127.0.0.1"


def browser_url(port: int, lan: bool = False) -> str:
    if lan:
        lan_ip = get_lan_ip()
        if lan_ip != "127.0.0.1":
            return f"http://{lan_ip}:{port}/"
    return f"http://127.0.0.1:{port}/"


def get_health(port: int, timeout: float = 1.2) -> dict[str, Any] | None:
    """Return a GraphPlot V4 health payload.

    The launcher intentionally does NOT require an exact APP_TITLE match. The Web UI
    title is presentation text and may be expanded (for example
    "CSV Data Plotter · Data Evaluation · Cycle Analysis") without changing the
    server identity. Older launcher versions rejected that perfectly healthy
    response and eventually killed the server after the startup timeout.
    """
    try:
        req = urllib.request.Request(health_url(port), headers={"Cache-Control": "no-cache"})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if int(getattr(response, "status", 200)) != 200:
                return None
            payload = json.loads(response.read().decode("utf-8", errors="replace"))

        ok = payload.get("ok") is True
        app_name = str(payload.get("app") or "").strip()
        version = str(payload.get("version") or "").strip().upper()

        # Identify GraphPlot by a stable product prefix + V4 version rather than
        # by the full display title. This remains strict enough not to accept an
        # unrelated service that merely happens to expose /api/health.
        if ok and app_name.startswith(APP_TITLE_PREFIX) and version.startswith("V4."):
            return payload
    except Exception:
        pass
    return None


def port_is_open(port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)
    try:
        return sock.connect_ex(("127.0.0.1", port)) == 0
    finally:
        sock.close()


def wait_for_health(port: int, process: subprocess.Popen | None = None, timeout: float = 15.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        health = get_health(port)
        if health:
            return health
        if process is not None and process.poll() is not None:
            return None
        time.sleep(0.2)
    return None


def wait_for_startup_health(port: int, process: subprocess.Popen, *, hidden: bool = False):
    """Wait robustly for a newly spawned server.

    Matplotlib can build its font cache on the first launch on a PC/profile.
    That initialization may take well beyond the old 15-second timeout while
    the Python process is still healthy.  Use a short first wait, then an
    extended grace period only when the child process is still alive.
    """
    health = wait_for_health(port, process, timeout=15.0)
    if health:
        return health

    if process.poll() is not None:
        return None

    message = (
        "GraphPlot is still initializing. First launch may take longer while "
        "Matplotlib prepares its font cache. Waiting up to 105 seconds more..."
    )
    log_line(message)
    if not hidden:
        print(message)

    return wait_for_health(port, process, timeout=105.0)


def stop_spawned_process(process: subprocess.Popen) -> None:
    """Best-effort cleanup for a child that never became healthy."""
    if process.poll() is not None:
        return
    try:
        process.terminate()
        process.wait(timeout=4.0)
        return
    except Exception:
        pass
    try:
        process.kill()
        process.wait(timeout=2.0)
    except Exception:
        pass


def wait_for_port_release(port: int, timeout: float = 8.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if not port_is_open(port):
            return True
        time.sleep(0.2)
    return not port_is_open(port)


def post_shutdown(port: int) -> bool:
    try:
        req = urllib.request.Request(
            f"http://127.0.0.1:{port}/api/shutdown",
            method="POST",
            data=b"",
            headers={"Content-Type": "text/plain"},
        )
        with urllib.request.urlopen(req, timeout=1.8) as response:
            payload = json.loads(response.read().decode("utf-8", errors="replace"))
        return bool(payload.get("ok"))
    except Exception:
        return False


def open_browser(port: int, lan: bool = False) -> None:
    try:
        webbrowser.open(browser_url(port, lan=lan), new=2)
    except Exception:
        pass


def no_window_flags() -> int:
    if os.name != "nt":
        return 0
    return int(getattr(subprocess, "CREATE_NO_WINDOW", 0))


def hidden_server_flags() -> int:
    if os.name != "nt":
        return 0
    return int(getattr(subprocess, "CREATE_NO_WINDOW", 0)) | int(
        getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
    )


def run_quiet(command: list[str], timeout: float = 8.0) -> subprocess.CompletedProcess:
    kwargs: dict[str, Any] = {
        "capture_output": True,
        "text": True,
        "encoding": "utf-8",
        "errors": "replace",
        "timeout": timeout,
    }
    if os.name == "nt":
        kwargs["creationflags"] = no_window_flags()
    return subprocess.run(command, **kwargs)


def listening_bind_hosts_windows(port: int) -> list[str]:
    """Return local bind hosts for LISTENING TCP sockets on a Windows port."""
    if os.name != "nt":
        return []
    try:
        result = run_quiet(["netstat", "-ano", "-p", "TCP"], timeout=5.0)
    except Exception:
        return []

    hosts: list[str] = []
    for raw in (result.stdout or "").splitlines():
        line = raw.strip()
        if not line.upper().startswith("TCP"):
            continue
        parts = line.split()
        if len(parts) < 5 or parts[-2].upper() != "LISTENING":
            continue
        local = parts[1]
        if local.startswith("["):
            # IPv6 form: [::]:8800
            idx = local.rfind("]:")
            if idx < 0:
                continue
            host, ptext = local[1:idx], local[idx + 2:]
        else:
            if ":" not in local:
                continue
            host, ptext = local.rsplit(":", 1)
        if ptext != str(port):
            continue
        host = host.strip().strip("[]")
        if host not in hosts:
            hosts.append(host)
    return hosts


def port_is_lan_bound(port: int) -> bool:
    """True when the listener accepts non-loopback connections."""
    if os.name != "nt":
        # The application itself binds 0.0.0.0 whenever --lan is supplied.
        return True
    hosts = listening_bind_hosts_windows(port)
    if not hosts:
        return False
    loopback_only = {"127.0.0.1", "::1", "localhost"}
    return any(host not in loopback_only for host in hosts)


# -----------------------------------------------------------------------------
# Windows port/process inspection
# -----------------------------------------------------------------------------
def _endpoint_port(endpoint: str) -> str:
    endpoint = endpoint.strip()
    if ":" not in endpoint:
        return ""
    return endpoint.rsplit(":", 1)[-1].strip()


def find_listening_pids_windows(port: int) -> list[int]:
    """Find Windows PIDs in LISTENING state for the requested TCP port."""
    try:
        result = run_quiet(["netstat", "-ano", "-p", "TCP"], timeout=5.0)
    except Exception:
        return []

    pids: set[int] = set()
    for raw in (result.stdout or "").splitlines():
        line = raw.strip()
        if not line.upper().startswith("TCP"):
            continue
        parts = line.split()
        if len(parts) < 5:
            continue
        # Normal Windows format: TCP <local> <foreign> LISTENING <pid>
        local = parts[1]
        state = parts[-2].upper()
        pid_text = parts[-1]
        if _endpoint_port(local) != str(port):
            continue
        if state != "LISTENING" or not pid_text.isdigit():
            continue
        pid = int(pid_text)
        if pid > 4:
            pids.add(pid)
    return sorted(pids)


def find_listening_pids(port: int) -> list[int]:
    if os.name == "nt":
        return find_listening_pids_windows(port)
    # Launcher ownership remediation is specifically for Windows. On other
    # platforms we still detect the open port, but do not guess a PID to kill.
    return []


def get_process_info_windows(pid: int) -> dict[str, Any]:
    """Read process name/path/command line through Win32_Process (PowerShell/CIM)."""
    ps = (
        f"$p=Get-CimInstance Win32_Process -Filter \"ProcessId={int(pid)}\" "
        "-ErrorAction SilentlyContinue; "
        "if($null -ne $p){"
        "[PSCustomObject]@{ProcessId=$p.ProcessId;Name=$p.Name;"
        "ExecutablePath=$p.ExecutablePath;CommandLine=$p.CommandLine}"
        "| ConvertTo-Json -Compress}"
    )
    try:
        result = run_quiet(
            [
                "powershell.exe",
                "-NoProfile",
                "-NonInteractive",
                "-ExecutionPolicy",
                "Bypass",
                "-Command",
                ps,
            ],
            timeout=6.0,
        )
        text = (result.stdout or "").strip()
        if text:
            data = json.loads(text)
            return {
                "pid": int(data.get("ProcessId") or pid),
                "name": str(data.get("Name") or ""),
                "executable": str(data.get("ExecutablePath") or ""),
                "command_line": str(data.get("CommandLine") or ""),
            }
    except Exception:
        pass

    # Fallback: tasklist can at least identify the executable name, although it
    # cannot safely prove that a python.exe belongs to GraphPlot.
    try:
        result = run_quiet(
            ["tasklist", "/FI", f"PID eq {int(pid)}", "/FO", "CSV", "/NH"],
            timeout=4.0,
        )
        line = (result.stdout or "").strip().splitlines()
        if line and not line[0].lower().startswith("info:"):
            import csv
            import io

            row = next(csv.reader(io.StringIO(line[0])))
            if len(row) >= 2:
                return {
                    "pid": int(pid),
                    "name": row[0],
                    "executable": "",
                    "command_line": "",
                }
    except Exception:
        pass

    return {"pid": int(pid), "name": "", "executable": "", "command_line": ""}


def get_process_info(pid: int) -> dict[str, Any]:
    if os.name == "nt":
        return get_process_info_windows(pid)
    return {"pid": int(pid), "name": "", "executable": "", "command_line": ""}


def extract_graphplot_version(command_line: str) -> str:
    m = re.search(r"graphplot[^\s\"]*web_(v4(?:[_\.]\d+)+)\.py", command_line, flags=re.I)
    if not m:
        m = re.search(r"(v4(?:[_\.]\d+)+)", command_line, flags=re.I)
    if not m:
        return "unknown"
    return m.group(1).replace("_", ".").upper()


def is_graphplot_server_process(info: dict[str, Any]) -> bool:
    cmd = str(info.get("command_line") or "").lower()
    if not cmd:
        return False
    # Deliberately strict: only a Python command line that names the GraphPlot
    # WebServer script is eligible for forced termination.
    return (
        "graphplot_nisobc_web_v4" in cmd
        or "graphplot-nisobc-web-v4" in cmd
        or bool(re.search(r"graphplot[^\s\"]*web[_-]?v4", cmd, flags=re.I))
    )


def process_summary(info: dict[str, Any]) -> str:
    pid = int(info.get("pid") or 0)
    name = str(info.get("name") or "unknown")
    cmd = str(info.get("command_line") or "").strip()
    ver = extract_graphplot_version(cmd) if cmd else "unknown"
    if len(cmd) > 220:
        cmd = cmd[:217] + "..."
    lines = [f"PID {pid} | {name} | {ver}"]
    if cmd:
        lines.append(f"  {cmd}")
    return "\n".join(lines)


def listener_processes(port: int) -> list[dict[str, Any]]:
    return [get_process_info(pid) for pid in find_listening_pids(port)]


def terminate_pid_windows(pid: int) -> bool:
    if os.name != "nt" or int(pid) <= 4:
        return False
    try:
        result = run_quiet(["taskkill", "/PID", str(int(pid)), "/T", "/F"], timeout=8.0)
        return result.returncode == 0
    except Exception:
        return False


# -----------------------------------------------------------------------------
# User interaction
# -----------------------------------------------------------------------------
def message_box(text: str, title: str, flags: int) -> int:
    if os.name != "nt":
        return 0
    try:
        return int(ctypes.windll.user32.MessageBoxW(None, text, title, flags))
    except Exception:
        return 0


def ask_yes_no(message: str, hidden: bool = False) -> bool:
    log_line("PROMPT: " + message.replace("\n", " | "))
    if hidden and os.name == "nt":
        # MB_YESNO | MB_ICONWARNING | MB_SETFOREGROUND
        result = message_box(message, "GraphPlot launcher", 0x00000004 | 0x00000030 | 0x00010000)
        return result == 6  # IDYES
    try:
        answer = input(message.rstrip() + "\nContinue? [Y/N]: ").strip().lower()
        return answer in {"y", "yes"}
    except (EOFError, KeyboardInterrupt):
        return False


def show_error(message: str, hidden: bool = False) -> None:
    log_line("ERROR: " + message.replace("\n", " | "))
    if hidden and os.name == "nt":
        # MB_OK | MB_ICONERROR | MB_SETFOREGROUND
        message_box(message, "GraphPlot launcher", 0x00000000 | 0x00000010 | 0x00010000)
    else:
        print(message)


def show_info(message: str, hidden: bool = False) -> None:
    log_line("INFO: " + message.replace("\n", " | "))
    if hidden and os.name == "nt":
        message_box(message, "GraphPlot launcher", 0x00000000 | 0x00000040 | 0x00010000)
    else:
        print(message)


# -----------------------------------------------------------------------------
# Stale-server handling
# -----------------------------------------------------------------------------
def stop_recognized_listener_processes(port: int, hidden: bool = False, ask: bool = True) -> bool:
    infos = listener_processes(port)
    if not infos:
        show_error(
            f"Port {port} is in use, but the launcher could not identify its owner.\n"
            "No process was stopped. Use Launcher\\Debug\\Check_Port_8800.bat to inspect it.",
            hidden,
        )
        return False

    recognized = [info for info in infos if is_graphplot_server_process(info)]
    unknown = [info for info in infos if not is_graphplot_server_process(info)]

    if unknown:
        details = "\n\n".join(process_summary(info) for info in infos)
        show_error(
            f"Port {port} is occupied, and at least one listener cannot be proven to be GraphPlot.\n"
            "For safety, V4.4.3.1 will NOT kill it automatically.\n\n"
            f"Detected listener(s):\n{details}\n\n"
            "Close the application manually or choose another port.",
            hidden,
        )
        return False

    if not recognized:
        show_error(f"Port {port} is occupied by an unknown process. Nothing was stopped.", hidden)
        return False

    details = "\n\n".join(process_summary(info) for info in recognized)
    prompt = (
        f"An older/stale GraphPlot server is holding port {port}:\n\n{details}\n\n"
        f"Stop this GraphPlot process and start {EXPECTED_VERSION}?"
    )
    if ask and not ask_yes_no(prompt, hidden=hidden):
        show_info("Startup cancelled. The existing process was left untouched.", hidden)
        return False

    all_ok = True
    for info in recognized:
        pid = int(info.get("pid") or 0)
        if not terminate_pid_windows(pid):
            all_ok = False
            log_line(f"Failed to taskkill GraphPlot PID {pid}")
        else:
            log_line(f"Killed stale GraphPlot PID {pid}")

    if not all_ok or not wait_for_port_release(port, timeout=8.0):
        show_error(
            f"The stale GraphPlot process could not be stopped completely. Port {port} is still in use.",
            hidden,
        )
        return False
    return True


def replace_older_health_server(port: int, health: dict[str, Any], hidden: bool = False) -> bool:
    version = str(health.get("version") or "unknown")
    if version == EXPECTED_VERSION:
        return True

    prompt = (
        f"GraphPlot {version} is already running on port {port}.\n\n"
        f"Stop the older server cleanly and start {EXPECTED_VERSION}?"
    )
    if not ask_yes_no(prompt, hidden=hidden):
        show_info("Startup cancelled. The existing GraphPlot server was left running.", hidden)
        return False

    log_line(f"Requesting clean shutdown of older healthy GraphPlot {version}")
    if post_shutdown(port) and wait_for_port_release(port, timeout=8.0):
        return True

    # If a healthy older server did not exit cleanly, fall back to the same strict
    # PID validation used for pre-V4.2.4 stale processes.
    log_line("Clean shutdown did not release the port; trying recognized-PID fallback")
    return stop_recognized_listener_processes(port, hidden=hidden, ask=False)


def prepare_port_for_start(port: int, hidden: bool = False, lan: bool = False) -> str:
    """Return 'reuse', 'ready', or 'abort'."""
    health = get_health(port)
    if health:
        version = str(health.get("version") or "unknown")
        if version == EXPECTED_VERSION:
            if lan and not port_is_lan_bound(port):
                prompt = (
                    f"{EXPECTED_VERSION} is already running in Local-only mode on port {port}.\n\n"
                    "LAN mode requires the server to restart and bind to all network adapters. "
                    "The current browser session/data will be cleared.\n\nRestart GraphPlot in LAN mode?"
                )
                if not ask_yes_no(prompt, hidden=hidden):
                    return "abort"
                if post_shutdown(port) and wait_for_port_release(port, timeout=8.0):
                    return "ready"
                return "ready" if stop_recognized_listener_processes(port, hidden=hidden, ask=False) else "abort"
            return "reuse"
        return "ready" if replace_older_health_server(port, health, hidden=hidden) else "abort"

    if not port_is_open(port):
        return "ready"

    # A just-starting current server may open the socket a moment before /api/health
    # is ready. Give it a short grace period before treating the port as stale.
    health = wait_for_health(port, timeout=3.0)
    if health:
        version = str(health.get("version") or "unknown")
        if version == EXPECTED_VERSION:
            if lan and not port_is_lan_bound(port):
                prompt = (
                    f"{EXPECTED_VERSION} is already running in Local-only mode on port {port}.\n\n"
                    "LAN mode requires the server to restart and bind to all network adapters. "
                    "The current browser session/data will be cleared.\n\nRestart GraphPlot in LAN mode?"
                )
                if not ask_yes_no(prompt, hidden=hidden):
                    return "abort"
                if post_shutdown(port) and wait_for_port_release(port, timeout=8.0):
                    return "ready"
                return "ready" if stop_recognized_listener_processes(port, hidden=hidden, ask=False) else "abort"
            return "reuse"
        return "ready" if replace_older_health_server(port, health, hidden=hidden) else "abort"

    return "ready" if stop_recognized_listener_processes(port, hidden=hidden, ask=True) else "abort"


# -----------------------------------------------------------------------------
# Start/stop/inspect commands
# -----------------------------------------------------------------------------
def inspect_port(port: int) -> int:
    print(f"GraphPlot V4.4.3.2 - Port inspection ({port})")
    print("=" * 72)
    health = get_health(port)
    if health:
        print(f"Health endpoint : GraphPlot {health.get('version', 'unknown')}")
        print(f"Active clients  : {health.get('active_clients', 'unknown')}")
    else:
        print("Health endpoint : No GraphPlot /api/health response")

    print(f"TCP port open   : {'YES' if port_is_open(port) else 'NO'}")
    infos = listener_processes(port)
    if infos:
        print("\nListening process(es):")
        for info in infos:
            kind = "GraphPlot" if is_graphplot_server_process(info) else "UNKNOWN / protected"
            print(f"\n[{kind}]\n{process_summary(info)}")
    elif port_is_open(port):
        print("\nThe port is open, but process ownership could not be resolved.")
    else:
        print("\nPort is free.")
    return 0


def stop_server(port: int, hidden: bool = False) -> int:
    health = get_health(port)
    if health:
        version = str(health.get("version") or "unknown")
        log_line(f"Stop requested for healthy GraphPlot {version}")
        if post_shutdown(port):
            if wait_for_port_release(port, timeout=8.0):
                show_info(f"GraphPlot {version} stopped and port {port} was released.", hidden)
                return 0
        # Clean shutdown failed: fall back only when PID is proven GraphPlot.
        if stop_recognized_listener_processes(port, hidden=hidden, ask=True):
            show_info(f"GraphPlot stopped and port {port} was released.", hidden)
            return 0
        return 2

    if not port_is_open(port):
        show_info(f"No server is listening on port {port}.", hidden)
        return 0

    if stop_recognized_listener_processes(port, hidden=hidden, ask=True):
        show_info(f"Stale GraphPlot server stopped and port {port} was released.", hidden)
        return 0
    return 2


def start_server(mode: str, lan: bool, port: int) -> int:
    hidden = mode == "hidden"
    app_path = root_dir() / APP_FILENAME
    if not app_path.exists():
        show_error(f"Cannot find application:\n{app_path}", hidden)
        return 2

    state = prepare_port_for_start(port, hidden=hidden, lan=lan)
    if state == "abort":
        return 3
    if state == "reuse":
        health = get_health(port) or {}
        show_info(
            f"{EXPECTED_VERSION} is already running on port {port}. Opening the existing server.",
            hidden=False if mode in {"stable", "debug"} else hidden,
        )
        open_browser(port, lan=lan)
        return 0

    cmd = [sys.executable, str(app_path), "--port", str(port), "--no-browser"]
    if lan:
        cmd.append("--lan")

    if mode == "hidden":
        cmd.append("--quiet")
        log_path = root_dir() / LOG_FILENAME
        with log_path.open("a", encoding="utf-8") as log:
            log.write(time.strftime("\n%Y-%m-%d %H:%M:%S ") + f"Starting hidden {EXPECTED_VERSION}\n")
            log.flush()
            proc = subprocess.Popen(
                cmd,
                cwd=str(root_dir()),
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=log,
                creationflags=hidden_server_flags(),
            )
            health = wait_for_startup_health(port, proc, hidden=True)
            if not health:
                log.write(
                    time.strftime("%Y-%m-%d %H:%M:%S ")
                    + f"Server failed to become healthy. Exit code={proc.poll()}\n"
                )
                stop_spawned_process(proc)
                show_error(
                    "GraphPlot failed to start after the extended startup wait. "
                    "See GraphPlot_launcher.log for details.",
                    hidden=True,
                )
                return 4
        open_browser(port, lan=lan)
        return 0

    if mode == "stable":
        print(f"Starting GraphPlot {EXPECTED_VERSION}...")
        print("Close all GraphPlot browser tabs to stop the server automatically.")
        print("This Stable window closes automatically after the server exits.")
        print("First launch can take 30-120 seconds if Matplotlib builds/refreshes its font cache.\n")
    else:
        print(f"Starting GraphPlot {EXPECTED_VERSION} in DEBUG mode...\n")

    log_line("Stable/debug command: " + " ".join(cmd))
    proc = subprocess.Popen(cmd, cwd=str(root_dir()))
    health = wait_for_startup_health(port, proc, hidden=False)
    if not health:
        code = proc.poll()
        if code is None:
            print("ERROR: Server process stayed alive but did not become ready within 120 seconds.")
            print("The launcher will stop that child process to avoid leaving a stale server behind.")
        else:
            print(f"ERROR: Server exited during startup. Exit code: {code}")
        stop_spawned_process(proc)
        return 4

    if lan and mode in {"stable", "debug"}:
        lan_ip = get_lan_ip()
        print(f"LAN URL: http://{lan_ip}:{port}/")
        print("Other PCs on the same network must use this LAN URL, not 127.0.0.1.")
        if lan_ip == "127.0.0.1":
            print("WARNING: A usable LAN IPv4 address could not be detected.")
        print()

    open_browser(port, lan=lan)
    try:
        return int(proc.wait() or 0)
    except KeyboardInterrupt:
        try:
            post_shutdown(port)
        except Exception:
            pass
        return 0


def lan_info(port: int) -> int:
    lan_ip = get_lan_ip()
    print(f"GraphPlot {EXPECTED_VERSION} - LAN diagnostics")
    print("=" * 72)
    print(f"Detected LAN IP : {lan_ip}")
    print(f"LAN URL         : http://{lan_ip}:{port}/")
    print(f"Local URL       : http://127.0.0.1:{port}/")
    print(f"Port open local : {'YES' if port_is_open(port) else 'NO'}")
    if os.name == "nt":
        hosts = listening_bind_hosts_windows(port)
        print(f"Bind address(es): {', '.join(hosts) if hosts else 'No listener detected'}")
        print(f"LAN-capable bind: {'YES' if port_is_lan_bound(port) else 'NO'}")
    health = get_health(port)
    print(f"GraphPlot health: {health.get('version') if health else 'No response'}")
    print()
    print("If LAN-capable bind is YES but another PC cannot connect, Windows Firewall")
    print("or the network profile is usually the next item to check.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="GraphPlot V4.4.5 launcher helper")
    parser.add_argument(
        "--mode",
        choices=["stable", "hidden", "debug", "stop", "stop-hidden", "inspect", "lan-info"],
        default="stable",
    )
    parser.add_argument("--lan", action="store_true")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()

    if args.mode == "inspect":
        return inspect_port(args.port)
    if args.mode == "lan-info":
        return lan_info(args.port)
    if args.mode == "stop":
        return stop_server(args.port, hidden=False)
    if args.mode == "stop-hidden":
        return stop_server(args.port, hidden=True)
    return start_server(args.mode, args.lan, args.port)


if __name__ == "__main__":
    raise SystemExit(main())
