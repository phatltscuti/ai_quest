# Employee Self-Service Leave Cancellation — Requirements

| Item | Value |
|---|---|
| Source | Slack message |
| Requester | HR team |
| Target date | Before year-end holidays |
| Related code | leave_service.py |

## 1. Background
Employees currently cannot cancel leave requests they have already submitted, even when pending or approved. This creates unnecessary administrative overhead for HR and managers. The HR team requests a self-service leave cancellation feature allowing employees to cancel their leave, with manager notifications, partial cancellations for leave that has already started, and audit logging before the upcoming year-end holidays.

## 2. Goals / Non-goals
- Goal: Enable employees to self-service cancel pending or approved leave requests.
- Goal: Notify managers upon leave cancellation.
- Goal: Support full cancellation for future leave and partial cancellation (shortening the end date) for leave that has already started.
- Goal: Provide audit trails for all cancellation actions.
- Non-goal: Allowing cancellation of leave that has fully passed.

## 3. User stories
- US-01: As an employee, I want to cancel my pending or approved leave request so that I can reclaim my leave balance when plans change.
- US-02: As a manager, I want to be notified when my team member cancels their leave so that I can adjust team scheduling.
- US-03: As an employee, I want to shorten/cancel remaining days if my leave has already started so that I don't lose unspent leave needlessly.
- US-04: As an HR auditor, I want an audit log tracking who cancelled what leave and when so that leave records remain fully transparent.

## 4. Functional requirements
| ID | Requirement | Priority (Must/Should/Could) |
|---|---|---|
| FR-01 | The system must allow employees to cancel pending leave requests in full. | Must |
| FR-02 | The system must allow employees to cancel approved leave requests in full if the leave start date is in the future. | Must |
| FR-03 | The system must allow employees to partially cancel approved leave if the leave start date is in the past or today, by adjusting the end date to an earlier date (not earlier than start date). | Must |
| FR-04 | The system must notify the assigned approver / manager when an employee cancels a leave request (full or partial). | Must |
| FR-05 | The system must record an audit trail tracking cancellation events, including timestamp, request ID, employee, action type (full/partial), and modified dates. | Must |
| FR-06 | The system must update the leave days count and restore leave balances upon full or partial cancellation. | Must |

## 5. Non-functional requirements
| ID | Category (Security/Audit/Performance/Usability) | Requirement |
|---|---|---|
| NFR-01 | Audit | All cancellation records must be immutably stored and accessible via the admin/HR audit dashboard. |
| NFR-02 | Security | Employees can only cancel their own leave requests; validation must enforce authorization. |

## 6. Acceptance criteria
| ID | Verifies | Given | When | Then |
|---|---|---|---|---|
| AC-01 | FR-01 | An employee has a pending leave request with ID REQ-101. | The employee submits a full cancellation request for REQ-101. | The request status updates to cancelled and leave days are not deducted. |
| AC-02 | FR-02 | An employee has an approved leave request REQ-102 with start date 2026-12-25 (future). | The employee requests full cancellation of REQ-102. | The request status updates to cancelled, the manager is notified, and leave balance is fully restored. |
| AC-03 | FR-03 | An employee has an approved leave request REQ-103 from 2026-11-18 to 2026-11-25 (current date 2026-11-20). | The employee requests to shorten the leave end date to 2026-11-21. | The leave end date updates to 2026-11-21, days are recalculated, remaining unused days are restored to balance, and manager is notified. |
| AC-04 | FR-04 | An approved leave request is cancelled (full or partial). | The cancellation successfully completes. | A notification is dispatched to the manager/approver associated with the request. |
| AC-05 | FR-05 | Any leave cancellation action occurs. | The action is committed to the system. | An audit log entry is recorded with timestamp, employee name, request ID, and cancellation details. |

## 7. Assumptions
- A-01: Manager notification is sent via email or in-app notification system (to be integrated with existing notification service).
- A-02: Leave database schema (leave_requests table) will require new columns/tables for audit logging and status updates (cancelled, modified).

## 8. Open questions
| ID | Question | To |
|---|---|---|
| Q-01 | Should partial cancellation require manager approval, or can employees shorten leave unilaterally? | HR |
| Q-02 | What specific notification channel should be used for manager alerts (Email, Slack, In-app)? | HR / Dev |

## 9. Out of scope
- Retrospective cancellation of leave periods that have already completely elapsed in the past.
- Direct refund of cash/compensation for unused leave outside standard policy.
