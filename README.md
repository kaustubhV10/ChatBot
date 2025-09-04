<<<<<<< HEAD
# ChatBot
=======
# 🧠 ChatBot with LangGraph, LangChain, and OpenAI

This is a conversational chatbot built using [LangGraph](https://github.com/langchain-ai/langgraph), 
[LangChain](https://www.langchain.com/), and [OpenAI's GPT-4o-mini](https://platform.openai.com/docs/models/gpt-4o). 
The backend uses `SqliteSaver` for checkpointing chat state, and optionally integrates with Streamlit for the frontend interface.

---

## 🚀 Features

- 💬 Natural language chat interface powered by GPT-4o-mini
- 🧠 Multi-node conversational flow using LangGraph
- 🗂️ State checkpointing and persistence with SQLite
- 🧱 Modular graph nodes: `save_title`, `chat_node`, etc.
- 🔄 Replayable conversations with unique thread IDs
- 🌐 Environment configuration via `.env`

---

## 🧩 Tech Stack

| Layer       | Library         |
|-------------|-----------------|
| LLM         | `langchain_openai` |
| Graph Logic | `langgraph`     |
| State Mgmt  | `SqliteSaver`   |
| Frontend    | `Streamlit` *(optional)* |
| Database    | `SQLite`        |
| Env Config  | `python-dotenv` |

---

## 📂 Project Structure (Assumed)

ChatBot/
│
├── streamlit_frontend_database.py # Frontend UI (Streamlit)
├── langgraph_database_backend.py # LangGraph graph logic & SQLite checkpointing
├── chatbot.db # SQLite database file
├── .env # Environment variables (e.g., OpenAI API key)
├── requirements.txt
└── README.md

## ⚙️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/kaustubhV10/ChatBot.git
cd ChatBot

Install dependencies
pip install -r requirements.txt

Create a .env file:
OPENAI_API_KEY=your_openai_key_here

Run the chatbot
streamlit run streamlit_frontend_database.py
>>>>>>> b6304b8dc05b055dde48e70fdc53d859a5f781de
