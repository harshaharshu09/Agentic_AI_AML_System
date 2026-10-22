import pandas as pd
import streamlit as st

from workflow import AMLWorkflow


st.set_page_config(
    page_title="AML Transaction Monitoring System",
    page_icon="AML",
    layout="wide",
)

st.title("AML Transaction Monitoring System")
st.caption("Rule-based transaction screening and risk analysis")
st.write(
    "Review sample transactions, inspect risk indicators, and export screening results."
)

st.warning(
    "Educational demo only. A risk flag is not proof of money laundering and must not "
    "be used as a real compliance decision."
)

try:
    result = AMLWorkflow().run()
    transactions = result["all_transactions"]
except Exception as exc:
    st.error(f"Unable to load or analyse the transaction data: {exc}")
    st.stop()

suspicious_transactions = result["suspicious_transactions"]
high_risk_transactions = result["high_risk_transactions"]

metric1, metric2, metric3 = st.columns(3)
metric1.metric("Total Transactions", len(transactions))
metric2.metric("Suspicious Transactions", len(suspicious_transactions))
metric3.metric("High Risk Transactions", len(high_risk_transactions))

st.divider()

left, right = st.columns([1, 2])

with left:
    st.subheader("Risk Distribution")
    risk_counts = (
        transactions["risk_level"]
        .value_counts()
        .reindex(["Low", "Medium", "High"], fill_value=0)
        .rename_axis("Risk Level")
        .to_frame("Transactions")
    )
    st.bar_chart(risk_counts)

with right:
    st.subheader("Screening Summary")
    st.write(
        f"**{len(suspicious_transactions)} of {len(transactions)}** transactions "
        "are classified as Medium or High risk by the current demo rules."
    )
    st.write(
        f"**{len(high_risk_transactions)}** transactions are in the High-risk category "
        "and are displayed separately below."
    )

st.divider()
st.subheader("Transaction Explorer")

filter1, filter2, filter3 = st.columns([1.4, 1, 1])
with filter1:
    search_text = st.text_input(
        "Search transaction or customer",
        placeholder="For example: TXN021 or CUST011",
    )
with filter2:
    risk_options = ["Low", "Medium", "High"]
    selected_risks = st.multiselect(
        "Risk level",
        options=risk_options,
        default=risk_options,
    )
with filter3:
    country_options = ["All countries"] + sorted(
        transactions["country"].dropna().astype(str).unique().tolist()
    )
    selected_country = st.selectbox("Country", country_options)

filtered = transactions.copy()

if selected_risks:
    filtered = filtered[filtered["risk_level"].isin(selected_risks)]
else:
    filtered = filtered.iloc[0:0]

if selected_country != "All countries":
    filtered = filtered[filtered["country"] == selected_country]

if search_text.strip():
    query = search_text.strip()
    match_transaction = filtered["transaction_id"].astype(str).str.contains(
        query, case=False, na=False
    )
    match_customer = filtered["customer_id"].astype(str).str.contains(
        query, case=False, na=False
    )
    filtered = filtered[match_transaction | match_customer]

display_columns = [
    "transaction_id",
    "customer_id",
    "amount",
    "country",
    "risk_score",
    "risk_level",
    "flags",
]
display_df = filtered[display_columns].copy()

st.caption(f"Showing {len(display_df)} of {len(transactions)} transactions.")
st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "amount": st.column_config.NumberColumn("Amount", format="₹%.2f"),
        "risk_score": st.column_config.NumberColumn("Risk Score", format="%d / 100"),
    },
)

download_col1, download_col2 = st.columns(2)
with download_col1:
    st.download_button(
        "Download filtered results (CSV)",
        data=display_df.to_csv(index=False).encode("utf-8-sig"),
        file_name="aml_filtered_transactions.csv",
        mime="text/csv",
        use_container_width=True,
    )
with download_col2:
    st.download_button(
        "Download all results (CSV)",
        data=transactions[display_columns].to_csv(index=False).encode("utf-8-sig"),
        file_name="aml_all_transactions.csv",
        mime="text/csv",
        use_container_width=True,
    )

st.divider()
st.subheader("High Risk Transactions")
if high_risk_transactions.empty:
    st.info("No high-risk transactions detected by the current demo rules.")
else:
    high_risk_df = high_risk_transactions[display_columns].copy()
    st.dataframe(
        high_risk_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "amount": st.column_config.NumberColumn("Amount", format="₹%.2f"),
            "risk_score": st.column_config.NumberColumn("Risk Score", format="%d / 100"),
        },
    )

st.caption("KN Harsha Vardhan Kumar | Rule-based AML learning prototype")
