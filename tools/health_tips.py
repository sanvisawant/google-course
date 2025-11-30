from typing import Dict, Any

def health_tips(symptoms: list[str]) -> dict:
    """
    Provides general health tips based on the symptoms provided.
    Uses built-in google-search tool to fetch relevant health advice.
    This tool does not provide medical diagnoses.
        Args:
        symptoms: A list of symptoms as strings. Example:
                  ["fever", "joint pain"]
        Returns:
         A payload indicating need for Google Search
    """
    return  {
            "status": "need-search",
            "query": "general health tips for symptoms - site:cdc.gov OR site:who.int "
        }          
   