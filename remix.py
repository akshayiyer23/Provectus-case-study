from crewai import Agent, Task, Crew

llm = "anthropic/claude-sonnet-5-5"

source = open("case.txt").read()

analyst = Agent(
    role="Analyst",
    goal="Find the business problem, what was built, and every before/after number",
    backstory="You read technical case studies and find the part a CFO cares about.",
    llm=llm)

writer = Agent(
    role="Writer",
    goal="Write content that opens with the business result, not the technology",
    backstory="You write plain, specific B2B content. No hype words, no em dashes.",
    llm=llm)

checker = Agent(
    role="Fact-checker",
    goal="Make sure every number and claim matches the source exactly",
    backstory="You delete anything not in the source. You never invent numbers.",
    llm=llm)

t1 = Task(
    description=f"Read this case study and list: the problem, what was built, and every result number.\n\n{source}",
    expected_output="Three labeled bullet lists: Problem, Build, Results",
    agent=analyst)

t2 = Task(
    description=("Using the analysis, write three pieces. Each must open with the business result. "
                 "1) A 150-word summary. 2) A LinkedIn post under 200 words. "
                 "3) A 60-second video script with a hook in the first line."),
    expected_output="Three labeled pieces of content",
    agent=writer)

t3 = Task(
    description=f"Check all three pieces against this source. Fix or remove anything not in it.\n\n{source}",
    expected_output="The final three pieces, plus a short list of what you fixed",
    agent=checker)

result = Crew(agents=[analyst, writer, checker], tasks=[t1, t2, t3]).kickoff()
print(result)
open("output.md", "w").write(str(result))