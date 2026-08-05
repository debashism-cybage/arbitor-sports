"""
Uplight Zendesk MCP Server

This MCP server provides sample Zendesk ticket data that can be
consumed by AI agents for ticket summarization, incident analysis,
priority classification, and reporting.
"""

from typing import Any
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP(
    host="0.0.0.0",
    port=8091,
    stateless_http=True,
    streamable_http_path="/Uplight_zendesk"
)


@mcp.tool()
def get_zendesk_tickets() -> dict[str, Any]:
    """
    Retrieve sample Zendesk tickets.

    Returns:
        dict[str, Any]: Sample Zendesk ticket data.
    """

    return {
        "ticket_count": 10,
        "tickets": [
            {
                "ticket_id": 1001,
                "subject": "Application login page is slow",
                "description": "Users experience login times greater than 30 seconds after today's deployment.",
                "status": "Open",
                "priority": "High",
                "type": "Incident",
                "category": "Application Performance",
                "requester": "John Smith",
                "assignee": "Application Support Team",
                "created_at": "2026-06-28T09:15:00Z",
                "tags": ["login", "performance", "production"]
            },
            {
                "ticket_id": 1002,
                "subject": "High CPU utilization on production server",
                "description": "CPU utilization has exceeded 95%, causing application slowdown.",
                "status": "Open",
                "priority": "Critical",
                "type": "Incident",
                "category": "Infrastructure",
                "requester": "Emma Wilson",
                "assignee": "Infrastructure Team",
                "created_at": "2026-06-28T10:40:00Z",
                "tags": ["cpu", "server", "critical"]
            },
            {
                "ticket_id": 1003,
                "subject": "Database queries timing out",
                "description": "Database queries are exceeding timeout limits during business hours.",
                "status": "Pending",
                "priority": "High",
                "type": "Problem",
                "category": "Database",
                "requester": "Michael Brown",
                "assignee": "Database Team",
                "created_at": "2026-06-27T14:20:00Z",
                "tags": ["database", "timeout", "sql"]
            },
            {
                "ticket_id": 1004,
                "subject": "API response latency increased",
                "description": "REST APIs respond in 8 to 10 seconds after production deployment.",
                "status": "Open",
                "priority": "Critical",
                "type": "Incident",
                "category": "API Performance",
                "requester": "Sophia Davis",
                "assignee": "API Support Team",
                "created_at": "2026-06-29T08:10:00Z",
                "tags": ["api", "latency", "deployment"]
            },
            {
                "ticket_id": 1005,
                "subject": "Memory leak in payment service",
                "description": "Memory usage continuously increases, causing frequent service restarts.",
                "status": "In Progress",
                "priority": "Critical",
                "type": "Problem",
                "category": "Application",
                "requester": "Olivia Taylor",
                "assignee": "Platform Engineering",
                "created_at": "2026-06-26T11:30:00Z",
                "tags": ["memory", "restart", "payment"]
            },
            {
                "ticket_id": 1006,
                "subject": "Dashboard widgets loading slowly",
                "description": "Dashboard widgets require over 20 seconds to render after login.",
                "status": "Open",
                "priority": "Medium",
                "type": "Incident",
                "category": "Frontend",
                "requester": "David Johnson",
                "assignee": "UI Support Team",
                "created_at": "2026-06-29T07:50:00Z",
                "tags": ["dashboard", "frontend", "performance"]
            },
            {
                "ticket_id": 1007,
                "subject": "File uploads timing out",
                "description": "Users cannot upload files larger than 50 MB due to timeout.",
                "status": "Open",
                "priority": "High",
                "type": "Incident",
                "category": "Application",
                "requester": "Sarah Williams",
                "assignee": "Application Support Team",
                "created_at": "2026-06-25T15:45:00Z",
                "tags": ["upload", "timeout"]
            },
            {
                "ticket_id": 1008,
                "subject": "Background jobs delayed",
                "description": "Scheduled background jobs are delayed, affecting downstream processing.",
                "status": "Pending",
                "priority": "Medium",
                "type": "Task",
                "category": "Scheduler",
                "requester": "Daniel Lee",
                "assignee": "Batch Operations Team",
                "created_at": "2026-06-24T18:20:00Z",
                "tags": ["scheduler", "batch", "delay"]
            },
            {
                "ticket_id": 1009,
                "subject": "Application unavailable during load testing",
                "description": "Application becomes unresponsive after 500 concurrent users.",
                "status": "Open",
                "priority": "Critical",
                "type": "Problem",
                "category": "Scalability",
                "requester": "Performance Testing Team",
                "assignee": "Architecture Team",
                "created_at": "2026-06-23T13:10:00Z",
                "tags": ["load-test", "capacity", "performance"]
            },
            {
                "ticket_id": 1010,
                "subject": "Monthly billing reports are slow",
                "description": "Monthly billing reports require over 15 minutes to generate.",
                "status": "In Progress",
                "priority": "High",
                "type": "Service Request",
                "category": "Reporting",
                "requester": "Finance Operations",
                "assignee": "Reporting Team",
                "created_at": "2026-06-22T09:30:00Z",
                "tags": ["report", "billing", "performance"]
            },,
{
    "ticket_id": 78459,
    "subject": "PSEG NJ AMI Completeness Below Threshold",
    "description": "AMI data completeness for PSEG NJ has fallen below the acceptable threshold. Missing interval data has been detected for multiple smart meters. Investigation is required to identify the root cause, validate data ingestion, and restore data completeness.",
    "status": "Open",
    "priority": "High",
    "severity": "P2",
    "type": "Incident",
    "category": "AMI Data",
    "product": "AMI Platform",
    "customer": "PSEG NJ",
    "environment": "Production",
    "requester": "PSEG Operations",
    "assignee": "AMI Support Team",
    "created_at": "2026-07-03T07:37:00Z",
    "updated_at": "2026-07-03T08:05:00Z",
    "business_impact": "Meter data completeness below SLA causing inaccurate reporting.",
    "root_cause": "",
    "resolution": "",
    "tags": [
        "ami",
        "meter-data",
        "completeness",
        "production",
        "pseg"
    ]
},
{
    "ticket_id": 78499,
    "subject": "GEORGIA POWER - ORDER NOT RECEIVED - TAZANGI",
    "description": "Georgia Power reported that customer orders are not being received in the TAZANGI platform. Initial investigation suggests an issue with downstream order processing or integration. Support team needs to validate message flow and order synchronization.",
    "status": "Open",
    "priority": "High",
    "severity": "P2",
    "type": "Incident",
    "category": "Order Management",
    "product": "TAZANGI",
    "customer": "Georgia Power",
    "environment": "Production",
    "requester": "Georgia Power Operations",
    "assignee": "Order Management Team",
    "created_at": "2026-07-03T07:34:00Z",
    "updated_at": "2026-07-03T07:50:00Z",
    "business_impact": "Customer orders are not reaching downstream systems, affecting order fulfillment.",
    "root_cause": "",
    "resolution": "",
    "tags": [
        "order",
        "integration",
        "tazangi",
        "georgia-power",
        "production"
    ]
},
{
    "ticket_id": 78501,
    "subject": "Georgia Power - Refund Request (Mohan)",
    "description": "Customer requested a refund for an incorrectly processed transaction. Billing team must validate payment history, confirm refund eligibility, and complete the refund process.",
    "status": "Open",
    "priority": "Medium",
    "severity": "P3",
    "type": "Service Request",
    "category": "Billing",
    "product": "Customer Billing",
    "customer": "Georgia Power",
    "environment": "Production",
    "requester": "Mohan",
    "assignee": "Billing Support Team",
    "created_at": "2026-07-03T07:35:00Z",
    "updated_at": "2026-07-03T07:42:00Z",
    "business_impact": "Customer refund pending. Limited business impact.",
    "root_cause": "",
    "resolution": "",
    "tags": [
        "refund",
        "billing",
        "customer",
        "finance",
        "georgia-power"
    ]
}

        ]
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")