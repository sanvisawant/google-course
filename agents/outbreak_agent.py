from typing import Dict, Any
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search, AgentTool, ToolContext

TRUSTED_DOMAINS = [
    "who.int",
    "ncdc.mohfw.gov.in/"
    "cdc.gov"
]

outbreak_agent = LlmAgent(
    name="symptom_classifier_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=
    """
    You are an Outbreak Information Agent.
    Your job:
    1. Given a city name, search for recent outbreak information using trusted health sources only.
    2. If no trusted information is found, respond with 'no outbreak info'.
    Rules:
    1. ONLY use information from trusted domains: who.int, cdc.gov, ncdc.mohfw.gov.in.
    2. Provide concise summaries of any outbreaks found.
    """
)

def fetch_outbreak_info(symptoms: list, city: str | None) -> Dict[str, Any]:
    """
    Multi-step agent:
    1. Ask user for city if not provided.
    2. Then perform trusted Google Search using the outbreak tool wrapper.
    """
    if not city:
        return {"ask_for_city": True}

    # Build query
    from tools.outbreak_tool import fetch_outbreak_info_from_google
    search_payload = fetch_outbreak_info_from_google(city)

    return search_payload
