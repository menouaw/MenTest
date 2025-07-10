from browser_use.llm import ChatOpenAI
from browser_use import Agent, BrowserSession
from dotenv import load_dotenv
from PIL import Image, ImageFont
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

import asyncio

url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
task="connect on the system"
context="you working as a hr manager and you are trying to login to the system to check the employee details"

initial_actions = [
	{'go_to_url': {'url': url, 'new_tab': True}},
	{'scroll': {'down': True, 'num_pages': 1}},
]

browser_session = BrowserSession(
    highlight_elements=True,
    deterministic_rendering=False,
    include_dynamic_attributes=True,
    save_recording_path="logs/recording",
)

llm = ChatOpenAI(model="gpt-4.1")
planner_llm = ChatOpenAI(model='o3-mini')

gif_path = "gifs/conversation.gif"
gif_dir = os.path.dirname(gif_path)
if gif_dir and not os.path.exists(gif_dir):
    os.makedirs(gif_dir)


async def main():
    agent = Agent(
    task=task,
    llm=llm,
    initial_actions=initial_actions,
    browser_session=browser_session,
    use_vision=False,
    planner_llm=planner_llm,
    use_vision_for_planner=True,
    planner_interval=1,
    save_conversation_path="logs/conversation",
    message_context=context,
    extend_system_message="You are a shy and funny assistant",
    generate_gif=gif_path,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
