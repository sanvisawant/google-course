def severity_calculator(symptoms: list[str]) -> dict:
    """
    Calculates a numerical severity score (0–10) based on the symptoms provided.

    This tool assigns weights to symptoms and computes an overall risk score.
    It helps the RiskScorerAgent decide urgency levels.

    Args:
        symptoms: A list of symptoms as strings. Example:
                  ["fever", "joint pain"]

    Returns:
        Success:
            {
                "status": "success",
                "data": {
                    "score": 7,
                    "urgency": "high",
                    "reasoning": "Multiple high-weight symptoms detected"
                }
            }

        Error:
            {
                "status": "error",
                "error_message": "Invalid or empty symptom list"
            }
    """

    if not symptoms or not isinstance(symptoms, list):
        return {
            "status": "error",
            "error_message": "Invalid or empty symptom list"
        }

    # Weight mapping (simple demo)
    weights = {
        "fever": 3,
        "joint pain": 3,
        "headache": 1,
        "fatigue": 2,
        "cough": 1
    }

    total = 0
    used_symptoms = []

    for s in symptoms:
        s_lower = s.lower().strip()
        if s_lower in weights:
            used_symptoms.append(s_lower)
            total += weights[s_lower]

    if not used_symptoms:
        return {
            "status": "error",
            "error_message": "No known symptom weights found"
        }

    # Determine urgency
    if total >= 7:
        urgency = "high"
    elif total >= 3:
        urgency = "moderate"
    else:
        urgency = "low"

    return {
        "status": "success",
        "data": {
            "score": total,
            "urgency": urgency,
            "reasoning": f"Symptoms analyzed: {', '.join(used_symptoms)}"
        }
    }
