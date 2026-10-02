import asyncio
import os
import streamlit as st
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

# --- Configuration ---
tavily_api_key = os.getenv("TAVILY_API_KEY")
model = ChatOllama(model="llama3.2")

# --- Backend Logic ---
async def answer_question_async(query):
    async with streamablehttp_client(
        f"https://mcp.tavily.com/mcp/?tavilyApiKey={tavily_api_key}"
    ) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)
            response = await agent.ainvoke({
                "messages": [{"role": "user", "content": query}]
            })
            return response["messages"][-1].content

def answer_question(query):
    return asyncio.run(answer_question_async(query))

# --- Streamlit Frontend ---
st.set_page_config(page_title="Synapse", page_icon="⚡")
st.title("⚡ Synapse - Local LLM Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar: History and Reset Button
with st.sidebar:
    st.header("Conversation History")
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            
    st.divider()
    
    if st.button("🔄 Reset Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main Chat Area
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if query := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.write(query)

    # >>> CHANGED SPINNER TEXT HERE <<<
    with st.spinner("Synapse is processing..."):
        try:
            answer = answer_question(query)
        except Exception as e:
            answer = f"An error occurred: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)