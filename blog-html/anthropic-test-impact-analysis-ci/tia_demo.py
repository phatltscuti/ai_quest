"""
tia_demo.py - MINH HOA / ILLUSTRATION ONLY
==========================================
Day la vi du do tac gia blog tu viet de minh hoa y tuong
"changed files -> dependency map -> selected tests" va mo hinh
"listener stateless -> journal -> rollup consumer -> selector".
KHONG phai code cua Anthropic. Anthropic khong cong bo source code
cua test impact analysis service trong bai viet goc.

This is the blog author's OWN toy example. It is NOT Anthropic's code.

Run:  python tia_demo.py
Only the Python standard library is used.
"""
from collections import defaultdict, deque

# ---------------------------------------------------------------------------
# 1) Repository model: file -> package, package -> depends on packages
# ---------------------------------------------------------------------------
FILE_TO_PACKAGE = {
    "billing/invoice.py": "billing",
    "billing/tax_jp.py": "billing",
    "auth/session.py": "auth",
    "common/dates.py": "common",
    "api/routes.py": "api",
    "web/checkout.tsx": "web",
    "docs/README.md": None,  # docs-only change -> no package
}

PACKAGE_DEPENDS_ON = {
    "common": [],
    "auth": ["common"],
    "billing": ["common"],
    "api": ["auth", "billing"],
    "web": ["api"],
}

TESTS_BY_PACKAGE = {
    "common": ["test_dates_parse", "test_dates_tz"],
    "auth": ["test_login", "test_session_expiry"],
    "billing": ["test_invoice_total", "test_tax_jp_rounding"],
    "api": ["test_api_contract"],
    "web": ["e2e_checkout_flow"],
}


def reverse_deps(graph):
    rev = defaultdict(set)
    for pkg, deps in graph.items():
        for d in deps:
            rev[d].add(pkg)
    return rev


def impacted_packages(changed_files):
    """changed files -> touched packages -> + every package that depends on them."""
    rev = reverse_deps(PACKAGE_DEPENDS_ON)
    touched = {FILE_TO_PACKAGE.get(f) for f in changed_files} - {None}
    seen, queue = set(touched), deque(touched)
    while queue:
        pkg = queue.popleft()
        for parent in rev[pkg]:
            if parent not in seen:
                seen.add(parent)
                queue.append(parent)
    return touched, seen


# ---------------------------------------------------------------------------
# 2) Listener (stateless workers) -> journal -> rollup consumer -> history
# ---------------------------------------------------------------------------
JOURNAL = []                    # stand-in for an in-memory store (e.g. a Redis stream)
HISTORY = defaultdict(list)     # per-test rolled-up history read by the selector


def listener_worker(worker_id, ci_result):
    """Any worker can take any result: append and forget (no state kept)."""
    JOURNAL.append({**ci_result, "worker": worker_id})


def rollup_consumer():
    """Small separate process: fold journal entries into per-test history."""
    processed = 0
    while JOURNAL:
        ev = JOURNAL.pop(0)
        HISTORY[ev["test"]].append(ev["status"])
        processed += 1
    return processed


def classify(test):
    runs = HISTORY.get(test, [])
    if not runs:
        return "new"            # never seen -> must run
    fails = runs.count("fail")
    if fails == len(runs) and len(runs) >= 3:
        return "broken-on-main"  # failing for everybody -> not this PR's fault
    if 0 < fails < len(runs):
        return "flaky"
    return "healthy"


def select_tests(changed_files):
    touched, impacted = impacted_packages(changed_files)
    candidates = sorted(t for p in impacted for t in TESTS_BY_PACKAGE[p])
    plan = {"run": [], "run_but_non_blocking": [], "skip": []}
    for t in candidates:
        c = classify(t)
        if c == "broken-on-main":
            plan["skip"].append((t, c))
        elif c == "flaky":
            plan["run_but_non_blocking"].append((t, c))
        else:
            plan["run"].append((t, c))
    return touched, impacted, candidates, plan


if __name__ == "__main__":
    # simulate CI results arriving from many jobs, spread over 3 stateless workers
    fake_results = [
        ("test_dates_parse", "pass"), ("test_dates_tz", "pass"),
        ("test_invoice_total", "pass"), ("test_tax_jp_rounding", "fail"),
        ("test_tax_jp_rounding", "pass"), ("test_api_contract", "fail"),
        ("test_api_contract", "fail"), ("test_api_contract", "fail"),
        ("test_login", "pass"), ("test_session_expiry", "pass"),
        ("e2e_checkout_flow", "pass"), ("test_invoice_total", "pass"),
    ]
    for i, (test, status) in enumerate(fake_results):
        listener_worker(worker_id=i % 3, ci_result={"test": test, "status": status})
    jobs_in = len(fake_results)
    jobs_out = rollup_consumer()
    print(f"[listener] jobs in = {jobs_in}, jobs rolled up = {jobs_out}, "
          f"lag = {jobs_in - jobs_out}")

    all_tests = sum(TESTS_BY_PACKAGE.values(), [])
    pr = ["billing/tax_jp.py", "docs/README.md"]
    touched, impacted, candidates, plan = select_tests(pr)
    print(f"\nPR changed files : {pr}")
    print(f"touched packages : {sorted(touched)}")
    print(f"impacted (+rdeps): {sorted(impacted)}")
    print(f"candidate tests  : {len(candidates)} / {len(all_tests)} total")
    for k, v in plan.items():
        print(f"  {k:<22}: {[f'{t} ({c})' for t, c in v]}")
    ran = len(plan["run"]) + len(plan["run_but_non_blocking"])
    print(f"\n=> run {ran} of {len(all_tests)} tests "
          f"({100 * (1 - ran / len(all_tests)):.0f}% fewer CI jobs for this PR)")
