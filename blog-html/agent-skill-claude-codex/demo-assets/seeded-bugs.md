# Seeded issues in demo-project/leave_service.py (ground truth — NOT shown to the agents)

| # | Line(s) | Issue | Expected severity |
|---|---|---|---|
| B1 | 6 | Hard-coded secret `ADMIN_TOKEN` in source | Critical |
| B2 | 15 | SQL injection: f-string interpolation of `name` into SQL | Critical |
| B3 | 21 | Off-by-one: docstring says inclusive, `(end - start).days` excludes the end date (also no check end >= start) | Major |
| B4 | 24–25 | Mutable default argument `attachments=[]` shared across calls | Major |
| B5 | 36–43 | Missing authorization: approver can approve own request; status not checked (re-approving / approving cancelled) | Major |
| B6 | 47–50 | `except Exception: pass` swallows errors and returns None | Minor |

Also acceptable extra findings: connections never closed, no tests, no input validation on dates/reason.
