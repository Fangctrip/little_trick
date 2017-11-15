import xlrd
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from selenium import webdriver
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ( "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36" )
driver=webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',desired_capabilities=dcap)
driver.set_page_load_timeout(10)


def get_info(url):
    try:
        driver.get(url)
        print('currtturl: '+str(url))
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        #print(soup.text)
        roominfo=[]
        #if '我们走遍全球，但尚未找到您想要查看的页面。 要不我们开始新的旅程？' in soup.text:
        #    print(url+'failed')
        #else:
        roomlist = soup.find_all('h3', {'class': 'dg-PropertyRoomGroup-header room-group-master-name'})
        if roomlist is None:
            roomlist = soup.findall('a', {'class': 'MasterRoom-headerTitle'})
        if roomlist is None:
            roominfo = []
        if not roomlist == []:
            for room in roomlist:
                roominfo.append(room.text.strip())
    except:
        roominfo=[]
    print(roominfo)
    return roominfo


filepath='D:/Users/fangjw/Desktop/file_list_fangjw.xlsx'
data=xlrd.open_workbook(filepath)
table=data.sheets()[0]
cityname=[x.lower() for x in ['-'.join(city.split(' ')) for city in table.col_values(0)]][403:-1]
countrycode=table.col_values(1)[403:-1]
hotelname=[x.lower() for x in ['-'.join(hotel.split(' ')) for hotel in table.col_values(3)]][403:-1]
mock_url='https://www.agoda.com/zh-cn/' \
         '{}/hotel/{}-{}.' \
         'html?pagetypeid=7&origin=CN&languageId=8&storefrontId=3&currencyCode=CNY&htmlLanguage=zh-cn&trafficType=' \
         'User&cultureInfoName=zh-CN' \
         '&checkIn=2017-12-06&checkout=2017-12-07&los=1&rooms=1&adults=2&childs=0'
count=1
with open('agoda_info.csv','a') as f:
    for city,country,hotel in zip(cityname,countrycode,hotelname):
        print(city,country,hotel)
        print(mock_url.format(hotel, city, country))
        paraseurl=get_info(url=mock_url.format(hotel, city, country))
        print('目前第{}个'.format(count))
        print('---------------------------------------------------')
        count+=1
        sleeptime = random.randrange(1,4)
        f.write(str(paraseurl)+'|'+hotel+'\n')
        time.sleep(sleeptime)

