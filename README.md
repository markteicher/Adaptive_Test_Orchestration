# Adaptive Test Orchestration (ATO)

Adaptive Test Orchestration (ATO) is a system designed to **validate whether proof-of-concept automated exploitation code continues to function once real, commercial-grade software and security standards are applied**.

Recent demonstrations of automated or AI-assisted exploitation—such as so-called “one-click RCE” workflows or “AI agents that can hack”—show how quickly known techniques can be chained **when guardrails are absent**. In practice, these demonstrations almost always rely on assumptions that do not hold in real enterprises, including local execution context, implicit authorization, permissive runtime environments, unlimited retries, and incomplete documentation.

ATO exists to remove those assumptions.

ATO intentionally applies **commercial QA guardrails** to proof-of-concept automation and observes what still works once those guardrails are enforced.

**ATO applies commercial QA standards—scope control, bounded execution, reproducibility, and full documentation—to proof-of-concept automated exploitation workflows to determine whether they remain functional under real-world constraints.**

---

## What the statement above means (explicitly explained)

This section exists so that **nothing is implicit and nothing is left to interpretation**.

- **Commercial QA standards**  
  The same expectations used for software that is actually deployed, supported, and audited:
  - explicit inputs and configuration  
  - predictable execution behavior  
  - bounded runtime and resource usage  
  - documented assumptions and limitations  
  - reviewable and reproducible output  

- **Scope control**  
  The automation must be told exactly:
  - which target it is allowed to interact with  
  - which protocols it may use  
  - which actions are permitted  
  Nothing happens implicitly or “because the environment allows it”.

- **Bounded execution**  
  The automation cannot:
  - run indefinitely  
  - retry endlessly  
  - escalate activity quietly  
  Hard global limits define how much work is allowed in a single run.

- **Reproducibility**  
  Given the same inputs, configuration, and code version, behavior is repeatable.  
  Results can be rerun, reviewed, and independently verified.

- **Full documentation**  
  Behavior, limits, assumptions, and failure conditions are written down.  
  If something cannot be documented clearly, it is not considered acceptable.

- **Proof-of-concept automated exploitation workflows**  
  Code written to demonstrate automated attack chaining, decision logic, or orchestration.  
  Often impressive in demos, but rarely hardened for enterprise conditions.

- **Determine whether they remain functional**  
  ATO does not attempt to “make attacks succeed”.  
  It observes what still works once constraints are applied.

- **Real-world constraints**  
  Conditions that exist in actual enterprises:
  authorization, rate limits, auditability, accountability, operational visibility, and change control.

---

## ✨ Capabilities

### 🔒 Commercial Guardrails Applied

ATO applies **engineering discipline**, not exploit coverage.

- **Explicit scope declaration**
  - A target base URL must be provided
  - Execution is bound to that target
  - No discovery beyond declared scope

- **Global execution limits**
  - One request budget shared across all modules
  - One rate limit shared across all modules
  - No per-module bypassing of limits

- **Centralized orchestration**
  - All execution is controlled by a single orchestrator
  - Modules cannot trigger other modules
  - Modules cannot expand scope

- **Deterministic stop conditions**
  - Execution stops when limits are reached
  - Execution stops on explicit errors
  - Stop conditions are intentional and recorded

These guardrails exist to answer one question:

> *Does this automation still work once it is treated like real software?*

---

### 🔁 Orchestration and Sequencing

ATO executes approved modules **one at a time**.

- Each module:
  - receives a constrained execution context  
  - performs only its explicitly defined behavior  
  - returns structured results  

- The orchestrator:
  - controls execution order  
  - decides whether execution continues  
  - enforces global limits  

There is no autonomous branching, speculative behavior, or hidden retries.

---

### 🧾 Evidence and Observability

ATO records **everything it does**.

For each request:
- timestamp  
- executing module  
- HTTP method and URL  
- request data (where applicable)  
- response status and content  

Evidence is written **during execution**, not reconstructed later.

This enables:
- audit and review  
- debugging and failure analysis  
- QA validation  
- third-party verification  

---

### ♻️ Reproducibility and Review

ATO is designed to be rerun.

Given the same:
- code version  
- configuration  
- target  

The system behaves the same way.

This allows proof-of-concept automation to be evaluated the same way production software is evaluated: by rerunning it and inspecting the results.

---

## 📁 Repository Structure

    ato/
      pyproject.toml        Project metadata and dependencies
      README.md             Documentation
      ato/
        cli.py              Command-line interface
        orchestrator.py     Central execution control
        http_client.py      Shared HTTP client
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

## 🧩 Python Dependencies

All dependencies are declared explicitly in `pyproject.toml`.

- **requests**  
  Used for HTTP and HTTPS request execution.

- **PyYAML**  
  Used for configuration parsing.

No dynamic dependency loading occurs at runtime.

---

## 📦 Installation

This installation process mirrors **commercial engineering standards**.  
Follow every step exactly. Do not skip steps.

### 1) Verify Python Version

ATO requires Python **3.10 or newer**.

    python --version
    python3 --version

---

### 2) Verify pip

    pip --version

Ensure pip is bound to the same Python interpreter.

---

### 3) Confirm Repository Root

    ls pyproject.toml

---

### 4) Create Virtual Environment

    python -m venv .venv

---

### 5) Activate Environment

Linux / macOS:

    source .venv/bin/activate

Windows:

    .venv\Scripts\Activate.ps1

Verify:

    python --version

---

### 6) Upgrade Toolchain

    pip install --upgrade pip setuptools wheel

---

### 7) Install ATO

    pip install .

---

### 8) Verify Installation

    ato --help

---

### 9) Editable Install (Development Only)

    pip install -e .
    ato --help

---

## ▶️ Usage

### Example Run

    ato --base-url https://app.example.com \
        --policy policies/example_policy.yaml \
        --run-dir runs/example

- `--base-url`: target under test  
- `--policy`: execution boundaries and limits  
- `--run-dir`: artifact storage  

---

### Output Artifacts

Each run produces:

    evidence.jsonl
    results.json

- `evidence.jsonl`: raw request/response evidence  
- `results.json`: structured execution outcomes  

---

## 🔗 References and Validation Context

The references below are included to make the problem space explicit and auditable.

They describe the class of proof-of-concept automation and claims that ATO is designed to validate under commercial QA guardrails.

### Automated / AI-Assisted Exploitation Claims

- Ethiack – MoltBot “One-Click RCE”  
  https://ethiack.com/news/blog/one-click-rce-moltbot

- Ethiack – Hackian: An AI Agent That Can Hack  
  https://blog.ethiack.com/blog/introducing-the-hackian-an-ai-agent-that-can-hack

- Ethiack Research Blog  
  https://ethiack.com/blog

These demonstrations typically assume:
- local execution context  
- implicit authorization  
- permissive runtime environments  
- limited operational constraints  

ATO exists to test whether those assumptions survive commercial QA standards.

---

### Security Engineering and Industry Context

- OWASP Top Ten  
  https://owasp.org/www-project-top-ten/

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework

- SANS Institute Research  
  https://www.sans.org/blog

- Dark Reading – Enterprise Security Analysis  
  https://www.darkreading.com/attacks-breaches

---

### Research Ethics and Responsible Engineering

- ACM Code of Ethics  
  https://www.acm.org/code-of-ethics

- Black Hat Conference Archives  
  https://www.blackhat.com

These references reinforce that automation claims must be testable, observable, documented, and reviewable.

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
