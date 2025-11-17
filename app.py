import streamlit as st
import json
from pipelines.build_personas import build_personas_pipeline

st.set_page_config(
    page_title="AI Persona Builder",
    page_icon="🧠",
    layout="wide",
)

st.title("🧠 AI Persona Generator")
st.write("Generate realistic customer personas instantly using LLaMA 3 + Groq 🚀")

# --- BRAND BRIEF INPUT ---
st.subheader("📌 Brand Brief")
brand_brief = st.text_area(
    "Describe the brand, value proposition, and audience focus.",
    placeholder="Example: We are a D2C skincare brand focused on acne-prone Indian Gen-Z",
    height=130
)

# --- CONSTRAINT UI ---
st.subheader("🎯 Audience Constraints")

col1, col2 = st.columns(2)

with col1:
    age_range = st.text_input("Age Range", "18-35")
    region = st.text_input("Region", "India Tier 1 & Tier 2")
    gender = st.text_input("Gender (optional)", "")
with col2:
    income = st.text_input("Income Range", "25k–80k INR")
    category = st.text_input("Product Category", "Skincare / Beauty")
    interests = st.text_input("Audience Interests (comma separated)", "Instagram, Self-care, Fashion")

constraints = {
    "age_range": age_range,
    "region": region,
    "income": income,
    "gender": gender,
    "category": category,
    "interests": [x.strip() for x in interests.split(",")],
}

# --- RUN PIPELINE ---
if st.button("🚀 Generate Personas", type="primary"):
    if not brand_brief.strip():
        st.error("❗ Brand brief cannot be empty")
    else:
        with st.spinner("⏳ Generating personas using Groq + LLaMA 3..."):
            personas = build_personas_pipeline(brand_brief, constraints)

        st.success("✨ Personas generated successfully!")

        st.subheader("🧬 Generated Personas")
        st.json(personas)

        # DOWNLOAD BUTTON
        st.download_button(
            label="⬇ Download Personas JSON",
            data=json.dumps(personas, indent=2),
            file_name="personas.json",
            mime="application/json"
        )
