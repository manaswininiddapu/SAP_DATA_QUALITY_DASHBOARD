import pandas as pd
import streamlit as st

# Load Data
st.title("SAP Data Quality Checker Dashboard")
uploaded_file = st.file_uploader("Upload SAP Data (CSV)", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.write("### Raw Data Preview", df.head())

    # Null Value Check
    st.write("### Null Value Report")
    null_report = df.isnull().sum().reset_index()
    null_report.columns = ['Column', 'Null Values']
    st.dataframe(null_report)

    # Duplicate Check
    st.write("### Duplicate Records")
    duplicates = df[df.duplicated()]
    st.dataframe(duplicates)

    # Format Validation Example - Amount should be numeric
    st.write("### Invalid Amount Entries")
    invalid_amount = df[pd.to_numeric(df['Amount'], errors='coerce').isnull()]
    st.dataframe(invalid_amount)

    # Summary KPIs
    st.metric(label="Total Records", value=len(df))
    st.metric(label="Null Values Found", value=null_report['Null Values'].sum())
    st.metric(label="Duplicate Records", value=len(duplicates))

else:
    st.info("Please upload a SAP data file to begin analysis.")
