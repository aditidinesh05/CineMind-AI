import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CineMind AI",
    page_icon="🎬",
    layout="wide"
)


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY not found in .env file.")
    st.stop()


# ============================================================
# GEMINI CLIENT
# ============================================================

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🎬 CineMind AI")

st.subheader(
    "Your AI-powered movie recommendation assistant"
)

st.write(
    "Tell me what you're in the mood for, and I'll find "
    "movies from our database that match your request."
)


# ============================================================
# LOAD EMBEDDING MODEL
# ============================================================

@st.cache_resource
def load_embedding_model():

    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )


# ============================================================
# LOAD FAISS DATABASE
# ============================================================

@st.cache_resource
def load_database():

    embedding = load_embedding_model()

    db = FAISS.load_local(
        "movie_index",
        embedding,
        allow_dangerous_deserialization=True
    )

    return db


# Load database

try:

    db = load_database()

except Exception as e:

    st.error(
        f"❌ Could not load the movie database:\n\n{e}"
    )

    st.stop()


# ============================================================
# USER INPUT
# ============================================================

query = st.text_input(
    "🍿 What would you like to watch?",
    placeholder=(
        "Example: I want a dark psychological thriller"
    )
)


# ============================================================
# RECOMMEND BUTTON
# ============================================================

if st.button(
    "🔍 Recommend Movies",
    type="primary"
):

    if not query.strip():

        st.warning(
            "Please enter what kind of movie you want to watch."
        )

        st.stop()


    # ========================================================
    # RETRIEVE MOVIES FROM FAISS
    # ========================================================

    results = db.similarity_search_with_score(
        query,
        k=8
    )


    # ========================================================
    # CREATE CONTEXT FOR GEMINI
    # ========================================================

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

    context = "\n\n".join(
        context_parts
    )


    # ========================================================
    # RAG PROMPT
    # ========================================================

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


    # ========================================================
    # GENERATE GEMINI RESPONSE
    # ========================================================

    with st.spinner(
        "🎬 Finding the best movies for you..."
    ):

        try:

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            answer = response.text

        except Exception as e:

            st.error(
                f"❌ Gemini error:\n\n{e}"
            )

            st.stop()


    # ========================================================
    # DISPLAY RESPONSE
    # ========================================================

    st.subheader(
        "🍿 CineMind's Recommendations"
    )

    st.markdown(answer)


    # ========================================================
    # SHOW RETRIEVED MOVIES
    # ========================================================

    with st.expander(
        "🔎 View movies considered by CineMind"
    ):

        for i, (movie, score) in enumerate(
            results,
            start=1
        ):

            st.write(
                f"**{i}. {movie.page_content}**"
            )

            st.caption(
                f"Similarity score: {score:.4f}"
            )

            st.divider()