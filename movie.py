import requests
import customtkinter as ctk

API_KEY = "YOUR_API_KEY"

app = ctk.CTk()
app.geometry("600x700")
app.title("Movie Explorer")

def search_movie():

    movie_name = search_box.get()

    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(search_url)
    data = response.json()

    if data["results"]:

        movie = data["results"][0]
        movie_id = movie["id"]

        details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
        details_response = requests.get(details_url)
        details = details_response.json()

        title = movie["title"]
        rating = movie["vote_average"]
        release_date = movie["release_date"]
        overview = movie["overview"]

        genres = ", ".join([g["name"] for g in details["genres"]])
        language = details["original_language"]
        popularity = details["popularity"]
        runtime = details["runtime"]

        result_label.configure(
            text=f"🎬 {title}\n\n⭐ Rating: {rating}\n📅 Release: {release_date}\n🎭 Genres: {genres}\n🌍 Language: {language}\n🔥 Popularity: {popularity}\n⏱ Runtime: {runtime} min\n\n📝 {overview}"
        )

    else:
        result_label.configure(text="Movie not found")


title = ctk.CTkLabel(app, text="Movie Explorer", font=("Arial", 28))
title.pack(pady=20)

search_box = ctk.CTkEntry(app, placeholder_text="Enter movie name", width=300)
search_box.pack(pady=10)

search_button = ctk.CTkButton(app, text="Search", command=search_movie)
search_button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="Search a movie", font=("Arial", 16), justify="left")
result_label.pack(pady=20)

app.mainloop()