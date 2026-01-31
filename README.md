# Adaptive Test Orchestration (ATO)
Adaptive Test Orchestration is a policy-governed system that sequences approved security tests based on observed results and evidence, without autonomous exploit generation.

# Adaptive Test Orchestration (ATO)

Adaptive Test Orchestration is a policy-governed system that sequences approved security tests based on observed results and evidence, without autonomous exploit generation.

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-yellow.svg)

---

## ✨ Capabilities

- 🔒 **Policy Enforcement**
  - Requires an explicit policy file for execution
  - Enforces allowed hosts, schemes, HTTP methods, and path prefixes
  - Enforces global request budgets and rate limiting
  - Stops execution when policy boundaries are violated

- 🔁 **Test Orchestration**
  - Executes approved test modules in a controlled sequence
  - Uses observed results to determine which approved module runs next
  - Centralizes orchestration logic (modules do not self-expand scope)

- 🧾 **Evidence Collection**
  - Captures request and response evidence for executed tests
  - Timestamps and associates evidence with the responsible module
  - Writes run artifacts to the specified output directory

- ♻️ **Reproducibility**
  - Deterministic behavior given the same inputs (policy, target, version)
  - Consistent boundaries, request limits, and execution flow per run

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

ATO installs dependencies from `pyproject.toml`. Key runtime libraries include:

- **requests**
  - Used for HTTP/HTTPS request execution inside approved test modules
- **PyYAML**
  - Used to load and validate YAML policy files

---

## 📦 Installation

Follow these steps in order. Do not skip steps.

### 1) Verify Python Version (Required)

ATO requires Python **3.10+**.

Run:

    python --version

If multiple Python versions are installed, also run:

    python3 --version

If the version is below 3.10, install/activate a supported Python version before continuing.

---

### 2) Verify pip (Required)

Run:

    pip --version

If this fails, fix pip for your active Python installation before continuing.

---

### 3) Confirm Repository Root (Required)

All install commands must be run from the directory that contains `pyproject.toml`.

Confirm `pyproject.toml` exists in your current working directory before proceeding.

---

### 4) Create a Virtual Environment (Required)

From the repository root:

    python -m venv .venv

This creates an isolated environment in `.venv/`.

---

### 5) Activate the Virtual Environment (Required)

Linux / macOS:

    source .venv/bin/activate

Windows (PowerShell):

    .venv\Scripts\Activate.ps1

Verify that the active Python belongs to the virtual environment:

    python --version

(Optional verification)

Linux / macOS:

    which python

Windows:

    where python

The path should reference `.venv`.

---

### 6) Upgrade Packaging Tools (Required)

Inside the activated virtual environment:

    pip install --upgrade
