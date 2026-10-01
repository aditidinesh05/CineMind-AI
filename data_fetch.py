import requests
import pandas as pd
from dotenv import load_dotenv
import os
import time

# ---------------------------------------
# 1. Load API key
# ---------------------------------------

load_dotenv()

TMDB_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_KEY:
    print("❌ TMDB_API_KEY not found in .env")
    exit()


# ---------------------------------------
# 2. Fetch movies from TMDB
# ---------------------------------------

def fetch_movies(page=1):

    url = "https://api.themoviedb.org/3/movie/popular"

    params = {
        "api_key": TMDB_KEY,
        "language": "en-US",
        "page": page
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        data = response.json()

        if "results" in data:

            print(f"✅ Page {page} fetched")

            return data["results"]

        else:

            print(
                f"❌ API error on page {page}:",
                data
            )

            return []

    except Exception as e:

        print(
            f"❌ Error on page {page}:",
            e
        )

        return []


# ---------------------------------------
# 3. Collect movies
# ---------------------------------------

movies = []

# Fetch 20 pages × ~20 movies
# ≈ 400 movies

for page in range(1, 21):

    result = fetch_movies(page)

    if result:

        movies.extend(result)

    # Small delay to avoid API/network problems
    time.sleep(0.5)


print(
    "\n🎬 Total movies fetched:",
    len(movies)
)


# ---------------------------------------
# 4. Check if data exists
# ---------------------------------------

if len(movies) == 0:

    print(
        "❌ No movies were fetched."
    )

    exit()


# ---------------------------------------
# 5. Convert to DataFrame
# ---------------------------------------

df = pd.DataFrame(movies)


# ---------------------------------------
# 6. Select useful columns
# ---------------------------------------

columns = [
    "id",
    "title",
    "overview",
    "release_date",
    "vote_average",
    "vote_count",
    "genre_ids",
    "poster_path"
]

# Keep only columns that actually exist
columns = [
    column
    for column in columns
    if column in df.columns
]

df = df[columns]


# ---------------------------------------
# 7. Clean missing values
# ---------------------------------------

df["overview"] = df["overview"].fillna("")

df["title"] = df["title"].fillna("")

df["release_date"] = df[
    "release_date"
].fillna("")

df["poster_path"] = df[
    "poster_path"
].fillna("")


# ---------------------------------------
# 8. Create text for embeddings
# ---------------------------------------

df["content"] = (
    df["title"]
    + ". "
    + df["overview"]
)


# ---------------------------------------
# 9. Remove duplicate movies
# ---------------------------------------

df = df.drop_duplicates(
    subset=["id"]
)


# ---------------------------------------
# 10. Save dataset
# ---------------------------------------

df.to_csv(
    "movies.csv",
    index=False
)


print(
    "\n🎉 Dataset successfully saved!"
)

print(
    "📁 File: movies.csv"
)

print(
    "🎬 Number of movies:",
    len(df)
)