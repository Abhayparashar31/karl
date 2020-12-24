Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c message.bat"
oShell.Run strArgs, 0, false