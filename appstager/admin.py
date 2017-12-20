from django.contrib import admin

from .models import Action
from .models import Show,Theater

# Register your models here.

admin.site.register(Action)
admin.site.register(Show)
admin.site.register(Theater)