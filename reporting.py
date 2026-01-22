import sqlite3
from datetime import datetime

def generate_report():
    with sqlite3.connect("iocs.db") as conn:
        total = conn.execute("SELECT COUNT(*) FROM iocs").fetchone()[0]
        high = conn.execute(
            "SELECT COUNT(*) FROM iocs WHERE severity='High'"
        ).fetchone()[0]

    report = f"""
SOC Threat Intelligence Report
Generated: {datetime.utcnow().isoformat()}

Total IOCs: {total}
High Severity IOCs: {high}
"""

    with open("C:\\Users\\bashp\\OneDrive\\Desktop\\threat-intel-aggregator\\output\\reports\\soc_report.txt", "w") as f:
        f.write(report)
