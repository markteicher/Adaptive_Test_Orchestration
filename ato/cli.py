# ato/cli.py

import argparse
from pathlib import Path
import json
import yaml

from .policy import Policy, Scope, Limits
from .evidence import EvidenceWriter
from .http_client import HttpClient
from .orchestrator import Orchestrator, Context
from .budget import RequestBudget


def load_policy(path: Path) -> Policy:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))

    scope = Scope(
        allowed_hosts=data["scope"]["allowed_hosts"],
        allowed_schemes=data["scope"]["allowed_schemes"],
        allowed_methods=data["scope"]["allowed_methods"],
        allowed_path_prefixes=data["scope"]["allowed_path_prefixes"],
    )

    limits = Limits(
        max_requests_total=data["limits"]["max_requests_total"],
        max_requests_per_minute=data["limits"]["max_requests_per_minute"],
        max_depth=data["limits"]["max_depth"],
        timeout_seconds=data["limits"]["timeout_seconds"],
    )

    return Policy(scope=scope, limits=limits)


def main():
    parser = argparse.ArgumentParser(description="Adaptive Test Orchestration (ATO)")
    parser.add_argument("--base-url", required=True, help="Base URL for testing")
    parser.add_argument(
        "--policy",
        default="policies/example_policy.yaml",
        help="Path to policy YAML",
    )
    parser.add_argument(
        "--run-dir",
        default="runs/latest",
        help="Directory to store run artifacts",
    )

    args = parser.parse_args()

    # Load policy
    policy = load_policy(Path(args.policy))

    # Prepare run directory
    run_dir = Path(args.run_dir)
    run_dir.mkdir(parents=True, exist_ok=True)

    # Evidence writer
    evidence_writer = EvidenceWriter(run_dir)

    # Global request budget (hard enforcement)
    budget = RequestBudget(
        max_total=policy.limits.max_requests_total,
        max_per_minute=policy.limits.max_requests_per_minute,
    )

    # HTTP client (single choke point)
    http = HttpClient(
        policy=policy,
        evidence_writer=evidence_writer,
        timeout=policy.limits.timeout_seconds,
        budget=budget,
    )

    # Orchestrator
    orchestrator = Orchestrator(max_depth=policy.limits.max_depth)

    ctx = Context(
        base_url=args.base_url.rstrip("/"),
        http=http,
        run_state={},
    )

    # Execute run
    results = orchestrator.run(ctx)

    # Write results
    results_path = run_dir / "results.json"
    results_path.write_text(
        json.dumps(results, indent=2),
        encoding="utf-8",
    )

    print("ATO run complete")
    print(f"  Evidence: {run_dir / 'evidence.jsonl'}")
    print(f"  Results : {results_path}")
    print(
        f"  Requests used: {budget.total_count} / {policy.limits.max_requests_total}"
    )


if __name__ == "__main__":
    main()
