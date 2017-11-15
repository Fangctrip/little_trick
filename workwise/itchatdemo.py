# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:34:01 2017

@author: fangjw
"""

import itchat
itchat.auto_login()
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login()
itchat.run()

a=itchat.get_friends()