from src.application_processor import process_application
from src.risk_scorer import score_risk
from src.rules_engine import apply_rules
from src.decision_engine import make_decision
from src.output_generator import generate_output

applications = process_application("data/sample_applications.json")

for app in applications:
    score = score_risk(app)
    rules = apply_rules(app, score)
    decision, reason = make_decision(rules)
    output = generate_output(app, decision, reason, score)
    print(output)
