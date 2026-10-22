import pandas as pd
from tools.aml_rules import analyze_transaction, calculate_risk_score, get_risk_level


class AMLDetectionAgent:

    def __init__(self, data_path="data/transactions.csv"):
        self.data_path = data_path

    def run(self):
        df = pd.read_csv(self.data_path)

        results = []

        for _, transaction in df.iterrows():

            customer_transactions = df[
                df["customer_id"] == transaction["customer_id"]
            ]

            flags = analyze_transaction(
                transaction,
                customer_transactions
            )

            risk_score = calculate_risk_score(flags)
            risk_level = get_risk_level(risk_score)

            results.append({
                "transaction_id": transaction["transaction_id"],
                "customer_id": transaction["customer_id"],
                "amount": transaction["amount"],
                "country": transaction["country"],
                "risk_score": risk_score,
                "risk_level": risk_level,
                "flags": ", ".join(flags) if flags else "No suspicious activity"
            })

        return pd.DataFrame(results)
