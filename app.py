import streamlit as st
import pandas as pd

# Step 1: Load data from Google Sheet
# Share your sheet as "Anyone with link can view" and copy the sheet ID
SHEET_ID = "1D2Se_QOfzKjLYLPC7VZ32WGTEhsjEiZcz1PPX08rmU8"
SHEET_NAME = "FY2025-2026"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# Read sheet into DataFrame
df = pd.read_csv(URL)
df.head()

st.title("🏠 Society Maintenance Tracker")

# Step 2: User Input
flat_number = st.text_input("Enter your Flat Number:")

if flat_number:
    result = df[df["Flat No."].astype(str) == flat_number]

    if not result.empty:
        maintenance = result.iloc[0]["Unnamed: 6"]
        interest = result.iloc[0]["Unnamed: 7"]

        st.success(f"✅ Flat {flat_number}")
        st.write(f"**Maintenance Amount:** ₹{maintenance}")
        st.write(f"**Late Payment Interest:** ₹{interest}")
    else:
        st.error("❌ Flat number not found. Please check again.")