from imdb import IMDb
# searching for a movie id randomly to see which movie is associated with the id
movie = IMDb().get_movie('15097216')
print(movie)
#the directors of this movie:
for i in movie["directors"]:
    print(i)
#look at the top 250 movies at IMDb:
movies = IMDb().get_top250_movies()
for i in movies:
    print(i)