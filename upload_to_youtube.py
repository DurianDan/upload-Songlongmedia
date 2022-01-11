#this implementation comes from the file /home/duriandan/learning/personal project/upload Songlongmedia/upload_to_Youtube_sample.py
from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import json
from glob import glob
CLIENT_SECRET_FILE = r'/home/duriandan/learning/personal project/upload Songlongmedia/client_secret_file.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

def get_video_data(video_name,video_description,video_tags,video_file):
    request_body = {
        'snippet': {
            'title': video_name,
            'description': video_description,
            'tags': video_tags,
            "categoryId": "28"#đây là phân loại video dựa trên số ID,https://gist.github.com/dgp/1b24bf2961521bd75d6c
        },
        'status': {
            'privacyStatus': 'private',
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }
    mediaFile = MediaFileUpload(video_file)
    response_upload = service.videos().insert(part='snippet,status',body=request_body,media_body=mediaFile).execute()
    service.thumbnails().set(videoId=response_upload.get('id'),media_body=MediaFileUpload('/home/duriandan/learning/personal project/upload Songlongmedia/plusultraendeavor')).execute()


for i in glob("/home/duriandan/learning/personal project/upload Songlongmedia/json_description/*"):
    data = {}
    with open(i) as jsonfile:
        data = json.load(jsonfile)
    get_video_data(data["video_name"],data["video_des"],data["video_tags"],data["MP4_file_name"])

