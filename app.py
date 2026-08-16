import streamlit as st
import ollama


MODEL_NAME = "llama3.2:1b"

st.title("Chatbot using Ollama in Local System")
st.caption(f"Model Name Is> : {MODEL_NAME}")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
prompt = st.chat_input("Ask me anything...")


if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )


    # Call local Ollama model
    try:

        response = ollama.chat(
            model=MODEL_NAME,
            messages=st.session_state.messages
        )

        assistant_reply = response["message"]["content"]

    except Exception as e:
        assistant_reply = f"Error: {str(e)}"


    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)


    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )