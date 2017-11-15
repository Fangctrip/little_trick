# -*- coding: utf-8 -*-
"""
Part1利用pyguiaui模拟手工浏览天眼查,同时保存网页.
Part2利用Os,Beaufitulsoup模块解析本地网页，获取TargetData
Created on Wed Oct 25 15:21:32 2017
@author: fangjw

存网页
"""
import pyautogui as pg
import time
from bs4 import BeautifulSoup
#import random
import xlwt
import os
import json
#time.sleep(2)
#pg.click()
#oldstr='携程'
# needstr=str(oldstr.encode('utf-8')).replace('\\x','%').upper()
#targeturl='https://www.tianyancha.com/search?key={}&checkFrom=searchBox'.format(needstr)
#pg.typewrite('asdasdasd')
urlspace=[548,42]
spnamespace=[189,539]
closesp=[186,10]

pg.FAILSAFE = True
def convert_url(spname):
    needname=str(spname.encode('utf-8')).replace('\\x','%').replace('b\'','',1).strip('\'').upper()
    targeturl='https://www.tianyancha.com/search?key={}&checkFrom=searchBox'.format(needname)
    return targeturl

def get_url():
    current_url = convert_url('携程')
    pg.moveTo(urlspace[0],urlspace[1],duration=0.4)
    time.sleep(0.5)
    pg.click()
    pg.press('delete')
    pg.typewrite(current_url,interval=0.02)
    pg.press('enter')
    pg.press('enter')
    pg.moveTo(189,539,duration=0.4)
    pg.click()
    time.sleep(2)
    pg.moveTo(closesp[0],closesp[1],duration=0.4)
    pg.click()

def save_url():
    x_p=random.randint(70,700)
    y_p=random.randint(150,162)
    pg.moveTo(x_p,y_p,duration=0.4)
    pg.rightClick()
    pg.moveRel(100,100,duration=0.25)
    pg.click()
    pg.moveTo(465,476)
    pg.click()
    pg.click()
    
def parase_url(filepath):
    with open(filepath,'r',encoding='utf-8') as f:
        stafflist=[]
        try:
            soup=BeautifulSoup(f.read(),'html5lib')
            try:
                name=soup.find('span',{'class':'f18 in-block vertival-middle sec-c2'}).text
            except:
                name=''
            try:
                status=soup.find('div',{'class':'baseinfo-module-content-value statusType1'}).text
            except:
                status=""
            try:
                updatetime=soup.find('span',{'class':'updatetimeComBox'}).text
            except:
                updatetime=""
            try:
                address=soup.find('span',{'class':'in-block overflow-width vertical-top pr10'})['title']
            except:
                address=''
            runpunish=soup.find('div',{'id':'_container_punish'})
            lawsuit=soup.find('div',{'id':'_container_lawsuit'})
            courtnotice=soup.find('div',{'id':'_container_court'})
            abnormal=soup.find('div',{'id':'_container_abnormal'})
            historyname=soup.find('div',{'class':'historyName45Bottom position-abs new-border pl8 pr8 pt4 pb4'})
            mainstaff=soup.find_all('a',{'class':'overflow-width in-block vertival-middle pl15 mb4'})
            stafftitle=soup.find_all('div',{'class':'in-block f14 new-c5 pt9 pl10 overflow-width vertival-middle'})
            taxperformance=soup.find('div',{'id':'_container_taxcredit'})
            mangagecheck=soup.find_all('div',{'id':'_container_check'})
            #for s,b in zip(mainstaff,stafftitle):
            #    stafflist.append(s.text+':'+b.text) 包含职位
            for b in mainstaff:
                stafflist.append(b.text)
            stockholders=soup.find('div',{'id':'_container_holder'})
            #是否有2016年报
            annualreport=soup.find_all('span',{'class':'pl5 pt15 in-block'})
            historyname='' if historyname==None else historyname.text.strip()
            ishonest='F'
            for oneyearreport in annualreport:
                if '2016' in oneyearreport.text:
                    ishonest='T'
                    break
            #print(ishonest)
            #print(annualreport)
            #print(mangagecheck)
            #basicinfo=soup.find('table',{'class':'table companyInfo-table f14'}).find_all('td')
            #for xx,yy in zip(basicinfo[:-1:2],basicinfo[1::2]):
            #    print(xx.text,yy.text,sep='\n---------\n')
            #print(name,status,lawsuit,courtnotice,abnormal,updatetime,sep='|||')
            absum=''
            suitsum=''
            courtsum=''
            punishsum=''
            stockholdersum=''
            taxsum=''
            #解析税务情况 年份/纳税评级/类型/纳税人识别号/评价单位
            if not taxperformance==None:
                taxall=taxperformance.find_all('tr')[1:]
                for onetax in taxall:
                    ot=onetax.find_all('td')
                    singletax=''
                    for sgtx in ot:
                        singletax=singletax+'/'+sgtx.text.strip()
                taxsum=taxsum+"#"+singletax
            #print(taxsum)
            #解析股东信息 股东/出资比例/认缴出资
            if not stockholders==None:
                stall=stockholders.find_all('tr')[1:]
                for oneholder in stall:
                    oh=oneholder.find_all('td')
                    singleholder=''
                    for sgoh in oh:
                        singleholder=singleholder+'/'+sgoh.text.strip()
                stockholdersum=stockholdersum+'#'+singleholder
            #print(stockholdersum)
            #解析经营异常
            #例如日期,列如原因，决定机关，移除日期，移除原因，移除机关
            if not abnormal==None:
                aball=abnormal.find_all('tr')[1:]
                for oneab in aball:
                    o=oneab.find_all('td')
                    singleab=''
                    for oo in o:
                        singleab=singleab+'/'+oo.text
                    absum=absum+"#"+singleab
                    #absum=absum + '/' + oneab.text
            #解析法院表格 日期/裁判文书/案由/案件身份/案件号
            if not lawsuit==None:
                ls=lawsuit.find_all('tr')[1:]
                for onecase in ls:
                    casedetail=onecase.find_all('td')
                    suit=''
                    for case in casedetail:
                        suit=suit+'/'+case.text
                    #print(suit)
                    suitsum=suitsum+'#'+suit
            #print(updatetime,name,status,absum,suitsum,sep='\n------------\n')
            #解析法院公告  公告时间/上诉方/被诉方/公告类型/法院
            if not courtnotice==None:
                ctall=courtnotice.find_all('tr')[1:]
                for onect in ctall:
                    ctdetail=onect.find_all('td')[:5]
                    ct=''
                    for c in ctdetail:
                        ct=ct+'/'+c.text
                    courtsum=courtsum+'#'+ct
            #解析行政处罚 处罚日期/决定书文号/类型/决定机关
            if not runpunish==None:
                pshall = runpunish.find_all('tr')[1:]
                for oneph in pshall:
                    singleph = ''
                    one = oneph.find_all('td')
                    for ph in one:
                        singleph=singleph+'/'+ph.text
                    punishsum=punishsum+'#'+singleph
            ##print(soup.prettify())
            basicinfo=soup.find('table',{'class':'table companyInfo-table f14'}).find_all('td')
            #解析工商注册号/组织机构代码/统一信用代码/企业类型/纳税人识别号/行业类型/营业期限/核准日期/登记机关/英文名称/注册地址/经营范围
            infolist=[]
            infostring=''
            for basic in basicinfo:
                if not 'table-left' in str(basic) and str(basic.text)!='':
                    infolist.append(basic.text)
                    infostring=infostring+"#"+basic.text
                    #print(basic.text)
                    #print('\n---------------------')

            #更新时间/名字/状态/异常情况/诉讼问题/法院公告/行政处罚/主要人员/纳税情况/公司地址/是否有2016年报/基础信息
            #print(updatetime,name,status,absum,suitsum,courtsum,punishsum,sep='\n----------\n')

            data = {
                'updateteime':updatetime,
                'name':name,
                'historyname':historyname,
                'status':status,
                'absum':absum.strip('\#').split('#'),
                'suitsum':suitsum.strip('\#').split('#'),
                'courtsum':courtsum.strip('\#').split('#'),
                'punishsum':punishsum.strip('\#').split('#'),
                'stafflist':stafflist,
                'stockholdersum':punishsum.strip('\#').split('#'),
                'taxsum':taxsum.strip('\#').split('#'),
                'address':address,
                'ishonest':ishonest,
                'infolist':infolist
            }
        except:
            data={}
        print(data)
        #return data
        #return [updatetime,name,historyname,status,absum,suitsum,courtsum,punishsum,stafflist,stockholdersum,taxsum,address,ishonest,infostring]
        return [name,'|',stafflist]
        #print(abnormal)
#time.sleep(2)
def none_sense():
    wbk=xlwt.Workbook()
    ws=wbk.add_sheet('wbk')
    rootpath='D:/root/'
    verifystring='【信用信息_诉讼信息_财务信息_注册信息_电话地址_招聘信息】查询-天眼查'
    filelist=os.listdir(rootpath)
    rowcount=0
    for file in filelist:
        if verifystring in file:
            filename=file[:file.find('_')]
            #print(filename)
            filepath=''.join([rootpath,file])
            one_row=parase_url(filepath)
            ws.write(rowcount,1,str(one_row))
        rowcount+=1
        print('目前到第{}个,总共{},完成度{}'.format(rowcount,len(filelist),round(rowcount/len(filelist),2)))

    wbk.save('infolistaaa.xls')
none_sense()

'''
    pass
rootpath='D:/root/'
infolist=[]
filelist=os.listdir(rootpath)
for file in filelist:
    filepath=''.join([rootpath,file])
    one_data=parase_url(filepath)
    infolist.append(one_data)
with open('js_spinfo.json','w') as f:
    f.write(json.dumps(infolist))
'''



#with open('supplier_censor.csv','a',encoding='utf-8') as f:
#    f.write(parase_url('D:/Users/fangjw/Downloads/上海携程商务有限公司_【信用信息_诉讼信息_财务信息_注册信息_电话地址_招聘信息】查询-天眼查.html')+'\n')
print(str(__name__))