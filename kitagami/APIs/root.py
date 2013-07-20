# -*- coding: utf-8 -*-
from flask import Module, render_template, make_response,url_for
app = Module(__name__)


@app.route("/")
def index():
#	url_for('static', filename="style.css")

#	url_for('static', filename="ansimpletop_slice_r2_c2.png")


	response = make_response(render_template('index.html'))
	response.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
	#response.cache_control.no_cache = False
	return response

