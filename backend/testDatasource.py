import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    
    def setUp(self):
	self.connection = DataSource('yuez','glass944happy').tryConnect()

    def test_getDirectorByMovie(self):
        title = 'Avatar'
        self.assertEqual(self.getDirectorByMovie(self.connection, title), "James Cameron")

if __name__ == "__main__":
	unittest.main()
