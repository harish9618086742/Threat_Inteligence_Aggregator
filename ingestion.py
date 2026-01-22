import requests
import logging

logging.basicConfig(
    filename="logs/ti_aggregator.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def fetch_feed(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        logging.info(f"Fetched feed: {url}")
        return r.text
    except Exception as e:
        logging.error(f"Failed to fetch {url}: {e}")
        return ""
