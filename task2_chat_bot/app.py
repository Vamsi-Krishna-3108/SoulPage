import os
import streamlit as st
from langchain_community.llms import Ollama

HISTORY_FILE = "chat_history.txt"

# ------------------ MEMORY (FILE STORAGE) ------------------
def save_message(role, message):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{role}:{message}\n")

def load_messages():
    if not os.path.exists(HISTORY_FILE):
        return []
    msgs = []
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                role, msg = line.split(":", 1)
                msgs.append({"role": role, "content": msg.strip()})
    return msgs

def delete_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

# ------------------ LLM ------------------
def build_bot():
    return Ollama(model="llama3.2:1b", temperature=0)

# ------------------ MAIN APP ------------------
def main():
    st.set_page_config(page_title="Local ChatGPT", page_icon="🤖", layout="wide")

    st.title("🤖 Local ChatGPT (Offline AI Assistant)")
    st.caption("Powered by **Ollama + Llama3.2:1b** — with Love ❤️")

    llm = build_bot()

    # Load session memory
    if "messages" not in st.session_state:
        st.session_state.messages = load_messages()

    # Sidebar: Reset chat
    with st.sidebar:
        st.header("⚙️ Settings")
        if st.button("🔄 Reset Conversation"):
            st.session_state.messages = []
            delete_history()
            st.success("Conversation reset!")

        st.markdown("Made with ❤️ for your local AI workflow.")

    # Display chat messages (ChatGPT style)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # User input at bottom
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Show user message immediately
        st.session_state.messages.append({"role": "user", "content": user_input})
        save_message("user", user_input)

        with st.chat_message("user"):
            st.write(user_input)

        # Build model prompt with memory
        history_text = "\n".join(
            f"{m['role'].capitalize()}: {m['content']}"
            for m in st.session_state.messages
        )

        prompt = f"""
You are a helpful conversational AI assistant. Maintain memory based ONLY on the full conversation below.
Never repeat the user's name unless asked.
Never say you forget anything — memory is provided.
Keep responses short and clear.

Conversation:
{history_text}

Assistant:
"""

        # Generate reply
        bot_reply = llm.invoke(prompt).strip()

        # Save memory
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        save_message("assistant", bot_reply)

        # Display bot message
        with st.chat_message("assistant"):
            st.write(bot_reply)

if __name__ == "__main__":
    main()
