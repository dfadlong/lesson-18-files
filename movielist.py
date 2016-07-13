import collections

class MovieList(object):
  def __init__(self):
    self.movies = []
    self.moviesByYear = collections.defaultdict(list)

  def add(self, info):
    self.movies.append(info)
  	# info == {'year': '1990', 'length': '111', ...}
    year = info['year'] # '1990'
    # moviesByYear['1990']
    last = len(self.movies) - 1
    self.moviesByYear[year].append(last)

  def getByYear(self, year):
    return self.moviesByYear[year]

m = MovieList()

f = open('film.csv', 'r')
while True:
  line = f.readline()
  if line == '':
    break
  line = line.strip()
  pieces = line.split(';')
  movieInfo = {
	'year': pieces[0],
	'length': pieces[1],
	'title': pieces[2],
	'subject': pieces[3],
	'actor': pieces[4],
	'actress': pieces[5],
	'director': pieces[6],
	'popularity': pieces[7],
	'awards': pieces[8],
	'image': pieces[9]
  }
  m.add(movieInfo)

print(len(m.getByYear('1990')))
