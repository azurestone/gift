# -*- coding: utf-8 -*-
import sqlite3
import sqldb
import csv





db = sqldb.SQLDB("test.db")
db.New_DB("git")

spamReader = open('gif.csv', 'rb')
for row in spamReader:
	tmp = row.split(',')
	print tmp[0]
	data = ""
	str = ""
	str = db.strmix(str, "id")
	data = db.strmix(data, tmp[0])
	str = db.strmix(str, "title")
	data = db.strmix(data, tmp[1])
	str = db.strmix(str, "gifurl")
	data = db.strmix(data, tmp[2])
	str = db.strmix(str, "tag")
	data = db.strmix(data, "game")
	str = db.strmix(str, "like")
	data = db.strmix(data, "0")
	str = str.rstrip(",") 
	data = data.rstrip(",") 
	
	db.Set_Column("git",str,data)
	db.Commit()
	

for i in db.Get_Column("git","like") :
	print i
	