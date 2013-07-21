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
def gifread():
	
	import gift_config
	api = gift_config.Conf()	

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
	for i in db.Get_Column("git","*") :
		#print i[0]
		#tmp["id"]  = j#i[0]
		#api.Return["gifurl"]  = i[1]
		#api.Return["like"]  = i[2]
		#api.Return["tag"]  = i[3]
		#api.Return["title"]  = i[4]
		tmp = {	
				#"id": i[0],
				"gifurl" : i[1].strip("\r\n"),
				"like" :  i[2],
				"tag" : i[3],
				"title" : u"%s" % i[4],
				}
		tmp2.append(tmp)
		j = j + 1

	#print tmp
	#print json.dumps(tmp,sort_keys=True, indent=4) 
	
	#return "Hello GIF-MAGAZINE"

	return json.dumps(tmp2,indent=4) 
	