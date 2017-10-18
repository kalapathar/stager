from django.db import models

# Create your models here.
class Event(models.Model):
	event_name=models.CharField(max_length=30)
	# def __init__(self):
	# 	self.event_name=event_name

	def __str__(self):
		return (self.event_name)

	