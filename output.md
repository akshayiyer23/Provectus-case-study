## 1) 150-word summary

nugs.net cut its data platform cost by 80%, from about $10,000 a month to about $2,000, on the same workload. That is roughly $96,000 a year, and the savings paid for the migration within the first year.

The full pipeline run also fell from 12 to 16 hours to under 1 hour. Critical flows now refresh hourly instead of once a day, a change from the day-old numbers that had informed decisions on live-event performance, churn and marketing spend.

Provectus moved nugs.net from an Azure SQL warehouse, where logic spanned 118 Data Factory pipelines and 164 stored procedures, to a Databricks lakehouse and dbt. 297 dbt models now hold the logic, with about 2,900 documented columns, automated tests and review in version control. Every engineer and analyst gets a private environment per branch.

Analysts now own the reporting layer, and reliance on the two engineers who maintained the old platform is reduced. AI-assisted development and Genie for business teams are the next phase.

## 2) LinkedIn post

nugs.net now pays about $2,000 a month for a data platform that used to cost about $10,000. Same workload. That is roughly $96,000 a year back, and it paid for the migration within the first year.

The bigger change is speed. A full run used to take 12 to 16 hours. It now takes under 1. Critical flows refresh hourly, not once a day, so decisions on live-event performance, churn and marketing spend no longer have to rely on day-old numbers for those flows.

Why not just add compute? Provectus recommended replacing the architecture instead. More compute could have shortened the runs, but it would have left two problems in place:
- Ten years of logic spread across 118 pipelines and 164 stored procedures, where one column change could silently break a report.
- Two engineers who held the knowledge to maintain it, with every analyst request in the same queue.

So the team rebuilt it on Databricks and dbt. 297 tested, documented models replaced the stored procedures and visual data flows. Changes go through review. Every engineer and analyst gets a private environment per branch and can test against the full production dataset.

One setting stands out: shutting compute down after 1 minute idle instead of 5 recovered 30 to 40% of warehouse spend. This is part of the overall cost reduction, not on top of it.

Analysts now own the reporting layer. AI-assisted modeling and Genie for business teams come next, and there are no results to report on those yet.

## 3) 60-second video script

**[0:00 to 0:08] HOOK**
Voiceover: "This team cut its data bill by 80% and moved its critical data flows from daily to hourly. Here is how."

**[0:08 to 0:20]**
Voiceover: "nugs.net streams live music. Its data platform cost about $10,000 a month, and the nightly run took 12 to 16 hours. If a run failed, there was no fresh data that day."

**[0:20 to 0:32]**
Voiceover: "Ten years of logic spanned 118 pipelines and 164 stored procedures. Two engineers held the knowledge to maintain it. Every request, including analysts', waited in the same queue."

**[0:32 to 0:46]**
Voiceover: "Adding compute would not fix that. So Provectus rebuilt it on Databricks and dbt. 297 tested, documented models replaced the stored procedures and data flows. Every change is reviewed, and every engineer and analyst gets a private environment."

**[0:46 to 0:57]**
Voiceover: "The result: about $2,000 a month, roughly $96,000 saved a year. Full runs now take under an hour. Critical data flows refresh hourly."

**[0:57 to 1:00] CLOSE**
Voiceover: "Analysts now own the reporting layer. Talk to Provectus about your data platform."

**On-screen text suggestions:** "$10,000 to $2,000 a month" at 0:00. "12 to 16 hours to under 1 hour" at 0:48. "$96,000 saved a year" at 0:52.

## What I fixed

**Summary**
- Replaced "decisions... no longer rest on day-old numbers" with wording tied to critical flows, since the source only says critical flows went hourly.
- Changed "Provectus replaced an Azure SQL warehouse, 118 pipelines and 164 procedures" to say the logic spanned those items. The source says the 297 models replaced the 164 procedures and 17 data flows, not the 118 pipelines.
- Changed "knowledge no longer sits with two engineers" to "reliance on the two engineers... is reduced," which matches the source.

**LinkedIn post**
- Replaced "Provectus advised against it" with "recommended replacing the architecture instead."
- Replaced "logic buried in 164 stored procedures" with "spread across 118 pipelines and 164 stored procedures."
- Removed "all the knowledge" and used "the knowledge to maintain it."
- Softened "working with current numbers" to the critical-flows version.
- Added that each person can test against the full production dataset, and noted that the idle-compute saving is part of the overall reduction.

**Video script**
- Changed "daily reports to hourly ones" to "critical data flows from daily to hourly."
- Changed "replaced the old code" to "replaced the stored procedures and data flows."
- Changed "Two engineers knew how it all worked" to "held the knowledge to maintain it."
- Changed "everyone tests in a private environment" to "every engineer and analyst gets a private environment."
- Added the 118 pipelines to the claim about where the logic sat, and changed "Critical data refreshes hourly" to "Critical data flows refresh hourly."

**Left as is**
- The closing "Talk to Provectus" line is a call to action, not a factual claim, so I kept it. Delete it if you want strictly source-only text.