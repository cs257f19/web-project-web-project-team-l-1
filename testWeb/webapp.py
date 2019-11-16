import flask
from flask import render_template
import json
import sys
from datasource import *



app = flask.Flask(__name__)
connection = DataSource('yuez', 'glass944happy').tryConnect()
datasource = DataSource('yuez', 'glass944happy')



@app.route('/')
def displayHomepage():
	return render_template('homepage1.html')

@app.route('/fruit')
def fruit():
    myFruit = datasource.getMoviesByGenre(connection, 'Horror')

    return render_template('fruit.html',
                           fruits=myFruit)


@app.route('/action')
def action():
    str x = 'WHERE genre1 = \'Action\' OR genre2 = \'Action\' OR genre3 = \'Action\''
    myMovies = datasource.getMoviesByCategory(connection, x)

    return render_template('generic.html',
                           movies= myMovies)

@app.route('/horror')
def horror():
    myMovies = datasource.getMoviesByCategory(connection, 'Horror')

    return render_template('generic.html',
                           movies= myMovies)


	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: {0} host post'.format(sys.argv[0]), file = sys.stderr)
		exit()
		
	host = sys.argv[1]
	port = sys.argv[2]
	app.run(host = host, port = port)
