f = open('film.csv', 'r')
line = f.readline()
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

print(movieInfo)