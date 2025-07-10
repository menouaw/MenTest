from browser_use import BrowserSession, BrowserProfile, Agent
from browser_use.llm import ChatOpenAI
import asyncio

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1")

browser_profile = BrowserProfile(
    headless=False,
    storage_state="logs/storage_state.json",
    wait_for_network_idle_page_load_time=3.0,
    viewport={"width": 1280, "height": 1100},
    locale='en-US',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    highlight_elements=True,
    viewport_expansion=500,
    allowed_domains=['*.google.com', 'http*://*.wikipedia.org', 'http*://*.orangehrmlive.com'],
    user_data_dir=None,
)

async def main():
    browser_session = BrowserSession(
        browser_profile=browser_profile,
        headless=True,                          # extra kwargs to the session override the defaults in the profile
    )

    # you can drive a session without the agent / reuse it between agents
    await browser_session.start()
    page = await browser_session.get_current_page()
    await page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    agent = Agent(
        task='connect on the system',
        llm=llm,
        page=page,                        # optional: pass a specific playwright page to start on
        browser_session=browser_session,  # optional: pass an existing browser session to an agent
    )
    result = await agent.run()
    print(result)
    await browser_session.close()

if __name__ == "__main__":
    asyncio.run(main())