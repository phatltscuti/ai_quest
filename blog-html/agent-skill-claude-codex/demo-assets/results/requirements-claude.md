# Self-service Leave Cancellation — Requirements

| Item | Value |
|---|---|
| Source | Slack message from HR team, pasted in `feature-request.txt` |
| Requester | HR team |
| Target date | "Before the year-end holidays if possible" (no exact date; see Q-01) |
| Related code | `leave_service.py` — table `leave_requests` (`id`, `employee`, `start`, `end`, `days`, `reason`, `status`, `approver`); functions `create_request`, `approve_request`, `leave_days`, `remaining_balance` |

## 1. Background
Employees cannot cancel a leave request after submitting it, so they ask HR to do it manually.
This happens even for requests that are already approved.
HR wants employees to cancel by themselves, managers to be notified, and a record of every cancellation for audit.
The request is time-sensitive because of the year-end holiday period.

## 2. Goals / Non-goals
- Goal: Employees can cancel their own pending or approved leave requests in the app without contacting HR.
- Goal: Employees can cancel only the remaining (future) days of a leave that has already started.
- Goal: The manager/approver is notified of every cancellation.
- Goal: HR can see who cancelled what, and when, for audit.
- Non-goal: Editing the dates of a request (other than shortening via partial cancellation).
- Non-goal: Cancelling leave on behalf of another employee (HR/manager cancellation).
- Non-goal: Changing the approval workflow itself.

## 3. User stories
- US-01: As an employee, I want to cancel a leave request I submitted so that I do not need to ask HR.
- US-02: As an employee whose leave has already started, I want to cancel the remaining days so that I can return to work early and keep those days in my balance.
- US-03: As a manager, I want to be notified when a team member cancels leave so that I can update team planning.
- US-04: As an HR staff member, I want to see a history of cancellations (who, what, when) so that I can audit leave changes.

## 4. Functional requirements
| ID | Requirement | Priority (Must/Should/Could) |
|---|---|---|
| FR-01 | An employee can cancel their own leave request whose status is `pending` and whose start date is after today. | Must |
| FR-02 | An employee can cancel their own leave request whose status is `approved` and whose start date is after today. | Must |
| FR-03 | A fully cancelled request gets the new status `cancelled` (*new* status value). | Must |
| FR-04 | If an approved leave has started (start ≤ today ≤ end), the employee cannot cancel the whole request. | Must |
| FR-05 | If an approved leave has started, the employee can cancel the remaining days from a chosen date (≥ tomorrow) to the end date. | Must |
| FR-06 | After a partial cancellation, the request `end` and `days` are updated to the kept period, and the status stays `approved`. | Must |
| FR-07 | A request whose end date is before today cannot be cancelled, fully or partially. | Must |
| FR-08 | A request with status `cancelled` (or `rejected`, if that status exists) cannot be cancelled again. | Must |
| FR-09 | An employee can only cancel requests where `employee` matches the logged-in user. | Must |
| FR-10 | The employee may enter an optional cancellation reason (max 500 characters). | Should |
| FR-11 | Cancelled days are returned to the employee's leave balance (as computed by `remaining_balance`). | Must |
| FR-12 | When an `approved` request is fully or partially cancelled, the approver stored in `approver` is notified. | Must |
| FR-13 | When a `pending` request is cancelled, the employee's manager is notified (see Q-03 on how the manager is identified). | Should |
| FR-14 | The notification contains: employee name, original dates, cancelled dates, number of cancelled days, reason (if given), and cancellation timestamp. | Must |
| FR-15 | Every cancellation (full or partial) writes one record to a *new* audit log: request id, actor, action (`full_cancel` / `partial_cancel`), old start/end/days/status, new start/end/days/status, reason, timestamp. | Must |
| FR-16 | HR can view the cancellation audit log, filtered by employee and by date range. | Must |
| FR-17 | The employee sees a confirmation dialog showing the days to be cancelled before the cancellation is saved. | Should |

## 5. Non-functional requirements
| ID | Category (Security/Audit/Performance/Usability) | Requirement |
|---|---|---|
| NFR-01 | Security | Ownership (FR-09) is checked on the server side; the client must not be trusted. |
| NFR-02 | Security | All database access for this feature uses parameterized queries (no string-formatted SQL, unlike the current `find_requests_by_employee`). |
| NFR-03 | Security | The audit log view is accessible only to the HR role. |
| NFR-04 | Audit | Audit records are append-only: no update or delete through the application. |
| NFR-05 | Audit | Audit records are retained for at least the period defined by HR (see Q-06). |
| NFR-06 | Audit | The status/date change and the audit record are written in the same database transaction; if one fails, both are rolled back. |
| NFR-07 | Privacy | The cancellation reason is visible only to the employee, the notified manager/approver and HR. |
| NFR-08 | Performance | A cancellation request completes (saved + audit written) within 2 seconds at the 95th percentile. |
| NFR-09 | Performance | A notification failure does not block or roll back the cancellation; it is retried or logged. |
| NFR-10 | Usability | "Today" is evaluated in the company time zone (see Q-05), not the server or browser time zone. |

## 6. Acceptance criteria
| ID | Verifies | Given | When | Then |
|---|---|---|---|---|
| AC-01 | FR-01, FR-03 | Today is 2026-12-01; employee "alice" has request #10, status `pending`, 2026-12-22 to 2026-12-24 | alice cancels #10 | #10 status is `cancelled` |
| AC-02 | FR-02, FR-03, FR-11 | Today is 2026-12-01; alice has request #11, `approved`, 2026-12-22 to 2026-12-24 (3 days); balance remaining is 7 | alice cancels #11 | #11 status is `cancelled`; remaining balance is 10 |
| AC-03 | FR-04 | Today is 2026-12-23; #11 is `approved`, 2026-12-22 to 2026-12-26 | alice tries to cancel the whole request | The action is rejected with message "Leave already started: only remaining days can be cancelled"; #11 is unchanged |
| AC-04 | FR-05, FR-06, FR-11 | Today is 2026-12-23; #11 is `approved`, 2026-12-22 to 2026-12-26 (5 days) | alice cancels from 2026-12-24 | #11 end = 2026-12-23, days = 2, status `approved`; 3 days are returned to the balance |
| AC-05 | FR-05 | Today is 2026-12-23; #11 is `approved`, 2026-12-22 to 2026-12-26 | alice chooses cancel-from date 2026-12-23 | The action is rejected with message "Cancel-from date must be tomorrow or later" |
| AC-06 | FR-07 | Today is 2026-12-30; #11 is `approved`, 2026-12-22 to 2026-12-26 | alice tries to cancel #11 | The cancel action is not shown; a direct API call returns an error and #11 is unchanged |
| AC-07 | FR-08 | #10 has status `cancelled` | alice tries to cancel #10 again | The action is rejected; no new audit record is written |
| AC-08 | FR-09, NFR-01 | Request #12 belongs to "bob" | alice sends a cancel call for #12 directly to the API | Response is "forbidden"; #12 is unchanged; no audit record is written |
| AC-09 | FR-10 | alice cancels #11 | She enters a 501-character reason | Validation error "Reason must be 500 characters or fewer"; nothing is saved |
| AC-10 | FR-12, FR-14 | #11 is `approved` with approver "carol" | alice cancels #11 with reason "Family plans changed" | carol receives one notification with alice's name, 2026-12-22–2026-12-24, 3 days, the reason and the timestamp |
| AC-11 | FR-13 | #10 is `pending`; alice's manager is "carol" | alice cancels #10 | carol receives one notification |
| AC-12 | FR-15, NFR-06 | #11 is `approved`, 2026-12-22 to 2026-12-26, today 2026-12-23 | alice cancels from 2026-12-24 | Exactly one audit record exists with actor alice, action `partial_cancel`, old end 2026-12-26 / days 5, new end 2026-12-23 / days 2, and a timestamp |
| AC-13 | NFR-06 | Writing the audit record fails (simulated DB error) | alice cancels #11 | #11 status and dates are unchanged; alice sees an error |
| AC-14 | FR-16, NFR-03 | 3 cancellations by alice and 2 by bob exist in December 2026 | An HR user filters the log by employee "alice" and 2026-12-01 to 2026-12-31 | Exactly 3 records are shown |
| AC-15 | NFR-03 | A user without the HR role | They open the audit log page or API | Response is "forbidden" |
| AC-16 | NFR-04 | An audit record exists | Any user calls an update or delete on it through the application | The operation is not available / rejected |
| AC-17 | NFR-09 | The notification service is down | alice cancels #11 | #11 is `cancelled`; the audit record is written; the notification failure is logged for retry |
| AC-18 | FR-17 | alice clicks "Cancel leave" on #11 | The confirmation dialog appears | It shows the dates and number of days to be cancelled; nothing is saved until she confirms |

## 7. Assumptions
- A-01: Only the employee who owns the request can cancel it through this feature; HR/manager cancellation is out of scope.
- A-02: "Remaining days" means days from tomorrow onward; today's day of leave cannot be cancelled.
- A-03: A leave whose start date is today counts as "already started".
- A-04: Cancelling an approved leave does not need manager re-approval; the manager is only notified.
- A-05: Partial cancellation shortens the existing request (updates `end` and `days`) instead of creating a new request record.
- A-06: The leave balance is derived from the `days` of non-cancelled requests, so updating `days` / status is enough to return days to the balance.
- A-07: The day count uses the inclusive rule stated in the `leave_days` docstring (start and end both included). Note: the current implementation returns `(end - start).days`, which is one day short; this must be fixed or the cancelled-day counts will be wrong (see Q-07).
- A-08: The existing `approver` column identifies the manager to notify for approved requests.
- A-09: The app has an authenticated user identity that can be matched to the `employee` field.
- A-10: Weekends and public holidays are counted the same way as the current `leave_days` logic (no change in this feature).

## 8. Open questions
| ID | Question | To |
|---|---|---|
| Q-01 | What is the exact deadline? Which date counts as "before the year-end holidays"? | HR / PM |
| Q-02 | Should cancelling an *approved* leave require manager approval, or is notification enough (A-04)? | HR |
| Q-03 | `leave_requests` stores no manager for pending requests. How is an employee's manager identified (HR system, new column, org table)? | Dev / HR |
| Q-04 | Which notification channel is required: in-app, email, Slack, or several? No notification module exists in the code today. | HR / PM |
| Q-05 | Which time zone defines "today" for the started/finished checks? | HR |
| Q-06 | How long must cancellation audit records be kept? | HR / Legal |
| Q-07 | `leave_days` excludes the end date despite its docstring. Is the inclusive count the intended rule, and should existing `days` values be corrected? | HR / Dev |
| Q-08 | Is there a minimum notice period (e.g. no cancellation of an approved leave within 24 hours of its start)? | HR |
| Q-09 | Is there a `rejected` status in production data? Only `pending` and `approved` appear in the code. | Dev |
| Q-10 | Should the employee be able to cancel a single middle day of a not-yet-started leave (splitting the request), or only the whole request? | HR |

## 9. Out of scope
- HR or managers cancelling leave on behalf of employees.
- Changing leave dates other than shortening via partial cancellation.
- Splitting a request into several periods (pending Q-10).
- Undo / reinstating a cancelled request.
- Fixing unrelated issues in `leave_service.py` (e.g. hard-coded `ADMIN_TOKEN`, mutable default argument in `create_request`, swallowed exception in `remaining_balance`), except where required by NFR-02 and A-07.
