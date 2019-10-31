import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    user = 'yuez'
    password = 'glass944happy'
    datasource = Datasource(user, password)
    connection = datasource.tryConnect()
    
    def setUp(self) -> None:
        self.movie = DataSource()

    def test_getDirectorByMovie(self):
        title = 'Avatar'
        self.assertEqual(self.movie.getDirectorByMovie(connection, title), "James Cameron")

if __name__ == "__main__":
	unittest.main()
