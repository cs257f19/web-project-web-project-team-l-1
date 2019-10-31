import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    
    def setUp(self):
	self.connection = DataSource('yuez','glass944happy').tryConnect()
	self.ds = DataSource()

    def test_getDirectorByMovie(self):
        title = 'Avatar'
        self.ds.assertEqual(getDirectorByMovie(self.connection, title), "James Cameron")

if __name__ == "__main__":
	unittest.main()
