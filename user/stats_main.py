from django.shortcuts import render, HttpResponse, redirect
from home.models import extendeduser
from django.contrib.auth.models import User
from user.models import Channel_statistics, GraphAnalitycs
from user.statistics import YTstats
import requests
import json


def get_all_videos(user):
    userx= extendeduser.objects.get(user=user)
    link = userx.link
    if 'https://www.youtube.com/channel/' in link:
        link= link.replace('https://www.youtube.com/channel/', '')


        API_KEY= 'AIzaSyB9h8mAYG-DHmExLfu7AFMjS9P0ApBCBlY'

        channel_id= link
        yt= YTstats(API_KEY, channel_id)
        six_videos= yt.get_channel_video_data()
        return six_videos


        

    
def subgoal_current_position(ttl_views, subgoal):
        crnt_pstn= (ttl_views/subgoal)*100
        return crnt_pstn

def subs_to_view_ratio(ttl_subs, total_avg_views):
    ratio= total_avg_views/ ttl_subs
    if ratio >1:
        ratio = 1
    ratio= ratio*10
    return ratio
        
def likeratio(total_avg_likes, total_avg_views):
    avg_like_ratio= total_avg_likes/total_avg_views
    if avg_like_ratio >= 0.5:
        tratio= 10
        return tratio
    elif avg_like_ratio > 0.3:
        tratio= 8
        return tratio
    elif avg_like_ratio > 0.2:
        tratio= 6
        return tratio
    elif avg_like_ratio > 0.1:
        tratio = 4
        return tratio
    elif avg_like_ratio > 0:
        tratio =2
        return tratio

def total_views_analitics(total_avg_views):
    if total_avg_views > 10000000:
        avg_views_ana= 50
    elif total_avg_views > 1000000:
        avg_views_ana= 45
    elif total_avg_views > 500000:
        avg_views_ana= 40
    elif total_avg_views > 100000:
        avg_views_ana= 30
    elif total_avg_views > 50000:
        avg_views_ana= 20
    elif total_avg_views > 10000:
        avg_views_ana= 10
    elif total_avg_views > 0:
        avg_views_ana= 5
    return avg_views_ana



# To add statistics of channel and videos

def channel_stats(user, language, state, tags):
    userx= extendeduser.objects.get(user=user)
    link = userx.link
    if 'https://www.youtube.com/channel/' in link:
        link= link.replace('https://www.youtube.com/channel/', '')


        
        API_KEY= 'AIzaSyB9h8mAYG-DHmExLfu7AFMjS9P0ApBCBlY'
        channel_id= link
        yt= YTstats(API_KEY, channel_id)
        data= yt.get_channel_statistics()
        
        
        ttl_views= data[1]['viewCount']
        ttl_subs= data[1]['subscriberCount']
        videoCount= data[1]['videoCount']
        
        channel_desc= data[0]['description']
        channel_name= data[0]['title']
        country= data[0]['country']
        channel_logo= data[0]['thumbnails']['medium']['url']
        channel_logo_low= data[0]['thumbnails']['default']['url']
        content_language= language

        six_videos= get_all_videos(user)
        init_video=0
        for i in six_videos:
            init_video+=1
            if init_video==0:
                first_video1= int(i[1]['viewCount']) #This first_video1 second_video and third_video repeat the value of first video
            
            if init_video==1:
                second_video= int(i[1]['viewCount']) 
                
            if init_video==2:
                third_video= int(i[1]['viewCount'])
        
            if init_video==3:
                fourth_video= int(i[1]['viewCount'])
                
            if init_video==4:
                fifth_video= int(i[1]['viewCount'])
                
            if init_video==5:
                sixth_video= int(i[1]['viewCount'])
                
            if init_video==6:
                seventh_video= int(i[1]['viewCount'])
                
            if init_video==7:
                eight_video= int(i[1]['viewCount'])
        
        total_avg_views= (fourth_video + fifth_video + sixth_video + seventh_video + eight_video)// (init_video-3)


        # To fetch the category of perticular user
        cate= extendeduser.objects.values().filter(user=user)
        cateuser= cate[0]['category']
        print(cate)
        


        initialfs= 1
        subgoal=0
        while True:
            if initialfs==1:
                subgoal = int(100000)
                if int(ttl_subs)< subgoal:
                    subgoal= subgoal
                    break
                initialfs +=1
                
                
            elif initialfs==3: 
                subgoal = int(1000000)

            if int(ttl_subs)< subgoal:
                subgoal=subgoal
                initialfs +=1
                break

            if initialfs !=2:
                subgoal += int(1000000)
                init_video+=1
            initialfs+=1

            
                

        
        sub_current_posi=subgoal_current_position(int(ttl_subs), subgoal)
        subs_curren_posi_graph= (sub_current_posi/subgoal)*100
        subs_to_views_ratio= subs_to_view_ratio(int(ttl_subs), int(total_avg_views))
        substoviewratio_graph= (int(total_avg_views)/int(ttl_subs))*100

        init_video=0
        for i in six_videos:
            init_video+=1
            if init_video==0:
                first_video1= int(i[1]['likeCount']) #This first_video1 second_video and third_video repeat the value of first video
            
            if init_video==1:
                second_video= int(i[1]['likeCount']) 
                
            if init_video==2:
                third_video= int(i[1]['likeCount'])
        
            if init_video==3:
                fourth_video= int(i[1]['likeCount'])
                
            if init_video==4:
                fifth_video= int(i[1]['likeCount'])
                
            if init_video==5:
                sixth_video= int(i[1]['likeCount'])
                
            if init_video==6:
                seventh_video= int(i[1]['likeCount'])
                
            if init_video==7:
                eight_video= int(i[1]['likeCount'])
        
        total_avg_likes= (fourth_video + fifth_video + sixth_video + seventh_video + eight_video)// (init_video-3)
        like_ratio= likeratio(total_avg_likes, int(total_avg_views))
        views_to_like_graph= (int(total_avg_likes)/int(total_avg_views))*100
        total_avg_views_analytics= total_views_analitics(total_avg_views)
        overall_marking= total_avg_views_analytics + like_ratio + subs_to_views_ratio
        overall_rating= (overall_marking/70)*100
        total_channnel_stats= Channel_statistics(total_views=ttl_views, total_subs=ttl_subs, total_videos=videoCount, user=user, username= user, desc= channel_desc, logo=channel_logo, country=country, language=content_language, channel_name=channel_name, state= state, avg_views= total_avg_views, overall_marking=overall_marking, category= cateuser, logo_low= channel_logo_low, tags=tags)
        total_channnel_stats.save()


       

        
        total_analytics= GraphAnalitycs(username= user, user= user, subsgoal=subgoal, subsgoal_current_position= sub_current_posi, substoviewratio= subs_to_views_ratio, views_to_like= like_ratio, overall_rating= overall_rating, overall_marking= overall_marking, subsgoal_current_position_graph= subs_curren_posi_graph, substoviewratio_graph= substoviewratio_graph, views_to_like_graph=views_to_like_graph)
        total_analytics.save()


            












