(Vietnamese only :3)
# **Đoạn Script tự động format và đăng video hàng loạt, lên 2 kênh youtube [Songlongmedia official](https://www.youtube.com/c/Songlongmedia) và [Songlongmedia Unboxing - 60s](https://www.youtube.com/channel/UCf1XWYqYED38dYmK2dQb44A/videos)**

## **Các Python Package cần cài đặt:**
>bitlyshortener  
selenium  
googlesearch  
googleapiclient.http  
Google   


## **Đặt vấn đề:**   
Mỗi 1 sản phẩm tai nghe có một video hướng dẫn sử dụng và hầu hết có cả video unboxing, Cần thu thập dữ liệu về sản phẩm để format tên và phần mô tả video khi đăng lên youtube.
- Title của video unbox: ***Unboxing 60s- <tên sản phẩm> - Songlongmedia***
- Title của video Hướng dẫn sử dụng: ***Hướng dẫn sử dụng và reset <tên sản phẩm>***
- Phần mô tả video:   
    ***#hashtag liên quan tới sản phẩm*   
    *Tên sản phẩm*   
    *Link mua hàng đã được rút gọn (shopee/songlongmedia.com)*   
    *Miêu tả sản phẩm***

## **Ý tưởng:**  
- Bước 1:   
+Dữ liệu đầu vào là các video cần được đăng.   
+Mỗi video có tên với format < (loại video)>< tên sản phẩm>.mp4   
>VD:  
Video hướng dẫn sử dụng và reset airpods pro có tiêu đề  **(reset) Airpods Pro.mp4**   
>Video mở hộp Jabra có tiêu đề **(60s)Jabra Elite 75t.mp4**
- Bước 2:  
+Với feed là tên của video(chính là tên sản phẩm), Sử dụng googlesearch để tìm link mua sản phẩm trên [trang web chính thức của cửa hàng](https://songlongmedia.com/).  
+Sử dụng **Selenium**, để Web-scrapping thu nhập thông tin và tạo hashtag cho sản phẩm.
- Bước 3:  
+Với feed là tên của video(chính là tên sản phẩm), Sử dụng googlesearch để tìm link mua sản phẩm ở [gian hàng shopee](https://shopee.vn/songlongmediashop)  
+Sử dụng **bitlyshortener** để rút gọn link mua sản phẩm trên [gian hàng shopee](https://shopee.vn/songlongmediashop) và trên [trang web chính thức của cửa hàng](https://songlongmedia.com/).
- Bước 4:   
+Tạo file json với tất cả những dữ liệu thu thập được cho từng video.  
+Sử dụng **Google API (được cung cấp bởi tài khoản Google Cloud Service)** để đăng video lên kênh Youtube 
    
    
