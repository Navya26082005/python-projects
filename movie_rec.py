import pandas as pd

# Sample movie data
movies = pd.DataFrame({
    "movie": ["Inception", "Avengers", "Titanic", "Interstellar", "Joker"],
    "genre": ["Sci-Fi", "Action", "Romance", "Sci-Fi", "Drama"]
})

# Simple recommendation by genre
def recommend(genre):
    rec = movies[movies['genre'].str.lower() == genre.lower()]
    print("Recommended movies:")
    for m in rec['movie']:
        print("-", m)

recommend("Sci-Fi")