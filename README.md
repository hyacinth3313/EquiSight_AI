EquiSight AI — Loan Fairness Auditor ⚖️
EquiSight AI is an automated fairness auditing tool designed to identify and mitigate algorithmic bias in financial lending. Developed for the Google Solution Challenge 2026, this project aligns with UN Sustainable Development Goal 10: Reduced Inequalities.

🚀 The Problem
Machine learning models in finance often inherit historical human biases. Our analysis of sample datasets revealed significant disparity gaps, such as a 60-percentage-point difference in approval rates between demographics.

✨ Features
Automated Bias Detection: Performs disparate impact analysis on loan datasets.

Gemini-Powered Insights: Uses Google Gemini to analyze statistical gaps and provide plain-language fairness warnings.

Algorithmic Mitigation: Implements reweighing strategies to balance approval rates across groups (e.g., correcting an 80/20 split to a fair 50/50).

Audit-Ready Exports: Generates sanitized CSV files for training fair machine learning models.

🛠️ Tech Stack
Backend: Django (Python)

Frontend: HTML5, CSS3 (Glassmorphism UI), Google Charts

Authentication: Firebase Google Auth

AI Engine: Google Gemini API

📦Installation & Setup
Clone the repo: git clone [https://github.com/your-username/EquiSight_AI.git](https://github.com/your-username/EquiSight_AI.git)

Install dependencies: pip install -r requirements.txt

Run Migrations: python manage.py migrate

Start Server: python manage.py runserver

Access: Navigate to 127.0.0.1:8000