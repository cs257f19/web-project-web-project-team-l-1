import flask
from flask import render_template
import json
import sys
from datasource import *



app = flask.Flask(__name__)
connection = DataSource('yuez', 'glass944happy').tryConnect()
datasource = DataSource('yuez', 'glass944happy')
x = ''


@app.route('/')
def displayHomepage():
	global x
	x=''
	return render_template('homepage.html')

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
    global x
    if x != '':
        x = x + 'AND'
    x =	x + "genre1 = \'Horror\' OR genre2 = \'Horror\' OR genre3 = \'Horror\'"
    return render_template('homepage.html')

@app.route('/Action')
def Action():
    global x
    x =	x + "genre1 = \'Action\' OR genre2 = \'Action\' OR genre3 = \'Action\'"
    return render_template('homepage.html')

@app.route('/Adventure')
def Adventure():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Adventure\' OR genre2 = \'Adventure\' OR genre3 = \'Adventure\'"
    return render_template('homepage.html')

@app.route('/Animation')
def Animation():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Animation\' OR genre2 = \'Animation\' OR genre3 = \'Animation\'"
    return render_template('homepage.html')

@app.route('/Comedy')
def Comedy():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Comedy\' OR genre2 = \'Comedy\' OR genre3 = \'Comedy\'"
    return render_template('homepage.html')

@app.route('/Crime')
def Crime():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Crime\' OR genre2 = \'Crime\' OR genre3 = \'Crime\'"
    return render_template('homepage.html')

@app.route('/Documentary')
def Documentary():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Documentary\' OR genre2 = \'Documentary\' OR genre3 = \'Documentary\'"
    return render_template('homepage.html')

@app.route('/Drama')
def Drama():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Drama\' OR genre2 = \'Drama\' OR genre3 = \'Drama\'"
    return render_template('homepage.html')

@app.route('/Family')
def Family():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Family\' OR genre2 = \'Family\' OR genre3 = \'Family\'"
    return render_template('homepage.html')

@app.route('/Fantasy')
def Fantasy():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Fantasy\' OR genre2 = \'Fantasy\' OR genre3 = \'Fantasy\'"
    return render_template('homepage.html')

@app.route('/Foreign')
def Foreign():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Foreign\' OR genre2 = \'Foreign\' OR genre3 = \'Foreign\'"
    return render_template('homepage.html')

@app.route('/History')
def History():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'History\' OR genre2 = \'History\' OR genre3 = \'History\'"
    return render_template('homepage.html')

@app.route('/Music')
def Music():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Music\' OR genre2 = \'Music\' OR genre3 = \'Music\'"
    return render_template('homepage.html')

@app.route('/Mystery')
def Mystery():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Mystery\' OR genre2 = \'Mystery\' OR genre3 = \'Mystery\'"
    return render_template('homepage.html')

@app.route('/Romance')
def Romance():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Romance\' OR genre2 = \'Romance\' OR genre3 = \'Romance\'"
    return render_template('homepage.html')

@app.route('/Science Fiction')
def ScienceFiction():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Science Fiction\' OR genre2 = \'Science Fiction\' OR genre3 = \'Science Fiction\'"
    return render_template('homepage.html')

@app.route('/Thriller')
def Thriller():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Thriller\' OR genre2 = \'Thriller\' OR genre3 = \'Thriller\'"
    return render_template('homepage.html')

@app.route('/TV Movie')
def TVMovie():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'TV Movie\' OR genre2 = \'TV Movie\' OR genre3 = \'TV Movie\'"
    return render_template('homepage.html')

@app.route('/War')
def War():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'War\' OR genre2 = \'War\' OR genre3 = \'War\'"
    return render_template('homepage.html')

@app.route('/Western')
def Western():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "genre1 = \'Western\' OR genre2 = \'Western\' OR genre3 = \'Western\'"
    return render_template('homepage.html')


#ssssoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languagesoriginal_languages

@app.route('/af')
def af():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'af\'"
    return render_template('homepage.html')

@app.route('/cn')
def cn():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'cn\'"
    return render_template('homepage.html')

@app.route('/da')
def da():
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'da\'"
    return render_template('homepage.html')

@app.route('/de')
def de():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'de\'"
    return render_template('homepage.html')

@app.route('/el')
def el():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'el\'"
    return render_template('homepage.html')

@app.route('/en')
def en():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'en\'"
    return render_template('homepage.html')

@app.route('/es')
def es():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'es\'"
    return render_template('homepage.html')

@app.route('/fa')
def fa():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'fa\'"
    return render_template('homepage.html')

@app.route('/fr')
def fr():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'fr\'"
    return render_template('homepage.html')

@app.route('/he')
def he():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'he\'"
    return render_template('homepage.html')

@app.route('/hi')
def hi():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'hi\'"
    return render_template('homepage.html')

@app.route('/hu')
def hu():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'hu\'"
    return render_template('homepage.html')

@app.route('/id')
def id():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'id\'"
    return render_template('homepage.html')

@app.route('/is')
def langis():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'is\'"
    return render_template('homepage.html')

@app.route('/it')
def it():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'it\'"
    return render_template('homepage.html')

@app.route('/ja')
def ja():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'ja\'"
    return render_template('homepage.html')

@app.route('/ko')
def ko():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'ko\'"
    return render_template('homepage.html')

@app.route('/ky')
def ky():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'ky\'"
    return render_template('homepage.html')

@app.route('/nb')
def nb():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'nb\'"
    return render_template('homepage.html')

@app.route('/nl')
def nl():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'nl\'"
    return render_template('homepage.html')

@app.route('/pl')
def pl():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'pl\'"
    return render_template('homepage.html')

@app.route('/ps')
def ps():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'ps\'"
    return render_template('homepage.html')

@app.route('/pt')
def pt():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'pt\'"
    return render_template('homepage.html')

@app.route('/ro')
def ro():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'ro\'"
    return render_template('homepage.html')

@app.route('/ru')
def ru():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'ru\'"
    return render_template('homepage.html')

@app.route('/sl')
def sl():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'sl\'"
    return render_template('homepage.html')

@app.route('/sv')
def sv():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'sv\'"
    return render_template('homepage.html')

@app.route('/ta')
def ta():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'ta\'"
    return render_template('homepage.html')

@app.route('/te')
def te():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'te\'"
    return render_template('homepage.html')

@app.route('/th')
def th():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'th\'"
    return render_template('homepage.html')

@app.route('/tr')
def tr():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'tr\'"
    return render_template('homepage.html')

@app.route('/vi')
def vi():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'vi\'"
    return render_template('homepage.html')

@app.route('/zh')
def zh():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "original_language = \'zh\'"
    return render_template('homepage.html')

# Rating buttonRating buttonRating buttonRating buttonRating buttonRating buttonRating buttonRating buttonRating buttonRating button
@app.route('/rating')
def rating():
    global x
    if x != '':
        x = x + 'AND'
    x = x + "vote_average >= 7"
    return render_template('homepage.html')

# New Releases button  New Releases button  New Releases button  New Releases button  New Releases button  New Releases button  New Releases button  New Releases button 
@app.route('/newreleases')
def newreleases():
    if x != '':
        x = x + 'AND'
    x = x + "release_date between \'1/1/2015\' and \'1/1/2020\'"
    return render_template('homepage.html')


# SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button SUBMIT button
@app.route('/submit')
def submit():
    global x
    myMovies = datasource.getMoviesByCategory(connection, x)
    print(x)
    x=''
    return render_template('menuresults.html',movies= myMovies)

    
	
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: {0} host post'.format(sys.argv[0]), file = sys.stderr)
		exit()
		
	host = sys.argv[1]
	port = sys.argv[2]
	app.run(host = host, port = port)
