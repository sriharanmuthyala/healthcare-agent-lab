# Document intake and matching assistant

User: Records administrator

Problem: Faxes and forms require manual classification and careful matching to the correct patient record.

Workflow: Classify fictional faxes and match them to a synthetic patient register with an exception queue

Input: 30 fictional fax documents, including ambiguous names, plus a synthetic patient register.

Output: Document category, extracted identifiers, proposed match, supporting evidence and an exception queue.

Measure: Match precision, false-match rate, exception recall and staff review time.

Review: Human approval before live action. Clinical outputs require a qualified reviewer.

Source: Google Cloud industry examples: healthcare and life sciences, Healthcare & Life Sciences / Employee Agents / supplied entry 24: Covered California
https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders

Adaptation: Based on document handling examples. Synthetic data only. A reviewer confirms every patient match; ambiguous matches abstain.

Score: 95/100. Initial analyst judgement, not validated ROI.
