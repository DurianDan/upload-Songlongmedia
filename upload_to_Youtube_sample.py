from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = r'/home/duriandan/learning/personal project/upload Songlongmedia/client_secret_2.json'
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
            "categoryId": "28"#categoryID taken from this list https://gist.github.com/dgp/1b24bf2961521bd75d6c
        },
        'status': {
            'privacyStatus': 'private',
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False,
        "onBehalfOfContentOwner": "f1XWYqYED38dYmK2dQb44A", #taken from this  https://www.youtube.com/account_advanced
        "onBehalfOfContentOwnerChannel":"UCf1XWYqYED38dYmK2dQb44A"
    }

    mediaFile = MediaFileUpload(video_file)
    
    response_upload = service.videos().insert(part='snippet,status',
    body=request_body,
    media_body=mediaFile).execute()

    service.thumbnails().set(videoId=response_upload.get('id'),
    media_body=MediaFileUpload('/home/duriandan/Pictures/Screenshot from 2021-05-23 09-30-31.png')).execute()

get_video_data("test video name","test video description",["test","tags","banana"],"/home/duriandan/Downloads/intro unboxing 60s.mp4")