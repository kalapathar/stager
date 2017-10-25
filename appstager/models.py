from django.db import models
import uuid
# Create your models here.





class Event(models.Model):
    event_name=models.CharField(max_length=30,help_text="Name of the event Ex- 'Play', 'Vibrate'")
    def __str__(self):
        return (self.event_name)


class Sequence(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique id for the sequence")
    events_sequence=models.ManyToManyField(Event,help_text="Add Event")

    def __str__(self):
        return (self.id)



'''

		
class Sequence(models.Model):

    sequence_name = models.CharField(max_length=30)

    def __init__(self,Event):
        self.sequence_list=list()
        self.sequence_list.append(Event)
    def add_sequence(self,Event):
        self.sequence_list.append(Event)
    def delete_sequence(self):
            self.sequence_list=list()
    def delete_event(self,Event):
        self.sequence_list.remove(Event)
    def delete_latest_event(self):
        self.sequence_list=self.sequence_list[:-1]
        
    def display_sequence(self):
        for i in self.sequence_list:
            print (i)


class Event(models.Model):
	event_name=models.CharField(max_length=30)
	sequences =  models.ManyToManyField(Sequence)
	# def __init__(self):
	# 	self.event_name=event_name

	def __str__(self):
		return (self.event_name)



'''

