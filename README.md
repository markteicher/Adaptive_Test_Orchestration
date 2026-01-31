# Adaptive Test Orchestration (ATO)

Adaptive Test Orchestration is a policy-governed system designed to evaluate security posture through controlled, auditable execution of approved tests.

Recent demonstrations of automated or AI-assisted exploitation highlight how quickly known techniques can be chained when guardrails are absent. In practice, these demonstrations rely on constrained environments, local execution context, and pre-existing access rather than autonomous, general-purpose exploitation.

ATO is intentionally designed to operate in the opposite direction: bounded by explicit policy, limited by global execution controls, and fully observable at every step. The goal is not autonomous exploitation, but disciplined, repeatable testing that reflects real-world constraints and enterprise authorization requirements.

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-yellow.svg)

---

## ✨ Capabilities

- 🔒 **Policy Enforcement**
  - Execution requires an explicit policy file; ATO will not run without one.
  - Policies define:
    - Allowed hosts or domains
    - Allowed schemes (`http`, `https`)
    - Permitted HTTP methods
    - Allowed URL path prefixes
    - Maximum total request count for the entire run
    - Maximum global request rate across all modules
  - Policy checks are enforced before **every** request.
  - Any policy violation immediately halts execution and is recorded as evidence.

- 🔁 **Test Orchestration**
  - Test modules execute in a deterministic, centrally controlled sequence.
  - Modules cannot expand scope, trigger other modules, or bypass limits.
  - Execution flow is decided exclusively by the orchestrator based on observed results.

- 🧾 **Evidence Collection**
  - Every request and response is captured in full.
  - Evidence includes timestamps, module attribution, request details, and response details.
  - Evidence is written during execution, not reconstructed post-run.

- ♻️ **Reproducibility**
  - Identical inputs (policy, target, version) produce identical execution behavior.
  - Enables audit, validation, regression testing, and peer review.

---

## 📁 Repository Structure

    ato/
      pyproject.toml
      README.md
      ato/
        __init__.py
        cli.py
        policy.py
        budget.py
        evidence.py
        orchestrator.py
        http_client.py
        modules/
          __init__.py
          base.py
          http_basic_probe.py
          headers_checks.py
      policies/
        example_policy.yaml
      runs/
        .gitkeep

---

## 🧩 Python Libraries

All dependencies are declared explicitly in `pyproject.toml`.

- **requests**
  - Used for all HTTP and HTTPS request execution.
- **PyYAML**
  - Used to load and validate YAML policy configuration files.

No dynamic or implicit dependency loading occurs at runtime.

---

## 📦 Installation

Follow all steps exactly as written. Do not skip steps.

### 1) Verify Python Version

ATO requires **Python 3.10 or newer**.

    python --version
    python3 --version

The reported version must be 3.10 or higher before proceeding.

---

### 2) Verify pip

Ensure `pip` is available and bound to the same Python interpreter.

    pip --version

Fix pip before continuing if this command fails.

---

### 3) Confirm Repository Root

All installation commands must be run from the directory containing `pyproject.toml`.

    ls pyproject.toml

Do not proceed if the file is not present.

---

### 4) Create a Virtual Environment

    python -m venv .venv

This creates an isolated environment in `.venv/`.

---

### 5) Activate the Virtual Environment

Linux / macOS:

    source .venv/bin/activate

Windows (PowerShell):

    .venv\Scripts\Activate.ps1

Verify:

    python --version
    which python
    where python

The path must reference `.venv`.

---

### 6) Upgrade Packaging Tools

    pip install --upgrade pip setuptools wheel
    pip --version

---

### 7) Install ATO

    pip install .

This installs all dependencies, builds the package, and registers the `ato` CLI.

---

### 8) Verify Installation

    ato --help

Help output must display without error.

---

### 9) Editable Installation (Development Only)

    pip install -e .
    ato --help

---

## ▶️ Usage

### Basic Execution

    ato --base-url https://app.example.com \
        --policy policies/example_policy.yaml \
        --run-dir runs/example

- `--base-url` defines the target system.
- `--policy` defines scope and execution limits.
- `--run-dir` defines where evidence and results are written.

---

### Output Artifacts

Each run directory contains:

    evidence.jsonl
    results.json

- `evidence.jsonl` contains full request/response evidence.
- `results.json` contains structured execution outcomes.

---

## 🔗 References & Context

The following references provide context for the automation and AI-assisted exploitation claims that ATO intentionally approaches with explicit controls and auditability:

- https://ethiack.com/news/blog/one-click-rce-moltbot
- https://blog.ethiack.com/blog/introducing-the-hackian-an-ai-agent-that-can-hack
- https://ethiack.com/research
- https://ethiack.com/blog
- https://www.darkreading.com/attacks-breaches
- https://www.sans.org/blog
- https://owasp.org/www-project-top-ten/
- https://www.nist.gov/cyberframework
- https://www.blackhat.com
- https://www.acm.org/code-of-ethics

These references are provided for technical grounding and comparison only.

---

## 🚧 Project Status

ATO is under active development.

Current functionality includes:
- Explicit policy enforcement
- Global request budgeting and rate limiting
- Deterministic test orchestration
- Full evidence capture

---

## 📄 License

MIT License
