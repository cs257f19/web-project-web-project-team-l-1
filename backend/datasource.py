import psycopg2
import getpass

class DataSource:
	
	def __init__(self, user, password,):
		self.user = user
		self.password = password
	
	def tryConnect(self):

		'''
		Connect with database
		'''

		try:
			connection = psycopg2.connect(host = "localhost", database = self.user, user = self.user, password = self.password)
		except Exception as e:
			print("Connection error: ", e)
			exit()
		return connection

	def getMoviesByGenre(self, connection, genre):	

		'''
		Retrieves all Movies with a certain genre.
		Parameters:
			Connection- the connection to the database
			Genre- retrieve every movie with this genre
		Returns:
		A collection of all movies with this genre
		'''		
	
		try:
			cursor = connection.cursor()
			query = "SELECT title FROM imdb_5000 WHERE genre1 = \'" + genre + "\' OR genre2 = \'" + genre + "\' OR genre3 = \'" + genre +"\'"
			cursor.execute(query)
			return cursor.fetchall()	
		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
        
    
    	def getMoviesByLength(self, connection, minRuntime, maxRuntime):

		'''
		Retrieve all movies within a certain range of runtime.
		Parameters:
		minRuntime: minimum of runtime
		maxRuntime: maximum of runtime
		Returns:
		A collection of movies within this certain range of runtime.
		'''

		try:
			cursor = connection.cursor()
			query = "SELECT title FROM imdb_5000 WHERE runtime > \'" + str(minRuntime) + "\' AND runtime < \'" + str(maxRuntime) + "\'"
			cursor.execute(query)
			return cursor.fetchall()
		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
		
	def getMoviesByVoteAverage(self, connection, vote_average):

		'''
		Retrieve all movies within a certain vote average.
		Parameters:
		Vote average minimum 
		Returns:
		Movies in descending order above threshold
		'''

		try:
			cursor = connection.cursor()
			query = "SELECT title FROM imdb_5000 WHERE vote_average > \'" + str(vote_average) + "\' ORDER BY vote_average Desc"
			cursor.execute(query)
			return cursor.fetchall()
		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
		
    	def getDirectorByMovie(self, connection, title):
        
           	try:
			cursor = connection.cursor()
			query = "SELECT director FROM imdb_5000 WHERE title = \'" + str(title) + "\'"
			cursor.execute(query)
			return cursor.fetchall()
		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
            
            
            
	'''
	These are methods that will be implemented in the website.
	def getMoviesByBudget(self, connection, budget):
	def getMoviesByRevenue(self, connection, revenue):
	def getMoviesByRating(self, connection, average_rating):
	def getMoviesByVoteCount(self, connection, vote_count):
	def getMoviesByVoteAverage(self, connection, vote_average):
	def getMoviesByPopularity(self, connection, popularity):
	def getMoviesByDirector(self, connection, director):
	def getMoviesByKeywords(self, connection, keywords):
	def getMoviesByTagline(self, connection, tagline):
	def getMoviesByTitle(self, connection, title):
	def getMoviesByReleaseDate(self, connection, release_date):
	def getMoviesByHomepage(self, connection, homepage):
	def getMoviesByOriginalLanguage(self, connection, original_language):
	def getMoviesByOverview(self, connection, overview):
	def getMoviesByHomepage(self, connection, homepage):
	def getMoviesByHomepage(self, connection, homepage):
	def getMoviesByProductionCompany(self, connection, production_company):
	def getMoviesByProductionCountires(self, connection, production_countries:
	def getMoviesBySpokenLanguage(self, connection, spoken_language):	
	def getMoviesByCharacterName(self, connection, charactername):
	'''


def main():

	'''
	Print out results of different methods
	'''

	user = 'yuez'
	password = 'glass944happy'
	datasource = DataSource(user, password)

	#Connect to database
	connection = datasource.tryConnect()
	
	# get list of movies in results
	# results = datasource.getMoviesByLength(connection, 60, 90)
	# results = datasource.getMoviesByGenre(connection, 'Horror')
	# results = datasource.getMoviesByVoteAverage(connection, 8.2)
    	results = datasource.getDirectorByMovie(connection, 'Avatar')
	
	if results is not None:
		print("Query results: ")
		for item in results:
			string s = item
			print(s)
			s = s.replace(',', '')
			print(s)

	# Disconnect from database
	connection.close()
		
main()
