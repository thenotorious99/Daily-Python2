import random

movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}

print("Welcome to the Movie Night Recommender!")
print("Available genres: Action, Comedy, Drama, Sci-Fi, Horror")

genres = input("Enter genre:")

if genres in movies:
    print("You should watch:", random.choice(movies[genres]))
else:
    print("Invalid genre. Please choose from the available options.")