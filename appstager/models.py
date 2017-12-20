from django.db import models
import uuid
from datetime import timedelta

class Theater(models.Model):
	name = models.CharField(max_length = 100,help_text = "Name of the Theater", unique = True)

	def __str__(self):
		return (str(self.name))

class Show(models.Model):
	name = models.CharField(max_length = 100, help_text = "Name of the Show", unique = True)
	theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=True)
	number_of_seats = models.IntegerField(null=True, help_text = "Input the number of seats this theater has")
	director=models.CharField(max_length=100, help_text = "Director of this show.")

	def __str__(self):
		return (str(self.name))


class Action(models.Model):
	show = models.ForeignKey(Show, on_delete=models.CASCADE)

	ACTION_TYPE = (
        ('Vibrate', 'Vibrate'),
        ('Background', 'Background'),
        ('Sound', 'Sound'),
        ('Image', 'Image'),
        ('Video', 'Video')
    )
	name = models.CharField(max_length = 50,help_text = "Name of the action", unique = True)
	description = models.TextField(max_length = 200, help_text = "Description of the action")
	action_type = models.CharField(max_length = 50, choices = ACTION_TYPE, help_text = "Name of the action type")
	order = models.IntegerField(null=True, help_text = "Order of the action in the show (from QLab)")

	duration = models.DurationField(default=timedelta, help_text = "Duration of the action (HH:MM:SS)")

	redValue = models.CharField(max_length = 3, help_text = "The value of the color red that should be used", default="0")
	greenValue = models.CharField(max_length = 3, help_text = "The value of the color green that should be used", default="0")
	blueValue = models.CharField(max_length = 3, help_text = "The value of the color blue that should be used", default="0")

    
	def __str__(self):
		return (str(self.action_type) + '~~~' + str(self.name) + '~~~' + str(self.description) + '~~~' + str(self.order) + '~~~' + str(self.duration) + '~~~' + str(self.redValue) + '~~~' + str(self.greenValue) + '~~~' + str(self.blueValue))




