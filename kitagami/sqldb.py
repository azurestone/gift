# -*- coding: utf-8 -*-
import sqlite3

class SQLDB:
	#=============================#
	def __init__(self, dbfile):
		#print self.root.tag
		self.con = sqlite3.connect(dbfile)


	#=============================#
	def New_DB(self ,table):
		str = "CREATE TABLE %s (id TEXT, url TEXT, like TEXT, tag TEXT,title TEXT);" % table
		try:
			self.con.execute(str)
		except Exception, ex:
		#	self.con.execute("delete from %s" % n )
			self.con.commit()
	#=============================#
	def Remove_DB(self,table):
		self.con.execute("delete from %s" % table )
		self.con.commit()
	#=============================#
	def Set_Column(self,table,column,val):
		#print "insert into %s ( %s ) values( %s );" % (table , column , val )
		self.con.execute( "insert into %s ( %s ) values( %s );" % (table , column , val ))
	#=============================#
	def Get_Column(self,table,column):
		#print "insert into %s ( %s ) values( %s );" % (table , column , val )
		return self.con.execute( "select %s from %s ;" % ( column , table))
	
	#=============================#
	def UpDate_Column(self,table , setcol ,  setdata , itcol ,  itdate ):
		print "UPDATE %s SET %s = %s WHERE %s = %s;" % ( table , setcol ,  setdata , itcol ,  itdate )
		
		return self.con.execute( "UPDATE %s SET %s = %s WHERE %s = %s;" % ( table , setcol ,  setdata , itcol ,  itdate ))
	#=============================#
	def Commit(self):
		self.con.commit()
	#=============================#
	def Close(self):
		self.con.commit()
		self.con.close()
		self.xmlfp.close()
	#=============================#
	def strmix(self,str,mix):
		str = str + "\"" + mix +  "\"" + ","
		return str
