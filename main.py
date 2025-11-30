import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search, AgentTool, ToolContext

# 1. AUTHENTICATION SETUP
try:
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found. Add it to .env.")

    print("✅ Setup and authentication complete.")
except Exception as e:
    print(f"🔑 Authentication Error: {e}")

# 2. IMPORT AGENTS + MEMORY
from memory.sessions_memory import InMemorySessionService
from agents.symptoms_classifier import symptom_classifier_agent
from agents.outbreak_agent import outbreak_agent
from agents.awareness_agent import awareness_agent
from agents.evaluation import evaluation_agent

# 3. MEMORY INSTANCE (if used inside agent logic)
session = InMemorySessionService()

# 4. PIPELINE FUNCTION (Sequential Multi-Agent Flow)
def run_pipeline(user_input: str):

    print("\n🔍 Step 1: Classifying symptoms...")
    classified = symptom_classifier_agent.run_llm(user_message=user_input)
    symptoms = classified.output.get("symptoms", [])
    print("Symptoms →", symptoms)

    print("\n🌍 Step 2: Asking city for outbreak search")
    city = input("Enter your city: ")

    print("\n📢 Step 3: Fetching outbreak info...")
    outbreak = outbreak_agent.run_llm(city=city)
    outbreak_info = outbreak.output.get("outbreak_info", [])
    print("Outbreak info →", outbreak_info)

    print("\n💡 Step 4: Awareness generation...")
    awareness = awareness_agent.run_llm(
        symptoms=symptoms,
        outbreak_info=outbreak_info
    )
    final_response = awareness.output_text
    print("\n=== FINAL AWARENESS MESSAGE ===")
    print(final_response)

    print("\n📝 Step 5: Evaluating system output...")
    evaluation = evaluation_agent.run_llm(
        user_query=user_input,
        agent_response=final_response
    )

    print("\n=== SYSTEM EVALUATION ===")
    print(evaluation.output_text)

# 5. START PROGRAM
if __name__ == "__main__":
    print("\n🤖 Health Awareness Multi-Agent System")
    user_msg = input("\nDescribe your symptoms: ")

    run_pipeline(user_msg)
