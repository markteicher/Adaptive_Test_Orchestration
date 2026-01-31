from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class ModuleResult:
    ok: bool
    signal: str                 # e.g. "endpoint_alive", "suspicious_header", "none"
    details: Dict[str, Any]
    next_hints: Optional[Dict[str, Any]] = None

class Module:
    name: str = "base"

    def run(self, ctx: "Context") -> ModuleResult:  # noqa: F821
        raise NotImplementedError
