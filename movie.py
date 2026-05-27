import requests
import customtkinter as ctk

from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "64e325025ff211aedbf030ef76b43f3e"

app = ctk.CTk()

app.geometry("500x700")
app.title("Movie Explorer")


def search_movie():

    movie_name = search_box.get()

    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"

    response = requests.get(url)

    data = response.json()

    if data["results"]:

        movie = data["results"][0]

        movie_title = movie["title"]

        rating = movie["vote_average"]

        release_date = movie["release_date"]

        poster_path = movie["poster_path"]

        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

        poster_response = requests.get(poster_url)

        image_data = poster_response.content

        image = Image.open(BytesIO(image_data))

        image = image.resize((200, 300))

        poster_image = ImageTk.PhotoImage(image)

        poster_label.configure(image=poster_image, text="")

        poster_label.image = poster_image

        result_label.configure(
            text=f"🎬 {movie_title}\n⭐ Rating: {rating}\n📅 Release Date: {release_date}"
        )

    else:

        result_label.configure(text="Movie not found")


title = ctk.CTkLabel(
    app,
    text="Movie Explorer",
    font=("Arial", 28)
)
title.pack(pady=20)

search_box = ctk.CTkEntry(
    app,
    placeholder_text="Enter movie name",
    width=300
)
search_box.pack(pady=10)

search_button = ctk.CTkButton(
    app,
    text="Search",
    command=search_movie
)
search_button.pack(pady=10)

result_label = ctk.CTkLabel(
    app,
    text="Search a movie",
    font=("Arial", 20)
)
result_label.pack(pady=20)

poster_label = ctk.CTkLabel(app, text="")
poster_label.pack(pady=10)

app.mainloop()