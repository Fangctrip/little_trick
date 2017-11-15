#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import re
import json


IPRE=re.compile(r'<td>((\d{1,3}\.)+\d{1,3})</td>')
TYPERE=re.compile(r'<td>(HTTP|HTTPS)</td>')
SPEEDRE=re.compile(r'<div class="bar_inner (slow|fast|medium)" style="width:\d{1,3}%">')

headers = {
    'accept-encoding': "gzip, deflate, sdch",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36",
    #'Referer':'http://www.xicidaili.com/nt/'
    }

def get_ip():
    data={}
    iplist=[]
    req=requests.get('http://www.xicidaili.com/nt/',headers=headers).content
    soup=BeautifulSoup(req,'lxml')
    tb=soup.find('table',{'id':'ip_list'})
    a=tb.find_all('tr')
    for b in a[1:]:
        ip=IPRE.search(str(b)).groups()[0]
        type=TYPERE.search(str(b)).groups()[0]
        SPRE=SPEEDRE.findall(str(b))
        if SPRE[0] == 'fast' and SPRE[1] == 'fast' and verify_ip(ip,type):
            data = {
                'ip':ip,
                'type':type
            }
            iplist.append(data)
        #print(SPRE)
            #print(b)
        #print(ip,type,SPRE,sep='|')
        #print('-'*100)
    print(iplist)
    with open('ip.json','w') as f:
        f.write(json.dumps(iplist))
    return iplist
def verify_ip(ip,type):
    proxies={
        type:ip
    }
    req=requests.get('https://www.baidu.com/',proxies=proxies)
    if req.status_code == 200:
        return True
    else:
        return False
if __name__ == '__main__':
    with open('ip.json','w') as f:
        json.dumps(get_ip())
        f.write(json.dumps(get_ip()))