from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Dict, Optional

@dataclass
class Evidence:
    ts_utc: str
    module: str
    request: Dict[str, Any]
    response: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

class EvidenceWriter:
    def __init__(self, run_dir: Path):
        self.run_dir = run_dir
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.file = self.run_dir / "evidence.jsonl"

    def write(self, ev: Evidence) -> None:
        with self.file.open("a", encoding="utf-8") as f:
            f.write(json.dumps(ev.to_dict(), ensure_ascii=False) + "\n")

def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat()
