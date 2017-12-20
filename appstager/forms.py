

from django import forms
from appstager.models import Action
from appstager.models import Show, Theater
from django.forms import ModelForm, Textarea
from django.forms import ModelForm

'''class ActionForm(ModelForm):
	class Meta:
		model=Action
		#fields=['name','description']
		fields = '__all__'
		#exclude=['id']

		#help_texts={
		#'name':None,
		#'description':None,
		#}
'''
class CueForm(forms.Form):
	name=forms.CharField(label='Name',max_length=100)
	description=forms.CharField(label='Description',max_length=100)
	sequenceNum=forms.IntegerField(label='sequencenum')
	showId=forms.IntegerField(label='showid')

class ShowForm(ModelForm):
	class Meta:
		model=Show
		fields=['name','director']
		exclude=['help_text']
		error_messages = {
			'name': {
				'unique': ("The name of each show must be unique."),
			},
		}






class ActionForm(ModelForm):
	class Meta:
		model = Action
		fields = ['show','action_type', 'name', 'description', 'order', 'duration']
		error_messages = {
			'name': {
				'unique': ("The name of each action must be unique."),
			},
		}

