import requests

from django.http import HttpResponse

#cuecount=list()
def sendcapstone(cues):
	#cuecount.append(len(cues))
	for action in cues:
		try:
			requests.post('http://localhost:4000/action?name='+action.name+'&description='+action.description+'&cueId=2&actionTypeId=1&deviceId=1')
		except requests.exceptions.RequestException:
			return ("Error with Capstone API")
	return ("Cues sent successfully!")
