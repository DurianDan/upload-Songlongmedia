#!/usr/bin/python3 
from selenium import webdriver
import json

below_des = '''{}

{}
link sản phẩm: {}

{}

---------------------------------
HỆ THỐNG CỬA HÀNG - SONGLONGMEDIA
Shop 1: Số 98.F phố Nguyễn Thái Học, Ba Đình, Hà Nội.
Shop 2: 12 ngõ 860 phố Minh Khai, Hai Bà Trưng, Hà Nội.
Shop 3: 12 Ngõ 282 Nguyễn Khoái, Hai Bà Trưng, Hà Nội. 
----------------------
📌 #Website Songlongmedia
https://songlongmedia.com

📌 Trang #Facebook Songlongmedia
https://www.facebook.com/songlongmedia

📌 Tham gia cộng đồng người yêu tai nghe để giao lưu, trao đổi kinh nghiệm
https://bit.ly/3edmis9

📌 Kênh giải trí #Tiktok
https://www.tiktok.com/@songlongmedia

📌 Gian hàng #Shopee 
https://shopee.vn/songlongmediashop

📌 Phone, Zalo, iMess, Viber
094.1144.666

👍 ĐĂNG KÍ KÊNH ĐỂ ỦNG HỘ TEAM REVIEW NHA!'''
def get_texts(full_link:str,shorten_link:str,is60s = True,reset = True):
    '''function tạo ra tên video,mục miêu tả, và Tags'''
    driver = webdriver.Firefox()
    driver.get(full_link)#mở link sản phẩm
    xemthem = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[2]/div[2]/div[2]")
    xemthem.click()#ấn vào chữ "xem thêm"

    #1 tạo tên video (video_name)
    if not is60s:
        if reset:
            video_name = "Hướng dẫn sử dụng và reset {}"
        else:
            video_name = "Hướng dẫn sử dụng {}"
    else:
        video_name = "Unboxing 60s - {} - songlongmedia"
    product_name =driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[2]/div[1]/h1").text #đây là tên sản phẩm ở dạng string (in được)
    video_name = video_name.format(product_name)

    #2 tạo tags (video_tags)
    video_tags = ""
    video_des_tags = ""
    product_summery_html = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[1]/div[2]/div[2]/div[1]") #đây là mục miêu tả sản phẩm ở dạng html (ko in được)
    tags = set()#đây là tags (cách nhau bởi dấu phẩy, ở mục tags riêng)
    for i in product_summery_html.find_elements_by_xpath(".//*"):#tìm tất cả chữ tô đậm trong mục miêu tả
        if i.value_of_css_property("font-weight") == "700":#sau đó
            tag = i.text
            if ">" in tag:
                tag = tag.replace(">"," lớn hơn ")
            if "<" in tag:
                tag = tag.replace("<"," nhỏ hơn ")
            tags.add(tag.strip("✔ ,.:\\/:;\'\"?!@#$\%^&*\(\)-_=+`~")) #thêm vào tags (loại bỏ các ký hiệu thừa)
    if is60s:
        video_tags= "Songlongmedia Unboxing 60s, "
        video_des_tags = "#songlongmedia #unboxing60s"
    else:
        video_tags= "Songlongmedia,Hướng dẫn sử dụng,cách dùng,"
        video_des_tags = "#songlongmedia #huongdansudung #cachdung #hdsd"
    for i in tags:
        video_tags +=(i+",")

    #3 tạo mục miêu tả sản phẩm (video_description)
    #3.1 tạo tags trong mục miêu tả (video_des_tags)
    tags_in_des = set() #đây là tags trong phần miêu tả (cách nhau bởi dấu "#")
    for i in tags:
        for j in i.split():
            if "<" in j: #youtube không cho phép có dấu "<",">" ở mục miêu tả
                j.replace("<"," nhỏ hơn ")#nên cần thay thế
            if ">" in j:
                j.replace('>',' lớn hơn ')
            tags_in_des.add(j.strip("✔ ,.:\\/:;\'\"?!@#$\%^&*\(\)-_=+`~"))
    for i in tags_in_des:
        video_des_tags += (" #"+i)
    #3.2 tạo mục miêu tả (video_description)
    Angleinit = False
    video_description= below_des.format(video_des_tags,product_name,shorten_link,product_summery_html.text.replace("\n","").replace("✔","\n✔"))
    angles = ["<",">"]
    angles_alt = ["nhỏ hơn","lớn hơn"]
    for i in range(2):
        if angles[i] in video_des_tags:
            Angleinit = True
            if Angleinit:
                video_description = video_description.replace(angles[i],angles_alt[i])
    driver.quit()
    return video_name,video_description,video_tags

#lưu tất cả mô tả video vào folder "json_description"
def save_json(MP4_name:str,full_link:str,shorten_link:str,MP4_file_name:str,is60s = True,reset = True):
    name,des,tags = get_texts(full_link,shorten_link,is60s = is60s,reset = reset)
    video_dict = {"video_name":name,"video_des":des,"video_tags":tags,"MP4_file_name":MP4_file_name}
    j = json.dumps(video_dict)
    with open("/home/duriandan/learning/personal project/upload Songlongmedia/json_description/{}.json".format(MP4_name),"w") as video_json:
        video_json.write(j)
        video_json.close()

