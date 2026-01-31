# 🧪 Adaptive Test Orchestration (ATO)

Adaptive Test Orchestration (ATO) is a system used to validate whether proof-of-concept automated exploitation workflows continue to function once real, commercial-grade software and security standards are applied.

Recent demonstrations of automated or AI-assisted exploitation—such as “one-click RCE” workflows or “AI agents that can hack”—show how quickly known techniques can be chained when guardrails are absent. In practice, these demonstrations usually rely on assumptions that do not hold in real enterprise environments, including trusted local execution, implicit authorization, unlimited retries, permissive networking, and incomplete documentation.

ATO exists to remove those assumptions.

ATO forces proof-of-concept automation to operate under the same conditions required of real software: explicit scope, bounded execution, centralized control, full observability, and complete documentation. The system does not attempt to improve or enhance exploitation techniques. It observes what still works once commercial constraints are enforced.

**ATO applies commercial QA standards—scope control, bounded execution, reproducibility, and full documentation—to proof-of-concept automated exploitation workflows to determine whether they remain functional under real-world constraints.**

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-yellow.svg)

---

## 🎯 Purpose and Scope

ATO is **not**:
- an exploit framework  
- an attack toolkit  
- an autonomous “AI hacking agent”  

ATO **is** a validation harness.

It is used to answer a single question:

> Does this automation still work when it is treated like real software that must meet enterprise engineering and QA standards?

Failures under these constraints are expected outcomes, not errors.

---

## ✨ Capabilities

### 🔒 Commercial Guardrails Applied

ATO enforces the same constraints expected of production-grade software.

- **Explicit scope**
  - A target base URL must be declared
  - Execution is limited to that target
  - No implicit discovery or environment-driven expansion

- **Bounded execution**
  - A single global request budget applies to the entire run
  - A single global rate limit applies across all modules
  - The system cannot retry endlessly or escalate activity silently

- **Centralized orchestration**
  - All execution is controlled by a single orchestrator
  - Modules cannot trigger other modules
  - Modules cannot expand scope or bypass limits

- **Deterministic stopping behavior**
  - Execution stops when limits are reached
  - Execution stops on explicit errors
  - Stop conditions are intentional and recorded

These guardrails exist to determine whether automation survives real operational constraints.

---

### 🔁 Orchestration and Execution Model

ATO executes approved test modules **one at a time**.

Each module:
- receives a constrained execution context
- performs only its defined behavior
- returns structured results

The orchestrator:
- controls execution order
- enforces shared limits
- decides whether execution continues

There is no autonomous branching, speculative behavior, or hidden retries.

---

### 🧾 Evidence and Observability

ATO records all activity as it occurs.

For each request, the system captures:
- timestamp
- executing module
- HTTP method and URL
- request data (when applicable)
- response status and content

Evidence is written during execution, not reconstructed later.

This enables:
- audit and review
- QA validation
- failure analysis
- independent verification

---

### ♻️ Reproducibility

Given the same:
- code version
- configuration
- target

ATO behaves the same way.

This allows proof-of-concept automation to be evaluated using the same standards applied to production software: repeatable runs and inspectable results.

---

## 📁 Repository Structure

    ato/
      pyproject.toml        Project metadata and dependencies
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

All dependencies are declared explicitly in `pyproject.toml`.

- **requests**  
  Used for HTTP and HTTPS request execution.

- **PyYAML**  
  Used for configuration parsing.

No dynamic or implicit dependency loading occurs at runtime.

---

## 📦 Installation

These steps reflect commercial engineering standards.  
Follow them exactly. Do not skip steps.

1. **Verify Python version**

       python --version
       python3 --version

   Python **3.10+** is required.

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

9. **Editable install (development only)**

       pip install -e .
       ato --help

---

## ▶️ Usage

Example execution:

    ato --base-url https://app.example.com \
        --policy policies/example_policy.yaml \
        --run-dir runs/example

- `--base-url` specifies the target under test
- `--policy` defines execution boundaries and limits
- `--run-dir` stores all output artifacts

---

## 📂 Output Artifacts

Each run produces:

    evidence.jsonl
    results.json

- `evidence.jsonl` contains raw request and response evidence
- `results.json` contains structured execution outcomes

---

## 🔗 References and Validation Context

The references below describe the class of proof-of-concept automation ATO is designed to evaluate.

### 🤖 Automated / AI-Assisted Exploitation

- Ethiack – MoltBot “One-Click RCE”  
  https://ethiack.com/news/blog/one-click-rce-moltbot

- Ethiack – Hackian: An AI Agent That Can Hack  
  https://blog.ethiack.com/blog/introducing-the-hackian-an-ai-agent-that-can-hack

- Ethiack Research Blog  
  https://ethiack.com/blog

These demonstrations typically assume trusted execution environments and minimal constraints.  
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
