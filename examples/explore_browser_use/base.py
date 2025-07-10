from browser_use.llm import ChatOpenAI
from browser_use import Agent, Controller, BrowserSession
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4.1")


controller = Controller()

async def main():
    agent = Agent(
    task="search for the meteo in my city for today",
    llm=llm,
    use_vision=True,              # Enable vision capabilities
    save_conversation_path="logs/conversation",  # Save chat logs
    extend_system_message="You are a shy and funny assistant"
    )
    result = await agent.run()
    print(result)

asyncio.run(main())