'''
https://www.booking.com/hotel/jp/shiki-niseko.en-gb.html?;checkin=2017-12-06;checkout=2017-12-21;dist=0;group_adults=2;hapos=1;hpos=1;room1=A&#hotelTmpl
'''
'''
https://www.booking.com/hotel/sg/kranji-farm-resort.en-gb.html?checkin=2017-12-06;checkout=2017-12-07;dest_id=-73635;dest_type=city;dist=0;group_adults=2;hapos=1;hpos=1;room1
'''
import requests
import time
from bs4 import BeautifulSoup
import xlrd
import random

filepath='D:/Users/fangjw/Desktop/file_list_fangjw.xlsx'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
cityname=[x.lower() for x in ['-'.join(city.split(' ')) for city in table.col_values(0)]][1000:-1]
countrycode=table.col_values(1)[1000:-1]
hotelname=[x.lower() for x in ['-'.join(hotel.split(' ')) for hotel in table.col_values(3)]][1000:-1]
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}
#url='https://www.booking.com/hotel/sg/kranji-farm-resort.en-gb.html?checkin=2017-12-06;checkout=2017-12-07;dest_id=-73635;dest_type=city;dist=0;group_adults=2;hapos=1;hpos=1;room1'
url='https://www.booking.com/hotel/{}/{}.en-gb.html?checkin=2017-12-06;checkout=2017-12-07;dest_type=city;dist=0;group_adults=2;hapos=1;hpos=1;room1'
def get_info(url):
    roomlist=[]
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html5lib')
    roomname=soup.find_all('a',{'class':'jqrt togglelink '})
    METHOD = 1
    if roomname == None:
        roomname = soup.find_all('i',{'class':"rt_room_type_ico bicon-triangleright"})
        METHOD=2
    if roomname == None:
        roomname = soup.find_all('td',{'class':'ftd'})
        METHOD=3
    if roomname == None:
        roomlist=[]
    else:
        if METHOD == 1:
            for oneroom in roomname:
                roomlist.append(oneroom.text.strip())
        elif METHOD == 2:
            for oneroom in roomname:
                roomlist.append(oneroom)
        else:
            for oneroom in roomname:
                roomlist.append(oneroom.text.strip())
    #print(soup.prettify())
    #print(roomlist)
    return roomlist

#get_info(url)

count=0
with open('booking_info1103.csv','a') as f:
    for country,hotel in zip(countrycode,hotelname):
        print(country,hotel)
        print(url.format(country,hotel))
        result=get_info(url.format(country,hotel))
        f.write(str(result)+'|'+str(hotel)+'\n')
        print(result)
        print('now is scraping the {} one'.format(count))
        count+=1
        sptime=random.randrange(2,8)
        time.sleep(sptime)
        print('*'*50)

#req=requests.get(url,headers=headers)
#soup=BeautifulSoup(req.content,'html5lib')
#roomname=soup.find_all('a',{'class':'jqrt togglelink '})
#print(soup.prettify())
#for oneroom in roomname:
#   print(oneroom.text.strip())