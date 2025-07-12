from browser_use.llm import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import os
import asyncio
import platform

load_dotenv()

# Set the appropriate event loop policy for Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4.1", api_key=openai_api_key)


async def run_browser_use_example():
    agent = Agent(
        task="search for the meteo in paris",
        llm=llm,
    )
    result = await agent.run()
    return result
