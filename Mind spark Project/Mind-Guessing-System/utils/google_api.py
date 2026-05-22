import requests, urllib.parse
from config import GOOGLE_API_KEY, GOOGLE_CX, BLOCKED_DOMAINS

def fetch_google_image(query_name):
    q = urllib.parse.quote_plus(query_name)
    url = f"https://www.googleapis.com/customsearch/v1?q={q}&cx={GOOGLE_CX}&key={GOOGLE_API_KEY}&searchType=image&num=10"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()

        for item in data.get("items", []):
            link = item.get("link", "")
            if not any(bad in link for bad in BLOCKED_DOMAINS):
                return link
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
    except Exception as e:
        print("Error fetching Google image:", e)
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
