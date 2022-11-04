from django.db import models

# Create your models here.
# if you create a class X then there will be a table x generated


class Room(models.Model):
    # models.model is what is turning it into an actual django model
    # host = 
    #topic = 
    name = models.CharField(max_length=200) #max length is required for charfield
    description = models.TextField(null=True, blank=True) #setting null to true means that it can be blank
    # participants = this will store all of the participants in a room
    updated = models.DateTimeField(auto_now=True) #every time that the save method is called were taking a time stamps
    created = models.DateTimeField(auto_now_add=True) #auto now add only takes a timestamp when we first save or create this instance

    def __str__(self):
        return self.name