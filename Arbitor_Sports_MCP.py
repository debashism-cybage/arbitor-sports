# -*- coding: utf-8 -*-
"""
Arbitor Sports MCP Server

This MCP server provides Arbitor Sports student registration data that can be
consumed by AI agents for registration insights, payment analysis,
capacity recommendations, and participant reporting.

Use Case: Registration Insights & Recommendations (Ask Arbiter AI)
"""

from typing import Any
from mcp.server.fastmcp import FastMCP

# -- Create MCP server -------------------------------------------------------
mcp = FastMCP(
    host="0.0.0.0",
    port=8092,
    stateless_http=True,
    streamable_http_path="/arbitor_sports"
)

# -- Inline mock data (30 rows per dataset) ----------------------------------
_REGISTRATIONS = [
    { "registration_id": "REG-10045", "participant_id": "P-2045", "program_id": "PRG-101", "section_ids": ["SEC-101-SAT-AM"], "registration_date": "2026-07-20", "registration_state": "Active", "approval": "Pending", "document": "Incomplete", "registrant": "Alex Johnson" },
    { "registration_id": "REG-10046", "participant_id": "P-2046", "program_id": "PRG-102", "section_ids": ["SEC-102-MON-PM"], "registration_date": "2026-07-18", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Maria Garcia" },
    { "registration_id": "REG-10047", "participant_id": "P-2047", "program_id": "PRG-101", "section_ids": ["SEC-101-SAT-AM"], "registration_date": "2026-07-15", "registration_state": "pending", "approval": "Pending", "document": "Incomplete", "registrant": "James Wilson" },
    { "registration_id": "REG-10048", "participant_id": "P-2048", "program_id": "PRG-103", "section_ids": ["SEC-103-WED-AM"], "registration_date": "2026-07-10", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Emily Davis" },
    { "registration_id": "REG-10049", "participant_id": "P-2049", "program_id": "PRG-104", "section_ids": ["SEC-104-FRI-PM"], "registration_date": "2026-07-08", "registration_state": "draft", "approval": "Pending", "document": "Incomplete", "registrant": "Noah Martinez" },
    { "registration_id": "REG-10050", "participant_id": "P-2050", "program_id": "PRG-102", "section_ids": ["SEC-102-MON-PM"], "registration_date": "2026-07-05", "registration_state": "canceled", "approval": "not_approved", "document": "Complete", "registrant": "Olivia Anderson" },
    { "registration_id": "REG-10051", "participant_id": "P-2051", "program_id": "PRG-105", "section_ids": ["SEC-105-TUE-AM"], "registration_date": "2026-07-03", "registration_state": "correction_required", "approval": "Pending", "document": "Incomplete", "registrant": "Liam Thomas" },
    { "registration_id": "REG-10052", "participant_id": "P-2052", "program_id": "PRG-101", "section_ids": ["SEC-101-SAT-AM"], "registration_date": "2026-07-01", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Sophia Jackson" },
    { "registration_id": "REG-10053", "participant_id": "P-2053", "program_id": "PRG-103", "section_ids": ["SEC-103-WED-AM"], "registration_date": "2026-06-28", "registration_state": "expired", "approval": "Pending", "document": "Incomplete", "registrant": "Mason White" },
    { "registration_id": "REG-10054", "participant_id": "P-2054", "program_id": "PRG-104", "section_ids": ["SEC-104-FRI-PM"], "registration_date": "2026-06-25", "registration_state": "listed_canceled", "approval": "approved", "document": "Complete", "registrant": "Ava Harris" },
    { "registration_id": "REG-10055", "participant_id": "P-2055", "program_id": "PRG-106", "section_ids": ["SEC-106-SAT-PM"], "registration_date": "2026-06-22", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Ethan Clark" },
    { "registration_id": "REG-10056", "participant_id": "P-2056", "program_id": "PRG-105", "section_ids": ["SEC-105-TUE-AM"], "registration_date": "2026-06-20", "registration_state": "pending", "approval": "Pending", "document": "Incomplete", "registrant": "Isabella Lewis" },
    { "registration_id": "REG-10057", "participant_id": "P-2057", "program_id": "PRG-102", "section_ids": ["SEC-102-MON-PM"], "registration_date": "2026-06-18", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Aiden Robinson" },
    { "registration_id": "REG-10058", "participant_id": "P-2058", "program_id": "PRG-101", "section_ids": ["SEC-101-SAT-AM"], "registration_date": "2026-06-15", "registration_state": "draft", "approval": "Pending", "document": "Incomplete", "registrant": "Mia Walker" },
    { "registration_id": "REG-10059", "participant_id": "P-2059", "program_id": "PRG-106", "section_ids": ["SEC-106-SAT-PM"], "registration_date": "2026-06-12", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Lucas Hall" },
    { "registration_id": "REG-10060", "participant_id": "P-2060", "program_id": "PRG-103", "section_ids": ["SEC-103-WED-AM"], "registration_date": "2026-06-10", "registration_state": "pending", "approval": "Pending", "document": "Incomplete", "registrant": "Charlotte Allen" },
    { "registration_id": "REG-10061", "participant_id": "P-2061", "program_id": "PRG-104", "section_ids": ["SEC-104-FRI-PM"], "registration_date": "2026-06-08", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Henry Young" },
    { "registration_id": "REG-10062", "participant_id": "P-2062", "program_id": "PRG-105", "section_ids": ["SEC-105-TUE-AM"], "registration_date": "2026-06-05", "registration_state": "correction_required", "approval": "not_approved", "document": "Incomplete", "registrant": "Amelia Hernandez" },
    { "registration_id": "REG-10063", "participant_id": "P-2063", "program_id": "PRG-101", "section_ids": ["SEC-101-SAT-AM"], "registration_date": "2026-06-03", "registration_state": "expired", "approval": "Pending", "document": "Incomplete", "registrant": "Benjamin King" },
    { "registration_id": "REG-10064", "participant_id": "P-2064", "program_id": "PRG-102", "section_ids": ["SEC-102-MON-PM"], "registration_date": "2026-06-01", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Evelyn Wright" },
    { "registration_id": "REG-10065", "participant_id": "P-2065", "program_id": "PRG-106", "section_ids": ["SEC-106-SAT-PM"], "registration_date": "2026-05-28", "registration_state": "pending", "approval": "Pending", "document": "Incomplete", "registrant": "Alexander Scott" },
    { "registration_id": "REG-10066", "participant_id": "P-2066", "program_id": "PRG-103", "section_ids": ["SEC-103-WED-AM"], "registration_date": "2026-05-25", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Abigail Torres" },
    { "registration_id": "REG-10067", "participant_id": "P-2067", "program_id": "PRG-104", "section_ids": ["SEC-104-FRI-PM"], "registration_date": "2026-05-22", "registration_state": "listed_canceled", "approval": "approved", "document": "Complete", "registrant": "Michael Nguyen" },
    { "registration_id": "REG-10068", "participant_id": "P-2068", "program_id": "PRG-105", "section_ids": ["SEC-105-TUE-AM"], "registration_date": "2026-05-20", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Ella Hill" },
    { "registration_id": "REG-10069", "participant_id": "P-2069", "program_id": "PRG-101", "section_ids": ["SEC-101-SAT-AM"], "registration_date": "2026-05-18", "registration_state": "draft", "approval": "Pending", "document": "Incomplete", "registrant": "Daniel Flores" },
    { "registration_id": "REG-10070", "participant_id": "P-2070", "program_id": "PRG-102", "section_ids": ["SEC-102-MON-PM"], "registration_date": "2026-05-15", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Madison Green" },
    { "registration_id": "REG-10071", "participant_id": "P-2071", "program_id": "PRG-106", "section_ids": ["SEC-106-SAT-PM"], "registration_date": "2026-05-12", "registration_state": "pending", "approval": "Pending", "document": "Incomplete", "registrant": "Jackson Adams" },
    { "registration_id": "REG-10072", "participant_id": "P-2072", "program_id": "PRG-103", "section_ids": ["SEC-103-WED-AM"], "registration_date": "2026-05-10", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Scarlett Baker" },
    { "registration_id": "REG-10073", "participant_id": "P-2073", "program_id": "PRG-104", "section_ids": ["SEC-104-FRI-PM"], "registration_date": "2026-05-08", "registration_state": "canceled", "approval": "not_approved", "document": "Incomplete", "registrant": "Sebastian Gonzalez" },
    { "registration_id": "REG-10074", "participant_id": "P-2074", "program_id": "PRG-105", "section_ids": ["SEC-105-TUE-AM"], "registration_date": "2026-05-05", "registration_state": "completed", "approval": "approved", "document": "Complete", "registrant": "Grace Nelson" },
]

_PAYMENTS = [
    { "payment_id": "PAY-78021", "registration_id": "REG-10045", "payment_state": "partial",          "amount_paid": 100.00, "balance": 150.00, "total": 250.00, "payment_method": "Online" },
    { "payment_id": "PAY-78022", "registration_id": "REG-10046", "payment_state": "completed",        "amount_paid": 300.00, "balance":   0.00, "total": 300.00, "payment_method": "Stripe" },
    { "payment_id": "PAY-78023", "registration_id": "REG-10047", "payment_state": "pending",          "amount_paid":   0.00, "balance": 250.00, "total": 250.00, "payment_method": "Online" },
    { "payment_id": "PAY-78024", "registration_id": "REG-10048", "payment_state": "completed",        "amount_paid": 200.00, "balance":   0.00, "total": 200.00, "payment_method": "PayPal" },
    { "payment_id": "PAY-78025", "registration_id": "REG-10049", "payment_state": "none",             "amount_paid":   0.00, "balance": 175.00, "total": 175.00, "payment_method": None },
    { "payment_id": "PAY-78026", "registration_id": "REG-10050", "payment_state": "refunded",         "amount_paid": 150.00, "balance":   0.00, "total": 150.00, "payment_method": "Stripe" },
    { "payment_id": "PAY-78027", "registration_id": "REG-10051", "payment_state": "partial",          "amount_paid":  75.00, "balance": 125.00, "total": 200.00, "payment_method": "MySchoolBucks" },
    { "payment_id": "PAY-78028", "registration_id": "REG-10052", "payment_state": "completed",        "amount_paid": 250.00, "balance":   0.00, "total": 250.00, "payment_method": "Online" },
    { "payment_id": "PAY-78029", "registration_id": "REG-10053", "payment_state": "none",             "amount_paid":   0.00, "balance": 300.00, "total": 300.00, "payment_method": None },
    { "payment_id": "PAY-78030", "registration_id": "REG-10054", "payment_state": "partial_refunded", "amount_paid": 100.00, "balance":   0.00, "total": 200.00, "payment_method": "Heartland" },
    { "payment_id": "PAY-78031", "registration_id": "REG-10055", "payment_state": "completed",        "amount_paid": 350.00, "balance":   0.00, "total": 350.00, "payment_method": "Stripe" },
    { "payment_id": "PAY-78032", "registration_id": "REG-10056", "payment_state": "pending",          "amount_paid":   0.00, "balance": 200.00, "total": 200.00, "payment_method": "Online" },
    { "payment_id": "PAY-78033", "registration_id": "REG-10057", "payment_state": "completed",        "amount_paid": 275.00, "balance":   0.00, "total": 275.00, "payment_method": "PayPal" },
    { "payment_id": "PAY-78034", "registration_id": "REG-10058", "payment_state": "none",             "amount_paid":   0.00, "balance": 250.00, "total": 250.00, "payment_method": None },
    { "payment_id": "PAY-78035", "registration_id": "REG-10059", "payment_state": "completed",        "amount_paid": 400.00, "balance":   0.00, "total": 400.00, "payment_method": "Stripe" },
    { "payment_id": "PAY-78036", "registration_id": "REG-10060", "payment_state": "partial",          "amount_paid":  80.00, "balance": 170.00, "total": 250.00, "payment_method": "Offline" },
    { "payment_id": "PAY-78037", "registration_id": "REG-10061", "payment_state": "completed",        "amount_paid": 300.00, "balance":   0.00, "total": 300.00, "payment_method": "CardPointe" },
    { "payment_id": "PAY-78038", "registration_id": "REG-10062", "payment_state": "failed",           "amount_paid":   0.00, "balance": 200.00, "total": 200.00, "payment_method": "Stripe" },
    { "payment_id": "PAY-78039", "registration_id": "REG-10063", "payment_state": "none",             "amount_paid":   0.00, "balance": 300.00, "total": 300.00, "payment_method": None },
    { "payment_id": "PAY-78040", "registration_id": "REG-10064", "payment_state": "completed",        "amount_paid": 225.00, "balance":   0.00, "total": 225.00, "payment_method": "PayPal" },
    { "payment_id": "PAY-78041", "registration_id": "REG-10065", "payment_state": "pending",          "amount_paid":   0.00, "balance": 175.00, "total": 175.00, "payment_method": None },
    { "payment_id": "PAY-78042", "registration_id": "REG-10066", "payment_state": "completed",        "amount_paid": 350.00, "balance":   0.00, "total": 350.00, "payment_method": "Online" },
    { "payment_id": "PAY-78043", "registration_id": "REG-10067", "payment_state": "void",             "amount_paid": 275.00, "balance":   0.00, "total": 275.00, "payment_method": "Offline" },
    { "payment_id": "PAY-78044", "registration_id": "REG-10068", "payment_state": "completed",        "amount_paid": 320.00, "balance":   0.00, "total": 320.00, "payment_method": "MySchoolBucks" },
    { "payment_id": "PAY-78045", "registration_id": "REG-10069", "payment_state": "none",             "amount_paid":   0.00, "balance": 250.00, "total": 250.00, "payment_method": None },
    { "payment_id": "PAY-78046", "registration_id": "REG-10070", "payment_state": "completed",        "amount_paid": 300.00, "balance":   0.00, "total": 300.00, "payment_method": "Stripe" },
    { "payment_id": "PAY-78047", "registration_id": "REG-10071", "payment_state": "partial",          "amount_paid": 100.00, "balance": 150.00, "total": 250.00, "payment_method": "Online" },
    { "payment_id": "PAY-78048", "registration_id": "REG-10072", "payment_state": "completed",        "amount_paid": 400.00, "balance":   0.00, "total": 400.00, "payment_method": "PayPal" },
    { "payment_id": "PAY-78049", "registration_id": "REG-10073", "payment_state": "canceled",         "amount_paid":   0.00, "balance": 200.00, "total": 200.00, "payment_method": None },
    { "payment_id": "PAY-78050", "registration_id": "REG-10074", "payment_state": "completed",        "amount_paid": 280.00, "balance":   0.00, "total": 280.00, "payment_method": "Heartland" },
]

_PROGRAMS_SECTIONS = [
    { "program_id": "PRG-101", "section_ids": ["SEC-101-SAT-AM"], "section_full_ids": [], "section_names": ["Robotics - Saturday Morning"],      "capacity": 30 },
    { "program_id": "PRG-102", "section_ids": ["SEC-102-MON-PM"], "section_full_ids": [], "section_names": ["Swimming - Monday Afternoon"],       "capacity": 25 },
    { "program_id": "PRG-103", "section_ids": ["SEC-103-WED-AM"], "section_full_ids": [], "section_names": ["Basketball - Wednesday Morning"],    "capacity": 20 },
    { "program_id": "PRG-104", "section_ids": ["SEC-104-FRI-PM"], "section_full_ids": [], "section_names": ["Soccer - Friday Afternoon"],         "capacity": 22 },
    { "program_id": "PRG-105", "section_ids": ["SEC-105-TUE-AM"], "section_full_ids": [], "section_names": ["Tennis - Tuesday Morning"],          "capacity": 18 },
    { "program_id": "PRG-106", "section_ids": ["SEC-106-SAT-PM"], "section_full_ids": [], "section_names": ["Gymnastics - Saturday Afternoon"],   "capacity": 15 },
    { "program_id": "PRG-107", "section_ids": ["SEC-107-THU-AM"], "section_full_ids": [], "section_names": ["Track & Field - Thursday Morning"],  "capacity": 35 },
    { "program_id": "PRG-108", "section_ids": ["SEC-108-MON-AM"], "section_full_ids": [], "section_names": ["Volleyball - Monday Morning"],       "capacity": 20 },
    { "program_id": "PRG-109", "section_ids": ["SEC-109-WED-PM"], "section_full_ids": [], "section_names": ["Chess Club - Wednesday Afternoon"],  "capacity": 40 },
    { "program_id": "PRG-110", "section_ids": ["SEC-110-FRI-AM"], "section_full_ids": [], "section_names": ["Martial Arts - Friday Morning"],     "capacity": 16 },
    { "program_id": "PRG-111", "section_ids": ["SEC-111-SAT-AM", "SEC-111-SAT-PM"], "section_full_ids": [], "section_names": ["Swimming - Saturday Morning", "Swimming - Saturday Afternoon"], "capacity": 25 },
    { "program_id": "PRG-112", "section_ids": ["SEC-112-TUE-PM"], "section_full_ids": [], "section_names": ["Coding Camp - Tuesday Afternoon"],   "capacity": 30 },
    { "program_id": "PRG-113", "section_ids": ["SEC-113-WED-AM"], "section_full_ids": [], "section_names": ["Baseball - Wednesday Morning"],      "capacity": 18 },
    { "program_id": "PRG-114", "section_ids": ["SEC-114-THU-PM"], "section_full_ids": [], "section_names": ["Football - Thursday Afternoon"],     "capacity": 22 },
    { "program_id": "PRG-115", "section_ids": ["SEC-115-FRI-PM"], "section_full_ids": [], "section_names": ["Debate Club - Friday Afternoon"],    "capacity": None },
    { "program_id": "PRG-116", "section_ids": ["SEC-116-SAT-AM"], "section_full_ids": [], "section_names": ["Art & Craft - Saturday Morning"],    "capacity": 20 },
    { "program_id": "PRG-117", "section_ids": ["SEC-117-MON-PM"], "section_full_ids": [], "section_names": ["Drama - Monday Afternoon"],          "capacity": 25 },
    { "program_id": "PRG-118", "section_ids": ["SEC-118-TUE-AM"], "section_full_ids": [], "section_names": ["Lacrosse - Tuesday Morning"],        "capacity": 18 },
    { "program_id": "PRG-119", "section_ids": ["SEC-119-WED-PM"], "section_full_ids": [], "section_names": ["Hockey - Wednesday Afternoon"],      "capacity": 20 },
    { "program_id": "PRG-120", "section_ids": ["SEC-120-THU-AM"], "section_full_ids": [], "section_names": ["Dance - Thursday Morning"],          "capacity": 30 },
    { "program_id": "PRG-121", "section_ids": ["SEC-121-FRI-AM"], "section_full_ids": [], "section_names": ["Cross Country - Friday Morning"],    "capacity": 40 },
    { "program_id": "PRG-122", "section_ids": ["SEC-122-SAT-PM"], "section_full_ids": [], "section_names": ["Music Band - Saturday Afternoon"],   "capacity": 25 },
    { "program_id": "PRG-123", "section_ids": ["SEC-123-MON-AM"], "section_full_ids": [], "section_names": ["Softball - Monday Morning"],         "capacity": 20 },
    { "program_id": "PRG-124", "section_ids": ["SEC-124-TUE-PM"], "section_full_ids": [], "section_names": ["Archery - Tuesday Afternoon"],       "capacity": 15 },
    { "program_id": "PRG-125", "section_ids": ["SEC-125-WED-AM"], "section_full_ids": [], "section_names": ["Wrestling - Wednesday Morning"],     "capacity": 16 },
    { "program_id": "PRG-126", "section_ids": ["SEC-126-THU-PM"], "section_full_ids": [], "section_names": ["Badminton - Thursday Afternoon"],    "capacity": 20 },
    { "program_id": "PRG-127", "section_ids": ["SEC-127-FRI-AM"], "section_full_ids": [], "section_names": ["Golf - Friday Morning"],             "capacity": 12 },
    { "program_id": "PRG-128", "section_ids": ["SEC-128-SAT-AM"], "section_full_ids": [], "section_names": ["Cycling - Saturday Morning"],        "capacity": 20 },
    { "program_id": "PRG-129", "section_ids": ["SEC-129-MON-PM"], "section_full_ids": [], "section_names": ["Rowing - Monday Afternoon"],         "capacity": 14 },
    { "program_id": "PRG-130", "section_ids": ["SEC-130-TUE-AM"], "section_full_ids": [], "section_names": ["Fencing - Tuesday Morning"],         "capacity": 10 },
]

_PARTICIPANTS = [
    { "participant_id": "P-2045", "registrant": "Alex Johnson",       "participant_age": 11, "gender": "Female", "grade": "6",  "school_name": "Lincoln Elementary" },
    { "participant_id": "P-2046", "registrant": "Maria Garcia",       "participant_age": 13, "gender": "Female", "grade": "8",  "school_name": "Jefferson Middle School" },
    { "participant_id": "P-2047", "registrant": "James Wilson",       "participant_age": 10, "gender": "Male",   "grade": "5",  "school_name": "Washington Elementary" },
    { "participant_id": "P-2048", "registrant": "Emily Davis",        "participant_age": 14, "gender": "Female", "grade": "9",  "school_name": "Roosevelt High School" },
    { "participant_id": "P-2049", "registrant": "Noah Martinez",      "participant_age": 12, "gender": "Male",   "grade": "7",  "school_name": "Madison Middle School" },
    { "participant_id": "P-2050", "registrant": "Olivia Anderson",    "participant_age": 15, "gender": "Female", "grade": "10", "school_name": "Adams High School" },
    { "participant_id": "P-2051", "registrant": "Liam Thomas",        "participant_age": 11, "gender": "Male",   "grade": "6",  "school_name": "Lincoln Elementary" },
    { "participant_id": "P-2052", "registrant": "Sophia Jackson",     "participant_age": 13, "gender": "Female", "grade": "8",  "school_name": "Jefferson Middle School" },
    { "participant_id": "P-2053", "registrant": "Mason White",        "participant_age":  9, "gender": "Male",   "grade": "4",  "school_name": "Franklin Elementary" },
    { "participant_id": "P-2054", "registrant": "Ava Harris",         "participant_age": 16, "gender": "Female", "grade": "11", "school_name": "Wilson High School" },
    { "participant_id": "P-2055", "registrant": "Ethan Clark",        "participant_age": 14, "gender": "Male",   "grade": "9",  "school_name": "Roosevelt High School" },
    { "participant_id": "P-2056", "registrant": "Isabella Lewis",     "participant_age": 12, "gender": "Female", "grade": "7",  "school_name": "Madison Middle School" },
    { "participant_id": "P-2057", "registrant": "Aiden Robinson",     "participant_age": 10, "gender": "Male",   "grade": "5",  "school_name": "Washington Elementary" },
    { "participant_id": "P-2058", "registrant": "Mia Walker",         "participant_age": 11, "gender": "Female", "grade": "6",  "school_name": "Lincoln Elementary" },
    { "participant_id": "P-2059", "registrant": "Lucas Hall",         "participant_age": 15, "gender": "Male",   "grade": "10", "school_name": "Adams High School" },
    { "participant_id": "P-2060", "registrant": "Charlotte Allen",    "participant_age": 13, "gender": "Female", "grade": "8",  "school_name": "Jefferson Middle School" },
    { "participant_id": "P-2061", "registrant": "Henry Young",        "participant_age": 17, "gender": "Male",   "grade": "12", "school_name": "Wilson High School" },
    { "participant_id": "P-2062", "registrant": "Amelia Hernandez",   "participant_age": 12, "gender": "Female", "grade": "7",  "school_name": "Madison Middle School" },
    { "participant_id": "P-2063", "registrant": "Benjamin King",      "participant_age": 10, "gender": "Male",   "grade": "5",  "school_name": "Franklin Elementary" },
    { "participant_id": "P-2064", "registrant": "Evelyn Wright",      "participant_age": 14, "gender": "Female", "grade": "9",  "school_name": "Roosevelt High School" },
    { "participant_id": "P-2065", "registrant": "Alexander Scott",    "participant_age": 11, "gender": "Male",   "grade": "6",  "school_name": "Lincoln Elementary" },
    { "participant_id": "P-2066", "registrant": "Abigail Torres",     "participant_age": 13, "gender": "Female", "grade": "8",  "school_name": "Jefferson Middle School" },
    { "participant_id": "P-2067", "registrant": "Michael Nguyen",     "participant_age": 16, "gender": "Male",   "grade": "11", "school_name": "Adams High School" },
    { "participant_id": "P-2068", "registrant": "Ella Hill",          "participant_age":  9, "gender": "Female", "grade": "4",  "school_name": "Franklin Elementary" },
    { "participant_id": "P-2069", "registrant": "Daniel Flores",      "participant_age": 12, "gender": "Male",   "grade": "7",  "school_name": "Madison Middle School" },
    { "participant_id": "P-2070", "registrant": "Madison Green",      "participant_age": 15, "gender": "Female", "grade": "10", "school_name": "Wilson High School" },
    { "participant_id": "P-2071", "registrant": "Jackson Adams",      "participant_age": 10, "gender": "Male",   "grade": "5",  "school_name": "Washington Elementary" },
    { "participant_id": "P-2072", "registrant": "Scarlett Baker",     "participant_age": 14, "gender": "Female", "grade": "9",  "school_name": "Roosevelt High School" },
    { "participant_id": "P-2073", "registrant": "Sebastian Gonzalez", "participant_age": 11, "gender": "Male",   "grade": "6",  "school_name": "Lincoln Elementary" },
    { "participant_id": "P-2074", "registrant": "Grace Nelson",       "participant_age": 13, "gender": "Female", "grade": "8",  "school_name": "Jefferson Middle School" },
]

_TRANSFERS = [
    { "transfer_id": "TR-45012", "registration_id": "REG-10045", "request_date": "2026-07-27", "reason": "Scheduling conflict",   "previous_school": "Lincoln Elementary",       "transfer_status": "pending" },
    { "transfer_id": "TR-45013", "registration_id": "REG-10046", "request_date": "2026-07-25", "reason": "Change of Address",      "previous_school": "Jefferson Middle School",  "transfer_status": "approved" },
    { "transfer_id": "TR-45014", "registration_id": "REG-10047", "request_date": "2026-07-22", "reason": "Military Order",         "previous_school": "Washington Elementary",    "transfer_status": "in_review_receiving_school" },
    { "transfer_id": "TR-45015", "registration_id": "REG-10048", "request_date": "2026-07-20", "reason": "Boarding School",        "previous_school": "Roosevelt High School",    "transfer_status": "completed_previous_school" },
    { "transfer_id": "TR-45016", "registration_id": "REG-10049", "request_date": "2026-07-18", "reason": "Family relocation",      "previous_school": "Madison Middle School",    "transfer_status": "rejected" },
    { "transfer_id": "TR-45017", "registration_id": "REG-10050", "request_date": "2026-07-15", "reason": "Program not available",  "previous_school": "Adams High School",        "transfer_status": "transfer_not_applicable" },
    { "transfer_id": "TR-45018", "registration_id": "REG-10051", "request_date": "2026-07-12", "reason": "Health reasons",         "previous_school": "Lincoln Elementary",       "transfer_status": "state_review_requested" },
    { "transfer_id": "TR-45019", "registration_id": "REG-10052", "request_date": "2026-07-10", "reason": "Academic reasons",       "previous_school": "Jefferson Middle School",  "transfer_status": "approved" },
    { "transfer_id": "TR-45020", "registration_id": "REG-10053", "request_date": "2026-07-08", "reason": "Change of Address",      "previous_school": "Franklin Elementary",      "transfer_status": "appeal_review_requested" },
    { "transfer_id": "TR-45021", "registration_id": "REG-10054", "request_date": "2026-07-05", "reason": "Scheduling conflict",    "previous_school": "Wilson High School",       "transfer_status": "appeal_review_in_progress" },
    { "transfer_id": "TR-45022", "registration_id": "REG-10055", "request_date": "2026-07-03", "reason": "Military Order",         "previous_school": "Roosevelt High School",    "transfer_status": "state_approved" },
    { "transfer_id": "TR-45023", "registration_id": "REG-10056", "request_date": "2026-07-01", "reason": "Family relocation",      "previous_school": "Madison Middle School",    "transfer_status": "in_review_previous_school" },
    { "transfer_id": "TR-45024", "registration_id": "REG-10057", "request_date": "2026-06-28", "reason": "Change of Address",      "previous_school": "Washington Elementary",    "transfer_status": "approved" },
    { "transfer_id": "TR-45025", "registration_id": "REG-10058", "request_date": "2026-06-25", "reason": "Program not available",  "previous_school": "Lincoln Elementary",       "transfer_status": "pending" },
    { "transfer_id": "TR-45026", "registration_id": "REG-10059", "request_date": "2026-06-22", "reason": "Boarding School",        "previous_school": "Adams High School",        "transfer_status": "state_approved_for_sub_varsity" },
    { "transfer_id": "TR-45027", "registration_id": "REG-10060", "request_date": "2026-06-20", "reason": "Health reasons",         "previous_school": "Jefferson Middle School",  "transfer_status": "in_review_receiving_school" },
    { "transfer_id": "TR-45028", "registration_id": "REG-10061", "request_date": "2026-06-18", "reason": "Academic reasons",       "previous_school": "Wilson High School",       "transfer_status": "approved" },
    { "transfer_id": "TR-45029", "registration_id": "REG-10062", "request_date": "2026-06-15", "reason": "Scheduling conflict",    "previous_school": "Madison Middle School",    "transfer_status": "state_rejected" },
    { "transfer_id": "TR-45030", "registration_id": "REG-10063", "request_date": "2026-06-12", "reason": "Change of Address",      "previous_school": "Franklin Elementary",      "transfer_status": "pending" },
    { "transfer_id": "TR-45031", "registration_id": "REG-10064", "request_date": "2026-06-10", "reason": "Family relocation",      "previous_school": "Roosevelt High School",    "transfer_status": "completed_previous_school" },
    { "transfer_id": "TR-45032", "registration_id": "REG-10065", "request_date": "2026-06-08", "reason": "Military Order",         "previous_school": "Lincoln Elementary",       "transfer_status": "appeal_approved" },
    { "transfer_id": "TR-45033", "registration_id": "REG-10066", "request_date": "2026-06-05", "reason": "Boarding School",        "previous_school": "Jefferson Middle School",  "transfer_status": "approved" },
    { "transfer_id": "TR-45034", "registration_id": "REG-10067", "request_date": "2026-06-03", "reason": "Health reasons",         "previous_school": "Adams High School",        "transfer_status": "rejected" },
    { "transfer_id": "TR-45035", "registration_id": "REG-10068", "request_date": "2026-06-01", "reason": "Program not available",  "previous_school": "Franklin Elementary",      "transfer_status": "transfer_not_applicable" },
    { "transfer_id": "TR-45036", "registration_id": "REG-10069", "request_date": "2026-05-28", "reason": "Academic reasons",       "previous_school": "Madison Middle School",    "transfer_status": "state_review_in_progress" },
    { "transfer_id": "TR-45037", "registration_id": "REG-10070", "request_date": "2026-05-25", "reason": "Change of Address",      "previous_school": "Wilson High School",       "transfer_status": "approved" },
    { "transfer_id": "TR-45038", "registration_id": "REG-10071", "request_date": "2026-05-22", "reason": "Scheduling conflict",    "previous_school": "Washington Elementary",    "transfer_status": "in_review_previous_school" },
    { "transfer_id": "TR-45039", "registration_id": "REG-10072", "request_date": "2026-05-20", "reason": "Family relocation",      "previous_school": "Roosevelt High School",    "transfer_status": "appeal_rejected" },
    { "transfer_id": "TR-45040", "registration_id": "REG-10073", "request_date": "2026-05-18", "reason": "Military Order",         "previous_school": "Lincoln Elementary",        "transfer_status": "pending" },
    { "transfer_id": "TR-45041", "registration_id": "REG-10074", "request_date": "2026-05-15", "reason": "Health reasons",         "previous_school": "Jefferson Middle School",  "transfer_status": "approved" },
]


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
    return {
        "registration_count": len(_REGISTRATIONS),
        "registrations": _REGISTRATIONS
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
    filtered = [r for r in _REGISTRATIONS if r.get("registration_state", "").lower() == state.lower()]
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
    filtered = [r for r in _REGISTRATIONS if r.get("approval", "").lower() == approval.lower()]
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
    filtered = [r for r in _REGISTRATIONS if r.get("document", "").lower() == "incomplete"]
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
    return {
        "payment_count": len(_PAYMENTS),
        "payments": _PAYMENTS
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
    filtered = [p for p in _PAYMENTS if p.get("payment_state", "").lower() == payment_state.lower()]
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
        dict[str, Any]: Payments with outstanding balances and total owed.
    """
    filtered = [p for p in _PAYMENTS if p.get("balance", 0) > 0]
    return {
        "payment_count": len(filtered),
        "total_outstanding_balance": round(sum(p.get("balance", 0) for p in filtered), 2),
        "payments": filtered
    }


@mcp.tool()
def get_payment_by_registration(registration_id: str) -> dict[str, Any]:
    """
    Retrieve the payment record linked to a specific registration.

    Args:
        registration_id: The registration ID (e.g. REG-10045).

    Returns:
        dict[str, Any]: Matching payment record.
    """
    match = [p for p in _PAYMENTS if p.get("registration_id") == registration_id]
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
    return {
        "program_count": len(_PROGRAMS_SECTIONS),
        "programs": _PROGRAMS_SECTIONS
    }


@mcp.tool()
def get_capacity_insights() -> dict[str, Any]:
    """
    Get capacity insights for all sections. Identifies sections that are
    at capacity, near capacity (>75% full), available, or have unlimited capacity.

    Returns:
        dict[str, Any]: Sections categorised by capacity status with enrollment counts.
    """
    # Count active registrations per section
    section_enrollment: dict[str, int] = {}
    for reg in _REGISTRATIONS:
        if reg.get("registration_state") in ("completed", "pending", "Active", "correction_required"):
            for sec_id in reg.get("section_ids", []):
                section_enrollment[sec_id] = section_enrollment.get(sec_id, 0) + 1

    unlimited, near_capacity, at_capacity, available = [], [], [], []

    for prog in _PROGRAMS_SECTIONS:
        cap = prog.get("capacity")
        for i, sec_id in enumerate(prog.get("section_ids", [])):
            enrolled = section_enrollment.get(sec_id, 0)
            names = prog.get("section_names", [])
            entry = {
                "program_id": prog["program_id"],
                "section_id": sec_id,
                "section_name": names[i] if i < len(names) else sec_id,
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
    Retrieve all participant / demographics records.

    Returns:
        dict[str, Any]: All participant records with count.
    """
    return {
        "participant_count": len(_PARTICIPANTS),
        "participants": _PARTICIPANTS
    }


@mcp.tool()
def get_participants_by_school(school_name: str) -> dict[str, Any]:
    """
    Retrieve participants from a specific school (case-insensitive partial match).

    Args:
        school_name: Full or partial school name.

    Returns:
        dict[str, Any]: Matching participant records with count.
    """
    filtered = [p for p in _PARTICIPANTS if school_name.lower() in p.get("school_name", "").lower()]
    return {
        "school_name": school_name,
        "participant_count": len(filtered),
        "participants": filtered
    }


@mcp.tool()
def get_participant_demographics_summary() -> dict[str, Any]:
    """
    Get an aggregated demographic summary: age range, gender, grade, and school distribution.

    Returns:
        dict[str, Any]: Demographic statistics across all participants.
    """
    gender_dist: dict[str, int] = {}
    grade_dist: dict[str, int] = {}
    school_dist: dict[str, int] = {}
    ages = []

    for p in _PARTICIPANTS:
        gender_dist[p.get("gender", "Unknown")] = gender_dist.get(p.get("gender", "Unknown"), 0) + 1
        grade_dist[p.get("grade", "Unknown")]   = grade_dist.get(p.get("grade", "Unknown"), 0) + 1
        school_dist[p.get("school_name", "Unknown")] = school_dist.get(p.get("school_name", "Unknown"), 0) + 1
        if p.get("participant_age") is not None:
            ages.append(p["participant_age"])

    return {
        "total_participants": len(_PARTICIPANTS),
        "age_range": {"min": min(ages), "max": max(ages), "avg": round(sum(ages) / len(ages), 1)} if ages else {},
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
    return {
        "transfer_count": len(_TRANSFERS),
        "transfers": _TRANSFERS
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
    filtered = [t for t in _TRANSFERS if t.get("transfer_status", "").lower() == transfer_status.lower()]
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
        dict[str, Any]: Transfer counts by status and by reason.
    """
    status_dist: dict[str, int] = {}
    reason_dist: dict[str, int] = {}
    for t in _TRANSFERS:
        st = t.get("transfer_status", "unknown")
        status_dist[st] = status_dist.get(st, 0) + 1
        re = t.get("reason", "unknown")
        reason_dist[re] = reason_dist.get(re, 0) + 1
    return {
        "total_transfers": len(_TRANSFERS),
        "status_distribution": status_dist,
        "reason_distribution": reason_dist
    }


# ===========================================================================
# CROSS-DATASET / ANALYTICS TOOLS
# ===========================================================================

@mcp.tool()
def get_registration_summary() -> dict[str, Any]:
    """
    Get an aggregated summary of all registrations including counts by state,
    approval status, document completeness, and payment totals.

    Returns:
        dict[str, Any]: Full registration analytics summary.
    """
    state_dist: dict[str, int] = {}
    approval_dist: dict[str, int] = {}
    doc_dist: dict[str, int] = {}

    for r in _REGISTRATIONS:
        st  = r.get("registration_state", "unknown")
        state_dist[st] = state_dist.get(st, 0) + 1
        ap  = r.get("approval", "unknown")
        approval_dist[ap] = approval_dist.get(ap, 0) + 1
        doc = r.get("document", "unknown")
        doc_dist[doc] = doc_dist.get(doc, 0) + 1

    payment_state_dist: dict[str, int] = {}
    total_collected = 0.0
    total_outstanding = 0.0

    for p in _PAYMENTS:
        ps = p.get("payment_state", "unknown")
        payment_state_dist[ps] = payment_state_dist.get(ps, 0) + 1
        total_collected   += p.get("amount_paid", 0)
        total_outstanding += p.get("balance", 0)

    return {
        "total_registrations": len(_REGISTRATIONS),
        "registration_state_distribution": state_dist,
        "approval_distribution": approval_dist,
        "document_completeness": doc_dist,
        "payment_summary": {
            "total_payments": len(_PAYMENTS),
            "payment_state_distribution": payment_state_dist,
            "total_amount_collected": round(total_collected, 2),
            "total_outstanding_balance": round(total_outstanding, 2)
        }
    }


@mcp.tool()
def search_registrations(query: str) -> dict[str, Any]:
    """
    Search registrations by registrant name, school name, or program ID.
    Case-insensitive keyword search across linked datasets.

    Args:
        query: Search keyword (e.g. a participant name, school, or program ID).

    Returns:
        dict[str, Any]: Matching registrations with linked participant and payment info.
    """
    q = query.lower()
    participants_map = {p["participant_id"]: p for p in _PARTICIPANTS}
    payments_map     = {p["registration_id"]: p for p in _PAYMENTS}

    results = []
    for reg in _REGISTRATIONS:
        participant = participants_map.get(reg.get("participant_id", ""), {})
        if (q in reg.get("registrant", "").lower() or
                q in participant.get("school_name", "").lower() or
                q in reg.get("program_id", "").lower()):
            results.append({
                "registration": reg,
                "participant": participant,
                "payment": payments_map.get(reg["registration_id"], {})
            })

    return {
        "query": query,
        "result_count": len(results),
        "results": results
    }


@mcp.tool()
def get_full_registration_detail(registration_id: str) -> dict[str, Any]:
    """
    Retrieve the complete record for a single registration, including the
    linked participant, payment, and transfer details (if any).

    Args:
        registration_id: The registration ID (e.g. REG-10045).

    Returns:
        dict[str, Any]: Full registration detail with all linked data.
    """
    reg_map      = {r["registration_id"]: r for r in _REGISTRATIONS}
    part_map     = {p["participant_id"]: p for p in _PARTICIPANTS}
    pay_map      = {p["registration_id"]: p for p in _PAYMENTS}
    transfer_map = {t["registration_id"]: t for t in _TRANSFERS}

    reg = reg_map.get(registration_id)
    if not reg:
        return {"error": f"Registration '{registration_id}' not found."}

    return {
        "registration_id": registration_id,
        "registration": reg,
        "participant": part_map.get(reg.get("participant_id", ""), {}),
        "payment": pay_map.get(registration_id, {}),
        "transfer": transfer_map.get(registration_id, None)
    }


# ===========================================================================
# ENTRY POINT
# ===========================================================================

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
