import flask
from flask import render_template
import json
import sys

app = flask.Flask(_name_)

@app.route('/')
def displayHomepage():
	return render_template('homepage1.html')
	
if _name_ == '_main_':
	if len(sys.argv) != 3:
		print('Usage: {0} host post'.format(sys.argv[0]), file = sys.stderr)
		exit()
		
	host = sys.argv[1]
	port = sys.argv[2]
	app.run(host = host, port = port)
