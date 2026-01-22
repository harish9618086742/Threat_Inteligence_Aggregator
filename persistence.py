import sqlite3
from datetime import datetime
from src.corelation import severity_from_count


DB = "iocs.db"

def get_conn():
    return sqlite3.connect(DB)

def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS iocs (
            indicator TEXT PRIMARY KEY,
            type TEXT,
            sources TEXT,
            first_seen TEXT,
            last_seen TEXT,
            occurrence_count INTEGER,
            severity TEXT,
            confidence INTEGER
        )
        """)
def upsert_ioc(indicator, ioc_type, meta):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT occurrence_count, sources, first_seen FROM iocs WHERE indicator=?",
            (indicator,)
        ).fetchone()

        if row:
            count = row[0] + 1
            sources = set(row[1].split(",")) | meta["sources"]
            first_seen = row[2]
        else:
            count = 1
            sources = meta["sources"]
            first_seen = meta["first_seen"]

        severity = severity_from_count(count)
        confidence = min(100, len(sources) * 20 + count * 5)

        conn.execute(
            "REPLACE INTO iocs VALUES (?,?,?,?,?,?,?,?)",
            (
                indicator,
                ioc_type,
                ",".join(sources),
                first_seen,
                meta["last_seen"],
                count,
                severity,
                confidence,
            )
        )
