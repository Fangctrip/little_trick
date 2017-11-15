# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:33:42 2017

@author: fangjw
"""

import itchat
from itchat.content import *
itchat.login()
friends=itchat.get_friends(update=True)
for f in friends:
    print(f['NickName'])
    print(f['Signature'].replace('\n',''))
