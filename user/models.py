from django.db import models
from django.contrib.auth.models import User

# Create your models here.




# For statistics of the channel
class Channel_statistics(models.Model):
    username= models.CharField(max_length=20, primary_key=True)
    channel_name= models.CharField(max_length=50)
    desc= models.TextField(max_length=9000, default='')
    category= models.CharField(max_length=100)
    country= models.CharField(max_length=50, default='')
    state= models.CharField(max_length=50)
    language= models.CharField(max_length=20, default='')
    total_views= models.CharField(max_length=50)
    total_subs= models.CharField(max_length=50)
    avg_views= models.CharField(max_length=50, default='')
    total_videos= models.CharField(max_length=50)
    overall_marking= models.CharField(max_length=1000)
    logo= models.CharField(max_length=100, default='')
    logo_low= models.CharField(max_length=100)
    tags= models.CharField(max_length=1000)
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
         return self.username



# For statistics of the most popular video 
class GraphAnalitycs(models.Model):
    username= models.CharField(max_length=20, primary_key=True)
    subsgoal= models.CharField(max_length=100)
    subsgoal_current_position= models.CharField(max_length=50)
    subsgoal_current_position_graph= models.CharField(max_length=50)
    substoviewratio= models.TextField(max_length=10000)
    substoviewratio_graph= models.TextField(max_length=10000)
    views_to_like= models.CharField(max_length=50)
    views_to_like_graph= models.CharField(max_length=50)
    overall_rating= models.CharField(max_length=50)
    total_comment= models.CharField(max_length=50, default= '')
    overall_marking= models.CharField(max_length=50)
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
         return self.username


