import streamlit as st
import pandas as pd
from backend import movieDescription, popularMovies

movieDf = pd.read_csv(r'C:\Users\Gurmeet\Documents\Python Projects\Movie Recommendation App'
                          r'\Movies Data\movie_pages.csv', sep=';')
movieList = dict(zip(popularMovies, movieDescription))


st.set_page_config(page_title="Movie Page", layout='wide', initial_sidebar_state='collapsed')
st.title("Movie Page")

with st.sidebar:
    st.page_link('home.py', label='Home')
    st.page_link('pages/movie_page.py', label='Movie Page')


if st.session_state:
    st.page_link(r"C:\Users\Gurmeet\Documents\Python Projects\Movie Recommendation App\home.py",
                 label='Home', icon='🏠')
    if st.session_state['movie_title']:
        movieTitle = st.session_state['movie_title']
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(r"C:\Users\Gurmeet\Documents\Python Projects\Movie Recommendation App"
                     f"\images\{movieTitle}.jpg", width=350)
        with col2:
            st.header(movieTitle)
            st.write(movieList[movieTitle])
            movieLink = movieDf.loc[movieDf['movie_title']==movieTitle]['link'].squeeze()
            st.write(f"Movie IMDB page:- {movieLink}")
        st.write("Browse similar movies like this: ")


else:
    st.write("Please select a movie from the home page!")
    st.page_link(r"C:\Users\Gurmeet\Documents\Python Projects\Movie Recommendation App\home.py",
                 label='Home', icon='🏠')



margins_css = """
    <style>
        .main > div {
            margin-left: 5rem;
            }
        [data-testid='column']{
            margin-top: 80px;
            margin-bottom: 5rem;
        }
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)

