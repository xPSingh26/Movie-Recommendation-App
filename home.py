import streamlit as st
import pandas as pd
from backend import popularMovies, movieDescription


st.set_page_config(layout='wide')
st.title("Movie Recommendation App")
st.write('Browse from the most popular movies:')
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col1:
    for title, desc in zip(popularMovies[:3], movieDescription):
        st.title(title)
        st.image(f"images/{title}.jpg", width=300)
        st.write(desc)

with col2:
    for title, desc in zip(popularMovies[3:6], movieDescription):
        st.title(title)
        st.image(f"images/{title}.jpg", width=400)
        st.write(desc)

with col3:
    for title, desc in zip(popularMovies[6:9], movieDescription):
        st.title(title)
        st.image(f"images/{title}.jpg", width=400)
        st.write(desc)

with col4:
    for title, desc in zip(popularMovies[9:12], movieDescription):
        st.title(title)
        st.image(f"images/{title}.jpg", width=400)
        st.write(desc)


