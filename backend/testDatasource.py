import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    
    def setUp(self):
	self.movie = DataSource('yuez','glass944happy')
	self.connection = self.movie.tryConnect()

    def test_getDirectorByMovie(self):
        title = 'Avatar'
        self.assertEqual(self.movie.getDirectorByMovie(self.connection, title), "James Cameron")
	
    def test_getDirectorByMovie_empty(self):
        title = 'Avatar'
        self.assertEqual(self.movie.getDirectorByMovie(self.connection, title), "")
	
if __name__ == "__main__":
	unittest.main()
