import streamlit as st
import pandas as pd
from supabase import create_client
SUPABASE_URL = "https://ytkvjbndjzcpbdizlaky.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl0a3ZqYm5kanpjcGJkaXpsYWt5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDQyNTgsImV4cCI6MjA4MTYyMDI1OH0.CMVxjDC8L1w5TzaOqCoVNH10SkM4Npork2jepgQJ-X4"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
st.title("HDFC BANK (Supabase)")
menu = ["REGISTER", "VIEW"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "REGISTER":
    name = st.text_input("Enter name")
    age = st.number_input("Age", min_value=18, step=1)
    account = st.number_input("Account Number", step=1)
    bal = st.number_input("Balance", min_value=500)
    if st.button("Save"):
        if name and account:
            supabase.table("users").insert({
                "name": name,
                "age": int(age),
                "account": int(account),
                "balance": bal
            }).execute()
            st.success("User added successfully ✅")
        else:
            st.error("Please fill all fields")
elif choice == "VIEW":
    st.subheader("View Users")
    data = supabase.table("users").select("*").execute()
    df = pd.DataFrame(data.data)
    st.dataframe(df)
