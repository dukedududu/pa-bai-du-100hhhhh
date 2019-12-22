#爬取一百次网页 
import requests,time
starttime=time.time()
for i in range(1,101):
    try :
        r=requests.get("https://www.baidu.com")
        r.rasie_for_status()
        r.encoding=r.apparent_encoding
        print( r.text)
    except :
        print("发生异常")
endtime=time.time()
print("访问网页一百次时间： ",endtime-starttime)
