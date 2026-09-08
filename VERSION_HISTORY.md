# SignalWorks Studio Version History

## Branding refresh — 2026-09-08

The V4.4.5 production baseline is now branded **SignalWorks Studio**. The application core, CSV binding logic, plotting behavior, Cycle Analysis and report workflow remain on the validated V4.4.5 code line.

- Product name changed to **SignalWorks Studio**.
- Main source renamed to `SignalWorks_Studio_webserv_v4_4_5.py`.
- Launcher helper renamed to `signalworks_studio_launcher.py`.
- Added a compact signal-wave brand mark to the Web UI header.
- Browser title, footer, launchers, installer, firewall rule and export defaults use the new brand.
- New presets export as `SignalWorksStudioPreset`.
- Legacy `GraphPlotSignalPreset` and `CSVDataPlotterPreset` V1 files remain import-compatible.
- Legacy GraphPlot V4 process detection is retained in the launcher for safe migration.

> This is a branding/package refresh of V4.4.5, not a new analysis-engine version. Historical entries below keep the names used by those releases.

---

> **Current V4.4.5 package configuration:** main source `SignalWorks_Studio_webserv_v4_4_5.py`, default Local/LAN port **8800**. Older port numbers appearing in historical entries describe the configuration used by those earlier releases.


## V4.4.5 — 2026-09-03

- Added multi-file CSV selection and confirmation workflow.
- Added initial ordering by browser-visible Last Modified time.
- Added drag-and-drop source-file reordering.
- Added server-side Bind Data with repeated metadata/header removal.
- Added CSV header/column compatibility validation.
- Added bind progress indicator.
- Added Load Bound CSV and Download Bound CSV actions.
- Loaded bound datasets use the existing plot/preset/analysis/report pipeline unchanged.



## V4.4.4 — 2026-09-02

- Added Cycle Analysis profile selector: Auto / Temp cycling / Thermal shock.
- Added dominant plateau detection for thermal-shock soak analysis.
- Auto detects fast thermal-shock transitions and rejects transient overshoot extrema.
- Slow temperature-cycling profiles retain the previous extrema-based method.
- Added observed-extrema, plateau-center, transition-time and transition-rate diagnostics.
- Extended Cycle Analysis CSV export with profile diagnostics.
- Retains Cursor A/B fix and corrected launcher health detection.

This document tracks the WebServer generation of the CSV Data Plotter, starting from the migration away from the Tkinter desktop GUI.

**Current recommended release:** `V4.4.3.1`

## V4.4.3.1 — 2026-09-01

### Fixed
- Fixed false `Server did not start. Exit code: None` from the Stable/Hidden launcher when Matplotlib needs more than 15 seconds to build its font cache.
- Added an extended startup grace period (15 s initial + up to 105 s additional while the child process remains alive).
- Failed startup now cleans up the spawned child process to prevent a stale Python server from being left behind.
- Improved launcher diagnostics for exited vs. still-running startup failures.


## Release summary

| Version | Date | Main focus | Key result |
|---|---|---|---|
| V4.0.0 | 2026-08-31 | Desktop GUI -> WebServer | Browser-based CSV plotting with the V3.5.2 plotting/report engine preserved |
| V4.1.0 | 2026-08-31 | Interactive graph | Offline Plotly preview with zoom, pan, hover and legend control |
| V4.2.0 | 2026-08-31 | Analysis + UI redesign | Minimal workspace plus Cursor A/B and range statistics |
| V4.2.1 | 2026-08-31 | Portable configuration | Manual signal colors and import/export `.preset` files |
| V4.2.2 | 2026-08-31 | UI refinement | Aligned toolbar and readable Data Series rows |
| V4.2.3 | 2026-08-31 | UI polish + hidden launch | Compact Primary/Secondary labels, semantic toolbar colors, hidden-launch concept |
| V4.2.3.1 | 2026-08-31 | Launcher hotfix | Replaced direct `pythonw.exe` dependency with the same `python` command used by Debug |
| V4.2.4 | 2026-08-31 | Server lifecycle | Browser heartbeat, auto-shutdown and Stable/Hidden/Debug launcher structure |
| V4.2.4.1 | 2026-08-31 | Stale-server recovery | Safe PID/process detection and guided cleanup of older GraphPlot servers on port 8000 |
| V4.3.0 | 2026-09-01 | Smart CSV + cycle analysis | Automatic header-row detection plus Tmin/Tmax cycle, soak and cycle-time analysis |
| V4.3.1 | 2026-09-01 | Theme + compact navigation | System/Light/Dark modes and dropdown-based Preset/Export/Theme toolbar |
| V4.3.1.1 | 2026-09-01 | Dropdown UI hotfix | Fixed Preset dropdown overflow and made header dropdowns mutually exclusive |
| V4.3.1.2 | 2026-09-01 | LAN access correction | LAN launch opens the detected LAN IPv4 address, detects Local-only server reuse, and adds firewall/LAN diagnostics |
| V4.4.0 | 2026-09-01 | Engineering annotations | Reference/Limit lines, tolerance bands, click-to-place comments, preset persistence and report export |
| V4.4.0.1 | 2026-09-01 | Annotation sidebar UI hotfix | Collapsible Data Series and compact Reference/Range creator panels |
| V4.4.1 | 2026-09-01 | Annotation workflow + drag editing | Persistent sidebar state, reliable scrolling, fixed comment modal, and draggable annotations |
| V4.4.2.1 | 2026-09-01 | Wide PDF correction + rich comments | Separate 1200 × 650 pt report pages, multiline comments, arrow toggle, border/box sizing controls |
| V4.4.3 | 2026-09-01 | Export workflow | Select report pages, custom filenames/preset names, browser Save As support |
| V4.4.3.1 | 2026-09-01 | Launcher startup hotfix | Adaptive startup wait and orphan-process cleanup for slow first launch |

---

## V4.4.3 — 2026-09-01

### Added
- Added a report-page selection dialog before PDF Wide, PDF A4 and Word exports.
- Users can tick only the Plot Tabs/pages required instead of always exporting all eight pages.
- Added user-defined file names before PDF, Word, PNG, Cycle Analysis CSV and `.preset` exports.
- Added user-defined **Preset name** stored inside exported `.preset` files.
- Added browser-native Save As support through the File System Access API when available.
- Added standard browser-download fallback for environments where native folder selection is unavailable.

### Changed
- `/report/pdf`, `/report/pdf-a4` and `/report/word` now accept selected tab IDs through the `tabs` query parameter.
- Plot PNG and Cycle Analysis CSV use the common Save / Export dialog.
- Preset export accepts a custom preset display name.

### Compatibility note
- Browser JavaScript cannot force an arbitrary local save path on insecure HTTP LAN pages. On compatible secure Chromium contexts, the native Save As picker provides folder selection. LAN HTTP sessions fall back to the browser download mechanism; enable the browser's **Ask where to save** option for an explicit path prompt.


## V4.4.2.1 - Wide PDF page correction

### Fixed

- Corrected the V4.4.2 PDF interpretation: reports are again **separate pages**, not one vertically concatenated page.
- Added a custom wide report page size of **1200 x 650 pt**, larger than A4 landscape (approximately 842 x 595 pt).
- Preserved the exact custom page size by exporting without `bbox_inches="tight"`.
- Renamed the export menu item to `PDF wide report`.
- Kept `PDF A4 report` as a separate compatibility option.

### Preserved

- Multiline comments.
- Arrow on/off.
- Border/text/background styling.
- Comment box width/height and drag editing.

---

## V4.0.0 - First WebServer release

### Added

- Replaced the Tkinter desktop GUI with a local **FastAPI + Uvicorn** WebServer.
- Browser-based CSV upload and graph configuration.
- Browser navigation for all eight graph tabs/presets.
- Per-signal **Primary / Secondary Y-axis** assignment.
- Bulk assignment of checked signals to Primary or Secondary.
- Server-side Matplotlib rendering using the non-GUI `Agg` backend.
- Localhost-only default operation with optional `--lan` mode.
- Per-browser session data to reduce conflicts between clients.

### Preserved from V3.5.2

- High-contrast signal color palettes.
- Solid Primary traces and dashed Secondary traces.
- Separate compact legends for the two Y axes.
- PNG plot download.
- A4 landscape PDF report generation.
- A4 landscape Word report generation.

### Architecture

- Plot preview: server-rendered Matplotlib.
- Report/export engine: Matplotlib.
- External internet/CDN: not required.

---

## V4.1.0 - Interactive Plotly graph

### Added

- Replaced the static browser preview with an **interactive Plotly graph**.
- Mouse-wheel zoom.
- Box zoom and pan.
- Hover inspection showing timestamp and signal value.
- Click legend item to show/hide a signal.
- Double-click legend item to isolate a signal.
- Separate Primary and Secondary legend groups.
- `Reset View`, `Autoscale` and `Show All Signals` controls.
- WebGL traces for better responsiveness on larger CSV datasets.
- Plotly.js served locally by FastAPI, so LAN/offline use does not depend on a CDN.

### Preserved

- Matplotlib remained the export engine for PNG/PDF/Word to keep report formatting stable.

---

## V4.2.0 - Minimal UI and engineering analysis tools

### UI redesign

- Introduced a cleaner **Control Sidebar + Graph Workspace** layout.
- Reduced visual density in the top bar.
- Moved plot setup and signal selection into organized control panels.
- Increased the visual priority of the graph area.

### Added analysis functions

- **Cursor A** and **Cursor B** placement directly on the interactive graph.
- A-B highlighted analysis region.
- `Delta Time` for timestamp data or `Delta X` for numeric/index data.
- Per-signal Cursor A value.
- Per-signal Cursor B value.
- Per-signal Delta Value.
- Min / Max / Average / sample-count statistics.
- With both cursors set: statistics use the A-B interval.
- Without both cursors: statistics follow the current zoomed X range.
- Signals hidden through the Plotly legend are excluded from statistics.

---

## V4.2.1 - Manual colors and portable `.preset`

### Fixed

- Fixed the persistent **`Loading graph...`** placeholder/spinner.
- Explicitly clears the loading placeholder before Plotly rendering.
- Added an error state instead of leaving the spinner active forever.
- Made interactive graph height responsive to the browser viewport.

### Manual signal colors

- Added an individual color picker for each signal.
- Default mode remains **Auto color**.
- Manual color can be selected per signal.
- One-click `A` button restores Auto color.
- Manual color is shared by:
  - Interactive Plotly graph
  - PNG export
  - PDF report
  - Word report
  - Exported preset

### Portable preset system

- Added import/export of UTF-8 JSON configuration using the `.preset` extension.
- Presets contain configuration only; no CSV measurement data.
- Preset stores:
  - Tab/title configuration
  - X-axis label
  - Primary/Secondary labels, ranges and tick steps
  - Selected signal names
  - Primary/Secondary assignment
  - Manual color or Auto color state
- Presets can be imported before or after CSV upload.
- Signals are matched by exact CSV column/header name.
- Missing signals are skipped safely.
- Preset remains active for subsequent CSV loads in the same session.

### Normal Plot Mode

- If no preset is loaded, the application behaves as a generic CSV plotting tool and does not auto-select project signals.
- The previous Nissan defaults were separated into `Nissan_OBC_Default.preset`.

---

## V4.2.2 - Toolbar and Data Series readability

### Top toolbar

- Aligned Skip Rows, CSV picker, Load CSV, preset controls and report controls on one horizontal control plane on wide screens.
- Normalized input, file-picker and button heights.
- Added responsive wrapping for smaller browser widths.

### Data Series

- Increased desktop sidebar width.
- Reworked signal rows so the **signal name receives the largest available width**.
- Removed the dedicated PRESET column.
- Replaced it with a compact `P` badge beside the signal name.
- Preserved full signal names in hover tooltips.
- Kept Axis, Manual Color and Auto controls available in each row.

---

## V4.2.3 - Compact controls and visual polish

### Added / modified

- Renamed axis selectors:
  - `Primary / Left` -> `Primary`
  - `Secondary / Right` -> `Secondary`
- Added restrained semantic colors to the top toolbar actions:
  - Load CSV: blue
  - CSV file picker: light blue
  - Preset import: light purple
  - Preset export: light green
  - Normal mode: neutral gray
  - PDF: light red
  - Word: light blue
- Introduced launchers intended to run the WebServer without a persistent Command Prompt.
- Retained Debug BAT launchers for troubleshooting.

### Known launcher issue discovered later

- The first hidden-launch implementation relied directly on `pythonw.exe`.
- On systems where `python` was available in PATH but `pythonw.exe` was not, hidden launch silently failed while Debug still worked.

---

## V4.2.3.1 - Launcher hotfix

**Scope:** launcher-only hotfix; the application code remained V4.2.3.

### Fixed

- Removed the direct dependency on `pythonw.exe` from hidden startup.
- Used the same `python` command that was already confirmed to work in Debug mode.
- VBScript hid the helper CMD window.
- Added `GraphPlot_launcher.log` for hidden-start errors.

### Remaining issue discovered later

- Closing the browser did not necessarily terminate the old V4.2.3 server process.
- A stale Python server could remain attached to port 8000 and block the next launch.

---

## V4.2.4 - Managed WebServer lifecycle

### Added browser/server lifecycle management

- Browser tabs send periodic heartbeats to the server.
- Page close sends a best-effort client release notification.
- When no GraphPlot clients remain, an idle countdown begins.
- After approximately 10 seconds, the managed Uvicorn server shuts down cleanly.
- Stale heartbeat cleanup handles browser crash/sleep as a fallback.
- Python process exits and TCP port 8000 is released.

### Added management API

- `/api/health`
- localhost-only `/api/shutdown`

### Launcher architecture

Reorganized launchers into:

```text
Launcher/
  Stable/
  Hidden/
  Debug/
```

- Stable: recommended normal launcher.
- Hidden: no persistent Command Prompt.
- Debug: visible Python/Uvicorn logs and port inspection.

### Duplicate-start protection

- Launcher checks `/api/health` first.
- If the same V4.2.4 server is already active, a second server is not started.
- Browser is opened against the existing server instead.

### Limitation discovered during migration

- V4.2.3/V4.2.3.1 did not provide `/api/health` or automatic lifecycle management.
- Therefore an old server could still hold port 8000 and V4.2.4 could detect the conflict but could not safely remove the old process automatically.

---

## V4.2.4.1 - Safe stale-server recovery

### Added

- Windows listener PID discovery for port 8000.
- Windows process name, executable path and command-line inspection.
- GraphPlot-specific process classification.
- Version extraction from old `graphplot_NisOBC_web_v4...py` command lines.

### Startup decision flow

```text
Start GraphPlot
    |
    v
Check /api/health
    |
    +-- Current V4.2.4.1 -> reuse existing server -> open browser
    |
    +-- Older healthy GraphPlot -> ask -> /api/shutdown -> start V4.2.4.1
    |
    +-- No health response -> inspect port 8000 PID/command line
                            |
                            +-- Proven old GraphPlot -> ask -> taskkill PID/tree -> start
                            |
                            +-- Unknown application -> DO NOT KILL -> report process
```

### Safety rules

- Never uses `taskkill /IM python.exe /F`.
- Never force-kills a Python process merely because it uses port 8000.
- Forced PID termination is offered only when the process command line is positively identified as a GraphPlot WebServer script.
- If any listener is unknown, automatic cleanup is aborted.

### Stable launcher behavior

- Stale GraphPlot -> visible Y/N confirmation.
- Startup error -> window remains open so the error can be read.
- Successful normal server shutdown -> Stable console closes automatically.

### Hidden launcher behavior

- Stale GraphPlot -> Windows Yes/No dialog.
- Critical startup errors -> Windows error dialog plus `GraphPlot_launcher.log`.
- No persistent Command Prompt.

### Debug improvements

- Debug launchers use the same stale-server protection before starting.
- `Check_Port_8000.bat` reports:
  - health endpoint result
  - active client count when available
  - listening PID
  - executable name
  - command line
  - GraphPlot/unknown classification

---

## Current feature set at V4.3.1

- System / Light / Dark appearance modes with System-following default.
- Compact Preset / Export / Theme dropdown navigation.
- Smart CSV header-row detection from `Timestamp` / `Date&Time` / `Date` / `Time` in the first column.
- Generic CSV plotting in Normal Plot Mode.
- Automatic cycle and soak analysis for plotted signals.
- Portable per-project `.preset` import/export.
- External Nissan OBC preset example.
- Per-signal Primary/Secondary axis assignment.
- Per-signal Auto or Manual color.
- Interactive offline Plotly graph.
- Zoom, pan, hover, trace show/hide and isolate.
- Cursor A/B analysis.
- Delta Time / Delta X / Delta Value.
- Min / Max / Average / Sample Count for selected/visible range.
- PNG export.
- PDF report export.
- Word report export.
- Localhost mode.
- LAN mode.
- Automatic server shutdown after browser clients close.
- Duplicate-server prevention.
- Safe stale GraphPlot process recovery on port 8000.
- Stable, Hidden and Debug launch workflows.

## Versioning note

The application currently uses the V4.x project version scheme rather than strict Semantic Versioning. A fourth component such as `V4.2.4.1` is used for a focused hotfix that does not justify a larger feature-number change.

---

## V4.3.0 - Smart Header Detection and Cycle Analysis

### Smart Header Detection

- Removed the normal need for a manually entered `Skip Rows` value.
- Scans the first CSV column for `Timestamp`, `Date&Time`, `Date`, or `Time`.
- Normalizes common `Date&Time` separator variants such as `Date/Time`, `Date Time`, and `Date_Time`.
- Uses the detected row as the CSV header automatically.
- If no recognized marker is found, row 1 is used as a generic CSV fallback.
- Displays the detected header-row number and detection result in the dataset information strip.
- If the first header is `Date` and the second is `Time`, both are combined for timestamp parsing.

### Cycle Analysis

Cycle Analysis was ported from the earlier Tkinter `graphplot_common.py` V3.1.1 concept into the WebServer.

- Select any currently plotted numeric signal for cycle analysis.
- Infer Tmin and Tmax from the signal.
- Use a configurable tolerance band around Tmin/Tmax (default `±2 °C`).
- Detect contiguous Tmin/Tmax plateau/soak events.
- Compress repeated same-state band entries so noise/re-entry does not create a false opposite-state transition.
- Define a complete cycle as `A -> B -> A` (`Tmin -> Tmax -> Tmin` or the reverse).
- Calculate:
  - complete cycle count
  - cycle start/end
  - time per cycle
  - soak time at Tmin
  - soak time at Tmax
  - average cycle time
  - average Tmin soak
  - average Tmax soak
- Uses real CSV timestamp differences when timestamp parsing succeeds.
- Uses configurable fallback seconds/sample when timestamp parsing fails.
- Adds browser CSV export for cycle-analysis results.
- Reports when no complete cycle is detected or when Tmin/Tmax tolerance bands overlap.

### Preserved

All V4.2.4.1 launcher/lifecycle behavior and all previous plotting, preset, color, cursor/statistics and report functions remain available.

---

## V4.3.1.2 — 2026-09-01

### Fixed
- Fixed the Preset dropdown layout where the **Import preset** button could overflow outside the dropdown panel.
- Changed the preset import form to a single-column grid with constrained file-input/button widths.
- Header dropdown menus are now mutually exclusive: opening **Preset**, **Export**, or **Theme** automatically closes the previously open menu.
- Clicking outside a header dropdown or pressing **Esc** closes the open menu.

## V4.3.1 - Appearance Themes and Compact Top Navigation

### Added

- Added three appearance modes: **System**, **Light**, and **Dark**.
- `System` is the default behavior and follows the browser/Windows `prefers-color-scheme` setting automatically.
- The selected appearance mode is stored in browser `localStorage`, so the preference is reused on the next session.
- Dark mode covers the application shell, controls, sidebar, analysis tables, status panels, and the interactive Plotly graph.
- Plotly paper/plot backgrounds, grid lines, fonts, and legend surfaces are updated when the theme changes without requiring a page reload.

### Top toolbar changes

- Removed the visible **Header / Auto detect** control from the header. Smart Header Detection from V4.3.0 still runs automatically in the backend.
- Kept **CSV file selection + Load CSV** directly accessible because it is the primary workflow.
- Reorganized signal-preset actions into a compact **Preset ▾** menu:
  - Import `.preset`
  - Export current `.preset`
  - Switch to Normal mode / unload preset
- Reorganized report actions into an **Export ▾** menu:
  - PDF report
  - Word report
- Added a **Theme ▾** menu for System / Light / Dark selection.
- Kept the current preset/Normal-mode badge visible, but constrained its width to prevent long project names from expanding the toolbar.
- Improved responsive wrapping so dropdown menus remain usable on narrower displays.

### Preserved

- Smart Header Detection and Date/Time parsing from V4.3.0.
- Cycle Analysis and cycle CSV export.
- Portable `.preset`, manual colors, Cursor A/B, range statistics, Plotly interactivity, PNG/PDF/Word export, and managed server lifecycle.
---

## V4.3.1.1 - Dropdown UI hotfix

### Fixed

- Kept the Preset import file selector and Import button inside the dropdown boundary.
- Made Preset, Export, and Theme dropdowns mutually exclusive.
- Clicking outside a header dropdown or pressing `Esc` closes it.

---

## V4.3.1.2 - LAN access correction

### Fixed

- LAN launchers now open the primary PC browser using the detected LAN IPv4 URL instead of always opening `127.0.0.1`.
- The WebServer still binds to `0.0.0.0` in `--lan` mode so other devices can connect.
- Improved LAN IPv4 selection when more than one Windows network adapter exists.
- Launcher now checks whether an already-running current GraphPlot server is bound only to loopback. If LAN mode is requested, it offers to restart that server in LAN mode instead of silently reusing a Local-only listener.

### Added

- `Launcher\LAN_Setup\Check_LAN_Status.bat` for LAN IP, bind-address and network-profile diagnostics.
- `Launcher\LAN_Setup\Allow_GraphPlot_Port_8000_Firewall.bat` to create an inbound TCP 8000 rule for Windows Private/Domain profiles.
- `Launcher\LAN_Setup\Remove_GraphPlot_Port_8000_Firewall.bat` to remove that rule.
- Stable/Debug LAN launchers print the LAN URL that should be used from other PCs.

### Security

- The firewall helper intentionally excludes the Windows Public network profile.
- LAN mode still has no application login/authentication; use only on a trusted LAN.


---


## V4.4.1 — 2026-09-01

### Fixed

- Fixed the **Add comment** modal appearing transparent over the graph. The annotation UI now uses the actual theme surfaces rather than undefined CSS variables.
- Strengthened the modal backdrop and added a small blur so graph traces/hover text no longer compete visually with the comment form.
- Added additional vertical spacing between **Plot Mode**, **Plot Setup**, **Data Series**, and **Annotations & limits**.
- Reworked the sticky sidebar height/padding so the final annotation controls remain reachable when every card is expanded.
- Added wheel handoff from the nested Data Series list to the parent sidebar when the signal list reaches its top/bottom.

### Sidebar state memory

- Plot Setup, Data Series, Annotations & Limits, annotation creator panels, and individual annotation editor panels now keep their open/closed state in browser `sessionStorage`.
- Sidebar scroll position is also restored after a form submission or refresh.
- Adding or editing a Reference Line / Range Band no longer forces the user to close all the other cards again after the page reload.

### Direct graph annotation editing

- Reference Lines can be dragged vertically on the Plotly graph. The line remains horizontal/full-width and its new value is synchronized to the server.
- Range Bands can be moved/resized vertically; updated Min/Max values are synchronized to the server.
- Graph Comment boxes can be dragged directly in Plotly. Comment text-box offsets are persisted and are also used by PNG/PDF/Word Matplotlib exports.
- Added X/Y anchor and text-offset fields to the Comment editor for precise manual correction.
- Dragged values are reflected immediately in the Annotation Manager fields and static plot cache is invalidated for the next export.
- Cursor A/B overlay shapes remain non-editable and continue to coexist with persistent engineering annotations.

### Preserved

- `.preset` behavior is unchanged: Reference Lines and Range Bands remain portable; Comments remain session/test specific.
- Smart Header Detection, Cycle Analysis, Theme modes, LAN tools, server lifecycle management, and all report exports remain available.

---

## V4.4.0.1 — 2026-09-01

### Fixed / improved
- Made **Data Series** collapsible like Plot setup.
- Converted Reference Line and Range Band creation forms into collapsed sub-panels to prevent the Annotation card from becoming excessively tall.
- Increased spacing between sidebar cards and main analysis cards for better readability.
- Preserved all V4.4.0 annotation, preset, cycle-analysis and export behavior.

## V4.4.0 — 2026-09-01

### Main focus

Engineering annotations and requirement visualization directly on the interactive graph and exported reports.

### Added

- Added **Reference / Limit Lines** on either Primary or Secondary Y axis.
- Added manual line label, value, color, width and line-style settings.
- Added **Tolerance / Range Bands** with Min/Max, line color, fill color and opacity.
- Added **click-to-place graph comments** with arrow, text/background colors and font size.
- Added an **Annotations & Limits Manager** in the sidebar.
- Added show/hide, edit and delete controls for engineering annotations.
- Reference Lines and Range Bands now appear in the Interactive Plotly graph and Matplotlib PNG/PDF/Word outputs.
- Graph Comments also appear in Plotly and static report outputs.
- Extended `.preset` v1 with optional `reference_lines` and `range_bands` arrays.

### Preset policy

- Reference Lines and Range Bands are portable engineering requirements and are exported/imported with `.preset`.
- Comments are treated as test-log-specific observations and are **not** exported into presets by default.
- Older V4.2/V4.3 presets without annotation fields remain valid.

### Fixed / integration work

- Cursor A/B Plotly shapes now merge with persistent engineering annotation shapes instead of replacing them.
- Secondary-axis annotations can create/use the Secondary Y axis even if no Secondary signal trace is currently selected.
- Annotation changes invalidate the static plot cache so PNG/PDF/Word outputs stay synchronized with the browser graph.



## V4.4.2.1 — 2026-09-01

### Added
- Continuous long-page PDF report: all plot tabs stacked vertically on one PDF page.
- Legacy A4 multi-page PDF retained as `PDF A4 report`.
- Comment border color and border width.
- Comment box width and box height controls after placement.
- Comment arrow color and arrow width.
- Explicit multiline comment rendering using user-entered line breaks.

### Changed
- Default `PDF report` export is now the continuous long-page layout.
- Comment manager exposes all presentation controls in one NOTE editor.

### Preserved
- Reference/range annotations, drag-to-move comments, Cursor A/B, cycle analysis, Smart Header Detection, preset workflow, LAN/Local lifecycle management, PNG and Word exports.
