#!/usr/bin/python3 
from bitlyshortener import Shortener
from googlesearch import search
def meta_data(MP4_file_name,token:str,alt_link = None):
    """tạo ra llink rút gọn, và cho biết là video 60s hay hdsd
    MP4_file_name: tên của file mp4 (VD: (60s)topping L30,(reset)Airpods 2,(noreset)Pamu Quiet)
    token: đây là chìa khóa mà bit.ly cung cấp cho tài khoản đăng ký"""

    #1 tạo link rút gọn (video_des_shorten_link)
    key = [token]
    shortener = Shortener(tokens = key)
    video_des_shorten_link = ""
    fulllink = ""
    if alt_link == None:
        list_long = []
        #google tìm kết quả cho cụm từ trong query
        for i in search(query="songlongmedia.com {}".format(MP4_file_name.replace(MP4_file_name[:MP4_file_name.find(")")+1],"")),tld = "com",num = 1,stop = 1,pause=2,lang="vi"):
            list_long.append(i)
        short_urls = shortener.shorten_urls(list_long)#rút gọn link(các kết quả tìm kiếm google)
        video_des_shorten_link = short_urls[0]
        fulllink = list_long[0]
    else:
        fulllink = alt_link
        video_des_shorten_link = shortener.shorten_urls([fulllink])[0]
    
    #2 cho biết là loại video gì (is60s,reset)
    is60s = True
    Reset = False
    if "(60s)" not in MP4_file_name:
        is60s = False
        if "(reset)" in MP4_file_name:
            Reset = True        
    return fulllink,video_des_shorten_link,is60s,Reset
