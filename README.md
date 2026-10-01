# 🎬 CineMind AI

### RAG-Based Personalized Movie Recommendation System

CineMind AI is an AI-powered movie recommendation system that uses **Retrieval-Augmented Generation (RAG)**, **semantic search**, and **Gemini LLM** to recommend movies based on natural-language user preferences.

Instead of relying only on keyword matching, CineMind AI retrieves semantically relevant movies from a **FAISS vector database** and uses Gemini to generate personalized recommendations.

---

## ✨ Features

- 🎯 Natural-language movie search
- 🧠 Semantic similarity-based retrieval
- 🔎 RAG-based movie recommendations
- 🤖 Gemini LLM integration
- 📚 Hugging Face text embeddings
- ⚡ FAISS vector search
- 💬 Context-aware recommendations
- 🌐 Interactive Streamlit interface

---

## 🧠 How It Works

```text
User Query
    ↓
Hugging Face Embeddings
    ↓
FAISS Similarity Search
    ↓
Relevant Movie Information
    ↓
Gemini LLM
    ↓
Personalized Recommendations
    ↓
Streamlit Interface
🛠️ Tech Stack

Python, LangChain, FAISS, Hugging Face Embeddings, Gemini LLM, NLP, Streamlit, TMDB API

📂 Project Structure
CineMind-AI/
│
├── app.py
├── rag_chatbot.py
├── data_fetch.py
├── rag_model.py
├── movie_chatbot.py
│
├── movies.csv
├── movie_index/
│
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/CineMind-AI.git
cd CineMind-AI
2. Create a virtual environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
🔑 API Configuration

Create a .env file in the project folder:

GEMINI_API_KEY=your_gemini_api_key
TMDB_API_KEY=your_tmdb_api_key

Important: Never upload your .env file to GitHub.

The .gitignore file is configured to keep it private.

▶️ Run the Application

Start CineMind AI using:

streamlit run app.py

Then open the local URL shown in your terminal.

💡 Example Queries

Try asking:

Movies like Interstellar
I want a dark psychological thriller
I want something emotional and inspiring
🔍 RAG Pipeline

CineMind AI follows a Retrieval-Augmented Generation workflow:

Movie data is collected using the TMDB API.
Movie information is converted into vector embeddings using Hugging Face Embeddings.
The embeddings are stored in a FAISS vector database.
A user's query is converted into an embedding.
FAISS retrieves the most relevant movies.
The retrieved information is provided as context to Gemini.
Gemini generates a concise, personalized recommendation.
🚀 Future Improvements
🎞️ Movie poster integration
⭐ Ratings and popularity filters
📅 Release-year filtering
🎭 Genre-based filtering
🎬 Cast and director-based recommendations
❤️ Personalized watchlists
💬 Multi-turn conversations
🎨 Enhanced movie-card UI
☁️ Streamlit Cloud deployment
👩‍💻 Author

Aditi Dineshan

B.Tech — Computer Science & Data Science

Interested in Data Science, Machine Learning, NLP, Generative AI, and RAG Systems.

📄 License

This project is intended for educational and portfolio purposes.