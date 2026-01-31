# 🧪 Adaptive Test Orchestration (ATO)

Adaptive Test Orchestration (ATO) is a software system whose purpose is to **verify whether proof-of-concept automated exploitation code actually works when subjected to real, commercial-grade software and security standards**.

In recent years, multiple demonstrations have claimed that automated tools or “AI agents” can perform complex exploitation with minimal human involvement. These demonstrations often show impressive results in controlled environments. However, they typically depend on assumptions that do not exist in real organizations, such as unrestricted execution, implicit authorization, unlimited retries, permissive networking, and undocumented behavior.

ATO exists specifically to remove those assumptions.

ATO does not attempt to invent new exploitation techniques. It does not attempt to “outperform” existing tools. Instead, it takes existing proof-of-concept automation and forces it to operate under the same rules that real, deployed software must follow.

**ATO applies commercial QA standards—scope control, bounded execution, reproducibility, and full documentation—to proof-of-concept automated exploitation workflows to determine whether they remain functional under real-world constraints.**

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-yellow.svg)

---

## 🎯 Purpose and Scope

ATO is not an exploit framework.  
ATO is not an attack toolkit.  
ATO is not an autonomous “AI hacking agent”.

ATO is a **validation system**.

Its role is to answer a single, practical question:

> Does this automated workflow still function when it must behave like real software operating inside a real enterprise?

If automation fails under these conditions, that failure is not an error. It is the result.

---

## ✨ Capabilities

### 🔒 Commercial Guardrails Applied

ATO applies the same constraints expected of production-grade software.

These guardrails exist to eliminate hidden assumptions.

- **Explicit scope**
  - A target base URL must be provided.
  - Execution is limited to that declared target.
  - The system will not discover or interact with anything outside that scope.

- **Bounded execution**
  - A single global request budget limits how much activity can occur in one run.
  - A single global rate limit controls how fast requests may be sent.
  - The system cannot retry endlessly or escalate activity silently.

- **Centralized orchestration**
  - All activity is controlled by a single orchestrator.
  - Individual modules cannot trigger other modules.
  - Modules cannot expand scope or bypass limits.

- **Deterministic stopping behavior**
  - Execution stops when limits are reached.
  - Execution stops on explicit errors.
  - Stop conditions are deliberate and recorded.

These guardrails are not features. They are test conditions.

---

### 🔁 Orchestration and Execution Model

ATO executes test modules sequentially.

Each module:
- receives a constrained execution context
- performs only its defined behavior
- returns structured results

The orchestrator:
- controls execution order
- enforces shared limits
- decides whether execution continues

There is no autonomous branching, speculation, or hidden retry logic.

---

### 🧾 Evidence and Observability

ATO records everything it does.

For every request, the system captures:
- the time the request occurred
- which module issued the request
- the HTTP method and URL
- request data when present
- the full response returned

Evidence is written as execution happens, not reconstructed later.

This ensures all behavior can be reviewed, audited, and verified.

---

### ♻️ Reproducibility

ATO is designed so that the same inputs produce the same behavior.

If the following remain unchanged:
- the code version
- the configuration
- the target

Then execution behavior remains consistent.

This allows proof-of-concept automation to be evaluated repeatedly using the same standards applied to production software.

---

## 📁 Repository Structure

    ato/
      pyproject.toml        Project metadata and dependency definitions
      README.md             Documentation
      ato/
        cli.py              Command-line interface
        orchestrator.py     Central execution control
        http_client.py      Shared HTTP execution layer
        budget.py           Global budgeting and rate limiting
        evidence.py         Evidence capture
        modules/
          base.py            Module interface
          http_basic_probe.py
          headers_checks.py
      policies/
        example_policy.yaml
      runs/
        .gitkeep

---

## 🧩 Dependencies

All dependencies are explicitly declared in `pyproject.toml`.

- **requests**  
  Used to send HTTP and HTTPS requests.

- **PyYAML**  
  Used to parse configuration files.

No hidden or runtime-loaded dependencies are used.

---

## 📦 Installation

These steps reflect real-world engineering standards.  
They must be followed exactly.

1. **Verify Python version**

   Python 3.10 or newer is required.

       python --version
       python3 --version

2. **Verify pip**

       pip --version

3. **Confirm repository root**

       ls pyproject.toml

4. **Create a virtual environment**

       python -m venv .venv

5. **Activate the environment**

   Linux / macOS:

       source .venv/bin/activate

   Windows:

       .venv\Scripts\Activate.ps1

6. **Upgrade packaging tools**

       pip install --upgrade pip setuptools wheel

7. **Install ATO**

       pip install .

8. **Verify installation**

       ato --help

9. **Editable install (development use only)**

       pip install -e .
       ato --help

---

## ▶️ Usage

Example execution:

    ato --base-url https://app.example.com \
        --policy policies/example_policy.yaml \
        --run-dir runs/example

- `--base-url` specifies the target being tested.
- `--policy` defines execution limits and scope.
- `--run-dir` specifies where output artifacts are written.

---

## 📂 Output Artifacts

Each run produces:

    evidence.jsonl
    results.json

- `evidence.jsonl` contains raw request and response records.
- `results.json` contains structured execution outcomes.

---

## 🔗 References and Validation Context

The references below describe the class of proof-of-concept automation that ATO evaluates.

### 🤖 Automated / AI-Assisted Exploitation

- Ethiack – MoltBot “One-Click RCE”  
  https://ethiack.com/news/blog/one-click-rce-moltbot

- Ethiack – Hackian: An AI Agent That Can Hack  
  https://blog.ethiack.com/blog/introducing-the-hackian-an-ai-agent-that-can-hack

- Ethiack Research Blog  
  https://ethiack.com/blog

These demonstrations typically assume trusted environments and minimal constraints.  
ATO evaluates what remains once those assumptions are removed.

---

### 🛡️ Security Engineering Context

- OWASP Top Ten  
  https://owasp.org/www-project-top-ten/

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework

- SANS Institute Research  
  https://www.sans.org/blog

- Dark Reading  
  https://www.darkreading.com/attacks-breaches

---

### ⚖️ Responsible Engineering and Research

- ACM Code of Ethics  
  https://www.acm.org/code-of-ethics

- Black Hat Conference Archives  
  https://www.blackhat.com

---

## 🚧 Project Status

ATO is under active development.

Current focus:
- applying commercial QA guardrails
- documenting assumptions explicitly
- validating proof-of-concept automation behavior

---

## 📄 License

MIT License
