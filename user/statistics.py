import json
import requests

class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None


    # For youtube channel statistics
    def get_channel_statistics(self):
        """Extract the channel statistics"""
        url = f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2Cstatistics&id={self.channel_id}&key={self.api_key}'
       
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        complete_channel_data=[]
        channel_data= data['items'][0]['snippet']
        
        complete_channel_data.append(channel_data)
        stats_data = data['items'][0]['statistics']
        complete_channel_data.append(stats_data)
         
        return complete_channel_data


    # For geting ids of all the videos available on the channel
    def get_channel_video_data(self):
        channel_videos= self._get_channel_videos(limit=6)
        List_of_all_video_ids= channel_videos
        url_for_stats= f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet%2CcontentDetails%2Cstatistics&id=' 
        initial=0
        for i in List_of_all_video_ids:
            if initial==0:
                url_for_stats= url_for_stats+i
                initial +=1
            url_for_stats= url_for_stats+'%2C'+i
        url_for_stats= url_for_stats + f'&key={self.api_key}'


        json_url= requests.get(url_for_stats)
        data= json.loads(json_url.text)
        first_data= data['items']
        list_of_data= []
        for i in first_data:
            temp_list= []
            temp_list.clear()
            snippet= i['snippet']
            temp_list.append(snippet)
            stats= i['statistics']
            temp_list.append(stats)
            list_of_data.append(temp_list)
            
        return list_of_data
       
        
    


    def _get_channel_videos(self, limit):
        url= f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        if limit is not None and isinstance(limit, int):
            url += '&maxResults=' + str(limit)
        
        vid= self._get_channel_videos_per_page(url)
        return vid
        
      


    def _get_channel_videos_per_page(self, url):
        json_url= requests.get(url)
        data= json.loads(json_url.text)
        video_raw_data= data['items']
        videos_id= []
        for i in video_raw_data:
            if i['id']['kind']== 'youtube#video':
                videos_id.append(i['id']['videoId'])
        return videos_id


    