import streamlit as st
import google.generativeai as genai

# Setup Gemini
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="UnitySync", page_icon="🤝")
st.title("🤝 UnitySync: AI Resource Allocation")

# Interface
st.markdown("### Step 1: Input Community Need")
report = st.text_area("Enter a field report (e.g., 'Block B needs clean water and a plumber')")

if st.button("Run Smart Match"):
    if report:
        # Gemini analyzes the text
        response = model.generate_content(f"Analyze this report: '{report}'. Tell me the Urgency (1-10) and the primary skill needed. Format as: Urgency: X | Skill: Y")
        st.info(f"AI Analysis: {response.text}")
        st.success("Match found! Notifying best-fit volunteer...")
    else:
        st.error("Please enter a report first!")
