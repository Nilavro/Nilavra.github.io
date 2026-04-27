from __future__ import annotations
import json, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

QUERIES = [
    "computational marketing machine learning",
    "dynamic regret reinforcement learning",
    "marketing budget allocation machine learning",
    "energy economics data centers smart cities",
    "ad auctions reinforcement learning",
]
OUTPUT = Path("data/research_news.json")

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()

def parse_date(raw):
    if not raw:
        return ""
    try:
        return parsedate_to_datetime(raw).date().isoformat()
    except Exception:
        return ""

def fetch_google_news_rss(query):
    encoded = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded}&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as response:
        xml_data = response.read()
    root = ET.fromstring(xml_data)
    items = []
    for item in root.findall(".//item")[:5]:
        title = clean_text(item.findtext("title"))
        link = item.findtext("link") or ""
        pub_date = parse_date(item.findtext("pubDate"))
        summary = clean_text(item.findtext("description"))
        if title and link:
            items.append({"title":title,"link":link,"source":"Google News RSS","date":pub_date,"summary":summary[:240],"query":query})
    return items

def main():
    seen, results = set(), []
    for query in QUERIES:
        try:
            for item in fetch_google_news_rss(query):
                key = item["title"].lower()
                if key not in seen:
                    seen.add(key)
                    results.append(item)
        except Exception as exc:
            print(f"Failed query {query!r}: {exc}")
    results.sort(key=lambda x: x.get("date",""), reverse=True)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(results[:20], indent=2), encoding="utf-8")
    print(f"Wrote {min(len(results), 20)} items to {OUTPUT}")

if __name__ == "__main__":
    main()
