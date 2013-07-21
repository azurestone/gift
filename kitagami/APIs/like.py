# -*- coding: utf-8 -*-
from flask import Module, render_template
from flask import Flask, make_response,request,abort, redirect, url_for
import json

import datetime
import time
import os.path
import sqldb

app = Module(__name__)

@app.route('', methods=['POST','GET'])
def like():
	
	import like_config
	api = like_config.Conf()	

	if request.method == 'POST':
		for slist in api.Request:
			api.Request[slist] = request.form[slist]
	else :	
		for slist in api.Request:
			api.Request[slist] = request.values[slist]

	db = sqldb.SQLDB("test.db")
	db.New_DB("git")
	j = 0
	tmp = {}
	tmp2 = []
	for i in db.Get_Column("git","gifurl") :
		print  i
		if i == api.Request["gifurl"]:
			print i[3]
			db.UpDate_Column("git","like",i[3]+1,"gifurl",api.Request["gifurl"])
	#print json.dumps(tmp,sort_keys=True, indent=4) 
	
	#return "Hello GIF-MAGAZINE"

	return json.dumps(tmp2,indent=4) 
	