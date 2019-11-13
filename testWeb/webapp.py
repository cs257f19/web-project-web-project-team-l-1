import flask
from flask import render_template
import json
import sys
from datasource import *

app = flask.Flask(__name__)
dataConnection = DataSource('yuez', 'glass944happy').tryConnect()

@app.route('/')
def displayHomepage():
	return render_template('homepage1.html')

@app.route('/fruit')
def fruit():
    myFruit = dataConnection.getMoviesByGenre(connection, 'Horror')

    return render_template('fruit.html',
                           fruits=myFruit)

	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: {0} host post'.format(sys.argv[0]), file = sys.stderr)
		exit()
		
	host = sys.argv[1]
	port = sys.argv[2]
	app.run(host = host, port = port)
