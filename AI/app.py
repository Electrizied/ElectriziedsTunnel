import streamlit as st
import time
from duckduckgo_search import DDGS
from google import genai
from openai import OpenAI

# ─────────────────────────────────────────────
# PAGE
# ─────────────────────────────────────────────
st.set_page_config(page_title="AI Chat Search", page_icon="💬", layout="wide")
st.title("💬 AI Chat Search (Memory Fixed)")

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
gemini_key = st.sidebar.text_input("Gemini API Key", type="password")
openrouter_key = st.sidebar.text_input("OpenRouter API Key", type="password")

gemini_model = st.sidebar.selectbox(
    "Gemini Model",
    ["gemini-2.5-flash", "gemini-2.5-flash-lite"]
)

openrouter_model = st.sidebar.selectbox(
    "OpenRouter Model",
    ["meta-llama/llama-3.1-8b-instruct"]
)

num_results = st.sidebar.slider("Search results", 3, 10, 5)

# ─────────────────────────────────────────────
# MEMORY
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

# ─────────────────────────────────────────────
# SEARCH
# ─────────────────────────────────────────────
def ddg_search(q, max_results=5):
    results = []
    try:
        with DDGS(timeout=8) as ddgs:
            for r in ddgs.text(q, max_results=max_results):
                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "snippet": r.get("body", "")
                })
    except:
        pass

    return results if results else [{
        "title": "No results",
        "url": "",
        "snippet": "Search failed."
    }]

# ─────────────────────────────────────────────
# GEMINI
# ─────────────────────────────────────────────
def ask_gemini(prompt):
    client = genai.Client(api_key=gemini_key)
    return client.models.generate_content(
        model=gemini_model,
        contents=prompt
    ).text

# ─────────────────────────────────────────────
# OPENROUTER
# ─────────────────────────────────────────────
def ask_openrouter(prompt):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=openrouter_key
    )

    res = client.chat.completions.create(
        model=openrouter_model,
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content

# ─────────────────────────────────────────────
# AI ROUTER
# ─────────────────────────────────────────────
def ask_ai(prompt):
    # Gemini first
    if gemini_key:
        try:
            return ask_gemini(prompt)
        except Exception as e:
            if "429" not in str(e):
                return f"Gemini error: {e}"

    # OpenRouter fallback
    if openrouter_key:
        try:
            return ask_openrouter(prompt)
        except Exception as e:
            return f"OpenRouter error: {e}"

    return "No AI key provided."

# ─────────────────────────────────────────────
# SHOW CHAT HISTORY
# ─────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ─────────────────────────────────────────────
# INPUT
# ─────────────────────────────────────────────
query = st.chat_input("Ask something...")

if query:

    # store user msg
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    # SEARCH
    with st.spinner("Searching web..."):
        results = ddg_search(query, num_results)

    context = "\n\n".join(
        f"[{i+1}] {r['title']}\n{r['snippet']}"
        for i, r in enumerate(results)
    )

    # ─────────────────────────────────────────────
    # 🔥 PROPER CHAT MEMORY (THIS IS THE FIX)
    # ─────────────────────────────────────────────
    chat_history = "\n".join(
        f"{m['role']}: {m['content']}"
        for m in st.session_state.messages[-10:]   # last 10 messages
    )

    prompt = f"""
You are a helpful AI assistant.

IMPORTANT: Continue the conversation using chat history.

Chat history:
{chat_history}

Web results:
{context}

User question:
{query}

Rules:
- Use chat history for context
- Use web results when relevant
- Be clear and concise
- Use citations [1], [2]
"""

    # AI CALL
    with st.spinner("Thinking..."):
        answer = ask_ai(prompt)

    # store assistant msg
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)
