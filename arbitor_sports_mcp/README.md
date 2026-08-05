# Arbitor Sports MCP Server

An MCP (Model Context Protocol) server that exposes Arbitor Sports student registration data to AI agents via a Streamable HTTP interface.

**Use Case:** Registration Insights & Recommendations — powers the "Ask Arbiter AI" chat interface.

---

## Project Structure

```
arbitor_sports_mcp/
├── server.py          ← Main MCP server (FastMCP)
├── mock_data.json     ← Mock dataset (30 rows × 5 tables)
├── requirements.txt   ← Python dependencies
└── README.md          ← This file
```

---

## Setup & Deployment

### 1. Prerequisites

- Python 3.10 or higher
- pip

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Server

```bash
python server.py
```

The server starts on:
```
http://0.0.0.0:8092/arbitor_sports
```

> **Note:** To change the port, edit `port=8092` in `server.py`.

---

## MCP Endpoint

| Setting | Value |
|---------|-------|
| Host | `0.0.0.0` |
| Port | `8092` |
| Path | `/arbitor_sports` |
| Transport | `streamable-http` |
| Full URL | `http://<server-ip>:8092/arbitor_sports` |

---

## Available Tools

### Registrations

| Tool | Description |
|------|-------------|
| `get_all_registrations()` | All registration records |
| `get_registrations_by_state(state)` | Filter by registration_state |
| `get_registrations_by_approval(approval)` | Filter by approval status |
| `get_incomplete_document_registrations()` | Registrations with incomplete docs |

### Payments

| Tool | Description |
|------|-------------|
| `get_all_payments()` | All payment records |
| `get_payments_by_state(payment_state)` | Filter by payment_state |
| `get_outstanding_payments()` | Payments with balance > 0 |
| `get_payment_by_registration(registration_id)` | Payment for a specific registration |

### Programs & Sections

| Tool | Description |
|------|-------------|
| `get_programs_and_sections()` | All programs and sections |
| `get_capacity_insights()` | Sections at/near/available capacity |

### Participants

| Tool | Description |
|------|-------------|
| `get_all_participants()` | All participant records |
| `get_participants_by_school(school_name)` | Participants from a school |
| `get_participant_demographics_summary()` | Age, gender, grade, school stats |

### Transfers

| Tool | Description |
|------|-------------|
| `get_all_transfers()` | All transfer records |
| `get_transfers_by_status(transfer_status)` | Filter by transfer status |
| `get_transfers_summary()` | Transfer counts by status and reason |

### Cross-Dataset Analytics

| Tool | Description |
|------|-------------|
| `get_registration_summary()` | Full aggregated analytics summary |
| `search_registrations(query)` | Keyword search across registrant/school/program |
| `get_full_registration_detail(registration_id)` | Complete record for one registration |

---

## Status Enums Reference

### Registration State
`draft` · `pending` · `expired` · `completed` · `canceled` · `listed_canceled` · `correction_required`

### Payment State
`none` · `void` · `pending` · `partial` · `partial_refunded` · `refunded` · `completed` · `canceled` · `failed`

### Approval
`approved` · `not_approved` · `Pending`

### Document
`Complete` · `Incomplete`

### Transfer Status
`pending` · `approved` · `rejected` · `in_review_receiving_school` · `in_review_previous_school` · `completed_previous_school` · `state_review_requested` · `appeal_review_requested` · `state_review_in_progress` · `state_approved` · `state_approved_for_sub_varsity` · `state_rejected` · `appeal_review_in_progress` · `appeal_approved` · `appeal_rejected` · `transfer_not_applicable`

---

## Connecting to Claude Desktop

Add to your Claude Desktop `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "arbitor_sports": {
      "url": "http://localhost:8092/arbitor_sports"
    }
  }
}
```

---

## Sample Prompts (Ask Arbiter AI)

- "How many registrations are currently pending?"
- "Show me all participants with incomplete documents."
- "Which sections are near capacity?"
- "What is the total outstanding payment balance?"
- "Find all registrations from Lincoln Elementary."
- "Give me a full demographic breakdown of participants."
- "What are the most common reasons for transfer requests?"
- "Show me the full details for registration REG-10045."
