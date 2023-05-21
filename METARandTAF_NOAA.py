import requests#爬虫
import pandas.io.clipboard as cb#剪贴板的
from bs4 import BeautifulSoup#爬虫的
import time
airportaico=input("请输入一个机场ICAO:")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
response = requests.get("https://aviationweather.gov/metar/data?ids="+airportaico+"&format=decoded&hours=0&taf=on&layout=on",headers=headers)
html=response.text#https://aviationweather.gov/metar/data?ids=zspd&format=decoded&hours=0&taf=on&layout=on
soup=BeautifulSoup(html,"html.parser")
all_titles=soup.findAll("td")#td
print("首先严止DFA及其连飞平台使用!")
# for td in all_titles:
    # title_string = td.string
    # print(title_string)
ap_meter=[]
for td in all_titles:
    title_string = td.string
    # print(title_string)#测试|打印所有td标签的内容
    ap_meter.append(title_string)#把完整报文存到变量里
# print(ap_meter)测试|用途
print("本产品数据来源:NOAA,网址:https://aviationweather.gov/")
time.sleep(1)
print("METAR报文:",ap_meter[3])
time.sleep(0.5)
print("TAF报文:",ap_meter[21])#21或者21
time.sleep(1)
cb.copy(ap_meter[3]+"\n"+ap_meter[21])
time.sleep(1)
print("METAR和TAF报文已复制在剪贴板")
yn=input("请输入是否输出完整信息(包括英文解析)[y/n]")
if yn == "y" or yn == "Y":
    time.sleep(1)
    print("——————下面是报文解析——————")
    time.sleep(1)
    print("完整数据:")
    for td in all_titles:
        title_string = td.string
        time.sleep(0.1)
        print(title_string)
elif yn == "n" or yn == "N":
    print("感谢您的使用,作者B站:https://space.bilibili.com/1118162018")
    time.sleep(60)
elif yn == "114514" or yn == "191910" or yn == "114514191910":
    print("您发现了新大陆,达成:恶臭哥")
    time.sleep(60)
else:
    print("您发现了新大陆,达成:成就BUG检测员")
    time.sleep(60)
    # print("提醒一下接下来会循环114514191910次哦")
    # for i in range(114514191910):
    #     print("您发现了新大陆,作者是")
    # print("大帅哥!")
