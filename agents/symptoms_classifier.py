from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search, AgentTool, ToolContext


symptom_classifier_agent = LlmAgent(
    name="symptom_classifier_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""
    You are a smart symptom classification assistant.

   Your job:
    1. Read the user's free-text symptom description.
    2. Extract a cleaned list of symptoms, durations, intensity words and any numeric values (e.g., "103 F", "2 days").
    3. Output ONLY JSON in this format:

{
  "symptoms": ["fever","headache"],
  "durations": {"fever": "2 days"},
  "intensity": {"fever": "high"},
  "raw_text": "<original user text>"
}


    Rules:
    - Do NOT invent symptoms not present in the user's text.
    - If uncertain about duration or intensity, use null or omit the key.
    """,
    
)


