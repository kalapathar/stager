from django.contrib import admin

from .models import Action, ActionType

# Register your models here.

admin.site.register(Action)
admin.site.register(ActionType)