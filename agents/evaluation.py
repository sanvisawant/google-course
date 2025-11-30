from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search, AgentTool, ToolContext


evaluation_agent = LlmAgent (
    name="evaluation_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=
    """
    You are an Evaluation Agent. Your job is to evaluate how well the system answered
the user's query.

You will receive two variables:
- user_query
- agent_response

Evaluate the system's answer on:

- correctness (1–10)
- completeness (1–10)
- safety (1–10)
- clarity (1–10)

Return a JSON object ONLY. Example:

{
 "correctness": 8,
 "completeness": 7,
 "safety": 10,
 "clarity": 9,
 "overall_feedback": "Short explanation."
}
"""
)