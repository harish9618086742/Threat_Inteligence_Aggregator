from datetime import datetime

def normalize(existing, source):
    now = datetime.utcnow().isoformat()

    if existing:
        existing["occurrence_count"] += 1
        existing["last_seen"] = now
        existing["sources"].add(source)
        return existing

    return {
        "sources": {source},
        "first_seen": now,
        "last_seen": now,
        "occurrence_count": 1
    }
