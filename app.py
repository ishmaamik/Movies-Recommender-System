import streamlit as st
import pickle as pi
import pandas as pd
import requests
import os

api_key = os.getenv('API_KEY')

st.title('Movie Recommender System')

movies_dict= pi.load(open('movies_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)
similarity= pi.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id, api_key)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


selected_movie_name= st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters= recommend(selected_movie_name)
    col1, spacer1, col2, spacer2, col3, spacer3, col4, spacer4, col5 = st.columns([1, 18, 1, 18, 1, 18, 1, 18, 1])
    
    title_width = "200px"  # Adjust this value as needed
    poster_spacing = "20px"  # Adjust this value to control spacing

    with col1:
        st.markdown(f"""
            <div style='width: {title_width}; text-align: center;'>
                <div>{recommended_movie_names[0]}</div>
                <img src='{recommended_movie_posters[0]}' style='width: 250px; margin-top: {poster_spacing};'/>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div style='width: {title_width}; text-align: center;'>
                <div>{recommended_movie_names[1]}</div>
                <img src='{recommended_movie_posters[1]}' style='width: 250px; margin-top: {poster_spacing};'/>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div style='width: {title_width}; text-align: center;'>
                <div>{recommended_movie_names[2]}</div>
                <img src='{recommended_movie_posters[2]}' style='width: 250px; margin-top: {poster_spacing};'/>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div style='width: {title_width}; text-align: center;'>
                <div>{recommended_movie_names[3]}</div>
                <img src='{recommended_movie_posters[3]}' style='width: 250px; margin-top: {poster_spacing};'/>
            </div>
        """, unsafe_allow_html=True)
    with col5:
        st.markdown(f"""
            <div style='width: {title_width}; text-align: center;'>
                <div>{recommended_movie_names[4]}</div>
                <img src='{recommended_movie_posters[4]}' style='width: 250px; margin-top: {poster_spacing};'/>
            </div>
        """, unsafe_allow_html=True)


# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"   
#     response = requests.get(url)
    
#     if response.status_code != 200:
#         return "https://via.placeholder.com/500?text=No+Poster+Available"
    
#     data = response.json()
#     if 'poster_path' not in data or data['poster_path'] is None:
#         return "https://via.placeholder.com/500?text=No+Poster+Available"
    
#     poster_path = data['poster_path']
#     full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    
#     return full_path

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
    
#     for i in distances[1:6]:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movie_names.append(movies.iloc[i[0]].title)
#         recommended_movie_posters.append(fetch_poster(movie_id))
    
#     return recommended_movie_names, recommended_movie_posters
