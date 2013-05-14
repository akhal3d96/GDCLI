class _UI:
	AppName = "GDCLI"
	FirstWindowItems = []
	#Char = None
	
	def _FirstWindow(self):
		print ('+'*20+" "+_UI.AppName+" "+'+'*20)
		print "\n"
		for x in _UI.FirstWindowItems:
			print "[" , _UI.FirstWindowItems.index(x) , "]" , x
		print ('+'*40+6*'+')
	
	def _Ask(self):
		answer = raw_input("Choose one number :")
		return answer
	
	
