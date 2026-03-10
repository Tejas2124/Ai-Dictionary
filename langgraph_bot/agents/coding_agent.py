from dotenv import load_dotenv
from langgraph_bot.agentschema.stateschema import State
from langchain.agents import create_agent
from langgraph_bot.models.generativemodel import codemodel
from pprint import pprint as pp
from langgraph_bot.tools.tools import python_executor,tavily_search_tool
from langgraph_bot.utils.prompts import CODING_PROMPT
load_dotenv()


code_agent = create_agent(
    model=codemodel,
    state_schema=State,
    system_prompt=CODING_PROMPT,
    tools=[python_executor,tavily_search_tool],  # scraper_tool will be added soon for web scraping.
)
