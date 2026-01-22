from src.ingestion import fetch_feed
from src.parsing import parse_iocs
from src.normalization import normalize
from src.persistence import init_db, upsert_ioc
from src.blocklists import generate_blocklists
from src.reporting import generate_report
from src.scheduler import run_forever

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
feeds_path = os.path.join(BASE_DIR, "feeds", "osint_urls.txt")

with open(feeds_path, "r") as f:
    FEEDS = f.read().splitlines()



init_db()

def pipeline():
    for url in FEEDS:
        data = fetch_feed(url)
        for indicator, ioc_type in parse_iocs(data):
            meta = normalize(None, url)
            upsert_ioc(indicator, ioc_type, meta)

    generate_blocklists()
    generate_report()

run_forever(pipeline, interval=300)
