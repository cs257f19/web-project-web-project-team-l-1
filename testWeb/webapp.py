import flask
from flask import render_template
import json
import sys
from datasource import *



app = flask.Flask(__name__)
connection = DataSource('yuez', 'glass944happy').tryConnect()
datasource = DataSource('yuez', 'glass944happy')
x=''


@app.route('/')
def displayHomepage():
	return render_template('homepage1.html')

@app.route('/search')
def displaySearch():
	return render_template('search.html')

@app.route('/about')
def about():
    return render_template('about.html')

# clicking on buttons formulates the search string for PSQL
#GenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenresGenres

@app.route('/Horror')
def Horror():
    if x != '':
        x = x + 'AND'
    x =	x + "genre1 = \'Horror\' OR genre2 = \'Horror\' OR genre3 = \'Horror\'"
    return x

@app.route('/Action')
def Action():
    x =	x + "genre1 = \'Action\' OR genre2 = \'Action\' OR genre3 = \'Action\'"
    return x

@app.route('/Adventure')
def Adventure():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Adventure\' OR genre2 = \'Adventure\' OR genre3 = \'Adventure\'"
    return x

@app.route('/Animation')
def Animation():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Animation\' OR genre2 = \'Animation\' OR genre3 = \'Animation\'"
    return x

@app.route('/Comedy')
def Comedy():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Comedy\' OR genre2 = \'Comedy\' OR genre3 = \'Comedy\'"
    return x

@app.route('/Crime')
def Crime():
    if x != '':
        x = x + 'AND'
    x = x + a	"genre1 = \'Crime\' OR genre2 = \'Crime\' OR genre3 = \'Crime\'"
    return x

@app.route('/Documentary')
def Documentary():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Documentary\' OR genre2 = \'Documentary\' OR genre3 = \'Documentary\'"
    return x

@app.route('/Drama')
def Drama():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Drama\' OR genre2 = \'Drama\' OR genre3 = \'Drama\'"
    return x

@app.route('/Family')
def Family():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Family\' OR genre2 = \'Family\' OR genre3 = \'Family\'"
    return x

@app.route('/Fantasy')
def Fantasy():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Fantasy\' OR genre2 = \'Fantasy\' OR genre3 = \'Fantasy\'"
    return x

@app.route('/Foreign')
def Foreign():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Foreign\' OR genre2 = \'Foreign\' OR genre3 = \'Foreign\'"
    return x

@app.route('/History')
def History():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'History\' OR genre2 = \'History\' OR genre3 = \'History\'"
    return x

@app.route('/Music')
def Music():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Music\' OR genre2 = \'Music\' OR genre3 = \'Music\'"
    return x

@app.route('/Mystery')
def Mystery():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Mystery\' OR genre2 = \'Mystery\' OR genre3 = \'Mystery\'"
    return x

@app.route('/Romance')
def Romance():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Romance\' OR genre2 = \'Romance\' OR genre3 = \'Romance\'"
    return x

@app.route('/Science Fiction')
def Science Fiction():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Science Fiction\' OR genre2 = \'Science Fiction\' OR genre3 = \'Science Fiction\'"
    return x

@app.route('/Thriller')
def Thriller():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Thriller\' OR genre2 = \'Thriller\' OR genre3 = \'Thriller\'"
    return x

@app.route('/TV Movie')
def TV Movie():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'TV Movie\' OR genre2 = \'TV Movie\' OR genre3 = \'TV Movie\'"
    return x

@app.route('/War')
def War():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'War\' OR genre2 = \'War\' OR genre3 = \'War\'"
    return x

@app.route('/Western')
def Western():
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Western\' OR genre2 = \'Western\' OR genre3 = \'Western\'"
    return x


#LanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguagesLanguages

@app.route('/af')
def af():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'af\'"
    return x

@app.route('/cn')
def cn():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'cn\'"
    return x

@app.route('/da')
def da():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'da\'"
    return x

@app.route('/de')
def de():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'de\'"
    return x

@app.route('/el')
def el():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'el\'"
    return x

@app.route('/en')
def en():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'en\'"
    return x

@app.route('/es')
def es():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'es\'"
    return x

@app.route('/fa')
def fa():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'fa\'"
    return x

@app.route('/fr')
def fr():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'fr\'"
    return x

@app.route('/he')
def he():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'he\'"
    return x

@app.route('/hi')
def hi():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'hi\'"
    return x

@app.route('/hu')
def hu():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'hu\'"
    return x

@app.route('/id')
def id():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'id\'"
    return x

@app.route('/is')
def is():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'is\'"
    return x

@app.route('/it')
def it():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'it\'"
    return x

@app.route('/ja')
def ja():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'ja\'"
    return x

@app.route('/ko')
def ko():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'ko\'"
    return x

@app.route('/ky')
def ky():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'ky\'"
    return x

@app.route('/nb')
def nb():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'nb\'"
    return x

@app.route('/nl')
def nl():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'nl\'"
    return x

@app.route('/pl')
def pl():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'pl\'"
    return x

@app.route('/ps')
def ps():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'ps\'"
    return x

@app.route('/pt')
def pt():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'pt\'"
    return x

@app.route('/ro')
def ro():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'ro\'"
    return x

@app.route('/ru')
def ru():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'ru\'"
    return x

@app.route('/sl')
def sl():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'sl\'"
    return x

@app.route('/sv')
def sv():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'sv\'"
    return x

@app.route('/ta')
def ta():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'ta\'"
    return x

@app.route('/te')
def te():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'te\'"
    return x

@app.route('/th')
def th():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'th\'"
    return x

@app.route('/tr')
def tr():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'tr\'"
    return x

@app.route('/vi')
def vi():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'vi\'"
    return x

@app.route('/zh')
def zh():
    if x != '':
        x = x + 'AND'
    x = x + "language = \'zh\'"
    return x


# SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button
@app.route('/submit')
def submit():
    myMovies = datasource.getMoviesByCategory(connection, x)
    return render_template('menuresults.html',movies= myMovies)
    x=''
	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: {0} host post'.format(sys.argv[0]), file = sys.stderr)
		exit()
		
	host = sys.argv[1]
	port = sys.argv[2]
	app.run(host = host, port = port)
