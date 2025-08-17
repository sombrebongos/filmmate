#!/usr/bin/env python3
import requests
import textwrap
from deep_translator import GoogleTranslator

API_KEY = "731c73a7"

import os
os.system("clear")
os.system("figlet FilmMate")

def translate_to_id(text: str) -> str:
    if not text or text == "N/A":
        return "-"
    try:
        return GoogleTranslator(source="en", target="id").translate(text)
    except Exception:

        return text

def get_movie_info(title: str, full_plot: bool = False):
    params = {
        "t": title,
        "apikey": API_KEY,
        "plot": "full" if full_plot else "short",
    }
    try:
        r = requests.get("http://www.omdbapi.com/", params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(f"API Error: {e}")
        return

    if data.get("Response") != "True":
        print(f"Film '{title}' not found.")
        if msg := data.get("Error"):
            print("Detail:", msg)
        return

    wrap = textwrap.TextWrapper(width=72)
    def fill(x): return "\n".join(wrap.wrap(x or "-"))

    plot_en = data.get("Plot") or "-"
    plot_id = translate_to_id(plot_en)

    print("\n" + "-"*72)
    print(f"🎬 Title     : {data.get('Title') or '-'}")
    print(f"📅 Year      : {data.get('Year') or '-'}")
    print(f"⭐ IMDb      : {data.get('imdbRating') or '-'}  (votes: {data.get('imdbVotes') or '-'})")
    print(f"🎭 Genre     : {data.get('Genre') or '-'}")
    print(f"🎬 Director  : {data.get('Director') or '-'}")
    print(f"👥 Actor     : {data.get('Actors') or '-'}")
    print(f"⏱️  Runtime   : {data.get('Runtime') or '-'}")
    print(f"🌍 Country   : {data.get('Country') or '-'}")
    print(f"🏆 Awards    : {data.get('Awards') or '-'}")
    print("📝 Synopsis (en):")
    print(fill(plot_en))
    print("\n📝 Synopsis (id):")
    print(fill(plot_id))
    print("-"*72 + "\n")

if __name__ == "__main__":
    try:
        judul = input("Enter the film name: ").strip()
        panjang = input("Would you like to see the full plot? (y/n): ").strip().lower() == "y"
        get_movie_info(judul, panjang)
    except KeyboardInterrupt:
        print("\nCancelled.")
    input("Press ENTER to exit, mate...")
