# Agentic AI Anti-Money Laundering (AML) System

A Python and Streamlit project that demonstrates rule-based transaction monitoring, suspicious-pattern flagging, and risk categorisation for sample financial transactions.

## Overview

The system reads a sample transaction dataset, checks each transaction against configurable rules, assigns a risk score, and displays the results in an interactive dashboard. It is intended as a learning prototype for understanding basic AML transaction-monitoring concepts.

## Workflow

```text
Sample Transaction Dataset (CSV)
              |
              v
     AML Detection Agent
              |
              v
       AML Rule Checks
              |
              v
      Risk Score Calculation
              |
              v
       Risk Level Assignment
       Low / Medium / High
              |
              v
      AML Workflow Summary
              |
              v
       Streamlit Dashboard
```

## Features

- Loads transaction records from a CSV file
- Checks transaction amount, same-day transaction activity, unusual amounts, and country
- Adds rule-based flags to transactions
- Calculates a demonstration risk score
- Categorises transactions as Low, Medium, or High risk
- Displays transaction details and a separate high-risk transaction table
- Shows summary metrics for total, suspicious, and high-risk transactions

## Technology Stack

- Python
- Pandas
- Streamlit
- CSV-based sample data
- Rule-based transaction screening

## Project Structure

```text
Agentic_AI_AML_System/
|
+-- agents/
|   +-- __init__.py
|   +-- aml_detection_agent.py
|
+-- config/
|   +-- __init__.py
|   +-- settings.py
|
+-- data/
|   +-- transactions.csv
|
+-- outputs/
|
+-- tools/
|   +-- __init__.py
|   +-- aml_rules.py
|
+-- app.py
+-- workflow.py
+-- requirements.txt
+-- README.md
+-- .gitignore
```

## Components

| File | Responsibility |
|---|---|
| `app.py` | Streamlit dashboard and summary metrics |
| `workflow.py` | Runs the AML detection process and returns all, suspicious, and high-risk transaction sets |
| `agents/aml_detection_agent.py` | Loads the CSV and applies rule checks to each transaction |
| `tools/aml_rules.py` | Contains rule checks, risk-score calculation, and risk-level assignment |
| `config/settings.py` | Contains app settings and AML threshold values |
| `data/transactions.csv` | Synthetic sample transaction dataset |
| `requirements.txt` | Python package dependencies |

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/harshaharshu09/Agentic_AI_AML_System.git
cd Agentic_AI_AML_System
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Install dependencies

On Windows, if PowerShell blocks environment activation, you can use the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Run the command-line workflow

```powershell
python workflow.py
```

### 5. Run the dashboard

```powershell
python -m streamlit run app.py
```

## Understanding the Results

The dashboard displays:

- **Total Transactions:** Number of rows screened from the CSV file
- **Suspicious Transactions:** Transactions with a non-zero rule-based risk score
- **High Risk Transactions:** Transactions whose score reaches the configured High-risk band
- **Transaction Risk Analysis:** The score, risk level, and rule flags for each transaction

The sample dataset is synthetic. Results depend on the rules and thresholds implemented in the current code.

## Important Limitations

- This is a rule-based educational prototype; it does not use an external LLM or a trained AML machine-learning model.
- The sample records are synthetic and do not represent real customers or real financial activity.
- A high-risk flag is only a prompt for further review, not proof of money laundering or criminal activity.
- Country-based flags and scoring thresholds are simplified demonstration choices, not regulatory determinations.
- The project is not connected to banks, payment networks, sanctions lists, politically exposed person databases, or regulatory reporting systems.
- The system must not be used for real compliance decisions without validation, governance, privacy controls, and expert review.

## Future Improvements

- Add transaction filtering and search
- Add risk-distribution charts and customer-level summaries
- Add tests for individual AML rules and risk-score boundaries
- Improve time-window and customer-baseline analysis
- Add a case-review queue and audit trail
- Explore validated anomaly-detection methods and explainable alerts
- Add approved reference-data sources where legally and operationally appropriate

## Author

**KN Harsha Vardhan Kumar**

GitHub: https://github.com/harshaharshu09
