Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c caller.bat"
oShell.Run strArgs, 0, false