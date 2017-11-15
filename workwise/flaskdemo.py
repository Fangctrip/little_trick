# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:56:41 2017

@author: fangjw
"""

from flask import Flask
app=Flask(__name__)
@app.route('/')
def hw():
    return "hello world"
app.
