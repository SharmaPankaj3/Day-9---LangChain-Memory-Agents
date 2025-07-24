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

from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

with open(r"D:\desktop\Key_GEN_AI.txt", "r") as f:
    openai_key = f.read().strip()

llm = OpenAI(temperature=0, openai_api_key=openai_key)

prompt = PromptTemplate(input_variables=["country"],template= "What is the captital of {country}?")
chain = prompt|llm
response = chain.invoke({"country":"England"})
print("Response:",response)
