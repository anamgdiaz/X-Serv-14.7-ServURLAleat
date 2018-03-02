#!/usr/bin/python3

import webapp

class AleatApp(webapp.webApp):
	def parse(self, request):
		try:
			return True
		except IndexError: 
			return None
	def process(self, parsedRequest):
		if not parsedRequest:
			return ("200 OK", "<html><body><h1> Go Away!"+"</h1></body></html>")
		else:
			import random 
			url = str(random.randint(1,1000000))
			return ("200 OK", "<html><body><h1>HOLA!</h1>""<a href=''"+ url+"'>Dame otra!</a>""<h1> URL:"+url+"</h1></body></html>")

if __name__ == "__main__":
    testWebApp = AleatApp("localhost", 1234)	