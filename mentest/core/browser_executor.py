from browser_use.llm import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")  # Initialize LLM once


async def execute_browser_prompt(prompt_text: str):
    """Executes the given prompt using Browser Use and returns the result."""
    try:
        agent = Agent(
            task=prompt_text,
            llm=llm,
        )
        result = await agent.run()
        return {"success": True, "result": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
