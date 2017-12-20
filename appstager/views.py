import requests
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core import serializers  # Convert query list to string
from django.http import HttpResponse # Return a basic HTTP response
from django.http import JsonResponse # Return a basic JSON response
from appstager.capstone import sendcapstone
from appstager.models import Action,Show, Theater

from .forms import ActionForm,ShowForm


def start(request):
	context = {'user':request.user}
	return render(request, "appstager/login.html",context)


def index(request):
	action = Action.objects.all().order_by('order')
	context = { 'action':action }
	#send the Cue to the capstone through HTTP Request
	if "Send" in request.POST:
			context['server_response']=(sendcapstone(action))

	
	return render(request, "appstager/planner.html", context)

#added a shows function which lists all the shows and allows the user to add a show.
def show(request):
	shows=Show.objects.all()
	context={'shows':shows}
	if request.method=="POST":
		form=ShowForm(request.POST)
		if form.is_valid():
			form.save()
			try:
				requests.post('http://localhost:4000/shows?name='+str(request.POST['name'])+'&director='+str(request.POST['director']))
				context['server_response']="Show successfuly Added!"   #server_response contains the message if the POST/GET request was successful or not! 
				
			except requests.exceptions.RequestException:
				context['server_response']= "Error with Qlab API"
	else:
		form=ShowForm()
	
	context['form']=form
	return render(request,"appstager/shows.html",context)

# AJAX METHODS
def getAction(request):
	#Needs fixing
	#show_id is missing
	reqshow = Show.objects.get(id=show_id)
	print(reqshow)
	actionDataOrder = Action.objects.order_by('order').filter(show=reqshow)
	return render(request, 'appstager/actionList.html', {'actionData':actionDataOrder})

def createAction(request, actType):
	print("Showing form in the properties panel")

	data = {'action_type': actType}
	form = ActionForm(data)

	context = { 'form':form }
	return render(request, "appstager/createAction.html", context)

def submitAction(request):
	# We need to return something to report that the operation was successful
	if request.method == 'POST':


		form = ActionForm(request.POST)
		if form.is_valid():
			form.save()
			msg = "Add a new action!"
			return HttpResponse("success")
	msg = "There was an error in for submission"
	return HttpResponse(msg)

def updateActionUp(request, order):
	# This will create an object with the name passed to it as POST data
	print("Updating action")

	orderNum = int(order)

	# Get the type of foreign key from the argument
	action1 = Action.objects.get(order = orderNum)
	action2 = Action.objects.get(order = orderNum - 1)
	action1.order = orderNum - 1
	action2.order = orderNum
	action1.save()
	action2.save()

	# We need to return something to report that the operation was succesful
	return HttpResponse("success");

def updateActionDown(request, order):
	# This will create an object with the name passed to it as POST data
	print("Updating action")

	orderNum = int(order)

	# if last item, do nothing
	if orderNum == Action.objects.all().count():
		print("No changes made")
		return HttpResponse("success")

	# Get the type of foreign key from the argument
	action1 = Action.objects.get(order = orderNum)
	action2 = Action.objects.get(order = orderNum + 1)
	action1.order = orderNum + 1
	action2.order = orderNum
	action1.save()
	action2.save()

	# We need to return something to report that the operation was succesful
	return HttpResponse("success");


def activeAction(request, name):
	print("THIS IS THE PRINT!!")
	print(name)
	data = Action.objects.get(name = name)
	return HttpResponse(data, content_type='text/plain') # Return it as json http response

def showActions(request, show_id):
	reqshow = Show.objects.get(id=show_id)
	print(reqshow)
	action = Action.objects.order_by('order').filter(show=reqshow)
	print("These are the actions found: "+ str(action))
	context = { 'action':action }
	#send the Cue to the capstone through HTTP Request
	if "Send" in request.POST:
			context['server_response']=(sendcapstone(action))

	
	return render(request, "appstager/planner.html", context)

def choice(request):
	availableTheaters = Theater.objects.all().order_by('name')

	if request.POST:
		if(request.POST.get("theatername","") !='' ):
			selectedTheater = Theater.objects.get(id=request.POST.get("theatername",""))
			print(selectedTheater)
			availableShows = Show.objects.filter(theater=selectedTheater)
			print(availableShows)
		try:
			availableShows = Show.objects.filter(theater=selectedTheater)
		except:
			availableShows = {}
		if(request.POST.get("showname","") !='' ):
			show_id=request.POST.get("showname","")
			return redirect('/' + show_id)
	else:
		availableShows = {}

	print(availableShows)
	context = {'theaters': availableTheaters, 'shows': availableShows}
	return render(request, "appstager/choice.html", context)
