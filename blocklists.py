import os
import sqlite3
from datetime import date

def generate_blocklists():
    os.makedirs("output/blocklists", exist_ok=True)

    with sqlite3.connect("iocs.db") as conn:
        rows = conn.execute("""
        SELECT indicator, type FROM iocs
        WHERE severity IN ('High','Medium')
        """).fetchall()

    by_type = {}
    for ind, t in rows:
        by_type.setdefault(t, []).append(ind)

    for t, indicators in by_type.items():
        filename = f"C:\\Users\\bashp\\OneDrive\\Desktop\\threat-intel-aggregator\\output\\blocklists\\{t}_blocklist_{date.today()}.txt"

        with open(filename, "w") as f:
            f.write("\n".join(indicators))
