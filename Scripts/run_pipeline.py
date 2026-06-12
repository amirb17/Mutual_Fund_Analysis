# run_pipeline.py

import subprocess

scripts = [
    "1_data_ingestion.py",
    "2_data_cleaning.py",
    "3_EDA_Analysis.py",
    "4_Performance_Analytics.py",
    "6_Advanced Analytics_Risk Metrics.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(["python", script])

print("Pipeline Completed")