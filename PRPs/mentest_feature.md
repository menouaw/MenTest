name: "MenTest: AI-Powered QA Testing Platform"
description: |

## Purpose
This PRP outlines the development of MenTest, a code-agnostic software package designed for QA testers. It leverages AI for test generation, execution, visualization, and self-healing, with a focus on web applications. The system is built on a modern Python stack, integrating Streamlit for the UI, FastAPI for the backend, Browser Use for web automation, and Allure for reporting.

## Core Principles
1. **Context is King**: Include ALL necessary documentation, examples, and caveats.
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix.
3. **Information Dense**: Use keywords and patterns from the codebase.
4. **Progressive Success**: Start simple, validate, then enhance.
5. **Global rules**: Be sure to follow all rules in CLAUDE.md.

---

## Goal
To build a comprehensive, user-friendly QA testing platform that automates the entire testing lifecycle for web applications. The platform will enable both technical and functional testers to easily set up projects, generate and validate test scenarios, execute tests, and visualize results in a rich, interactive dashboard.

## Why
- **Business value**: Drastically reduce the time and effort required for web application testing, improve test coverage, and accelerate release cycles.
- **Integration**: Provide a unified interface that combines the power of multiple specialized frameworks (Browser Use, Allure, etc.) into a seamless workflow.
- **Problems solved**: Addresses the complexity and manual effort of modern web QA by providing an easy-to-learn, hard-to-master tool that automates repetitive tasks and provides deep insights into application quality.

## What
A Streamlit-based web application that guides users through the following workflow:
1.  **Project Setup**: Configure the target URL, system instructions (like credentials), and software specifications.
2.  **Site Exploration**: Automatically crawl the target website to discover pages, components, and user flows, generating a navigation graph (inspired by SiteSpector and factif-ai).
3.  **Test Generation**: Based on the exploration phase, generate test cases and Gherkin-style scenarios for user validation.
4.  **Test Execution**: Run the validated scenarios, generating automation scripts in the framework of our choice (Selenium + PytestBDD, Playwright, Cypress, Robot Framework, Selenium + Cucumber => inspired by Agno) on the fly using Browser Use.
5.  **Results Visualization**: Present detailed test results, including OK/KO metrics, video recordings of test runs, action details, and a final summary with recommendations in an Allure dashboard.

### Success Criteria
- [ ] Users can set up a new testing project with a target URL.
- [ ] The application can perform an exploratory crawl of a given website.
- [ ] Test cases and Gherkin scenarios are successfully generated from the crawl data.
- [ ] The system can execute generated tests using Browser Use.
- [ ] Allure reports are generated and can be viewed from the UI.
- [ ] The entire application is covered by unit and integration tests.

## All Needed Context

### Documentation & References
```yaml
# MUST READ - Include these in your context window
- url: https://docs.browser-use.com/
  why: Core web automation framework documentation.
  
- url: https://docs.streamlit.io/
  why: UI framework for the application.
  
- url: https://fastapi.tiangolo.com/
  why: Backend API framework for internal processing.

- url: https://allure.org/
  why: Test reporting and visualization framework.
  
- url: https://playwright.dev/python/docs/intro
  why: One of the target code generation frameworks for Browser Use.
  
- url: https://cucumber.io/docs/gherkin/reference/
  why: Syntax for generating human-readable test scenarios.

- file: examples/site-spector/
  why: Inspiration for exploratory testing and navigation graph generation.
  
- file: examples/factif-ai/
  why: Inspiration for navigation graph with route classification.
  
- file: examples/browser-use-auto-testing/
  why: Example of integrating Browser Use with Allure.

- file: examples/Agno/
  why: Inspiration for separating code generation logic and framework choice.
```

### Architectural Patterns: Multi-Agent Pipeline & Provider Strategy
**Inspired by `examples/Agno/` and `examples/factif-ai/`**

We will adopt a component-based architecture where each "service" orchestrates a pipeline of specialized AI agents. This creates a clear separation of concerns and allows for more complex, multi-step reasoning.

A key pattern discovered in `factif-ai` is the use of a **Provider Strategy Pattern** for the LLM. Instead of just changing prompts for an agent, we will switch out the entire LLM Provider class based on the task. This allows for fundamentally different logic, state management, and prompting techniques for different modes of operation.

We will implement two main provider strategies:
1.  **Standard Provider**: Used for direct Q&A, code generation, and single-shot tasks. It is stateless and uses a general-purpose system prompt.
2.  **Explore Mode Provider**: A stateful provider used for the site exploration service. It maintains a list of visited pages, manages a dual-prompt system for analysis and action, and automatically triggers a documentation generation step for new pages.

The high-level flow will be:
1.  **Exploration Service**: Uses an `ExplorerAgent` running with the `Explore Mode Provider` to crawl the site, automatically generating detailed documentation for each unique view and identifying interactive elements.
2.  **Generation Service**: Orchestrates a `ManualTestCaseAgent` (to create test cases from the rich, generated documentation) followed by a `GherkinAgent` (to convert test cases into Gherkin scenarios).
3.  **Execution & CodeGen Service**: Orchestrates a `BrowserExecutionAgent` (to run the Gherkin scenario in a browser and capture history) followed by a `CodeGenAgent` (to translate the execution history into a test script for a specific framework).

### Desired Codebase tree with files to be added
```bash
.
├── mentest/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── project.py      # Project setup endpoints
│   │   │   └── testing.py      # Test execution endpoints
│   │   └── main.py             # FastAPI app definition
│   ├── app/
│   │   ├── __init__.py
│   │   ├── pages/
│   │   │   ├── __init__.py
│   │   │   ├── 1_Project_Setup.py
│   │   │   ├── 2_Site_Exploration.py
│   │   │   ├── 3_Test_Generation.py
│   │   │   ├── 4_Test_Execution.py
│   │   │   └── 5_Results_Dashboard.py
│   │   └── Mentest.py          # Main Streamlit app
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration using pydantic-settings
│   │   └── models.py           # Pydantic models for data
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── app_doc_generator.md
│   │   ├── browser_execution_agent.md
│   │   ├── code_gen_agent.md
│   │   ├── explore_mode.md
│   │   ├── gherkin_agent.md
│   │   ├── manual_test_case_agent.md
│   │   ├── route_classifier.md
│   │   ├── system_prompt.md
│   │   └── user_story_enhancement_agent.md
│   ├── services/
│   │   ├── __init__.py
│   │   ├── explorer.py         # Site exploration logic (SiteSpector-like)
│   │   ├── generator.py        # Test case and scenario generation
│   │   ├── executor.py         # Test execution using Browser Use
│   │   └── reporter.py         # Allure report generation
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Utility functions
├── tests/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── test_project.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── test_explorer.py
│   │   ├── test_generator.py
│   │   └── test_executor.py
│   └── conftest.py
├── .env.example                 # Environment variables template
├── requirements.txt             # Project dependencies
├── README.md                    # Comprehensive documentation
├── PLANNING.md                  # Project plan and architecture
└── TASK.md                      # Task tracking
```

### Known Gotchas & Library Quirks
```python
# CRITICAL: Streamlit reruns the entire script on each interaction. State management must be handled carefully (st.session_state).
# CRITICAL: The Explorer Service is STATEFUL. The graph of visited pages and docs must be persisted in Redis to be available across user interactions and app restarts.
# CRITICAL: FastAPI endpoints must be async if they perform I/O operations to avoid blocking the event loop.
# CRITICAL: Browser Use requires an LLM for its reasoning capabilities. The choice of LLM and API key management is essential.
# CRITICAL: Allure reports are static HTML files. Serving them from Streamlit requires a custom component or careful file handling.
# CRITICAL: The exploratory crawler needs to be robust against different website structures, SPAs, and anti-bot measures.
```

## Implementation Blueprint

### list of tasks to be completed to fullfill the PRP in the order they should be completed

```yaml
Task 1: Project Scaffolding and Setup
CREATE all directories and __init__.py files from the Desired Codebase Tree.
CREATE core/config.py:
  - Use pydantic-settings to manage environment variables.
CREATE core/models.py:
  - Define Pydantic models for Project, TestScenario, and ExecutionResult.
CREATE .env.example with placeholders for LLM API keys.
CREATE requirements.txt with initial dependencies: streamlit, fastapi, pydantic, pydantic-settings, browser-use, allure-pytest.

Task 1.5: Infrastructure Setup
- Provision a local Redis Stack instance using Docker to power the Site Explorer’s graph cache and JSON storage.  
  For local development you can run:

  ```bash
  docker run -d --name mentest-redis -p 6379:6379 \
      -e REDIS_ARGS="--appendonly yes --appendfsync everysec" \
      --restart=always redis/redis-stack:latest
  ```

  Redis Stack is required because the Explorer uses the RedisGraph and RedisJSON modules.

- Add `REDIS_HOST` and `REDIS_PORT` placeholders (default `localhost` / `6379`) to `.env.example`.
- Update `requirements.txt` to include `redis` and `networkx`.
- Optionally supply a `docker-compose.yml` for one-command startup in CI.

Task 2: Implement Backend API (FastAPI)
CREATE api/main.py to set up the FastAPI application.
CREATE api/endpoints/project.py:
  - Add endpoints for creating, retrieving, and updating project configurations.

Task 3: Build Basic UI (Streamlit)
CREATE app/Mentest.py as the main entry point.
CREATE app/pages/1_Project_Setup.py:
  - Build a form to capture project details (URL, credentials).
  - The form should call the FastAPI backend to save the project.

Task 4: Implement Site Explorer Service
CREATE services/explorer.py:
  - Implement the "Explore Mode Provider" strategy.
  - The service will be stateful, tracking visited URLs to avoid redundant work.
  - On visiting a NEW page, it will automatically use an `AppDocumentationGenerator` agent to analyze the screenshot and generate detailed documentation for the view.
  - For an existing view, it will use an `ExploreAgent` to analyze the screenshot and identify all interactive elements for the user.
  - The output will be a collection of rich markdown documents describing each unique page/view, which serves as a much richer "site map".
CREATE app/pages/2_Site_Exploration.py:
  - Add a button to trigger the exploration service.
  - Display the list of explored pages and their generated documentation.
  - Display the current view's screenshot and the list of interactive elements identified by the `ExploreAgent`.

Task 5: Implement Test Generation Service
CREATE services/generator.py:
  - Orchestrate a `ManualTestCaseAgent` and a `GherkinAgent`.
  - These agents will not operate on a simple URL site map, but on the rich, structured markdown documentation generated by the Explorer Service (Task 4). This provides deep context for generating high-quality, relevant test cases.
  - See `examples/Agno/src/Agents/agents.py` for agent definitions and `mentest/prompts/` for prompting inspiration.
CREATE app/pages/3_Test_Generation.py:
  - Allow the user to select which page documentation they want to generate tests for.
  - Display the generated scenarios to the user for review and validation.

Task 6: Implement Test Execution and Code Generation Service
CREATE services/executor.py:
  - Orchestrate a `BrowserExecutionAgent` to run a Gherkin scenario and a `CodeGenAgent` to generate a script from the results.
  - See `mentest/prompts/browser_execution_agent.md` for browser agent prompting strategy.
  - Implement a custom `browser-use` Controller (inspired by `examples/site-spector/site_spector/common/explorer_controller.py`) that adds a safety check to handle dynamic UIs. Before performing an action on an element by its index, it should verify that the page structure has not changed unexpectedly.
CREATE app/pages/4_Test_Execution.py:
  - Allow users to select scenarios and a target framework to run.
  - Display real-time progress and the final generated code.

Task 7: Implement Reporting
CREATE services/reporter.py:
  - A utility to generate the Allure report from test results. It will use the `allure` command-line tool to generate the report from the test result files.
CREATE app/pages/5_Results_Dashboard.py:
  - Display the generated Allure report (potentially in an iframe or by serving the files).
  - Add a button to trigger the test execution of a generated script. This will run the `pytest` command on the script and generate the Allure results.
  - The report should include performance metrics like action execution times.

Task 8: Add Comprehensive Tests
CREATE tests/ for all services and API endpoints.
- Mock external services and Browser Use where necessary.
- Ensure high test coverage.

Task 9: Create Documentation
CREATE README.md and PLANNING.md.
- Include setup, installation, usage instructions, and architecture decisions.

```

### Per task pseudocode as needed

```python
# Task 4 & 5: Site Explorer and Test Generation Services
# This pseudocode demonstrates the stateful, dual-mode exploration pattern.

# In services/explorer.py
# PATTERN: This service now uses a persistent graph structure inspired by `examples/site-spector`.
class SiteExplorer:
    def __init__(self, llm, start_url, project_id):
        self.llm = llm
        self.start_url = start_url
        # The graph is persisted in Redis, scoped to the project.
        self.graph = WebSiteGraph(graph_key=f"mentest:{project_id}")

    async def explore(self):
        """Main exploration loop, now guided by the graph."""
        # This would be driven by user interaction in the Streamlit app
        
        # Get the least-visited page from the graph to start, or use the start_url
        current_node_id = self.graph.get_available_pages()[0] if len(self.graph) > 0 else None
        if current_node_id:
            current_page = self.graph.get_node(current_node_id)
            current_url = current_page.url
        else:
            current_url = self.start_url

        while True: # Loop would be managed by user actions
            # Simulate getting browser state (screenshot, elements) for the current_url
            browser_state = await get_browser_state(current_url) 
            
            # Create a PageNode to represent the current page's structure
            current_page_node = PageNode(
                url=current_url, 
                screenshot=browser_state.screenshot, 
                description="", # Initially empty
                selector_map=browser_state.selector_map
            )

            # 1. Check if page is new using structural embeddings
            node_id, is_new = self.graph.add_node(current_page_node)

            if is_new:
                print(f"New page discovered: {current_url}. Generating documentation...")
                # 2. Auto-generate documentation for the new page
                docs = await self.generate_page_documentation(current_url)
                # Update the node in the graph with the new documentation
                page_node_with_docs = self.graph.get_node(node_id)
                page_node_with_docs.description = docs
                self.graph.update_node(node_id, page_node_with_docs)

            # 3. Analyze the current view to find interactive elements
            # PATTERN: Use the graph to guide exploration to the least-clicked elements
            current_page = self.graph.get_node(node_id)
            available_elements = current_page.get_available_elements()
            print(f"Analyzing page: {current_url}. Available elements to explore: {available_elements}")
            
            # 4. Present elements to user and wait for action
            # (In Streamlit, this would be rendering the screenshot and a list of buttons)
            user_choice_element_index = await get_user_interaction(available_elements) # pseudo-function
            
            # 5. Execute the chosen action and update the graph
            result = await perform_browser_action(user_choice_element_index)
            current_page.click_element_count(user_choice_element_index) # Update click count
            
            # Create a new node for the resulting page and add an edge between the two
            new_page_state = await get_browser_state()
            new_page_node = PageNode(...)
            new_node_id, _ = self.graph.add_node(new_page_node)
            self.graph.add_edge(from_id=node_id, to_id=new_node_id, edge_attrs={"action": "click", "element_index": user_choice_element_index})
            self.graph.update_node(node_id, current_page)

            # Update current_url for the next loop iteration
            current_url = new_page_state.url


    async def generate_page_documentation(self, url: str) -> str:
        """Uses a specialized agent to generate documentation for a single page."""
        # PATTERN: This mimics the `generateComponentDescription` function from factif-ai.
        # It's a single, powerful call to an agent with a very detailed prompt.
        doc_generator_agent = Agent(
            instructions=app_documentation_generator_prompt, # From mentest/prompts/
            llm=self.llm
        )

        # The agent receives the screenshot and other metadata (URL, title, etc.)
        # and returns a comprehensive markdown document.
        documentation = await doc_generator_agent.run(
            f"Generate documentation for the page at {url} based on the provided screenshot and metadata."
        )
        return documentation.content

# In services/generator.py
def generate_gherkin_from_docs(page_documentation: str) -> str:
    """Orchestrates agents to generate Gherkin from the rich documentation."""
    # PATTERN: The input is now the rich markdown doc, not a simple site map.
    manual_test_agent = Agent(instructions=manual_test_case_agent_prompt) # from mentest/prompts
    gherkin_agent = Agent(instructions=gherkin_agent_prompt)     # from mentest/prompts

    manual_test_cases = manual_test_agent.run(f"Create manual test cases from this application documentation:\n{page_documentation}")
    gherkin_scenarios = gherkin_agent.run(manual_test_cases.content)
    
    return gherkin_scenarios.content

# Task 6 & 7: Test Execution, Code Generation, and Reporting
# This pseudocode clarifies the full loop from execution to report visualization.

def execute_and_generate_script(scenario: str, framework: str) -> str:
    """
    Executes a Gherkin scenario, captures detailed history, and generates a test script.
    """
    from browser_use import AgentHistoryList
    from mentest.prompts import browser_prompts, generator_prompts

    # 1. Define the Browser Execution Agent
    # PATTERN: Use a highly-detailed prompt to guide the browser agent.
    # See: examples/Agno/src/Prompts/browser_prompts.py
    browser_agent = Agent(
        task=browser_prompts.generate_browser_task(scenario),
        # PATTERN: Use a custom controller that checks for unexpected UI changes before acting.
        # This makes the execution more robust against dynamic web pages.
        controller=get_mentest_robust_controller(),
    )

    # 2. Run the browser agent to get execution history
    history = browser_agent.run()
    if history.has_errors():
        raise Exception(f"Browser execution failed: {history.errors()}")

    # 3. Process the raw history into a structured format for the code-gen agent
    # PATTERN: Extract structured data from history to feed the next agent.
    # See: examples/Agno/src/Utilities/utils.py -> analyze_actions
    structured_history = extract_structured_history(history)
    
    # 4. Define the Code Generation Agent for Playwright + Pytest + Allure
    # The generated script will include allure decorators for rich reporting.
    # e.g., @allure.step, @allure.title, allure.attach
    # We need to ensure the correct python packages are installed for this:
    # `pip install pytest pytest-playwright allure-pytest allure-python-commons`
    code_gen_agent = Agent(
        instructions=generator_prompts.get_code_generation_prompt(framework)
    )

    # 5. Run the code-gen agent with rich context
    code_gen_prompt = f"""
    Gherkin Scenario:
    {scenario}

    Browser Execution Details (JSON):
    {structured_history}
    """
    generated_code = code_gen_agent.run(code_gen_prompt)

    # The generated code is a runnable pytest script.
    # It should be saved to a file (e.g., tests/generated/test_scenario_1.py)
    return generated_code.content

def run_generated_test_and_create_report(script_path: str):
    """
    Runs a generated pytest script and then generates the Allure report.
    """
    import subprocess
    import allure

    # 1. Run the generated test script using pytest
    # This command tells pytest to use the allure reporter and save results to 'allure-results'
    # The --clean-alluredir flag ensures old results are removed.
    pytest_command = [
        "pytest",
        script_path,
        "--alluredir=allure-results",
        "--clean-alluredir"
    ]
    subprocess.run(pytest_command, check=True)

    # 2. Generate the Allure HTML report
    # This command uses the allure CLI to generate the report into the 'allure-report' directory.
    allure_command = [
        "allure",
        "generate",
        "allure-results",
        "--output",
        "allure-report",
        "--clean"
    ]
    subprocess.run(allure_command, check=True)

    # 3. The report is now available in the 'allure-report' directory
    # The Streamlit app can now serve or display this report.
    print("Allure report generated successfully in 'allure-report'.")

def extract_structured_history(history: "AgentHistoryList") -> dict:
    """Processes agent history into a structured dict for code generation."""
    # PATTERN: Mimics the logic in examples/Agno/src/Utilities/utils.py
    actions = []
    for action, content in zip(history.model_actions(), history.action_results()):
        actions.append({
            "action_name": action.name,
            "action_params": action.parameters,
            "action_result": content, # This content includes our detailed element JSON
        })
    return {"urls": history.urls(), "actions": actions}

```

## Validation Loop

### Level 1: Syntax & Style
```bash
# Run these FIRST - fix any errors before proceeding
ruff check . --fix
black .
mypy .

# Expected: No errors.
```

### Level 2: Unit Tests
```python
# CREATE tests for each service and API endpoint.
# Example: tests/services/test_generator.py
def test_generate_scenarios_from_map():
    """Ensures test scenarios are correctly generated from a site map."""
    site_map = {"https://example.com": ["/login", "/about"]}
    scenarios = generate_scenarios(site_map)
    assert len(scenarios) > 0
    assert "Given I am on the homepage" in scenarios[0]
    assert "When I navigate to /login" in scenarios[0]
```
```bash
# Run and iterate until passing:
pytest tests/ -v
```

### Level 3: Integration Test
```bash
# 1. Start the backend API
uvicorn mentest.api.main:app --reload

# 2. Start the UI
streamlit run mentest/app/Mentest.py

# 3. Manual E2E Test:
# - Open the Streamlit app in your browser.
# - Create a new project for "http://example.com".
# - Run the site explorer.
# - Generate test scenarios.
# - Execute a scenario.
# - Check the Allure report.

# Expected: The flow completes without errors and a report is generated.
```

## Final validation Checklist
- [ ] All tests pass: `pytest tests/ -v`
- [ ] No linting errors: `ruff check .` && `black .`
- [ ] No type errors: `mypy .`
- [ ] Manual E2E test is successful.
- [ ] Error cases are handled gracefully (e.g., website not reachable).
- [ ] README is clear and complete.

---

## Anti-Patterns to Avoid
- ❌ Don't mix backend logic into the Streamlit UI scripts. Use the FastAPI service.
- ❌ Don't write monolithic functions. Break down services into smaller, testable units.
- ❌ Don't hardcode configurations. Use `core/config.py` and environment variables.
- ❌ Don't neglect state management in Streamlit; use `st.session_state`.

## Confidence Score: 9/10
High confidence in the plan due to clear project requirements and strong examples to draw from. The main challenge will be the robustness of the site explorer and the natural language step execution, which are heavily dependent on the quality of the underlying LLM and prompt engineering. The integration of multiple frameworks also adds complexity. By adopting the provider strategy and documentation-generation patterns from `factif-ai`, we significantly de-risk the exploration and test generation phases. 