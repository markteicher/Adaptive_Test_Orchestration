from dataclasses import dataclass
from urllib.parse import urlparse
from typing import List

@dataclass
class Scope:
    allowed_hosts: List[str]
    allowed_schemes: List[str]
    allowed_methods: List[str]
    allowed_path_prefixes: List[str]

@dataclass
class Limits:
    max_requests_total: int
    max_requests_per_minute: int
    max_depth: int
    timeout_seconds: int

class PolicyViolation(Exception):
    pass

class Policy:
    def __init__(self, scope: Scope, limits: Limits):
        self.scope = scope
        self.limits = limits

    def assert_allowed(self, url: str, method: str) -> None:
        p = urlparse(url)
        if p.scheme not in self.scope.allowed_schemes:
            raise PolicyViolation(f"scheme not allowed: {p.scheme}")
        if p.hostname not in self.scope.allowed_hosts:
            raise PolicyViolation(f"host not allowed: {p.hostname}")
        if method.upper() not in self.scope.allowed_methods:
            raise PolicyViolation(f"method not allowed: {method}")
        path = p.path or "/"
        if not any(path.startswith(pref) for pref in self.scope.allowed_path_prefixes):
            raise PolicyViolation(f"path not allowed: {path}")
