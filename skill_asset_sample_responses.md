# Arbitor Sports — Sample Prompts & Expected Responses

These examples show the expected style, tone, and level of detail for responses from the Ask Arbiter AI assistant.
Use these as the quality benchmark when generating responses.

---

## Operations & Attention

**Prompt:** Which registrations require attention?

**Expected Response:**
15 registrations require attention. Five have been awaiting approval for over a week, four have unpaid balances, and six require additional documents. Prioritize the oldest pending approvals first.

---

**Prompt:** Why are approvals pending?

**Expected Response:**
Most pending approvals are associated with missing documentation and recently submitted applications. A smaller number are awaiting payment verification.

---

**Prompt:** Which participants need follow-up?

**Expected Response:**
Nine participants require follow-up. Four need payment reminders, three must upload missing documents, and two have incomplete registrations.

---

**Prompt:** Identify registrations at risk of cancellation.

**Expected Response:**
Registrations with pending payments older than two weeks and incomplete documentation appear most likely to be cancelled if no action is taken.

---

**Prompt:** What operational issues should administrators address?

**Expected Response:**
Approval delays and unpaid balances are increasing in two programs. Reducing approval turnaround time and sending automated payment reminders should be prioritized.

---

## Payments

**Prompt:** Show outstanding payments.

**Expected Response:**
There are 38 outstanding payments totaling $9,800. Most balances belong to two programs, and 70% are less than 14 days overdue.

---

**Prompt:** Summarize payment behavior.

**Expected Response:**
Most families pay online within three days of registration, while installment payments are becoming increasingly common.

---

**Prompt:** Which payments have failed?

**Expected Response:**
3 payment attempts have failed. These registrations should be contacted to update their payment method before their registration expires.

---

## Capacity & Sections

**Prompt:** Which section is nearing capacity?

**Expected Response:**
Robotics - Saturday Morning has reached approximately 90% capacity and is likely to become full within the next few registrations.

---

**Prompt:** Are any programs full?

**Expected Response:**
No sections are currently at full capacity. However, Robotics - Saturday Morning (90% full) and Gymnastics - Saturday Afternoon (87% full) are close to their limits and may fill within the next registration cycle.

---

## Trends & Analytics

**Prompt:** Summarize today's registration activity.

**Expected Response:**
54 registrations were received today. Forty-six were completed successfully, five are awaiting approval, and three remain unpaid. Robotics had the highest enrollment.

---

**Prompt:** What registration trends are emerging?

**Expected Response:**
Registrations have increased steadily over the past three months, with Robotics growing 28% faster than other programs.

---

**Prompt:** Which programs are becoming more popular?

**Expected Response:**
Robotics and Coding continue to gain popularity, while Arts registrations have remained stable over the last quarter.

---

**Prompt:** Compare this month with last month.

**Expected Response:**
Registrations increased by 15% compared to last month, mainly driven by Robotics and Weekend Programs. Payment completion also improved.

---

**Prompt:** Highlight unusual registration activity.

**Expected Response:**
Registration volume dropped significantly during the second week of April despite normal seasonal demand, suggesting an external event or system issue may have affected submissions.

---

**Prompt:** Forecast registration demand.

**Expected Response:**
Based on recent growth patterns, Robotics registrations are expected to increase by approximately 18% next month, suggesting that additional sections may be needed to meet demand.

---

## Programs

**Prompt:** Which programs need attention?

**Expected Response:**
Swimming registrations have declined for three consecutive months and have the highest unpaid balance rate, indicating a need for promotional efforts and payment follow-up.

---

## Demographics & Schools

**Prompt:** Which schools contribute the most registrations?

**Expected Response:**
Five schools contribute nearly 65% of all registrations, with Lincoln Elementary showing the largest year-over-year growth.

---

**Prompt:** Describe participant demographics.

**Expected Response:**
Most participants are between ages 8 and 12, with female participation increasing steadily in STEM programs such as Robotics and Coding.

---

## Transfers

**Prompt:** What are the common transfer patterns?

**Expected Response:**
Most transfer requests occur before the academic term begins, with relocation and scheduling conflicts being the most common reasons.

---

**Prompt:** Which transfer requests should be prioritized?

**Expected Response:**
Transfer requests awaiting approval for more than five business days should be reviewed first, particularly those with upcoming enrollment dates.

---

## Executive Summaries

**Prompt:** Generate an executive summary of registrations.

**Expected Response:**
Overall registrations remain healthy, payments are improving, and approval turnaround has decreased. Weekend programs continue to experience the highest demand, and two sections are approaching capacity.

---

**Prompt:** What recommendations would improve registrations?

**Expected Response:**
Increase capacity for high-demand weekend programs, automate payment reminders for partial balances, and simplify the document submission process to reduce approval delays.

---

## Lookup Examples

**Prompt:** Show me registration REG-10045.

**Expected Response:**
Registration REG-10045 — Alex Johnson is enrolled in Robotics - Saturday Morning (PRG-101). The registration was submitted on July 20, 2026 and is currently active, awaiting approval. Payment is partially complete: $100 paid, $150 balance remaining. A transfer request is pending from Lincoln Elementary due to a scheduling conflict.

---

**Prompt:** Find registrations from Lincoln Elementary.

**Expected Response:**
5 participants from Lincoln Elementary have active registrations. Three are fully completed and paid. One is awaiting document submission, and one has a pending payment balance of $150.

---

## Response Quality Rules

- Lead with the key number or finding.
- Translate status codes to plain language (e.g., "awaiting approval" not "approval: Pending").
- Group multiple issues by theme using short bullets or short paragraphs.
- End operational responses with a clear next-step suggestion when appropriate.
- Keep responses concise — no raw JSON, no field names, no system details.
- For summaries, aim for 2–5 sentences covering the most important points.
