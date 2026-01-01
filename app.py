import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Taxi Analysis",
    layout="wide",
    page_icon="🚕"
)

st.title("Taxi revenue analysis 🚕")

# ---------------- Load Data ----------------
df = pd.read_csv("final_taxi_data.csv")

# 🔥 IMPORTANT FIX: clean payment_type column
df["payment_type"] = df["payment_type"].astype(str).str.strip().str.title()

# Optional safety filter (avoids weird values)
df = df[df["payment_type"].isin(["Card", "Cash"])]

st.divider()

# ---------------- Layout ----------------
col1, col2, col3 = st.columns([2, 2, 2])

# ---------------- Plot 1 ----------------
with col1:
    st.subheader("Average fare by payment type")

    fig, ax = plt.subplots()
    df.groupby("payment_type")["fare_amount"].mean().plot(
        kind="bar",
        ax=ax
    )
    ax.set_xlabel("Payment Type")
    ax.set_ylabel("Average Fare")
    st.pyplot(fig, use_container_width=True)

# ---------------- Plot 2 ----------------
with col2:
    st.subheader("Fare Distribution (Card vs Cash)")

    fig, ax = plt.subplots()
    sns.boxplot(
        x="payment_type",
        y="fare_amount",
        data=df,
        ax=ax
    )
    ax.set_ylim(0, 100)
    ax.set_xlabel("Payment Type")
    ax.set_ylabel("Fare Amount")
    st.pyplot(fig, use_container_width=True)

# ---------------- Plot 3 (FIXED) ----------------
with col3:
    st.subheader("Fare vs Distance Trend by Payment Type")

    fig, ax = plt.subplots()

    sns.regplot(
        x="trip_distance",
        y="fare_amount",
        data=df[df["payment_type"] == "Card"],
        scatter=False,
        ci=None,
        label="Card",
        ax=ax
    )

    sns.regplot(
        x="trip_distance",
        y="fare_amount",
        data=df[df["payment_type"] == "Cash"],
        scatter=False,
        ci=None,
        label="Cash",
        ax=ax
    )

    ax.set_xlim(0, 20)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Trip Distance")
    ax.set_ylabel("Fare Amount")
    ax.legend(title="Payment Type")

    st.pyplot(fig, use_container_width=True)
