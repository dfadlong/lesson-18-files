class MovieList(object):
  def __init__(self):
    self.movies = {}

  def add(self, title, info):
    self.movies[title] = info

  def getNumMovies(self):
  	return len(self.movies)