from browser_use.llm import ChatGoogle, ChatOpenAI
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
openai_api_key = os.getenv("OPENAI_API_KEY")

gemini25pro = ChatGoogle(model="gemini-2.5-pro")
gemini20flashlite = ChatGoogle(model="gemini-2.0-flash-lite")
gpt41 = ChatOpenAI(model="gpt-4.1")


async def run_browser_use_example(task: str, llm=gemini20flashlite, use_vision: bool = False):
    agent = Agent(
        task=task,
        llm=llm,
        use_vision=use_vision,
        max_failures=3,
        retry_delay=10,
        message_context="",
        generate_gif=True,
        override_system_message=None,
        extend_system_message=None,
        max_actions_per_step=10,
        use_thinking=False, # dev only
        max_history_items=40,
        images_per_step=1,
        page_extraction_llm= gemini20flashlite,
        planner_llm=gemini20flashlite,
        is_planner_reasoning=False,
        expend_planner_system_message=None,
        calculate_cost=True,
        save_conversation_path="logs/conversation",
    )
    
    result = await agent.run()
    return result