Set oShl = WScript.CreateObject("WScript.Shell")
Set oFso = WScript.CreateObject("Scripting.FileSystemObject")

While Not oFso.DriveExists("X")
	sMessage = "Reconnecting X drive"
	sTitle = "X drive lost"
	oShl.Popup sMessage, 5, sTitle
	oShl.Run "cmd /k net use x: \\w1p01-atbatch01.mediconnect.net\clientfiles\aanuc\inbound /user:w1p01-atbatch01\aanuc yZd2t;Qb & exit",8,True
Wend

Set oShl = Nothing
Set oFso = Nothing
