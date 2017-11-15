import json
from datetime import datetime as dt
from datetime import timedelta as td
print(dt.today())
print(dt.today()+td(days=1))
print(dt.today().strftime('%Y/%m/%d'))
print(dt(year=2017,day=20,month=11).strftime('%Y/%m/%d'))
#with open('D:/Users/fangjw/Desktop/sb.html','r',encoding='utf-8') as f:
    #req=f.read()
#with open('ip.json','r') as f:
#    iplist=json.loads(f.read())
##    for info in iplist:
 #       print(info)
from get_ip import verify_ip

print(verify_ip('27.219.38.130','HTTP'))
