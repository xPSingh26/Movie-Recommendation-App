import pandas as pd


# Script to remove ':' from movie titles in csv file
movies = pd.read_csv("Movies Data/movies.csv")
movieTitles = list(movies['title'])
for index, title in enumerate(movieTitles):
    if ':' in title:
        movieTitles[index] = title.replace(':', '')

movies['title'] = movieTitles
movies.to_csv("Movies Data/movies.csv")

# print(movieTitles[:30])
