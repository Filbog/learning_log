from django.contrib import admin

# imports the model from our models.py
from .models import Topic, Entry

# with this line, we enable admin to manage the model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)
