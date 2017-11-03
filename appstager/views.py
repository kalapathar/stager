import requests
from django.shortcuts import render
from appstager.models import Action, ActionType

def index(request):
	actionType = ActionType.objects.all()
	context = {'actionType':actionType}
	return render(request, "appstager/base.html",context)