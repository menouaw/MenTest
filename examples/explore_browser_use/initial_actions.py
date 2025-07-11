from browser_use.llm import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

import asyncio

url = "https://en.wikipedia.org/wiki/Randomness"
context = "Username : Admin, Password : admin123"

initial_actions = [
    {"go_to_url": {"url": url, "new_tab": True}},
    {"scroll": {"down": True, "num_pages": 1}},
]

llm = ChatOpenAI(model="gpt-4.1")


async def main():
    agent = Agent(
        task="what is the username and password provided in the context?",
        llm=llm,
        initial_actions=initial_actions,
        use_vision=False,  # Enable vision capabilities
        save_conversation_path="logs/conversation",  # Save chat logs
        message_context=context,
        extend_system_message="You are a shy and funny assistant",
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
