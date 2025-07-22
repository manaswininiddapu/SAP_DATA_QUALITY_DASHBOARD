AI-Powered SAP Data Quality Checker

Overview:
This project is a low-code AI-assisted tool built using GitHub Copilot, designed to:
•	Automate data validation (nulls, duplicates, invalid formats) on SAP datasets
•	Display results on a Streamlit dashboard for easy visualization

Goal: Speed up SAP data quality checks and reduce manual errors
Domain: SAP Data & Analytics
Tech Stack: Python, Pandas, Streamlit, GitHub Copilot

Execution:
At first, run the requirements.txt file to install all the python libraries using: 
pip install -r requirements.txt
Then, run the following command in your Project Folder
streamlit run app.py

Now, Your browser will automatically open at http://localhost:8501
You’ll see the SAP Data Quality Checker Dashboard.

Finally, Use the Upload SAP Data button
Upload your CSV/Excel file
See null checks, duplicate rows, invalid entries instantly

For rerun: Ctrl + C to stop, then streamlit run app.py again.
