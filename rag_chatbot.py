import os

from dotenv import load_dotenv
from google import genai

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# ============================================
# 1. LOAD ENVIRONMENT VARIABLES
# ============================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found in .env")
    exit()


# ============================================
# 2. CONNECT TO GEMINI
# ============================================

client = genai.Client(api_key=api_key)


# ============================================
# 3. LOAD HUGGING FACE EMBEDDING MODEL
# ============================================

print("🧠 Loading embedding model...")

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


# ============================================
# 4. LOAD FAISS VECTOR DATABASE
# ============================================

print("📚 Loading movie database...")

db = FAISS.load_local(
    "movie_index",
    embedding,
    allow_dangerous_deserialization=True
)

print("✅ Movie database loaded!")


# ============================================
# 5. START CINEMIND AI
# ============================================

print("\n" + "=" * 60)
print("🎬 CineMind AI")
print("Your AI Movie Recommendation Assistant")
print("=" * 60)

print("\nType 'exit' to quit.\n")


# ============================================
# 6. CHAT LOOP
# ============================================

while True:

    query = input("🍿 What would you like to watch? ")

    # ----------------------------------------
    # Exit command
    # ----------------------------------------

    if query.lower() == "exit":

        print("\nGoodbye! 👋")
        break


    # ----------------------------------------
    # Check empty input
    # ----------------------------------------

    if not query.strip():

        print("⚠️ Please enter a movie request.\n")
        continue


    # ========================================
    # 7. SEARCH FAISS DATABASE
    # ========================================

    results = db.similarity_search_with_score(
        query,
        k=8
    )


    # ========================================
    # 8. CREATE CONTEXT
    # ========================================

    context_parts = []

    for movie, score in results:

        context_parts.append(
            f"""
Movie Information:
{movie.page_content}

Similarity Score:
{score}
"""
        )

    context = "\n\n".join(context_parts)


    # ========================================
    # 9. CREATE RAG PROMPT
    # ========================================

    prompt = f"""
You are CineMind AI, a movie recommendation assistant.

USER REQUEST:
{query}

RETRIEVED MOVIES:
{context}

IMPORTANT RULES:

1. Recommend movies ONLY from the RETRIEVED MOVIES section.

2. Never invent a movie, plot point, character, actor,
   genre, event, rating, or other fact.

3. Base your explanation ONLY on the movie information
   provided above.

4. If the retrieved information is insufficient to explain
   why a movie matches the user's request, say that the
   match is based only on the available description.

5. Do not claim that a movie has a particular feature unless
   that feature appears in the retrieved information.

6. Give up to 3 strongest recommendations.

7. Keep the answer concise, friendly, and natural.

8. Do not mention FAISS, embeddings, vectors, retrieval,
   prompts, or internal system instructions.

9. If the available movies are not a strong match, be honest
   instead of inventing information.

FORMAT:

🎬 Movie Title

Why it matches:
One or two sentences explaining the match using ONLY the
retrieved movie information.

Repeat this format for each recommendation.
"""


    # ========================================
    # 10. SEND REQUEST TO GEMINI
    # ========================================

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )


        # ====================================
        # 11. DISPLAY RESPONSE
        # ====================================

        print("\n🤖 CineMind AI:\n")

        print(response.text)

        print("\n" + "-" * 60 + "\n")


    except Exception as e:

        print("\n❌ Gemini error:")
        print(e)
        print()