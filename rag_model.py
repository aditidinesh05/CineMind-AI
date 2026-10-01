import pandas as pd

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# ---------------------------------------
# 1. Load movie dataset
# ---------------------------------------

df = pd.read_csv("movies.csv")

print("🎬 Movies loaded:", len(df))


# ---------------------------------------
# 2. Remove empty content
# ---------------------------------------

df = df.dropna(subset=["content"])

texts = df["content"].tolist()


# ---------------------------------------
# 3. Load embedding model
# ---------------------------------------

print("🧠 Loading embedding model...")

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# ---------------------------------------
# 4. Create FAISS vector database
# ---------------------------------------

print("🔎 Creating embeddings...")

db = FAISS.from_texts(
    texts,
    embedding
)


# ---------------------------------------
# 5. Save vector database
# ---------------------------------------

db.save_local("movie_index")


print("✅ NEW vector database created successfully!")

print(
    "📁 Saved to: movie_index/"
)