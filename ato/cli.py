import argparse
from pathlib import Path
import yaml
from .policy import Policy, Scope, Limits
from .evidence import EvidenceWriter
from .http_client import HttpClient
from .orchestrator import Orchestrator, Context

def load_policy(path: Path) -> Policy:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    s = data["scope"]
    l = data["limits"]
    scope = Scope(**s)
    limits = Limits(**l)
    return Policy(scope, limits)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", required=True)
    ap.add_argument("--policy", default="policies/example_policy.yaml")
    ap.add_argument("--run-dir", default="runs/latest")
    args = ap.parse_args()

    policy = load_policy(Path(args.policy))
    run_dir = Path(args.run_dir)
    ew = EvidenceWriter(run_dir)

    http = HttpClient(policy=policy, evidence_writer=ew, timeout=policy.limits.timeout_seconds)
    orch = Orchestrator(max_depth=policy.limits.max_depth)

    ctx = Context(base_url=args.base_url.rstrip("/"), http=http, run_state={})
    results = orch.run(ctx)

    (run_dir / "results.json").write_text(__import__("json").dumps(results, indent=2), encoding="utf-8")
    print(f"ATO run complete. Evidence: {run_dir/'evidence.jsonl'} Results: {run_dir/'results.json'}")

if __name__ == "__main__":
    main()
