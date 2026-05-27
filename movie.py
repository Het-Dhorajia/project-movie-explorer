import requests
import customtkinter as ctk
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "64e325025ff211aedbf030ef76b43f3e"

app = ctk.CTk()
app.geometry("600x800")
app.title("Movie Explorer")


def search_movie():

    global img


    try:
        movie_name = search_box.get().strip()

        if movie_name == "":
            result_label.configure(text="Please enter a movie name")
            return

        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            result_label.configure(text="API Error (check key)")
            return

        data = response.json()

        if not data.get("results"):
            result_label.configure(text="Movie not found")
            poster_label.configure(image="", text="")
            return

        movie = data["results"][0]

        title = movie.get("title", "N/A")
        rating = movie.get("vote_average", "N/A")
        release_date = movie.get("release_date", "N/A")
        overview = movie.get("overview", "No overview")

        result_label.configure(
            text=f"{title}\n⭐ {rating}\n📅 {release_date}\n\n{overview}"
        )

        poster_path = movie.get("poster_path")

        if poster_path:

            img_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
            img_data = requests.get(img_url, timeout=5).content

            img_obj = Image.open(BytesIO(img_data)).convert("RGB")
            img_obj = img_obj.resize((250, 350))

            img = ImageTk.PhotoImage(img_obj)

            poster_label.configure(image=img, text="")
            poster_label.image = img

        else:
            poster_label.configure(text="No Image", image="")

    except Exception as e:
        result_label.configure(text=f"Error: {e}")


title_label = ctk.CTkLabel(app, text="Movie Explorer", font=("Arial", 28))
title_label.pack(pady=20)

search_box = ctk.CTkEntry(app, width=300, placeholder_text="Enter movie name")
search_box.pack(pady=10)

search_button = ctk.CTkButton(app, text="Search", command=search_movie)
search_button.pack(pady=10)

poster_label = ctk.CTkLabel(app, text="")
poster_label.pack(pady=20)

result_label = ctk.CTkLabel(app, text="Search a movie", justify="left")
result_label.pack(pady=10)

app.mainloop()