from Google import Create_Service
import pandas as pd

SECRET_FILE = r"/home/duriandan/learning/personal project/upload Songlongmedia/client_secret_file.json"
SCOPES = ["https://www.googleapis.com/auth/youtube"]
service = Create_Service(SECRET_FILE,"youtube","v3",SCOPES)

categorylist = service.videoCategories().list(part="snippet",regionCode="VN").execute()

dr_categorylist = pd.DataFrame(categorylist["item"])
pd.concat([dr_categorylist["id"],dr_categorylist["snippet"].apply(pd.Series)["title"]],axis = 1).to_csv("Category list.csv",index = False)