import pandas as pd

movies = pd.read_csv("Movies Data/movies.csv")

# Calculating a weighted rating using the following formula
# WR = (v ÷ (v+m)) × R + (m ÷ (v+m)) × C
# where WR = weighted rating, v = number of votes, m = min number of votes
# R = average rating of the movie, C = average rating across all movies

# calculate m
m = movies['vote_count'].quantile(0.9)
C = movies['vote_average'].mean()


def weighted_rating(df, m=m, C=C):
    v = df['vote_count']
    R = df['vote_average']
    # Calculation based on the IMDB formula
    wr = (v / (v + m) * R) + (m / (m + v) * C)
    return wr


movies['weighted_rating'] = movies.apply(weighted_rating, axis=1)
df_movies = movies.sort_values('weighted_rating', ascending=False)\
                [['title', 'vote_count', 'vote_average', 'weighted_rating', 'overview']].head(12)
popularMovies = df_movies['title'].tolist()
movieDescription = df_movies['overview'].tolist()

# removing : in title
for index, movie in enumerate(popularMovies):
    if ':' in movie:
        popularMovies[index] = movie.replace(':', '')


if __name__ == '__main__':
    for index, movie in enumerate(popularMovies):
        print(index, movie)
