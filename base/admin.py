from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

#the above code just communicates to the admin app that weve added these 
# and we want to be able to access them in the admin browser app