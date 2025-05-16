# 🎬 Movie Explorer

Application web pour explorer des films et générer des résumés avec IA.

## 🚀 Fonctionnalités

- Obtenir un film aléatoire
- Voir les détails (titre, année, réalisateur, acteurs)
- Générer un résumé intelligent avec Langchain + Groq

## 🛠️ Technologies

**Backend:**
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

**Frontend:**
- Streamlit

**IA:**
- Langchain
- Groq API

## ⚙️ Installation
cloner ce project : git clone https://github.com/Nour4git/Examen_tp_Python
### Prérequis
- Python 3.9+
- PostgreSQL
- Clé API Groq

### Configuration Backend

1. pip install -r requirements.txt

2. Create a .env file in the backend directory and add your Groq API key:

    GROQ_API_KEY=your_api_key_here

3. Initialize your database and run any migrations if applicable.

4. Run PostgreSQL locally and create the database and run FastApi :

      uvicorn main:app --reload
      http://localhost:8000/docs

### Configuration Frontend 

1. Navigate to the frontend folder
2. Install dependencies if needed:
     
     pip install streamlit requests

3.  run the streamlit app :
     
     streamlit run main_streamlit.py

### Important Note
  
  ✅ Vous devez ajouter des données de films via l'API backend avant d'utiliser l'application frontend, car la base de données est vide au départ.

* Ajouter des films en envoyant une requête POST à :


POST /movies/

* Exemple de charge utile JSON pour ajouter un film :

json

{
  "title": "Inception",
  "year": 2010,
  "director": "Christopher Nolan",
  "actors": [
    {"actor_name": "Leonardo DiCaprio"},
    {"actor_name": "Joseph Gordon-Levitt"}
  ]
}

* Une fois les films ajoutés, l’interface frontend peut récupérer un film aléatoire et générer son résumé.
Aperçu des points de terminaison de l'API :
GET /movies/random/
Récupérer un film aléatoire depuis la base de données.

POST /movies/
Ajouter un nouveau film avec ses acteurs.

POST /generate_summary/
Générer un court résumé d’un film en envoyant l’ID du film :

{
  "movie_id": 1
}



## Question :
 
# Q1: Why commit the movie before creating related actors?

 Because we need the movie's ID (primary key) to assign as a foreign key in the Actor records. Without committing, db_movie.id isn't generated yet.

# Question 2 : Difference between lazy loading and eager loading in SQLAlchemy?

* Lazy Loading: Actor data is fetched only when accessed, causing N+1 queries.

* Eager Loading (joinedload): Actor data is loaded in the same query, improving performance and preventing N+1 issues.
 
 # Question : How to format list of actors for LLM prompt?
 actor_list = ", ".join(actor.actor_name for actor in movie.actors)
 -> This creates a human-readable list:
    Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy


