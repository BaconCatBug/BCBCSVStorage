Set WshShell = CreateObject("WScript.Shell" ) 
WshShell.Run chr(34) & "RunScripts.bat" & Chr(34), 0 
Set WshShell = Nothing 