import unittest
from Backend import *

class TestBackend(unittest.TestCase):
    def setUp(self) -> None:
        self.ds = DataSource()

    def test_get_movie_by_length(self):
        vote_average = 8
        result = self.ds.getMoviesByLength(vote_average)


if __name__ == "__main__":
	unittest.main()