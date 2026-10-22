import pandas as pd


def check_high_value(transaction):
    return transaction["amount"] >= 100000


def check_rapid_transactions(transaction, customer_transactions):
    same_day_count = len(
        customer_transactions[
            customer_transactions["transaction_date"]
            == transaction["transaction_date"]
        ]
    )
    return same_day_count >= 3


def check_unusual_amount(transaction, customer_transactions):
    if len(customer_transactions) <= 1:
        return False

    previous_transactions = customer_transactions[
        customer_transactions["transaction_id"]
        != transaction["transaction_id"]
    ]

    if previous_transactions.empty:
        return False

    customer_average = previous_transactions["amount"].mean()

    return (
        customer_average > 0
        and transaction["amount"] >= customer_average * 3
    )


def check_international_transaction(transaction):
    return transaction["country"] != "India"


def analyze_transaction(transaction, customer_transactions):
    flags = []

    if check_high_value(transaction):
        flags.append("High Value Transaction")

    if check_rapid_transactions(
        transaction,
        customer_transactions
    ):
        flags.append("Rapid Transaction Pattern")

    if check_unusual_amount(
        transaction,
        customer_transactions
    ):
        flags.append("Unusual Transaction Amount")

    if check_international_transaction(transaction):
        flags.append("International Transaction")

    return flags


def calculate_risk_score(flags):
    score = 0

    if "High Value Transaction" in flags:
        score += 35

    if "Rapid Transaction Pattern" in flags:
        score += 30

    if "Unusual Transaction Amount" in flags:
        score += 25

    if "International Transaction" in flags:
        score += 25

    return min(score, 100)


def get_risk_level(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"
