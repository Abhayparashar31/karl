Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c calculator.bat"
oShell.Run strArgs, 0, false
