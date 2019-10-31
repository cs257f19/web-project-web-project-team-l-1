import unittest

from datasource import *

class TestBackend(unittest.TestCase):
    def setUp(self) -> None:
        self.movie = DataSource()

    def test_getDirectorByMovie(self):
        title = 'Avatar'
        self.assertEqual(self.movie.getDirectorByMovie(title), "James Cameron")

if __name__ == "__main__":
	unittest.main()
