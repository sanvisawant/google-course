from typing import Dict, Any

# A simple wrapper that your Orchestrator will replace with real Google Search tool call.
def fetch_outbreak_info_from_google(city: str) -> Dict[str, Any]:
    """
    Uses built-in Google Search tool to fetch outbreak information.
    The orchestrator must inject the actual search results.
    Args:
        city: Name of the city to search outbreaks for.
    Returns:
        A payload indicating need for Google Search.
    """
    return {
        "status": "need-search",
        "query": f"recent disease outbreaks in {city} site:who.int OR cdc.gov OR ncdc.mohfw.gov.in"
    }
