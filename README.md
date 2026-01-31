# Adaptive Test Orchestration (ATO)
Adaptive Test Orchestration is a policy-governed system that sequences approved security tests based on observed results and evidence, without autonomous exploit generation.


![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT%202.0-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-yellow.svg)

Adaptive Test Orchestration (ATO) is a policy-governed security testing framework designed to coordinate and execute approved security tests in a controlled, auditable, and repeatable manner.

---

## ✨ Capabilities

- 🔒 **Policy Enforcement**
  - Explicit allowlists for hosts, schemes, HTTP methods, and paths
  - Global request budgets and rate limiting
  - Deterministic execution boundaries

- 🔁 **Test Orchestration**
  - Sequenced execution of approved test modules
  - Signal-based execution flow
  - Centralized orchestration logic

- 🧾 **Evidence Collection**
  - Full request and response capture
  - Timestamped, module-attributed records
  - Run-level artifact generation

- ♻️ **Reproducibility**
  - Deterministic execution model
  - Stable inputs and outputs per run
  - Support for verification and regression workflows

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
          base.py
          http_basic_probe.py
          headers_checks.py
      policies/
        example_policy.yaml
      runs/

---

## 📦 Installation

Install ATO from the repository root:

    pip install .

For development and local iteration:

    pip install -e .

This installs the `ato` CLI entry point.

---

## ▶️ Examples

### Basic execution

Run ATO against a target using an explicit policy file:

    ato --base-url https://app.example.com \
        --policy policies/example_policy.yaml \
        --run-dir runs/example

---

### Using a custom output directory

Store run artifacts in a specific directory:

    ato --base-url https://app.example.com \
        --policy policies/example_policy.yaml \
        --run-dir runs/2026-02-01

---

### Typical run artifacts

Each execution produces the following files in the run directory:

    evidence.jsonl
    results.json

- `evidence.jsonl` contains request and response evidence
- `results.json` contains structured module execution results

## 🚧 Project Status

ATO is under active development.

Current functionality includes:
- Policy enforcement
- Global request budgeting
- Approved module execution
- Evidence capture
- Deterministic orchestration

---

## 📄 License

MIT License 2.0
