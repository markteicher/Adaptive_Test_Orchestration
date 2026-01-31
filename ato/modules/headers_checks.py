# ato/modules/headers_checks.py

from .base import Module, ModuleResult

# Baseline security headers we care about at this stage
REQUIRED_HEADERS = {
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Strict-Transport-Security",
}


class HeadersChecks(Module):
    """
    Deterministic, read-only security header inspection.
    No payloads, no fuzzing, no inference.
    """

    name = "headers_checks"

    def run(self, ctx):
        # Single, safe request
        response = ctx.http.get(
            ctx.base_url + "/",
            module=self.name
        )

        headers = response.get("headers", {})
        present = {h for h in headers.keys()}
        missing = sorted(list(REQUIRED_HEADERS - present))

        if missing:
            return ModuleResult(
                ok=True,
                signal="missing_security_headers",
                details={
                    "missing": missing,
                    "present": sorted(list(present & REQUIRED_HEADERS)),
                },
            )

        return ModuleResult(
            ok=True,
            signal="headers_ok",
            details={
                "present": sorted(list(REQUIRED_HEADERS)),
            },
        )
