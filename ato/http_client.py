import requests
from typing import Dict, Any, Optional
from .evidence import Evidence, now_utc_iso
from .budget import RequestBudget, BudgetExceeded

class HttpClient:
    def __init__(self, policy, evidence_writer, timeout: int, budget: RequestBudget):
        self.policy = policy
        self.evidence_writer = evidence_writer
        self.timeout = timeout
        self.budget = budget

    def _record(self, module: str, req: Dict[str, Any], resp: Dict[str, Any]) -> None:
        self.evidence_writer.write(Evidence(
            ts_utc=now_utc_iso(),
            module=module,
            request=req,
            response=resp
        ))

    def get(
        self,
        url: str,
        module: str = "unknown",
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:

        # 🔒 global enforcement point
        self.budget.consume()
        self.policy.assert_allowed(url, "GET")

        req = {"method": "GET", "url": url, "headers": headers or {}}

        try:
            r = requests.get(url, headers=headers, timeout=self.timeout)
            resp = {
                "status": r.status_code,
                "headers": dict(r.headers),
                "body": r.text[:200000]
            }
        except Exception as e:
            resp = {
                "status": 0,
                "error": str(e),
                "headers": {},
                "body": ""
            }

        self._record(module, req, resp)
        return resp
