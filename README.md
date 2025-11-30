**Problem Statement:**
In our daily lives, we often ignore small symptoms such as cough, cold, or mild fever, dismissing them as insignificant. However, these minor signs can sometimes be early indicators of more serious health conditions or ongoing outbreaks in our surroundings.
The lack of awareness about diseases around us can lead to delayed action and missed opportunities for prevention.
This project addresses that gap by providing an awareness agent that:
- Helps users understand possible diseases based on their symptoms
- Checks if there is an outbreak in their city
- Suggests basic home remedies for mild symptoms<br>
⚠️ Disclaimer: This system is intended for awareness and educational purposes only. It does not provide any type of Medical Diagnosis.

**Solution:**
This project implements a Disease Awareness Agent designed to help users understand potential health risks based on their input symptoms.
- 🩺 Symptom Analysis: The agent takes user-provided symptoms and suggests possible diseases.
- 🌍 Outbreak Detection: It checks whether there is an ongoing outbreak in the user’s city, providing timely awareness.
- 🏠 Home Remedies: Alongside disease information, the agent offers simple, general home remedy tips to help users manage mild symptoms.<br>
The goal is to increase public health awareness by combining symptom-based guidance, outbreak monitoring, and practical advice in one system using relevant and trusted resources only.

**Project Architecture**:
This project is a multi-agent Disease awareness system built using Google ADK (AI Development Kit) and Gemini models.
The system accepts a user's symptoms, classifies them, gathers outbreak info, provides general health awareness (not diagnosis), and evaluates its own response quality.
This project demonstrates the major concepts taught in the course:
1. Multi-Agent Cooperation
2. Sequential Agent Pipelines
3. Tools & MCP Tooling
4. Google Search Integration
5. In-Memory Session State
6. ADK Runner Execution
7. LLM-powered agents
8. Context engineering
9. Automated Evaluation Agent<br>
The goal is to build a safe, informative health assistant that provides:
-Symptom awareness
-General precautions
-Home remedies
-Outbreak alerts (via search tool)
-Safety-checked responses
-No medical advice or diagnosis is given.

**Workflow**:
Below is the behavioral flow of the system:
User → Symptom Classifier Agent → Outbreak Agent → Awareness Agent → Evaluation Agent → Final Answer

**Architecture Diagram**:

**Agents Used**:
1. Symptoms Classifier Agent : Clean, normalize and categorize symptoms
2. Outbreak Agent : Ask user city → Google Search → extract disease alerts
3. Awareness Agent : Generate awareness, home remedies, precautions
4. Evaluation Agent : Evaluate correctness, safety & completeness<br>
Each agent is implemented as an LlmAgent in ADK.

**Conclusion:**
This project showcases how Gemini-powered, tool-augmented multi-agent systems can be used for socially beneficial applications such as public health awareness.
By integrating sequential agents, Google Search tools, in-memory session state, and evaluation frameworks, the system demonstrates the practical application of modern LLM architectures using Google ADK.

