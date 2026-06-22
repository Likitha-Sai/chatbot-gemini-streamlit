# 🤖 Chatbot using Gemini + Streamlit

An AI-powered chatbot web application built using **Google Gemini API** and **Streamlit**.  
It enables real-time conversations with a generative AI model through a simple and interactive web interface.

---

## ✨ Features

- 💬 Real-time AI chatbot interface  
- 🧠 Powered by Google Gemini API  
- 🌐 Simple and clean Streamlit UI  
- 📜 Maintains chat history during session  
- ⚡ Fast and responsive responses  
- 🔑 Easy API integration  

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🌐  
- Google Generative AI (Gemini API) 🤖  
- JSON (for storing chat history)

---

## 📁 Project Structure


chatbot/
│── chatbot_backend.py # Main chatbot logic using Gemini API
│── chat.json # Stores chat history
│── .gitignore # Ignored files
│── README.md


---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install streamlit google-generativeai
2. Set your Gemini API key
Windows (PowerShell)
setx GEMINI_API_KEY "your_api_key"
Mac / Linux
export GEMINI_API_KEY="your_api_key"
3. Run the application
streamlit run chatbot_backend.py

💡 Use Cases
AI personal assistant
Learning and experimenting with LLMs
Chat-based web applications
AI prototype development

🔮 Future Improvements
Add memory-based long conversations
Improve UI with chat bubbles
Add voice input/output
Deploy on Streamlit Cloud
Add authentication system

👨‍💻 Author

Built by Likitha Sai
