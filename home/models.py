from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name= models.CharField(max_length=255)
     phone= models.CharField(max_length=13)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):
         return 'This message is from ' + self.name

class extendeduser(models.Model):
    id=models.AutoField(primary_key=True)
    username= models.CharField(max_length=50)
    channel_type= models.CharField(max_length=50)
    link= models.TextField(max_length=100)
    category= models.CharField(max_length=50)
    Min_amount= models.CharField(max_length=50)
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    phnno= models.CharField(max_length=12, default='')
    gender= models.CharField(max_length=8)
    tags=models.CharField(max_length=50, default='')
    state= models.CharField(max_length=30)
    id_store= models.TextField()
    

    def __str__(self):
         return self.username

