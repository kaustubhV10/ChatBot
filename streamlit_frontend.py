import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

config = {'configurable': {'thread_id': 'thread-1'}}
# st.session_state is dictionary
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content']) 

user_input = st.chat_input("Type here")


if user_input:

    st.session_state["message_history"].append({'role':'user', 'content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages':HumanMessage(content=user_input)})
    ai_message = response['messages'][-1].content

    st.session_state["message_history"].append({'role':'assistant', 'content':user_input})
    with st.chat_message('assistant'):
        st.text(ai_message) 