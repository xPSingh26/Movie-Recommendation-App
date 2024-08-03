import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies = pd.read_csv("Movies Data/movies.csv")
movies['overview'] = movies['overview'].fillna('')
movies['keywords'] = movies['keywords'].fillna('')


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


def keywords_combined():
    keywords = movies['keywords']
    keywordsFiltered = []
    for keyword in keywords:
        keyword = eval(keyword)
        keywordsFiltered.append(keyword)

    # print(len(keywordsFiltered))
    keywordsName = []
    moviesKeywords = []
    for keyword in keywordsFiltered:
        if len(keyword) == 0:
            moviesKeywords.append(k['name'])
            keywordsName.append(moviesKeywords)
        else:
            for x, k in enumerate(keyword):
                # print(x, k)
                moviesKeywords.append(k['name'])
                if x == len(keyword) - 1:
                    keywordsName.append(moviesKeywords)
                    moviesKeywords = []

    for i in range(len(keywordsName)):
        keywordsName[i] = ' '.join(keywordsName[i])

    return keywordsName


def genre_combined():
    genres = movies['genres']
    genresFiltered = []
    for genre in genres:
        genre = eval(genre)
        genresFiltered.append(genre)

    # print(len(genresFiltered))
    genresName = []
    moviesGenres = []
    for genre in genresFiltered:
        if len(genre) == 0:
            moviesGenres.append(k['name'])
            genresName.append(moviesGenres)
        else:
            for x, k in enumerate(genre):
                # print(x, k)
                moviesGenres.append(k['name'])
                if x == len(genre) - 1:
                    genresName.append(moviesGenres)
                    moviesGenres = []

    for i in range(len(genresName)):
        genresName[i] = ' '.join(genresName[i])

    return genresName


movies['weighted_rating'] = movies.apply(weighted_rating, axis=1)
df_movies = movies.sort_values('weighted_rating', ascending=False)\
                [['title', 'vote_count', 'vote_average', 'weighted_rating', 'overview']].head(12)
popularMovies = df_movies['title'].tolist()
movieDescription = df_movies['overview'].tolist()


genre_combined = genre_combined()
keywords_combined = keywords_combined()
movies['genre_combined'] = genre_combined
movies['keywords_combined'] = keywords_combined
movies['similarity_data'] = movies[['keywords_combined', 'overview', 'genre_combined']].agg(' '.join, axis=1)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['similarity_data'])
testData = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())

similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)


def movie_search(title, nr_of_movies=10):
    movie_index = movies[movies['title'] == title].index[0]
    similarity_score = list(enumerate(similarity_matrix[movie_index]))
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    similarity_score = similarity_score[1:nr_of_movies+1]
    similarity_score_filtered = []
    for score in similarity_score:
        if score[1] != 0:
            similarity_score_filtered.append(score)
    movie_indices = [i[0] for i in similarity_score_filtered]
    similar_movies = list(movies['title'].iloc[movie_indices])
    return similar_movies


similarMovieDict = {}
for movie in popularMovies:
    similarMovies = movie_search(movie, 5)
    similarMovieDict[movie] = similarMovies

if __name__ == '__main__':
    # for index, movie in enumerate(popularMovies):
    #     print(index, movie)
    print(similarMovieDict)
