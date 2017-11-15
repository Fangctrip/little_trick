import xlrd
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
from lxml import html
from lxml import etree

filepath='D:/hotel_list.xlsx'
data=xlrd.open_workbook(filepath)
table=data.sheets()[0]
hotellist=[str(x)[:-2] for x in table.col_values(0)[996:]]
#print(hotellist)
#proxy=webdriver.Proxy()
#proxy.proxy_type=ProxyType.MANUAL
#proxy.http_proxy=''
#proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ( "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36" )
driver=webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/bin/phantomjs.exe',
                           desired_capabilities=dcap,
                           service_args=['--ignore-ssl-errors=true','--load-images=false'])

driver.set_page_load_timeout(10)
driver.set_window_size(1280,4000)



def ctrip_price(hotelid,adate):
    url='http://m.ctrip.com/webapp/hotel/hoteldetail/{mh}.html?days=1&atime={dt}&contrl=0&num=undefined&biz=undefined'.format(mh=hotelid,dt=adate)
    driver.get(url)
    #soup=BeautifulSoup(driver.page_source,'lxml')
    #print(soup.prettify())
    #roomlist=soup.find_all('div',{'class':'room-bd'})
    tree=etree.HTML(driver.page_source)
    pricelist=tree.xpath(u'//div[@class="cell-end dt-cell room--space2 js_baseroomtoggle "]//span[@class="js-cas-p"]')
    roomlist=tree.xpath(u'//div[@class="cell-star room--space3 js_show_baseroom"]//h3')
    for room,price in zip(pricelist,roomlist):
        print(hotelid,room.text,price.text,sep='---')
        f.write(','.join([hotelid,room.text,price.text])+'\n')
    print(url)
    #获取起始价格//div[@class="cell-end dt-cell room--space2 js_baseroomtoggle "]//span[@class="js-cas-p"]
    #获取房型名称//div[@class="cell-star room--space3 js_show_baseroom"]//h3
    #print(roomlist)
    #for r in roomlist:
    #    print(r)
    #    print('*'*50)

with open('haha{}.csv','a') as f:
    count=0
    rest=0
    for ohotel in hotellist:
        try:
            if rest%10!=0:
                ctrip_price(ohotel,'20171120')
                print('not is scrping the {} one,total{} one'.format(count,len(hotellist)))
                count+=1
                rest+=1
                time.sleep(random.randrange(5,10))
            else:
                time.sleep(1)
                rest+=1
                print('休息20秒')
        except:
            print("got blocked,rest for 3 minutes")
            time.sleep(180)
            driver.delete_all_cookies()
            driver.quit()

#driver.quit()