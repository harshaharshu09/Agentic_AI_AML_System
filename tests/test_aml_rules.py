import unittest

import pandas as pd

from tools.aml_rules import (
    analyze_transaction,
    calculate_risk_score,
    check_high_value,
    check_international_transaction,
    check_rapid_transactions,
    check_unusual_amount,
    get_risk_level,
)


class AMLRulesTests(unittest.TestCase):
    def test_high_value_threshold(self):
        self.assertTrue(check_high_value(pd.Series({"amount": 100000})))
        self.assertFalse(check_high_value(pd.Series({"amount": 99999})))

    def test_rapid_same_day_pattern(self):
        transactions = pd.DataFrame(
            {
                "transaction_id": ["TXN001", "TXN002", "TXN003"],
                "transaction_date": ["2026-10-01"] * 3,
                "amount": [10000, 12000, 14000],
            }
        )
        self.assertTrue(check_rapid_transactions(transactions.iloc[0], transactions))

    def test_unusual_amount_against_other_customer_transactions(self):
        transactions = pd.DataFrame(
            {
                "transaction_id": ["TXN001", "TXN002"],
                "transaction_date": ["2026-10-01", "2026-10-02"],
                "amount": [10000, 50000],
            }
        )
        self.assertTrue(check_unusual_amount(transactions.iloc[1], transactions))

    def test_international_country_flag(self):
        self.assertTrue(check_international_transaction(pd.Series({"country": "Singapore"})))
        self.assertFalse(check_international_transaction(pd.Series({"country": "India"})))

    def test_combined_risk_score_and_level(self):
        flags = [
            "High Value Transaction",
            "Rapid Transaction Pattern",
            "International Transaction",
        ]
        score = calculate_risk_score(flags)
        self.assertEqual(score, 90)
        self.assertEqual(get_risk_level(score), "High")

    def test_no_flags_is_low_risk(self):
        self.assertEqual(calculate_risk_score([]), 0)
        self.assertEqual(get_risk_level(0), "Low")


if __name__ == "__main__":
    unittest.main()
