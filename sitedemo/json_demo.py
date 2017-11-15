import json
filepath='D:/little_trick/js_spinfo.json'
bigstafflist=[]
with open(filepath,'r') as f:
    info=json.loads(f.read())
    for f in info:
        try:
            #print(f['stafflist'])
            bigstafflist.append(f['stafflist'])
            #print(len(bigstafflist))
        except:
            pass
#print(len(bigstafflist))
#print(len(info))
overlapinfo=set()
current_index=0
maxnum=1416
#print(info[745])
for staff1 in bigstafflist:
    if not len(staff1) == 0:
        target_index = 0
        if not current_index == 745 or target_index == 745 :
            if not target_index == current_index:
                #print(info[current_index]['name'],info[target_index]['name'])
                for one_staff in staff1:
                    for staff2 in bigstafflist:
                        if one_staff in staff2 and target_index < maxnum and current_index != target_index: #and info[target_index]['name'] != '一起游国际旅行社有限公司':
                            print(current_index, target_index)
                            print(info[current_index]['name'], info[target_index]['name'])
                            print(one_staff, staff2)
                            target_index+=1
                            '''
                            if len(overlapinfo) == 0:
                                overlapinfo.append([info[current_index]['name'], info[target_index]['name']])
                                #print('branch1')
                            elif [info[current_index]['name'], info[target_index]['name']] in overlapinfo or [info[target_index]['name'],info[current_index]['name']] in overlapinfo:
                                pass
                                #print('branch2')
                            elif 1==1:
                                #print('branch3')
                                for ii in overlapinfo:
                                    #print('bb3')
                                    if not info[current_index]['name'] in ii and not info[target_index]['name'] in ii:
                                        overlapinfo.append([info[current_index]['name'], info[target_index]['name']])
                            else:
                                #print('branc4')
                                mycount=0
                                for i in overlapinfo:
                                    if info[current_index]['name'] in i:
                                        overlapinfo[mycount]=overlapinfo[mycount].append(info[target_index]['name'])
                            '''
                                #mycount+=1

    current_index+=1
#print('done')
print(len(overlapinfo))
print(overlapinfo)