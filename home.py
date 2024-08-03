import streamlit as st
from backend import popularMovies, movieDescription


st.set_page_config(page_title="Home", layout='wide', initial_sidebar_state='collapsed')
with st.sidebar:
    st.page_link('home.py', label='Home')
    st.page_link('pages/movie_page.py', label='Movie Page')
st.title("Movie Recommendation App")
st.write('Browse from the most popular movies:')
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
st.session_state['movie_title'] = ''

with st.container():
    with col1:
        for title, desc in zip(popularMovies[:3], movieDescription[:3]):
            st.title(title)
            st.image(f"images/{title}.jpg", width=300)
            if st.button("Movie Page", key=title):
                st.session_state['movie_title'] = title
                st.page_link('pages/movie_page.py', label=title)
            st.write(desc)

    with col2:
        for title, desc in zip(popularMovies[3:6], movieDescription[3:6]):
            st.title(title)
            st.image(f"images/{title}.jpg", width=300)
            if st.button("Movie Page", key=title):
                st.session_state['movie_title'] = title
                st.page_link('pages/movie_page.py', label=title)
            st.write(desc)

    with col3:
        for title, desc in zip(popularMovies[6:9], movieDescription[6:9]):
            st.title(title)
            st.image(f"images/{title}.jpg", width=300)
            if st.button("Movie Page", key=title):
                st.session_state['movie_title'] = title
                st.page_link('pages/movie_page.py', label=title)
            st.write(desc)

    with col4:
        for title, desc in zip(popularMovies[9:12], movieDescription[9:12]):
            st.title(title)
            st.image(f"images/{title}.jpg", width=300)
            if st.button("Movie Page", key=title):
                st.session_state['movie_title'] = title
                st.page_link('pages/movie_page.py', label=title)
            st.write(desc)

margins_css = """
    <style>
        .main > div {
            padding-left: 10rem;
            padding-right: 10rem;
        }
        
        [data-testid="column"] {
            padding-left: 5px;
            padding-right: 5px;
            margin-top: 50px;
        } 
    </style>
"""

st.markdown(margins_css, unsafe_allow_html=True)