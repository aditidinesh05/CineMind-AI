# 🎬 CineMind AI

### _Tell me what you feel like watching. I'll find the movie._

**CineMind AI** is a **RAG-powered movie recommendation system** that understands natural-language preferences and turns them into personalized movie recommendations.

Instead of simply matching keywords, CineMind AI uses **semantic search + vector retrieval + LLM reasoning** to understand what you're looking for, retrieve relevant movies, and generate grounded recommendations.

> 🧠 **RAG + NLP + Vector Search + Gemini = Your AI Movie Companion**

---

## 🎥 What Can CineMind AI Do?

You don't need to search for a specific movie.

Just tell CineMind what you're in the mood for.


🍿 "Movies like Interstellar"
🖤 "I want a dark psychological thriller"
❤️ "Give me something emotional and inspiring"
🚀 "I want a mind-bending sci-fi movie"

CineMind converts your request into a semantic representation, searches its movie knowledge base, and uses Gemini to generate recommendations from the retrieved context.

✨ Why CineMind?

Traditional movie search often depends on keywords.

CineMind takes a different approach:

             "I want something
              emotionally powerful"

                       ↓

                🧠 NLP / Embedding

                       ↓

              🔎 Semantic Search

                       ↓

                ⚡ FAISS Retrieval

                       ↓

              🎬 Relevant Movies

                       ↓

                  🤖 Gemini

                       ↓

            💬 Personalized Response

The result is a recommendation system designed around meaning and context, rather than exact keyword matching.

🧠 Under the Hood

CineMind AI follows a Retrieval-Augmented Generation (RAG) architecture.

01 → 📡 Data Collection

Movie information is collected using the TMDB API and stored as structured movie data.

02 → 🧩 Embedding Generation

Movie information is converted into numerical vector representations using Hugging Face Embeddings.

03 → 🗂️ Vector Storage

The generated embeddings are stored in a FAISS vector database for efficient similarity search.

04 → 🔎 Semantic Retrieval

When a user enters a query, the query is converted into an embedding and compared with the movie vectors.

The most relevant movies are retrieved.

05 → 🤖 LLM Reasoning

The retrieved movie information is passed to Google Gemini as context.

Gemini then generates a concise recommendation based on the retrieved information.

06 → 🎬 User Experience

Everything is presented through an interactive Streamlit interface.

🏗️ System Architecture
                         ┌───────────────────┐
                         │     👤 USER       │
                         │  Natural Language │
                         │      Query        │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   🧠 EMBEDDING    │
                         │  Hugging Face     │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   ⚡ FAISS        │
                         │ Vector Retrieval  │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  🎬 MOVIE CONTEXT │
                         │ Retrieved Results │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    🤖 GEMINI      │
                         │   LLM Reasoning   │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │  🍿 RECOMMENDATION│
                         │  Personalized     │
                         │     Response      │
                         └───────────────────┘
🛠️ Tech Stack
Category	Technology
💻 Language	Python
🧠 AI / LLM	Google Gemini
🔎 RAG Framework	LangChain
🧩 Embeddings	Hugging Face
⚡ Vector Database	FAISS
🗣️ NLP	Natural Language Processing
🌐 Frontend	Streamlit
🎬 Data Source	TMDB API
📊 Data Processing	Pandas, NumPy
📂 Project Structure
CineMind-AI/
│
├── 🎨 app.py
│      └── Streamlit application
│
├── 🤖 rag_chatbot.py
│      └── RAG + Gemini recommendation pipeline
│
├── 📡 data_fetch.py
│      └── Movie data collection from TMDB
│
├── 🧠 rag_model.py
│      └── Embedding generation + FAISS vector store
│
├── 💬 movie_chatbot.py
│      └── Movie recommendation chatbot logic
│
├── 🎬 movies.csv
│      └── Movie dataset
│
├── ⚡ movie_index/
│      ├── index.faiss
│      └── index.pkl
│
├── 📦 requirements.txt
│      └── Python dependencies
│
├── 🔐 .gitignore
│      └── Protected environment files
│
└── 📖 README.md
🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/YOUR-USERNAME/CineMind-AI.git
cd CineMind-AI
2️⃣ Create a virtual environment
python -m venv venv
Windows
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
🔐 API Configuration

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key
TMDB_API_KEY=your_tmdb_api_key
⚠️ Keep your API keys private!

The .env file is intentionally excluded from GitHub using .gitignore.

Never commit your API keys to a public repository.

▶️ Run CineMind AI

Start the Streamlit application:

streamlit run app.py

Then open the local URL displayed in your terminal.

💬 Try Asking...
💭 You Say	🎬 CineMind Understands
Movies like Interstellar	Similar movie concepts
I want a dark psychological thriller	Mood + genre
Something emotional and inspiring	Emotional tone
Give me a mind-bending sci-fi	Theme + genre
I want an adventurous movie	Preference + genre
🔍 What Makes This a RAG Project?

The core idea is simple:

Without RAG
User
 ↓
LLM
 ↓
Generated Answer
With CineMind's RAG Pipeline
User
 ↓
Query Embedding
 ↓
FAISS Retrieval
 ↓
Relevant Movie Context
 ↓
Gemini
 ↓
Grounded Recommendation

The LLM receives retrieved movie information as context before generating its response.

This makes the project a practical example of combining:

Semantic Retrieval + Vector Search + Generative AI

🧪 Key Concepts Demonstrated
🧠 Retrieval-Augmented Generation

Combines information retrieval with generative AI.

🔎 Semantic Search

Retrieves information based on contextual similarity rather than relying only on exact keywords.

⚡ Vector Database

FAISS stores and searches high-dimensional embeddings efficiently.

🧩 Text Embeddings

Movie descriptions and user queries are represented as numerical vectors for similarity comparison.

🤖 LLM Integration

Gemini converts retrieved context into natural-language recommendations.

🚧 What's Next?

CineMind AI can be extended into a more complete recommendation platform.

Planned Improvements
🎞️ Movie posters and visual recommendation cards
⭐ Ratings and popularity filters
📅 Release-year filtering
🎭 Genre filtering
🎬 Cast and director-based search
❤️ Personal watchlists
💬 Multi-turn conversational recommendations
👤 User profiles and recommendation history
🎨 More advanced Streamlit UI
☁️ Cloud deployment
🌟 Project Highlights
       🎬 CineMind AI

       RAG Architecture
              +
       Semantic Search
              +
       FAISS Retrieval
              +
       Hugging Face
              +
       Gemini LLM
              +
       Streamlit
              ↓
       AI Movie Discovery
👩‍💻 Author
Aditi Dineshan

B.Tech — Computer Science & Data Science

Interested in building applications around:

Data Science · Machine Learning · NLP · Generative AI · RAG

📜 License

This project is developed for educational and portfolio purposes.
