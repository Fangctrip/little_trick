#!/usr/bin/python
import requests
from lxml import etree
from datetime import datetime as dt
from datetime import timedelta as td
import xlrd
from get_ip import get_ip
import time

filepath = 'D:/hotel_list.xlsx'
data = xlrd.open_workbook(filepath)
table = data.sheets()[0]
hotellist = [str(x)[:-2] for x in table.col_values(0)[1:]]

headers = {
    'accept': "text/html",
    'accept-encoding': "gzip, deflate, sdch",
    'accept-language': "zh-CN,zh;q=0.8",
    'connection': "keep-alive",
    'content-type': "application/json",
    #'cookie': "supportwebp=true; JSESSIONID=2DE68183209FA58816A237266B50BC73; _abtest_userid=176ed5e7-8077-4787-acfd-212227236d2c; traceExt=campaign=CHNbaidu81&adid=index; _f_l_hk=1; Customer=HAL=ctrip_gb; _fpacid=09031171410784359139; GUID=09031171410784359139; FHXSearch_Cities=from=%E4%B8%8A%E6%B5%B7&to=%E4%B8%BD%E6%B1%9F&checkin=%E4%B8%BD%E6%B1%9F; ibulocale=en_us; ibulanguage=en; Session=SmartLinkCode=U172638&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; TraceSessionEx=FAA041EDEAAB35B8FE1620EB92A38A3C; corpid=; corpname=; CtripUserInfo=VipGrade=0&UserName=%b7%bd%bc%ce%95%a5&NoReadMessageCount=1&U=D6FA4257CEA975CD6A45E4FC5A0025C9; AHeadUserInfo=VipGrade=0&UserName=%b7%bd%bc%ce%95%a5&NoReadMessageCount=1&U=D6FA4257CEA975CD6A45E4FC5A0025C9; LoginStatus=1%7caipga4lat4u52e14vobt4kbx110118%2c; cticket=8145CC7FA070AF862D5DFC336026BC8917516AB78EC2D702F61724363FB94410; DUID=u=8310FD560AB25F900116474E67D737C1&v=0; IsNonUser=F; ticket_ctrip=uoeOwviAJ6VQEgTNwLuTqSV9j/bS+aOP3Riia1P+kyQbgkQZsD2gic//9BgQpGQilxiQMH87GBPufRh7q8CJIRvJNotmxB0gNZFuf1VH08/GxUYprDz8KTHs51WCSxitdXJgpMlZVAEjHtuclilWA84a5HZxvgX82WQY62tt0ov58Yj6p87VoTEZroeP4YaZ3/7Qo3RpshLGFU+WlX6R26636yRLszvUU558vVNBGTUPGluxWzc3edZWApNssvtnubpv32LsVrlyAO44ft/SGT2xNqgS9fAi0iJdV+BV74c5c4mS0jWyDw==; login_type=6; login_uid=8329DA2A453036A1EC13BCBC21D762F5; appFloatCnt=32; FD_SearchHistorty={\"type\":\"S\",\"data\":\"S%24%u4E0A%u6D77%28SHA%29%24SHA%242017-11-18%24%u91CD%u5E86%28CKG%29%24CKG\"}; ASP.NET_SessionSvc=MTAuMTUuMTI4LjMyfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTUwOTk3MTE2MzQzNQ; Union=OUID=20174016567967&AllianceID=2183&SID=23047&SourceID=&Expires=1511140925896; TicketSiteID=SiteID=1001; adscityen=Shanghai; __utma=13090024.1030275237.1508457983.1510566464.1510640397.23; __utmc=13090024; __utmz=13090024.1510640397.23.23.utmcsr=ctrip.com|utmccn=(referral)|utmcmd=referral|utmcct=/; IntHotelCityID=splitsplitsplit2018-02-15split2018-02-16splitsplitsplit1split1; DomesticHotelCityID=undefinedsplitundefinedsplitundefinedsplit2017-11-14split2017-11-15splitundefined; _bfs=1.4; __zpspc=9.96.1510643919.1510643935.4%233%7Cserver.sh.ctriptravel.com%7C%7C%7C%7C%23; _bfi=p1%3D100101991%26p2%3D102003%26v1%3D772%26v2%3D771; _bfa=1.1508457980744.mmjzu.1.1510636364121.1510645180673.98.778.212094; MKT_Pagesource=H5; Mkt_UnionRecord=%5B%7B%22aid%22%3A%224897%22%2C%22timestamp%22%3A1510206289982%7D%2C%7B%22aid%22%3A%222183%22%2C%22timestamp%22%3A1510645180867%7D%5D; _jzqco=%7C%7C%7C%7C1510620512078%7C1.1740182427.1508457982808.1510645062991.1510645180884.1510645062991.1510645180884.undefined.0.0.516.516; _ga=GA1.2.1030275237.1508457983; _gid=GA1.2.1813362509.1510531747; _gat=1; page_time=1510629944325%2C1510632781438%2C1510632796251%2C1510632804977%2C1510632924445%2C1510636364565%2C1510637751602%2C1510637754196%2C1510638200950%2C1510638203791%2C1510639613288%2C1510639661159%2C1510639692755%2C1510639695865%2C1510640394455%2C1510640397208%2C1510643915983%2C1510643918954%2C1510643928388%2C1510643932767%2C1510643944462%2C1510643956653%2C1510645058484%2C1510645063242%2C1510645181047; _RF1=140.207.231.6; _RSG=N44Wo_gs1XBypk8uj_J4tB; _RDG=28d7016f7a06452b322db8af4c61c522db; _RGUID=b841daaf-f280-4117-bdc4-4ffb7822ecfc",
    'host': "m.ctrip.com",
    'referer': "http://m.ctrip.com/webapp/hotel/hoteldetail/{}.html?days=1",
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X; en-us) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
    'x-requested-with': "XMLHttpRequest",
    'cache-control': "no-cache",
    }


def ctrip_price(htid,year,month,day,PROXY):
    global headers
    inday = dt(year=year,month=month,day=day)
    outday = inday + td(days = 1)
    headers['referer'] = headers['referer'].format(htid)
    proxies={PROXY['type']:PROXY['ip']}
    print(headers['referer'])
    url = 'http://m.ctrip.com/webapp/hotel/j/hoteldetail/dianping/rooms/{}?inday={}&outday={}'.format(
        htid,inday.strftime('%Y/%m/%d'),outday.strftime('%Y/%m/%d'))
    req = requests.get(url,headers = headers,proxies=proxies)
    #soup=BeautifulSoup(req.text.encode('utf-8'),'lxml')
    #print(req.encoding)
    #print(soup.prettify())
    tree = etree.HTML(req.text.encode('utf-8').decode('utf-8'))
    pricelist = tree.xpath(u'//div[@class="cell-end dt-cell room--space2 js_baseroomtoggle "]//span[@class="js-cas-p"]')
    roomlist = tree.xpath(u'//div[@class="cell-star room--space3 js_show_baseroom"]//h3')
    for room,price in zip(pricelist,roomlist):
        print(room.text,price.text,sep = '---')
        #f.write(','.join([hotelid,room.text,price.text])+'\n')
    print(url)

#ctrip_price(392668,2017,11,20)
if __name__ == '__main__':
    iplist = get_ip()
    currentip = iplist.pop()
    for hotel in hotellist:
        time.sleep(3)
        try:
            print('now using ip: {}'.format(currentip))
            ctrip_price(hotel,2017,11,20,currentip)
        except:
            if len(iplist) != 0:
                currentip = iplist.pop()
                print('currentip has changed to ip: {}'.format(currentip))
                ctrip_price(hotel, 2017, 11, 20, currentip)
            else:
                print('run out of ip, will get a new batch: {}')
                iplist=get_ip()
                currentip = iplist.pop()
                print('currentip has changed to: {}'.format(currentip))
                ctrip_price(hotel, 2017, 11, 20, currentip)




