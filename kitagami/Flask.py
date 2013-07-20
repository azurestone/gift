# -*- coding: utf-8 -*-
from flask import Flask, make_response,request,abort, redirect, url_for, make_response
import pymongo
import json  
import datetime
import time

app = Flask(__name__)

#_URL_ = "kitagami.org"
_URL_ = "localhost"
_PORT_ = 1234

from APIs import root
app.register_module(root.app, url_prefix="/")



if __name__ == '__main__':
	app.debug = True
	app.run(host=_URL_,port=_PORT_)

