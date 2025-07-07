def apply_rules(app, score):
    if "income" not in app or app["income"] is None:
        return "Request More Info", "Missing income information"

    if score < 0.3:
        return "Accept", "Low risk score"
    elif score < 0.6:
        return "Request More Info", "Moderate risk"
    else:
        return "Reject", "High risk score"
