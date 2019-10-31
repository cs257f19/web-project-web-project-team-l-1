import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    
    def setUp(self):
	self.movie = DataSource('yuez','glass944happy')
	self.connection = self.movie.tryConnect()

    def test_getDirectorByMovie_correct(self):
        title = 'Avatar'
        self.assertEqual(self.movie.getDirectorByMovie(self.connection, title), "James Cameron")
	
    def test_getDirectorByMovie_empty(self):
        title = 'Avatar'
        self.assertNotEqual(self.movie.getDirectorByMovie(self.connection, title), "")
	
    def test_getDirectorByMovie_type(self):
	title = 'Avatar'
	string = ''
	self.assertEqual(type(self.movie.getDirectorByMovie(self.connection, title)), type(string))
	
if __name__ == "__main__":
	unittest.main()
