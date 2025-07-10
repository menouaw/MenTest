# Feature

## Description
- MenTest is a code-agnostic software package based on Streamlit using Browser Use focused on QA:   
    - Generation
    - Execution
    - Visualization
    - Self-healing
- Web-focused (desktop app? mobile?)
- Human intervention required
- Easy to learn, hard to master

## Target Audience
- Technical and functional testers

## Test Scope
- **Base**:
    - Integration/end-to-end
    - Visual interface
    - Smoke/sanity
- **Performance**:
    - Load
    - Reliability
    - Recovery

### Usage
1.  **Project setup**
    - Target site (URL)
    - System instructions (e.g., credentials)
    - Software specifications
2.  **Test scope selection**
3.  **Scenario generation** (human validation)
4.  **Launching test processes**
5.  **Visualization of results**
    - OK/KO metrics
    - Video capture of processes (+details of actions performed)
    - Summary and recommendations

## Process
1.  **Site exploration** (exploratory tests) ⇒ SiteSpector?
2.  **Test case generation**
3.  **Gherkin scenario generation**
4.  **Test execution** (+code generation) ⇒ BrowserUse
5.  **Visuals generation**

## Frameworks
- **User interface** ⇒ Streamlit
- **Internal functioning** ⇒ FastAPI
- **Response generation** ⇒ Choice of LLM
- **Web automation** ⇒ Browser Use (+ Choice of LLM)
- **Visualization/reports** ⇒ Allure

---

# Examples

In the 'examples/', you will find different related projects, on which you can base yourself, select the features that seem most relevant and that suit the project.

- `examples/Agno/` - automation framework based on browser use, interesting for its way to separate the usage and its proposition to choose the framework of our choice to generate the code (Playwright, Selenium, etc.)
- `examples/allure2` - framework for reporting and visualization of tests results
- `examples/browser-use` - principal framework, contains a lot of examples and documentation
- `examples/browser-use-auto-testing` - framework for auto-testing, contains some examples of implementation of allure with browser use
- `examples/explore-browser-use` - some examples of my personal implementation of browser use
- `examples/factif-ai` - interesting framework of automation, exploratory test, navigation graphe with routes classification that I want to implement in my project
- `examples/playwright-npm-esm-js` - framework for testing, contains some examples of implementation of allure with playwright
- `examples/rocketship` - framework of automation testing, interesting for its functionnality that allowas to program the test and make it repeatable
- `examples/site-spector` - automation framework, interesting for its exploratory tests (url, nb of iterations, nb of max tasks), generate a navigation graph and synthetize the explorated pages

---

# Documentation

- **Browser Use**: https://docs.browser-use.com/quickstart
- **Streamlit**: https://docs.streamlit.io/
- **FastAPI**: https://fastapi.tiangolo.com/
- **Allure**: https://allure.org/
- **Playwright**: https://playwright.dev/
- **Gherkin**: https://cucumber.io/docs/gherkin/reference/

---

# Other Considerations

- Include a README with instructions for setup
- Include the project structure in the README.
- Use `python_dotenv` and `load_env()` for environment variables
