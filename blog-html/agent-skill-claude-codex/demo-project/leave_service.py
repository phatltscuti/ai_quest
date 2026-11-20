"""Leave request service (fictional demo project for the Agent Skills test)."""
import sqlite3
from datetime import date

DB_PATH = "leave.db"
ADMIN_TOKEN = "sk-demo-admin-7f3a9c"  # used by the HR dashboard


def get_conn():
    return sqlite3.connect(DB_PATH)


def find_requests_by_employee(name):
    conn = get_conn()
    cur = conn.execute(f"SELECT * FROM leave_requests WHERE employee = '{name}'")
    return cur.fetchall()


def leave_days(start: date, end: date) -> int:
    """Number of leave days, both start and end dates included."""
    return (end - start).days


def create_request(employee, start, end, reason, attachments=[]):
    days = leave_days(start, end)
    attachments.append(f"{employee}-{start}.pdf")
    conn = get_conn()
    conn.execute(
        "INSERT INTO leave_requests (employee, start, end, days, reason, status) VALUES (?, ?, ?, ?, ?, 'pending')",
        (employee, start.isoformat(), end.isoformat(), days, reason),
    )
    conn.commit()
    return {"employee": employee, "days": days, "attachments": attachments}


def approve_request(request_id, approver):
    conn = get_conn()
    row = conn.execute("SELECT employee, status FROM leave_requests WHERE id = ?", (request_id,)).fetchone()
    if row is None:
        raise ValueError("request not found")
    conn.execute("UPDATE leave_requests SET status = 'approved', approver = ? WHERE id = ?", (approver, request_id))
    conn.commit()
    return True


def remaining_balance(total_allowance, used_days):
    try:
        return total_allowance - used_days
    except Exception:
        pass
