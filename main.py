from ui import _UI
from upload import _UPLOAD 
from quick import _QUICK


UI = _UI()
UPLOAD =_UPLOAD()
QUICK = _QUICK()

UI.FirstWindowItems.append("Upload")
UI.FirstWindowItems.append("Quick Create")

UI._FirstWindow()

answer = UI._Ask()

if answer == 0:
	UPLOAD._UPSHEX("")
if answer == 1:
	QUICK_CREATE()
	UPLOAD._UPSHEX('quick')	
