import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("CSV Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

    # Columns
    columns = df.columns.tolist()

    # Select Chart Type
    chart_type = st.selectbox(
        "Select Chart",
        ["Bar Chart", "Line Chart", "Pie Chart"]
    )

    # Select Column
    column = st.selectbox(
        "Select Column",
        columns
    )

    fig, ax = plt.subplots()

    if chart_type == "Bar Chart":
        df[column].value_counts().plot(
            kind="bar",
            ax=ax
        )

    elif chart_type == "Line Chart":
        df[column].value_counts().plot(
            kind="line",
            ax=ax
        )

    elif chart_type == "Pie Chart":
        df[column].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            ax=ax
        )

    st.pyplot(fig)