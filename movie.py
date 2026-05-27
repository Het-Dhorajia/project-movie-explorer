import requests
import customtkinter as ctk
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "64e325025ff211aedbf030ef76b43f3e"

app = ctk.CTk()
app.geometry("600x800")
app.title("Movie Explorer")


def search_movie():

    movie_name = search_box.get().strip()

    if movie_name == "":
        result_label.configure(text="Please enter a movie name")
        return

    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"

    response = requests.get(search_url)
    data = response.json()

    if not data.get("results"):
        result_label.configure(text="Movie not found")
        return

    movie = data["results"][0]

    title = movie.get("title", "N/A")
    rating = movie.get("vote_average", "N/A")
    release_date = movie.get("release_date", "N/A")
    overview = movie.get("overview", "No overview available")
    poster_path = movie.get("poster_path")

    result_label.configure(
        text=f"🎬 {title}\n\n⭐ Rating: {rating}\n📅 Release: {release_date}\n\n📝 {overview}"
    )

    if poster_path:
        image_url = f"https://image.tmdb.org/t/p/w500{poster_path}"

        img_response = requests.get(image_url)
        img_data = Image.open(BytesIO(img_response.content))

        img_data = img_data.resize((250, 350))

        img = ImageTk.PhotoImage(img_data)

        poster_label.configure(image=img)
        poster_label.image = img


title_label = ctk.CTkLabel(app, text="Movie Explorer", font=("Arial", 28))
title_label.pack(pady=20)

search_box = ctk.CTkEntry(app, placeholder_text="Enter movie name", width=300)
search_box.pack(pady=10)

search_button = ctk.CTkButton(app, text="Search", command=search_movie)
search_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="Search a movie", font=("Arial", 16), justify="left")
result_label.pack(pady=20)

poster_label = ctk.CTkLabel(app, text="")
poster_label.pack(pady=10)

app.mainloop()