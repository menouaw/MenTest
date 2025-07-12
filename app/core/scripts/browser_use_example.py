from browser_use.llm import ChatGoogle
from browser_use import Agent
from dotenv import load_dotenv
import os
import asyncio
import platform

load_dotenv()

if platform.system() == "Windows":
    policy = getattr(asyncio, "WindowsProactorEventLoopPolicy", None)
    if policy is not None:
        asyncio.set_event_loop_policy(policy())

google_api_key = os.getenv("GOOGLE_API_KEY")
# openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatGoogle(model="gemini-2.5-pro")


async def run_browser_use_example(task: str, llm=llm, use_vision: bool = False):
    agent = Agent(
        task=task,
        llm=llm,
        use_vision=use_vision,
        save_conversation_path="logs/conversation",
    )
    
    result = await agent.run()
    return result
