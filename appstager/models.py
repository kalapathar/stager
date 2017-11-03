from django.db import models
import uuid
# Create your models here.

class Action(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = "Unique ID for the action")
    name = models.CharField(max_length = 50, help_text = "The name of the action")
    description = models.CharField(max_length = 200, help_text = "Description of the action")
    
    def __str__(self):
        return (str(self.id))

class ActionType(models.Model):
    name = models.CharField(max_length = 50, help_text = "Name of the event (i.e. 'Play', 'Vibrate')")
    def __str__(self):
        return (self.name)