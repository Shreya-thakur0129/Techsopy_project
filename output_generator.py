def generate_output(app, decision, reason, score):
    return {
        "application_id": app.get("id"),
        "risk_score": score,
        "decision": decision,
        "reason": reason
    }
