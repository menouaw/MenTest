from dotenv import load_dotenv

load_dotenv()

from browser_use.llm import ChatOpenAI
from browser_use import Agent, BrowserSession, Controller, ActionResult

import asyncio

llm = ChatOpenAI(model="gpt-4.1")

# Define sensitive data
# The LLM will only see placeholder names (x_member_number, x_passphrase), never the actual values
sensitive_data = {
    "https://*.orangehrmlive.com": {
        "x_username": "Admin",
        "x_password": "admin123",
    },
}

controller = Controller()


@controller.action(
    "Ask human for help with a question", domains=["https://*.orangehrmlive.com"]
)  # pass allowed_domains= or page_filter= to limit actions to certain pages
def ask_human(question: str) -> ActionResult:
    answer = input(f"{question} > ")
    return ActionResult(
        extracted_content=f"The human responded with: {answer}", include_in_memory=True
    )


# Use the placeholder names in your task description
task = """
1. go to https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
2. disconnect if already logged in, if not, sign in with your member number x_username and private access code x_password
3. ask human if he is able to see the page
"""

# Recommended: Limit the domains available for the entire browser so the Agent can't be tricked into visiting untrusted URLs
browser_session = BrowserSession(
    allowed_domains=["https://*.orangehrmlive.com"], storage_state="./auth.json"
)

agent = Agent(
    task=task,
    llm=llm,
    sensitive_data=sensitive_data,  # Pass the sensitive data to the agent
    browser_session=browser_session,  # Pass the restricted browser_session to limit URLs Agent can visit
    use_vision=False,  # Disable vision or else the LLM might see entered values in screenshots
    controller=controller,
)


async def main():
    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
