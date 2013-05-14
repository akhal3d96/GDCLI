import os

class _QUICK:
	def _CREATE(self):
		if os.path.exists("quick.txt"):
			f = open("quick.txt","r+")
		else:
			f = open("quick.txt","w")
		editable = raw_input()
		f.write(editable)
