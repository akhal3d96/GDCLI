#!/usr/bin/python
import inspect, os

import httplib2
import pprint
import os.path

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
 
class _UPLOAD:
	 CLIENT_ID = '882958819373-6ekd2b2qsabffr8m1ouo7s9skeo7a7je.apps.googleusercontent.com'
	 CLIENT_SECRET = 'bPckUyzopzfYsJsIQx0tKeVp'
	 OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'
	 REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
	 FILENAME = None
	 
	  
	 def _UPSHEX(self,quick):
		 self.quick = quick
		 if quick == 'quick':
			 _UPLOAD.FILENAME = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/quick.txt'  
			 #execfile("place.py") , 'quick.txt'
			 #execfile("p2.py")+'quick.txt'
		 if quick != 'quick':
			 _UPLOAD.FILENAME = raw_input('File place: ')
		 _descripe = raw_input('Add descripe to your file: ')
		 _type = os.path.splitext(_UPLOAD.FILENAME)[1]
		 _name = "TEST AHMED"
		 #os.path.basename(_UPLOAD.FILENAME)
		 #print _name
		 #send_type = None
		 types = {'.txt' : 'text/plain' , '.doc' : 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}
		 #print _type
		 #print types[_type]
		 flow = OAuth2WebServerFlow(_UPLOAD.CLIENT_ID, _UPLOAD.CLIENT_SECRET,_UPLOAD.OAUTH_SCOPE,_UPLOAD.REDIRECT_URI)
		 authorize_url = flow.step1_get_authorize_url()
		 print 'Go to the following link in your browser: ' + authorize_url 
		 code = raw_input('Enter verification code: ').strip()
		 credentials = flow.step2_exchange(code)
		 http = httplib2.Http()
	 	 http = credentials.authorize(http)
		 drive_service = build('drive', 'v2', http=http)
		 media_body = MediaFileUpload(_UPLOAD.FILENAME, mimetype=types[_type], resumable=True)
		 body = {'title': _name,'description': _descripe,'mimeType': types[_type]}
		 file = drive_service.files().insert(body=body, media_body=media_body).execute()
		 #pprint.pprint(file)
		 print 'Your file has uploaded successfuly and its ID: %s' % file['id']
	

		  
		  

		
		





