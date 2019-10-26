import psycopg2
import getpass

class DataSource:
	'''
	DataSource executes all of the queries on the database.
	It also formats the data to send back to the frontend, typically in a list
	or some other collection or object.
	'''

	#use psycopg2 to connect with database we have, it returns a connection which can be used in getting data.	
	def __init__(self, user, password,):
		self.user = user
		self.password = password
	
	def tryConnect(self):
		try:
			connection = psycopg2.connect(host = "localhost", database = self.user, user = self.user, password = self.password)
		except Exception as e:
			print("Connection error: ", e)
			exit()
		return connection

	def getMoviesByGenre(self, connection, genre):		
		try:
			cursor = connection.cursor()
			query = "SELECT title FROM imdb_5000 WHERE genre1 = \'" + genre + "\' OR genre2 = \'" + genre + "\' OR genre3 = \'" + genre +"\'"
			cursor.execute(query)
			return cursor.fetchall()	
		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
		
	def getMoviesByBudget(self, connection, budget):		
	def getMoviesByHomepage(self, connection, homepage):
	def getMoviesByRevenue(self, connection, revenue):
	def getMoviesByRating(self, connection, average_rating):
	def getMoviesByVoteCount(self, connection, vote_count):
		
	def getMoviesByDirector(self, connection, director):
	def getMoviesByKeywords(self, connection, keywords):
	def getMoviesByTagline(self, connection, tagline):
	def getMoviesByReleaseDate(self, connection, release_date):
	def getMoviesByReleaseDate(self, connection, release_date):

	def getMoviesByLength(self, connection, minRuntime, maxRuntime):
		try:
			cursor = connection.cursor()
			query = "SELECT title FROM imdb_5000 WHERE runtime > \'" + str(minRuntime) + "\' AND runtime < \'" + str(maxRuntime) + "\'"
			cursor.execute(query)
			return cursor.fetchall()
		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
		
def main():
	user = 'yuez'
	password = 'glass944happy'
	datasource = DataSource(user, password)

	connection = datasource.tryConnect()

	# Execute a simple query: how many earthquakes above the specified magnitude are there in the data?
	results = datasource.getMoviesByLength(connection, 60, 90)
	
	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	connection.close()
		
main()
