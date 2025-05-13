import pandas as pd
import streamlit as st
import plotly.express as px

#stock data
df = pd.read_csv("data/ALL_DATA_cleaned.csv")
df["Date"] = pd.to_datetime(df["Date"])

#company names
stock_info = pd.read_csv("data/sotcks_list.csv")  # Contains 'name' and 'ticker'
stock_info.rename(columns={"name": "Company", "ticker": "Ticker"}, inplace=True)

# Merge to add company names to main data
df = df.merge(stock_info, on="Ticker", how="left")


# Create a new column for display
df["DisplayName"] = df["Ticker"] + " - " + df["Company"]

# Get unique dropdown options
unique_companies = df[["Ticker", "DisplayName"]].drop_duplicates()

# Sidebar
st.sidebar.title("Tunisian Stock Dashboard")
selected_display = st.sidebar.selectbox(
    "Select a Company", unique_companies["DisplayName"].tolist()
)

# Extract the ticker from the selected display name
selected_ticker = unique_companies[unique_companies["DisplayName"] == selected_display]["Ticker"].values[0]



# Filter data for selected company
company_df = df[df["Ticker"] == selected_ticker]

# title
st.title(f"{selected_display} Stock Prices")

# line chart 
fig = px.line(company_df, x="Date", y="Close", title="Closing Price Over Time")
st.plotly_chart(fig)

# volume chart
if st.checkbox("Show Trading Volume"):
    fig_vol = px.bar(company_df, x="Date", y="Volume", title="Daily Trading Volume")
    st.plotly_chart(fig_vol)

# raw data
if st.checkbox("Show Raw Data"):
    st.dataframe(company_df)
