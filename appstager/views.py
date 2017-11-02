import requests
from django.shortcuts import render
from appstager.models import Event

def index(request):
	#context = {}
	allevents=Event.objects.all()
	print (request)
	context={'allevents':allevents}
	return render(request, "appstager/base.html",context)
