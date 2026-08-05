# -*- coding: utf-8 -*-
"""
Arbitor Sports MCP Server

This MCP server provides Arbitor Sports student registration data that can be
consumed by AI agents for registration insights, payment analysis,
capacity recommendations, and participant reporting.

Use Case: Registration Insights & Recommendations (Ask Arbiter AI)
"""

import json
import os
from typing import Any, Optional
from mcp.server.fastmcp import FastMCP

# -- Resolve paths relative to this file (deployment-safe) ------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "mock_data.json"), encoding="utf-8") as f:
    _DATA = json.load(f)

# -- Create MCP server -------------------------------------------------------
mcp = FastMCP(
    host="0.0.0.0",
    port=8092,
    stateless_http=True,
    streamable_http_path="/arbitor_sports"
)


# ===========================================================================
# REGISTRATIONS TOOLS
# ===========================================================================

@mcp.tool()
def get_all_registrations() -> dict[str, Any]:
    """
    Retrieve all student registration records.

    Returns:
        dict[str, Any]: All registration records with count.
    """
    registrations = _DATA["registrations"]
    return {
        "registration_count": len(registrations),
        "registrations": registrations
    }


@mcp.tool()
def get_registrations_by_state(state: str) -> dict[str, Any]:
    """
    Retrieve registrations filtered by registration_state.

    Valid states: draft, pending, expired, completed, canceled,
                  listed_canceled, correction_required, Active

    Args:
        state: The registration state to filter by.

    Returns:
        dict[str, Any]: Filtered registration records with count.
    """
    filtered = [
        r for r in _DATA["registrations"]
        if r.get("registration_state", "").lower() == state.lower()
    ]
    return {
        "state": state,
        "registration_count": len(filtered),
        "registrations": filtered
    }


@mcp.tool()
def get_registrations_by_approval(approval: str) -> dict[str, Any]:
    """
    Retrieve registrations filtered by approval status.

    Valid values: approved, not_approved, Pending

    Args:
        approval: The approval status to filter by.

    Returns:
        dict[str, Any]: Filtered registration records with count.
    """
    filtered = [
        r for r in _DATA["registrations"]
        if r.get("approval", "").lower() == approval.lower()
    ]
    return {
        "approval": approval,
        "registration_count": len(filtered),
        "registrations": filtered
    }


@mcp.tool()
def get_incomplete_document_registrations() -> dict[str, Any]:
    """
    Retrieve all registrations where document submission is Incomplete.

    Returns:
        dict[str, Any]: Registrations with incomplete documents.
    """
    filtered = [
        r for r in _DATA["registrations"]
        if r.get("document", "").lower() == "incomplete"
    ]
    return {
        "registration_count": len(filtered),
        "registrations": filtered
    }


# ===========================================================================
# PAYMENTS TOOLS
# ===========================================================================

@mcp.tool()
def get_all_payments() -> dict[str, Any]:
    """
    Retrieve all payment records.

    Returns:
        dict[str, Any]: All payment records with count.
    """
    payments = _DATA["payments"]
    return {
        "payment_count": len(payments),
        "payments": payments
    }


@mcp.tool()
def get_payments_by_state(payment_state: str) -> dict[str, Any]:
    """
    Retrieve payments filtered by payment_state.

    Valid states: none, void, pending, partial, partial_refunded,
                  refunded, completed, canceled, failed

    Args:
        payment_state: The payment state to filter by.

    Returns:
        dict[str, Any]: Filtered payment records with count.
    """
    filtered = [
        p for p in _DATA["payments"]
        if p.get("payment_state", "").lower() == payment_state.lower()
    ]
    return {
        "payment_state": payment_state,
        "payment_count": len(filtered),
        "payments": filtered
    }


@mcp.tool()
def get_outstanding_payments() -> dict[str, Any]:
    """
    Retrieve all payments with a balance greater than zero (money still owed).

    Returns:
        dict[str, Any]: Payments with outstanding balances and totals.
    """
    filtered = [
        p for p in _DATA["payments"]
        if p.get("balance", 0) > 0
    ]
    total_outstanding = sum(p.get("balance", 0) for p in filtered)
    return {
        "payment_count": len(filtered),
        "total_outstanding_balance": round(total_outstanding, 2),
        "payments": filtered
    }


@mcp.tool()
def get_payment_by_registration(registration_id: str) -> dict[str, Any]:
    """
    Retrieve the payment record for a specific registration.

    Args:
        registration_id: The registration ID (e.g. REG-10045).

    Returns:
        dict[str, Any]: Payment record for the registration, or empty if not found.
    """
    match = [
        p for p in _DATA["payments"]
        if p.get("registration_id") == registration_id
    ]
    return {
        "registration_id": registration_id,
        "payment_count": len(match),
        "payments": match
    }


# ===========================================================================
# PROGRAMS & SECTIONS TOOLS
# ===========================================================================

@mcp.tool()
def get_programs_and_sections() -> dict[str, Any]:
    """
    Retrieve all programs and their associated sections with capacity information.

    Returns:
        dict[str, Any]: All program and section records.
    """
    programs = _DATA["programs_sections"]
    return {
        "program_count": len(programs),
        "programs": programs
    }


@mcp.tool()
def get_capacity_insights() -> dict[str, Any]:
    """
    Get capacity insights for all sections -- identifies sections near capacity,
    at capacity, or with unlimited capacity (null).

    Returns:
        dict[str, Any]: Sections categorized by capacity status with enrollment counts.
    """
    programs = _DATA["programs_sections"]
    registrations = _DATA["registrations"]

    # Count active registrations per section
    section_enrollment: dict[str, int] = {}
    for reg in registrations:
        if reg.get("registration_state") in ("completed", "pending", "Active", "correction_required"):
            for sec_id in reg.get("section_ids", []):
                section_enrollment[sec_id] = section_enrollment.get(sec_id, 0) + 1

    unlimited = []
    near_capacity = []    # >75% full
    at_capacity = []      # 100% full
    available = []        # <75% full

    for prog in programs:
        cap = prog.get("capacity")
        for i, sec_id in enumerate(prog.get("section_ids", [])):
            enrolled = section_enrollment.get(sec_id, 0)
            section_names = prog.get("section_names", [])
            section_name = section_names[i] if i < len(section_names) else sec_id
            entry = {
                "program_id": prog["program_id"],
                "section_id": sec_id,
                "section_name": section_name,
                "capacity": cap,
                "enrolled": enrolled,
                "available_spots": None if cap is None else cap - enrolled
            }
            if cap is None:
                unlimited.append(entry)
            elif enrolled >= cap:
                at_capacity.append(entry)
            elif cap > 0 and enrolled / cap > 0.75:
                near_capacity.append(entry)
            else:
                available.append(entry)

    return {
        "summary": {
            "total_sections": len(unlimited) + len(near_capacity) + len(at_capacity) + len(available),
            "at_capacity": len(at_capacity),
            "near_capacity": len(near_capacity),
            "available": len(available),
            "unlimited_capacity": len(unlimited)
        },
        "at_capacity_sections": at_capacity,
        "near_capacity_sections": near_capacity,
        "available_sections": available,
        "unlimited_capacity_sections": unlimited
    }


# ===========================================================================
# PARTICIPANTS TOOLS
# ===========================================================================

@mcp.tool()
def get_all_participants() -> dict[str, Any]:
    """
    Retrieve all participant/demographics records.

    Returns:
        dict[str, Any]: All participant records with count.
    """
    participants = _DATA["participants"]
    return {
        "participant_count": len(participants),
        "participants": participants
    }


@mcp.tool()
def get_participants_by_school(school_name: str) -> dict[str, Any]:
    """
    Retrieve participants from a specific school.

    Args:
        school_name: Full or partial school name to search for.

    Returns:
        dict[str, Any]: Matching participant records with count.
    """
    filtered = [
        p for p in _DATA["participants"]
        if school_name.lower() in p.get("school_name", "").lower()
    ]
    return {
        "school_name": school_name,
        "participant_count": len(filtered),
        "participants": filtered
    }


@mcp.tool()
def get_participant_demographics_summary() -> dict[str, Any]:
    """
    Get a demographic summary of all participants -- age range, gender distribution,
    grade distribution, and school distribution.

    Returns:
        dict[str, Any]: Aggregated demographic statistics.
    """
    participants = _DATA["participants"]

    gender_dist: dict[str, int] = {}
    grade_dist: dict[str, int] = {}
    school_dist: dict[str, int] = {}
    ages = []

    for p in participants:
        g = p.get("gender", "Unknown")
        gender_dist[g] = gender_dist.get(g, 0) + 1

        gr = p.get("grade", "Unknown")
        grade_dist[gr] = grade_dist.get(gr, 0) + 1

        sc = p.get("school_name", "Unknown")
        school_dist[sc] = school_dist.get(sc, 0) + 1

        age = p.get("participant_age")
        if age is not None:
            ages.append(age)

    return {
        "total_participants": len(participants),
        "age_range": {
            "min": min(ages),
            "max": max(ages),
            "avg": round(sum(ages) / len(ages), 1)
        } if ages else {},
        "gender_distribution": gender_dist,
        "grade_distribution": grade_dist,
        "school_distribution": school_dist
    }


# ===========================================================================
# TRANSFERS TOOLS
# ===========================================================================

@mcp.tool()
def get_all_transfers() -> dict[str, Any]:
    """
    Retrieve all transfer records.

    Returns:
        dict[str, Any]: All transfer records with count.
    """
    transfers = _DATA["transfers"]
    return {
        "transfer_count": len(transfers),
        "transfers": transfers
    }


@mcp.tool()
def get_transfers_by_status(transfer_status: str) -> dict[str, Any]:
    """
    Retrieve transfers filtered by transfer_status.

    Valid statuses: pending, approved, rejected, in_review_receiving_school,
    in_review_previous_school, completed_previous_school, state_review_requested,
    appeal_review_requested, state_review_in_progress, state_approved,
    state_approved_for_sub_varsity, state_rejected, appeal_review_in_progress,
    appeal_approved, appeal_rejected, transfer_not_applicable

    Args:
        transfer_status: The transfer status to filter by.

    Returns:
        dict[str, Any]: Filtered transfer records with count.
    """
    filtered = [
        t for t in _DATA["transfers"]
        if t.get("transfer_status", "").lower() == transfer_status.lower()
    ]
    return {
        "transfer_status": transfer_status,
        "transfer_count": len(filtered),
        "transfers": filtered
    }


@mcp.tool()
def get_transfers_summary() -> dict[str, Any]:
    """
    Get a summary of all transfers grouped by status and reason.

    Returns:
        dict[str, Any]: Aggregated transfer statistics.
    """
    transfers = _DATA["transfers"]

    status_dist: dict[str, int] = {}
    reason_dist: dict[str, int] = {}

    for t in transfers:
        st = t.get("transfer_status", "unknown")
        status_dist[st] = status_dist.get(st, 0) + 1

        re = t.get("reason", "unknown")
        reason_dist[re] = reason_dist.get(re, 0) + 1

    return {
        "total_transfers": len(transfers),
        "status_distribution": status_dist,
        "reason_distribution": reason_dist
    }


# ===========================================================================
# CROSS-DATASET / ANALYTICS TOOLS
# ===========================================================================

@mcp.tool()
def get_registration_summary() -> dict[str, Any]:
    """
    Get an aggregated summary of all registrations -- counts by state,
    approval status, document completeness, and payment state.

    Returns:
        dict[str, Any]: Full registration analytics summary.
    """
    registrations = _DATA["registrations"]
    payments = _DATA["payments"]

    state_dist: dict[str, int] = {}
    approval_dist: dict[str, int] = {}
    doc_dist: dict[str, int] = {}

    for r in registrations:
        st = r.get("registration_state", "unknown")
        state_dist[st] = state_dist.get(st, 0) + 1

        ap = r.get("approval", "unknown")
        approval_dist[ap] = approval_dist.get(ap, 0) + 1

        doc = r.get("document", "unknown")
        doc_dist[doc] = doc_dist.get(doc, 0) + 1

    payment_state_dist: dict[str, int] = {}
    total_collected = 0.0
    total_outstanding = 0.0

    for p in payments:
        ps = p.get("payment_state", "unknown")
        payment_state_dist[ps] = payment_state_dist.get(ps, 0) + 1
        total_collected += p.get("amount_paid", 0)
        total_outstanding += p.get("balance", 0)

    return {
        "total_registrations": len(registrations),
        "registration_state_distribution": state_dist,
        "approval_distribution": approval_dist,
        "document_completeness": doc_dist,
        "payment_summary": {
            "total_payments": len(payments),
            "payment_state_distribution": payment_state_dist,
            "total_amount_collected": round(total_collected, 2),
            "total_outstanding_balance": round(total_outstanding, 2)
        }
    }


@mcp.tool()
def search_registrations(query: str) -> dict[str, Any]:
    """
    Search registrations by registrant name, school name, or program ID.
    Performs a case-insensitive keyword search across linked datasets.

    Args:
        query: Search keyword (e.g. participant name, school, program).

    Returns:
        dict[str, Any]: Matching registrations with linked participant and payment info.
    """
    query_lower = query.lower()
    registrations = _DATA["registrations"]
    participants = {p["participant_id"]: p for p in _DATA["participants"]}
    payments = {p["registration_id"]: p for p in _DATA["payments"]}

    results = []
    for reg in registrations:
        participant = participants.get(reg.get("participant_id", ""), {})
        school = participant.get("school_name", "").lower()
        registrant = reg.get("registrant", "").lower()
        program_id = reg.get("program_id", "").lower()

        if (query_lower in registrant or
                query_lower in school or
                query_lower in program_id):
            payment = payments.get(reg["registration_id"], {})
            results.append({
                "registration": reg,
                "participant": participant,
                "payment": payment
            })

    return {
        "query": query,
        "result_count": len(results),
        "results": results
    }


@mcp.tool()
def get_full_registration_detail(registration_id: str) -> dict[str, Any]:
    """
    Retrieve the complete record for a single registration, including
    linked participant info, payment, and transfer (if any).

    Args:
        registration_id: The registration ID (e.g. REG-10045).

    Returns:
        dict[str, Any]: Full registration detail with all linked data.
    """
    registrations = {r["registration_id"]: r for r in _DATA["registrations"]}
    participants = {p["participant_id"]: p for p in _DATA["participants"]}
    payments = {p["registration_id"]: p for p in _DATA["payments"]}
    transfers = {t["registration_id"]: t for t in _DATA["transfers"]}

    reg = registrations.get(registration_id)
    if not reg:
        return {"error": f"Registration '{registration_id}' not found."}

    participant = participants.get(reg.get("participant_id", ""), {})
    payment = payments.get(registration_id, {})
    transfer = transfers.get(registration_id, None)

    return {
        "registration_id": registration_id,
        "registration": reg,
        "participant": participant,
        "payment": payment,
        "transfer": transfer
    }


# ===========================================================================
# ENTRY POINT
# ===========================================================================

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
