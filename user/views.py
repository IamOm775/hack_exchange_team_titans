from django.http import request
from django.shortcuts import render, HttpResponse, redirect
from home.models import extendeduser
from django.contrib.auth.models import User
from user import stats_main
from client.models import Advertizerdetail
from user.models import Channel_statistics, GraphAnalitycs




# Create your views here.


# To display Profile
def UserProfile(request):
    x= request.user
    try:
        client_profile= Advertizerdetail.objects.get(username=x)
        context= {'client_profile': client_profile }
        return render(request, 'client/clientdashboard.html', context)
    except:
        userdetailsprofile= extendeduser.objects.get(user=x)
        extendeduser_profile= extendeduser.objects.get(user=x)
        channel_stats= Channel_statistics.objects.get(user=x)
        analysis= GraphAnalitycs.objects.get(user=x)
        userprofile= User.objects.get(username=x)
        six_videos= stats_main.get_all_videos(x)
        first_video={}
        first_video['title']= six_videos[0][0]['title']
        first_video['publishedAt']= six_videos[0][0]['publishedAt']
        first_video['thumbnail']= six_videos[0][0]['thumbnails']['default']['url']
        first_video['stats']= six_videos[0][1]

            

        params= {'userdetails_profile':userdetailsprofile,'extendeduser_profile': extendeduser_profile, 'channel_stats': channel_stats, 'user_profile':userprofile, 'first_video': first_video, 'analysis': analysis}
        return render(request, 'user/profile.html', params)


# To add user details in the database
def Userdetails(request):
    if request.method == 'POST':
        user= request.user  

        first_name= request.POST['firstname']
        last_name= request.POST['lastname']
        phone_no= request.POST['phn_no']
        tags= request.POST['tags']
        gender= request.POST['gender']
        language= request.POST['language']
        state= request.POST['state']
        
        new_user_details= extendeduser.objects.get(username=user)
        new_user_details.firstname= first_name
        new_user_details.lastname= last_name
        new_user_details.phnno= phone_no
        new_user_details.tags= tags
        new_user_details.gender= gender
        new_user_details.state=state
        new_user_details.save()

        # To save fetch stats of channel and add them ti database
        stats_main.channel_stats(user, language, state, tags)

        return redirect('/')

