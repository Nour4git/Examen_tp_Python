import streamlit as st
import requests

st.set_page_config(page_title="🎬 Movie Explorer with Nour", layout="centered")
st.title("🎬 Movie Explorer")

API_URL = "http://localhost:8000"

def fetch_random_movie():
    try:
        response = requests.get(f"{API_URL}/movies/random/")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching random movie: {e}")
        return None

def generate_summary(movie_id: int):
    try:
        response = requests.post(f"{API_URL}/generate_summary/", json={"movie_id": movie_id})
        response.raise_for_status()
        return response.json().get("summary_text")
    except requests.RequestException as e:
        st.error(f"Failed to generate summary: {e}")
        return None

if "movie" not in st.session_state:
    st.session_state.movie = None
if "summary" not in st.session_state:
    st.session_state.summary = None

if st.button("🎲 Show Random Movie"):
    st.session_state.movie = fetch_random_movie()
    st.session_state.summary = None

if st.session_state.movie:
    movie = st.session_state.movie

    st.markdown(f"## {movie['title']} ({movie['year']})")
    st.write(f"**Director:** {movie['director']}")
    
    st.markdown("### Actors")
    for actor in movie.get('actors', []):
        st.write(f"- {actor['actor_name']}")

    if st.button("📝 Get Summary"):
        with st.spinner("Generating summary..."):
            summary = generate_summary(movie["id"])
            if summary:
                st.session_state.summary = summary

    if st.session_state.summary:
        st.markdown("### Summary")
        st.info(st.session_state.summary)
else:
    st.info("Click 'Show Random Movie' to get started!")
