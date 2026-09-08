Option Explicit
Dim shell, fso, root, cmd
Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
root = fso.GetParentFolderName(fso.GetParentFolderName(WScript.ScriptFullName))
cmd = "cmd /c cd /d """ & root & """ && python signalworks_studio_launcher.py --mode hidden --lan --port 8800"
shell.Run cmd, 0, False
