import pandas as pd
from agents.aml_detection_agent import AMLDetectionAgent


class AMLWorkflow:

    def __init__(self):
        self.agent = AMLDetectionAgent()

    def run(self):
        results = self.agent.run()

        suspicious = results[
            results["risk_level"].isin(["Medium", "High"])
        ].copy()

        high_risk = results[
            results["risk_level"] == "High"
        ].copy()

        return {
            "all_transactions": results,
            "suspicious_transactions": suspicious,
            "high_risk_transactions": high_risk
        }


if __name__ == "__main__":
    workflow = AMLWorkflow()

    output = workflow.run()

    print("\nAML WORKFLOW COMPLETED")
    print("-" * 50)

    print(f"Total Transactions : {len(output['all_transactions'])}")
    print(f"Suspicious         : {len(output['suspicious_transactions'])}")
    print(f"High Risk          : {len(output['high_risk_transactions'])}")

    print("\nHigh Risk Transactions:")
    print(output["high_risk_transactions"].to_string(index=False))
