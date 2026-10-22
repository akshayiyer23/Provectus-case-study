# Case Study Remix

A small CrewAI agent that turns one published case study into three pieces of content that lead with the business result, not the technology.

**Input:** Provectus's nugs.net case study (`case.txt`)
**Output:** a 150-word summary, a LinkedIn post, and a 60-second video script (`output.md`)

## How it works

Three Claude agents work in order:

1. **Analyst** pulls out the problem, what was built, and every before/after number
2. **Writer** writes all three pieces, opening each with the business result
3. **Fact-checker** checks every claim against the source and fixes anything that isn't in it

## Why the fact-checker matters

On the first run, the writer overclaimed in a few places. The fact-checker caught them:

- The writer said the new dbt models replaced 118 pipelines. The source says they replaced 164 stored procedures and 17 data flows. Fixed.
- The writer said decisions no longer rely on day-old numbers. The source only says critical flows moved to hourly. Softened to match.
- The writer said the knowledge "no longer sits with two engineers." The source says reliance on them was reduced. Fixed.

For enterprise AI marketing, a wrong number costs more than a boring sentence. So the last step checks every claim before anything gets published.

## Run it

    uv venv --python 3.12
    source .venv/bin/activate
    uv pip install "crewai[anthropic]"
    export ANTHROPIC_API_KEY="your-key"
    python remix.py

Built by Akshay Iyer.