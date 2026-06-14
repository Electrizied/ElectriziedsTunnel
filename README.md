

# ⚡ Electrizieds tunnels

A modern **AI-powered search and chat assistant** that combines web search (DuckDuckGo) with advanced language models (Gemini + OpenRouter) to generate intelligent, context-aware responses.

[▶ Watch Demo Video Of Basic Algebra](https://files.catbox.moe/cxh6gz.mp4)
---

## 🚀 Features

* 💬 Continuous AI chat with memory
* 🔍 Live web search using DuckDuckGo
* 🤖 AI responses powered by:

  * Google Gemini
  * OpenRouter (fallback system)
* 🧠 Conversation context awareness
* ⚡ Fast Streamlit web interface
* 🔁 Automatic AI fallback if one model fails
* 📚 Citation-based answers from search results

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎈
* Google Gemini API 🤖
* OpenRouter API 🌐
* DuckDuckGo Search 🔍

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/electriziedstunnels.git
cd electriziedstunnels
```

---

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📄 requirements.txt

Make sure you include:

```txt
streamlit
duckduckgo-search
google-genai
openai
```

---

## ▶️ Running the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🔑 API Keys Required

You will need:

### Google Gemini

Get your key here:
[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### OpenRouter (optional fallback)

Get your key here:
[https://openrouter.ai/keys](https://openrouter.ai/keys)

---

## 🧠 How It Works

1. User enters a question
2. System performs DuckDuckGo web search
3. Search results are sent to AI
4. AI generates a response using:

   * Chat history (memory)
   * Web context
5. If Gemini fails → OpenRouter is used

---

## ⚡ AI Flow

```
User Input
   ↓
DuckDuckGo Search
   ↓
Gemini (Primary AI)
   ↓ (if fails)
OpenRouter (Fallback AI)
   ↓
Final Answer + Chat Memory
```

---

## 📁 Project Structure

```
electriziedstunnels/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔥 Future Improvements

* Streaming responses (typing effect)
* Better source citations UI
* Smart search detection (only search when needed)
* Conversation history sidebar
* Multi-model selector UI

---

## ⚠️ Notes

* Free API tiers may have rate limits
* Gemini may return quota errors on heavy usage
* OpenRouter model availability can change

---

## 📜 License

This project is for educational and personal use.

---

