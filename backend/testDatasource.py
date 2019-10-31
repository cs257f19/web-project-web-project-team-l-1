import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    
    def setUp(self):
	
	'''
	Set up the connection to database by providing username and password.
	'''
		
	self.movie = DataSource('yuez','glass944happy')
	self.connection = self.movie.tryConnect()

    def test_getDirectorByMovie_correct(self):
	
	'''
	Test if the method returns correct director name of a given movie.
	'''
	
        title = 'Avatar'
        self.assertEqual(self.movie.getDirectorByMovie(self.connection, title), "James Cameron")
	
    def test_getDirectorByMovie_empty(self):
	
	'''
	Test if the method returns empty string instead of director name given name of movie.
	'''
	
        title = 'Avatar'
        self.assertNotEqual(self.movie.getDirectorByMovie(self.connection, title), "")
	
    def test_getDirectorByMovie_type(self):
	
	'''
	Test if the method returns director name of a given movie in type of string.
	'''
	
	title = 'Avatar'
	string = ''
	self.assertEqual(type(self.movie.getDirectorByMovie(self.connection, title)), type(string))
	
if __name__ == "__main__":
	unittest.main()
