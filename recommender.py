import pickle

# Load the necessary files
movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

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
