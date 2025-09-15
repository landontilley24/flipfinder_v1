import requests
import os

EBAY_APP_ID = os.getenv("EBAY_APP_ID")

def search_ebay(keyword, limit=5):
    """
    Search eBay items using the Browse API
    """
    url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
    headers = {"Authorization": f"Bearer {EBAY_APP_ID}"}
    params = {"q": keyword, "limit": limit}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        items = []

        for item in data.get("itemSummaries", []):
            items.append({
                "title": item.get("title"),
                "price": item.get("price", {}).get("value"),
                "url": item.get("itemWebUrl")
            })

        return items

    except Exception as e:
        return [{"title": "Error fetching from eBay", "price": "N/A", "url": str(e)}]
