import json
filepath='D:/little_trick/js_spinfo.json'
bigstafflist=[]
with open(filepath,'r') as f:
    info=json.loads(f.read())
    for f in info:
        try:
            #print(f['stafflist'])
            if f['stafflist'] == []:
                pass
            else:
                bigstafflist.append([f['name'],f['stafflist']])
            #print(len(bigstafflist))
        except:
            pass
print(len(bigstafflist))
print(bigstafflist[0])

for one_staff in bigstafflist[1:]:
    companyname=one_staff[0]
    #print(companyname)
    for one_name in one_staff[1]:
        #print(one_name,companyname)
        for targetstaff in bigstafflist[1:]:
            if not targetstaff == one_staff:
                if one_name in targetstaff[1]:
                    print(companyname,targetstaff[0],one_name)