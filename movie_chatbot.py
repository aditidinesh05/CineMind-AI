from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load embedding model
embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load saved vector DB
db = FAISS.load_local(
    "movie_index",
    embedding,
    allow_dangerous_deserialization=True
)

print("🎬 Movie Chatbot Ready!")
print("Type 'exit' to quit.\n")

while True:
    query = input("Ask for movies: ")

    if query.lower() == "exit":
        break

    # Search similar movies
    results = db.similarity_search(query, k=5)

    print("\n🍿 Recommended Movies:\n")

    for i, movie in enumerate(results, 1):
        print(f"{i}. {movie.page_content[:300]}")
        print("-" * 50)