from django.db import models
from django.contrib.auth.models import User #were getting access to the user model built in
from django.db.models.deletion import CASCADE #were accessing the cascade method
# Create your models here.
# if you create a class X then there will be a table x generated

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    # models.model is what is turning it into an actual django model
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200) #max length is required for charfield
    description = models.TextField(null=True, blank=True) #setting null to true means that it can be blank
    # participants = this will store all of the participants in a room
    updated = models.DateTimeField(auto_now=True) #every time that the save method is called were taking a time stamps
    created = models.DateTimeField(auto_now_add=True) #auto now add only takes a timestamp when we first save or create this instance

    def __str__(self):
        return self.name

class Message(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #this is what establishes the one to many relationship between the room and it's messages. 
    #^^ on delete, we use cascade so that we remove anything else associated within the room. if you delete a room, you delete its messages
    body = models.TextField() #sets the body as a basic text field
    updated = models.DateTimeField(auto_now=True) #every time that the save method is called were taking a time stamps
    created = models.DateTimeField(auto_now_add=True) #auto now add only takes a timestamp when we first save or create this instance

    def __str__(self):
        return self.body[0:50] #we only want the first 50 characters on the preview