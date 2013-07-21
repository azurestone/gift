# -*- coding: utf-8 -*-
from flask import Flask, make_response,request,abort, redirect, url_for, make_response
import json  
import datetime
import time


import sqldb


app = Flask(__name__)

_URL_ = "0.0.0.0"
#_URL_ = "localhost"
_PORT_ = 8080

from APIs import root
app.register_module(root.app, url_prefix="/")

from APIs import gift
app.register_module(gift.app, url_prefix="/api/gifmagazine")
from APIs import like
app.register_module(like.app, url_prefix="/api/gifmagazine/like")


if __name__ == '__main__':
	app.debug = True
	app.run(host=_URL_,port=_PORT_)

