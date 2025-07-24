from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools,initialize_agent,AgentType

with open(r"D:\desktop\Key_GEN_AI.txt", "r") as f:
    openai_key = f.read().strip()

# Initialize the LLM
llm = OpenAI(temperature=0, openai_api_key=openai_key)

# Load tools (calculator in this case)
tools= load_tools(["llm-math"],llm = llm
                  )
# Initialize the Agent
agent = initialize_agent(tools,llm,agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,verbose = True)

# Run the Agent
response= agent.run("what is the product of 15 and 12")
print(f"Agent response: {response}")