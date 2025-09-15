def analyze_item(results):
    if not results:
        return "No results found."

    analysis = []
    for item in results:
        title = item.get("title", "N/A")
        price = item.get("price", "N/A")
        link = item.get("url", "#")
        analysis.append(f"- {title}: ${price} → [View]({link})")

    return "\n".join(analysis)
