🤖 Multi-Agent RAG Assistant
<img width="1861" height="1012" alt="Screenshot 2026-01-02 133320" src="https://github.com/user-attachments/assets/beabcc36-e92d-4b8a-9f6d-39c5f7d2ffc1" />
<img width="339" height="324" alt="{3F4BA9CF-BB9D-41AC-AB2E-E06FE1BCDE58}" src="https://github.com/user-attachments/assets/215f96fe-3c5f-4c0d-85a9-c855a07ae0cf" />
📝 Project Overview

The Multi-Agent RAG Assistant is an intelligent question-answering system that uses a multi-agent architecture to dynamically route user queries between a vector database and Wikipedia. Built using LangChain and LangGraph, the system leverages Retrieval-Augmented Generation (RAG) techniques to provide accurate and context-aware responses. A Streamlit-based frontend enables users to interactively ask questions and receive answers in real time.

⚙️ Key Features
🧠 Intelligent Query Routing

Uses an LLM-based routing agent to decide whether a query should be answered using a vector database or Wikipedia

Automatically classifies questions based on relevance and topic

📚 Retrieval-Augmented Generation (RAG)

Stores domain-specific knowledge in a vector database (Astra DB)

Retrieves the most relevant document chunks using semantic search

Improves accuracy over standard LLM responses

🌐 Wikipedia Search Agent

Handles general knowledge queries such as people, places, and topics

Fetches real-time information directly from Wikipedia

🔗 Multi-Agent Workflow (LangGraph)

Implements multiple agents connected through a state graph

Each agent performs a specific task such as routing, retrieval, or search

Ensures structured and scalable query processing

🖥️ Interactive Frontend

Built using Streamlit

Simple UI for entering questions and viewing responses

Real-time feedback with loading indicators

🧩 Project Workflow

User Input

User enters a question through the Streamlit interface

Query Routing

A routing agent analyzes the question and decides whether to use the vector database or Wikipedia

Information Retrieval

Relevant documents are retrieved from Astra DB (for domain-specific queries)

Wikipedia is queried for general knowledge questions

Response Handling

Retrieved content is processed and returned as the final answer

Result Display

The answer is displayed on the frontend

🧠 Technologies Used
Layer	Technology
Frontend	Streamlit
Backend	Python
LLM Framework	LangChain, LangGraph
Vector Database	DataStax Astra DB
Embeddings	HuggingFace (all-MiniLM-L6-v2)
LLM Provider	Groq (LLaMA 3.3)
Data Source	Web Documents, Wikipedia
Version Control	Git & GitHub
🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/multi-agent-rag.git
cd multi-agent-rag

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣Run the Application
streamlit run app.py

4️⃣ Run the Application
streamlit run app.py
