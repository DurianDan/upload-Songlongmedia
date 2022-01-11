#!usr/bin/python3
from glob import glob
from meta_data_get_texts import meta_data
from get_texts import get_texts,save_json
import selenium
token = "1e9b034f7e38910d13845f5621992722ff1fe707"
list_error_link =[]
#for i in glob("/home/duriandan/learning/personal project/upload Songlongmedia/test_video/*"):
for i in ['(60s)Tai nghe Bluetooth Earldom BH59 (Qua Xương)', '(60s)Behringer HC 2000BNC', '(60s)Behringer BB 560M', '(60s)Behringer HPX6000', '(60s)Behringer SD251', '(60s)Blon BL03', '(60s)HifiMan HE400se']:
    print(i)
    MP4_name = i[i.rfind(")")+1:i.rfind(".")]
    MP4_file_name = i[i.rfind("/")+1:i.rfind(".")]
    fulllink,shortlink,is60,rese = meta_data(MP4_file_name,token)
    try:
        save_json(MP4_file_name,fulllink,shortlink,i,is60s = is60,reset = rese)
    except selenium.common.exceptions.NoSuchElementException or selenium.common.exceptions.ElementNotInteractableException:
        list_error_link.append(MP4_name)
        print(i)
        alt_full_link = input("Google không tìm được link sản phẩm chính xác cho video trên, Hãy paste link trực tiếp vào đây:")
        fulllink,shortlink,is60,rese = meta_data(MP4_file_name,token,alt_full_link)
        save_json(MP4_file_name,fulllink,shortlink,i,is60s = is60,reset = rese)
        continue
