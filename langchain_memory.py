## ============================================
# Project: LangChain Chain Example
# Author: [Dr Pankaj Sharma]
# Description: Prompt + LLM with LangChain
# ============================================
# 📦 Setup instructions (run these in terminal):
# ------------------------------------------------
# Create & activate virtual environment:
# python -m venv .venv
# & ".venv\Scripts\Activate.ps1"   # for PowerShell
#
# Install dependencies:
# pip install -U pip
# pip install langchain-openai
# pip install openai
# pip install langchain
# pip install langchain-community
# pip install "langchain[all]"
#
# Notes:
# - Make sure your API key is saved in: Key_GEN_AI.txt
# - API key can be generated from: https://platform.openai.com/account/api-keys
#from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_core.runnables import RunnablePassthrough,RunnableLambda

with open(r"D:\desktop\Key_GEN_AI.txt", "r") as f:
    openai_key = f.read().strip()

llm = ChatOpenAI(temperature=0, openai_api_key=openai_key)

prompt = PromptTemplate(input_variables=["history","user_input"],
                        template="""
                        The following is a conversation between a human and an AI.
                        {history}
                        Human : {user_input}
                        AI:"""
                        )
# Define Memory:
memory = ConversationBufferMemory(memory_key = "history",
return_messages= False
)

def get_memory(inputs):
    return memory.load_memory_variables({})["history"]

history_runnable = RunnableLambda(get_memory)
# Build Runnable sequence

chain = ({ "history": history_runnable,
           "user_input": RunnablePassthrough()
           }
         |prompt
         |llm
         )

# Function to run a single turn and save context
def chat(user_message, ai_response):
    """Save turn in memory and print response."""
    print(ai_response.content)
    memory.save_context(
        {"user_input": user_message},
        {"output": ai_response.content}
    )


# Run the chain
response1 = chain.invoke("Hello!")
chat("Hello!", response1)

response2 =chain.invoke("What is your name?")
chat("What did I just say?", response2)

response3 = chain.invoke("What is your name?")
chat("What is your name?", response3)