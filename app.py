import streamlit as st
import pandas as pd
from workflow import AMLWorkflow

st.set_page_config(
    page_title="AML Transaction Monitoring System",
    page_icon="AML",
    layout="wide"
)

st.title("AML Transaction Monitoring System")
st.write("AI-powered transaction screening and risk analysis")

st.divider()

workflow = AMLWorkflow()
result = workflow.run()

transactions = result["all_transactions"]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Transactions", len(transactions))

with col2:
    st.metric(
        "Suspicious Transactions",
        len(result["suspicious_transactions"])
    )

with col3:
    st.metric(
        "High Risk Transactions",
        len(transactions[transactions["risk_level"] == "High"])
    )

st.divider()

st.subheader("Transaction Risk Analysis")

display_df = transactions[
    [
        "transaction_id",
        "customer_id",
        "amount",
        "country",
        "risk_score",
        "risk_level",
        "flags"
    ]
]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("High Risk Transactions")

high_risk = display_df[
    display_df["risk_level"] == "High"
]

if high_risk.empty:
    st.info("No high-risk transactions detected.")
else:
    st.dataframe(
        high_risk,
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.caption("AML Transaction Monitoring System | KN Harsha Vardhan Kumar")
