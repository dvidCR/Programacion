import python_filmaffinity

service = python_filmaffinity.FilmAffinity(lang='es')

movies = service.top_filmaffinity(from_year=2010, to_year=2011)

print(movies)
