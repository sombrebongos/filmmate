# 🎬 FilmMate
<img src="https://raw.githubusercontent.com/sombrebongos/filmmate/refs/heads/main/img/Screenshot_20250817-221328.jpg" height="300" width="300">

**FilmMate** is a simple command-line tool to fetch movie information from the [OMDb API](http://www.omdbapi.com/).  
It displays the movie title, year, IMDb rating, genre, cast, and also provides a translated synopsis in **Bahasa Indonesia** using `deep-translator`.

## ✨ Features
- Fetch movie details (title, year, rating, genre, actors, director, awards).
- Show short or full plot.
- Translate plot/synopsis into Bahasa Indonesia.
- Fancy CLI banner with `figlet`/`pyfiglet`.

## 🚀 Installation
```bash
git clone https://github.com/sombrebongos/filmmate
cd filmmate
pip install -r requirements.txt
python film.py
```

## 🔑 API Key
**FilmMate** uses OMDb API.
Get your free API key [here](http://www.omdbapi.com/apikey.aspx) then replace it in film.py:

`API_KEY = "your_api_key"`
