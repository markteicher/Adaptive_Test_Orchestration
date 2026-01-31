from dataclasses import dataclass
from typing import List, Dict, Any
from .modules.http_basic_probe import HttpBasicProbe

@dataclass
class Context:
    base_url: str
    http: Any
    run_state: Dict[str, Any]

class Orchestrator:
    def __init__(self, max_depth: int):
        self.max_depth = max_depth

    def run(self, ctx: Context) -> List[Dict[str, Any]]:
        # Deterministic queue (no LLM yet)
        modules = [HttpBasicProbe()]
        results = []

        depth = 0
        while modules and depth < self.max_depth:
            m = modules.pop(0)
            res = m.run(ctx)
            results.append({"module": m.name, "result": res.__dict__})

            # deterministic branching based on signals
            if res.signal == "endpoint_alive" and res.next_hints:
                # later: enqueue additional approved modules here
                pass

            depth += 1

        return results
