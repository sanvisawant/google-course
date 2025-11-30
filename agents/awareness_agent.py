# agents/awareness_agent.py
from tools.health_tips import health_tips
from typing import Dict, Any
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search, AgentTool, ToolContext

awareness_agent = LlmAgent (
    name="awareness_agent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction=
    """
    You are a smart awareness information generator agent.
    Your job:
    1. take the classified symptoms from the symptom classifier agent.
    2. combine with outbreak information (if any) to generate a user-friendly awareness message.
    3. provide general health tips related to the symptoms using the health tips tool.

    Rules:
    1. Do NOT provide any medical diagnoses.
    2. Focus on general awareness and preventive measures.
    3. Use bullet points for clarity where appropriate.
    4. keep tone simple and easy to understand
    """
)

def build_awareness_payload(symptom_payload: Dict[str, Any], outbreak_info=None) -> Dict[str, Any]:
    """
    This wrapper prepares the structured input that will be sent to the LLM.
    """

    symptoms = symptom_payload.get("symptoms", [])

    # Base awareness text (LLM will expand this)
    lines = []

    lines.append(
        f"You mentioned: {', '.join(symptoms)}.\n"
        "Here is general awareness information (NOT a diagnosis):"
    )

    # Simple symptom-based awareness hints
    if "fever" in symptoms:
        lines.append("• Fever may be caused by viral infections or seasonal illnesses.")
    if "cough" in symptoms:
        lines.append("• Cough can be linked to common cold, viral infections, or air quality issues.")
    if "headache" in symptoms:
        lines.append("• Headache often appears in dehydration, stress, or viral infections.")
    if "fatigue" in symptoms:
        lines.append("• Fatigue may arise from overexertion or seasonal viral illness.")

    # Outbreak info
    if outbreak_info:
        lines.append("\nRecent health updates from trusted sources:")
        for item in outbreak_info:
            lines.append(f"• {item}")

    # Health tips (tool)
    tips = get_health_tips("general")["data"]["tips"]

    # Send this to your LLM agent
    return {
        "message_seed": "\n".join(lines),
        "bullet_points": tips
    }


def awareness_agent_run(symptom_payload: Dict[str, Any], outbreak_info=None) -> Dict[str, Any]:
    """
    - Builds prompt for LLM agent
    - Runs LLM
    - Returns clean structured dict
    """

    payload = build_awareness_payload(symptom_payload, outbreak_info)

    llm_response = awareness_agent(
        {
            "symptoms": symptom_payload.get("symptoms", []),
            "draft_message": payload["message_seed"],
            "tips": payload["bullet_points"],
        }
    )

    return {
        "message": llm_response,       # Final LLM-generated awareness text
        "bullet_points": payload["bullet_points"]
    }