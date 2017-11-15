# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:44:04 2017

@author: fangjw
"""
import xlrd
import xlwt
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
from selenium import webdriver


spinfo='http://productinput.hotel.ctripcorp.com/Hotel-Supplier-Platform/SupplierInfo.aspx?CallType=Update&SupplierID=1311'
login='http://membersint.members.ctripcorp.com/offlineauthlogin/Login.aspx'
usname="fangjw"
psword="DSA9bB2992929292"
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ( "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36" )
driver=webdriver.PhantomJS(executable_path='E:/phantomjs-2.1.1-windows/bin/phantomjs.exe',desired_capabilities=dcap)

filepath="d:/Users/fangjw/Desktop/contactinfo.xlsx"
data=xlrd.open_workbook(filepath)
table=data.sheets()[0]
sumup=table.col_values(0)
maxrow=table.nrows
maxcol=table.ncols
wbk=xlwt.Workbook()
ws=wbk.add_sheet('info')
i=1
for one in sumup[1:]:
    pd=random.randint(3,10)
    if i==1:
        driver.get(login)
        time.sleep(3)
        driver.find_element_by_id("eid").clear()
        driver.find_element_by_id("eid").send_keys(usname)
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys(psword)
        driver.find_element_by_id("btnSubmit").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get(spinfo)
        soup=BeautifulSoup(driver.page_source,'lxml')
        #target=soup.find_all('div',{'class':'activity_tb_box'})
        contact=soup.find(id='ctl00_ContentMain_txtTel')['value']
    else:
        driver.get('http://productinput.hotel.ctripcorp.com/Hotel-Supplier-Platform/SupplierInfo.aspx?CallType=Update&SupplierID={}'.format(str(one).replace('.0','')))
        time.sleep(pd)
        soup=BeautifulSoup(driver.page_source,'lxml')
        contact=soup.find(id='ctl00_ContentMain_txtTel')['value']
    #print(driver.get_cookies())
    ws.write(i-1,1,contact)
    ws.write(i-1,0,str(int(one)))
    print(str(int(one))+'\n'+contact)
    i+=1
wbk.save('spinfo.xls')
driver.quit()