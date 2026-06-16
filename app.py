from fastapi import FastAPI
import pickle

# Load the necessary files
movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

# Define the recommend function
def recommend(movie):

    movie_index = movies[movies['title_y'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:6]

    result=[]

    for i in movies_list:
        result.append(movies.iloc[i[0]].title_y)

    return result

app = FastAPI()


@app.get("/")
def home():
    return {
        "message":"Movie Recommendation API"
    }


@app.get("/recommend/{movie}")
def get_movies(movie:str):

    return {
        "movie":movie,
        "recommendations":recommend(movie)
    }
