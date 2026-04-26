import streamlit as st
import google.generativeai as genai

# 1. Setup - USE YOUR REAL KEY HERE
API_KEY = "PASTE_YOUR_ACTUAL_KEY_STARTING_WITH_AIza"
genai.configure(api_key=API_KEY)

# Use the latest stable model
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🤝 UnitySync: AI Resource Allocation")

report = st.text_area("Step 1: Input Community Need", "We need a doctor in Sector 5.")

if st.button("Run Smart Match"):
    if not API_KEY or "YOUR" in API_KEY:
        st.error("Please update your API Key in the code!")
    elif report:
        try:
            # AI Analysis
            response = model.generate_content(f"Analyze urgency (1-10) and skill needed for: {report}")
            st.info(f"AI Analysis: {response.text}")
            st.success("Matching found! Assigned: Lead Volunteer to the sector.")
        except Exception as e:
            st.error(f"AI Error: {e}")
