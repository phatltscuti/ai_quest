# Review checklist

## Security
- [ ] No secrets, tokens or passwords in source code or logs
- [ ] All SQL uses parameter binding (no string formatting / f-strings)
- [ ] Authorization: the caller is allowed to perform the action (e.g. no self-approval)
- [ ] Input validation for user-supplied values

## Correctness
- [ ] Logic matches docstrings, comments and business rules (inclusive/exclusive ranges, off-by-one)
- [ ] State transitions are checked (e.g. cannot approve something already approved or cancelled)
- [ ] No mutable default arguments or shared global state

## Error handling & resources
- [ ] No silent `except: pass` / swallowed exceptions
- [ ] Connections, files and cursors are closed (context managers)

## Maintainability & tests
- [ ] Functions are small and named for what they do
- [ ] Changed logic has tests
