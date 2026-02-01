# 🧪 Adaptive Test Orchestration (ATO)

Adaptive Test Orchestration (ATO) is a Python based test harness whose purpose is to **verify whether proof-of-concept automated exploitation code actually works when subjected to real, commercial-grade software and security standards**.

In recent years, multiple demonstrations have claimed that automated tools or “AI agents” can perform complex exploitation with minimal human involvement. 

These demonstrations often show impressive results in controlled environments. 

However, they typically depend on assumptions that do not exist in real organizations, such as unrestricted execution, implicit authorization, unlimited retries, permissive networking, and undocumented behavior.

![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active%20development-yellow.svg)


---

## ✨ Capabilities

### 🔒 Commercial Guardrails Applied

Applies constraints expected of production-grade software.

- **Explicit scope**
  - A target base URL must be provided.
  - Execution is limited to that declared target.


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


---

### 🔁 Orchestration and Execution Model


## Each defined module:
- receives a constrained execution context
- performs only its defined behavior
- returns structured results

## Orchestrator:
- controls execution order
- enforces shared limits
- decides whether execution continues

---

### 🧾 Evidence and Observability

Records and Logs all activity.

For every request, the test harness captures:
- the time the request occurred
- which module issued the request
- the HTTP method and URL
- request data when present
- the full response returned

---

### ♻️ Reproducibility

If the following remain unchanged:
- the code version
- the configuration
- the target

Then execution behavior remains consistent.

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


The following steps describe how to prepare an environment and install ATO.
Verify all prerequisites depending on the operating system.

1. **Verify Python version**
from the command line or terminal

       python --version
       python3 --version

   Python 3.10 or newer is required.

3. **Verify pip**

       pip --version

4. **Confirm repository root**

       ls pyproject.toml

5. **Create a virtual environment**

       python -m venv .venv

6. **Activate the environment**

   Linux / macOS:

       source .venv/bin/activate

   Windows:

       .venv\Scripts\Activate.ps1

7. **Upgrade packaging tools**

       pip install --upgrade pip setuptools wheel

8. **Install ATO**

       pip install .

9. **Verify installation**

       ato --help

10. **Editable install (development use only)**

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

## 🔗 References

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

### 🛡️ Security Engineering

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


---

## 📄 License

MIT License
