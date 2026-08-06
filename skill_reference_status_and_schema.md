# Arbitor Sports — Status & Schema Reference

This document is a reference for the Arbitor Sports registration data model.
Use it to accurately translate field values into plain language when responding to users.

---

## Dataset Overview

| Dataset | Key Purpose |
|---------|-------------|
| `registrations` | Core record per student registration |
| `payments` | Payment linked to each registration |
| `programs_sections` | Programs, section names, and capacity |
| `participants` | Participant demographics |
| `transfers` | School transfer requests |

---

## Registration Fields

| Field | Description |
|-------|-------------|
| `registration_id` | Unique ID, e.g. REG-10045 |
| `participant_id` | Links to the participant record |
| `program_id` | Links to the program/section |
| `section_ids` | Array of section IDs enrolled in |
| `registration_date` | Date the registration was submitted |
| `registration_state` | Current lifecycle state (see below) |
| `approval` | Org approval status (see below) |
| `document` | Whether supporting docs are complete |
| `registrant` | Name of the person who registered |

---

## Registration State Values

| Value | Plain English | Meaning |
|-------|--------------|---------|
| `draft` | Not yet submitted | Registration started but not submitted by the user |
| `pending` | Awaiting action | Submitted; waiting for payment or org review |
| `completed` | Fully registered | Submitted, paid, and accepted by the organization |
| `expired` | Registration expired | Pending registration that passed its deadline without action |
| `canceled` | Canceled | Canceled from pending/expired state; not visible to org |
| `listed_canceled` | Canceled (visible) | Canceled after completion; remains visible to the organization |
| `correction_required` | Sent back for corrections | Returned to the registrant by the org for edits |

---

## Approval Values

| Value | Plain English | Meaning |
|-------|--------------|---------|
| `approved` | Approved | Reviewed and approved by the organization |
| `not_approved` | Rejected | Reviewed and rejected by the organization |
| `Pending` | Awaiting review | Not yet reviewed by the organization |

---

## Document Values

| Value | Meaning |
|-------|---------|
| `Complete` | All required documents have been submitted |
| `Incomplete` | Documents are missing or not yet uploaded |

---

## Payment State Values

| Value | Plain English | Meaning |
|-------|--------------|---------|
| `none` | No payment started | New registration; no payment initiated |
| `pending` | Payment in progress | Payment initialized but not confirmed |
| `partial` | Partially paid | Deposit or partial prepayment made; balance remains |
| `completed` | Fully paid | Payment fully received and confirmed |
| `partial_refunded` | Partially refunded | A portion of the payment has been refunded |
| `refunded` | Fully refunded | Full payment has been refunded |
| `void` | Paid offline | Marked as paid via a manual/offline payment method |
| `failed` | Payment failed | Payment attempt failed with an error from the payment system |
| `canceled` | Payment canceled | Payment was canceled by the user or an admin |

---

## Payment Method Values

| Value | Meaning |
|-------|---------|
| `Stripe` | Online credit/debit card via Stripe |
| `PayPal` | Standard PayPal checkout |
| `PayPal Marketplace` | PayPal split-payment flow |
| `Heartland` | Online card processing via Heartland |
| `MySchoolBucks` | School-focused payment platform |
| `CardPointe` | Card processing via CardPointe gateway |
| `Offline` | Check, cash, or money order — confirmed manually by the org |
| `null` / `nil` | No payment method recorded yet |

---

## Transfer Status Values

| Value | Plain English | Meaning |
|-------|--------------|---------|
| `transfer_not_applicable` | Not required | Transfer approval not required for this registration |
| `pending` | Awaiting action | Transfer request submitted, not yet reviewed |
| `in_review_receiving_school` | Under review (receiving school) | Being reviewed by the school the student is transferring to |
| `in_review_previous_school` | Under review (previous school) | Being reviewed by the school the student is transferring from |
| `completed_previous_school` | Previous school done | Previous school has completed their review |
| `approved` | Approved | Transfer fully approved |
| `rejected` | Rejected | Transfer has been rejected |
| `state_review_requested` | State review requested | A state-level authority review has been requested |
| `state_review_in_progress` | State review in progress | State authority is actively reviewing |
| `state_approved` | State approved | Transfer approved at the state level |
| `state_approved_for_sub_varsity` | Approved (sub-varsity only) | State approval for sub-varsity participation only |
| `state_rejected` | State rejected | Transfer rejected at the state level |
| `appeal_review_requested` | Appeal submitted | An appeal has been filed for further review |
| `appeal_review_in_progress` | Appeal in progress | Appeal is actively being reviewed |
| `appeal_approved` | Appeal approved | Appeal granted; transfer approved |
| `appeal_rejected` | Appeal denied | Appeal denied; transfer remains rejected |

---

## Section Capacity Notes

- `capacity` field stores the maximum number of participants per section.
- A `null` / `None` capacity means the section has **unlimited** capacity.
- `enrolled` = count of active registrations (completed + pending + correction_required) for the section.
- `available_spots` = capacity minus enrolled.
- **Near capacity** = enrolled > 75% of capacity.
- **At capacity** = enrolled >= capacity (no more registrations should be accepted).

---

## Table Relationships

```
participants (participant_id)
    └── registrations (participant_id FK)
            ├── payments (registration_id FK)
            ├── transfers (registration_id FK)
            └── programs_sections (program_id FK)
```

- One participant can have multiple registrations.
- Each registration has one payment record.
- Each registration may have one transfer record.
- Each registration links to one program, which contains one or more sections.
