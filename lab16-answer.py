import collections

class MovieList(object):
  def __init__(self):
    self.movies = []
    self.moviesByYear = collections.defaultdict(list)
    self.moviesByGenre = collections.defaultdict(list)
    self.moviesByActor = collections.defaultdict(list)

  def add(self, info):
    self.movies.append(info)
    last = len(self.movies) - 1
    # Lookup by year
    year = info['year']
    self.moviesByYear[year].append(last)
    # Look by genre
    genre = info['genre']
    self.moviesByGenre[genre].append(last)
    # Look by actor
    actor = info['actor']
    self.moviesByActor[actor].append(last)

  def getByYear(self, year):
    indexes = self.moviesByYear[year]
    return [self.movies[i] for i in indexes]

  def getByGenre(self, genre):
    indexes = self.moviesByGenre[genre]
    return [self.movies[i] for i in indexes]

  def getByActor(self, actor):
    indexes = self.moviesByActor[actor]
    return [self.movies[i] for i in indexes]

  def getAllActors(self):
    return self.moviesByActor.keys()



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
	'genre': pieces[3],
	'actor': pieces[4],
	'actress': pieces[5],
	'director': pieces[6],
	'popularity': pieces[7],
	'awards': pieces[8],
	'image': pieces[9]
  }
  m.add(movieInfo)

winner = ''
most = 0
for actor in m.getAllActors():
  num = len(m.getByActor(actor))
  if num > most:
    most = num
    winner = actor
print(winner)
print(most)

