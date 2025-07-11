from browser_use.llm import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import os

load_dotenv()

import asyncio
import platform

# Set the appropriate event loop policy for Windows
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4.1", api_key=openai_api_key)


async def run_browser_use_example():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm,
    )
    result = await agent.run()
    return result
