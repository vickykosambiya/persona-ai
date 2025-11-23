import streamlit as st
import pandas as pd
import time
import os
from agents.product_interpreter import product_interpreter_agent
from agents.data_validator import data_validator_agent
from agents.synthetic_cluster import synthetic_cluster_agent
from agents.persona_discovery import persona_discovery_agent
from agents.persona_validator import persona_validator_agent
from agents.jtbd_extraction import jtbd_extraction_agent
from agents.objection_intelligence import objection_intelligence_agent
from agents.channel_affinity import channel_affinity_agent
from agents.content_persona import content_persona_agent
from agents.offer_strategy import offer_strategy_agent

# Page Config
st.set_page_config(page_title="AI Persona Builder", layout="wide")

# Title and Description
st.title("AI Persona Builder")
st.markdown("Turn your product idea into a full customer strategy with AI agents.")

# Sidebar - Inputs


st.sidebar.header("Product Details")
product_name = st.sidebar.text_input("Product Name", "Acme SaaS")
category = st.sidebar.selectbox("Category", ["SaaS", "E-com", "Service", "Digital Product"])
description = st.sidebar.text_area("Product Description", "A tool that helps...")
geography = st.sidebar.selectbox("Target Geography", ["USA", "Europe", "Asia", "Global"])
primary_goal = st.sidebar.selectbox("Primary Business Goal", ["High LTV", "Quick Scale", "Brand Awareness"])
brand_voice = st.sidebar.multiselect("Brand Voice", ["Witty", "Professional", "Urgent", "Friendly"], default=["Professional"])
anti_personality = st.sidebar.text_input("Anti-Personality", "We are not cheap or low quality.")
uploaded_file = st.sidebar.file_uploader("User Data Upload (CSV/Excel)", type=['csv', 'xlsx'])

# State Management
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'data' not in st.session_state:
    st.session_state.data = {}

# Main Action Button
if st.sidebar.button("Start Strategy Generation"):
    st.session_state.step = 1
    st.rerun()

# --- Phase 1: Input & Preparation ---
if st.session_state.step >= 1:
    st.header("Phase 1: Input & Preparation")
    
    with st.status("Analyzing Product & Data...", expanded=True) as status:
        try:
            # 1. Product Interpreter
            st.write("🤖 Product Interpreter: Analyzing product...")
            product_context = product_interpreter_agent(product_name, description, category)
            st.session_state.data['product_context'] = product_context
            st.json(product_context)
            
            # 2. Data Validator
            st.write("🛡️ Data Validator: Checking data...")
            validation_result = data_validator_agent(uploaded_file)
            st.session_state.data['validation_result'] = validation_result
            st.write(f"Status: {validation_result['status']}")
            
            # 3. Synthetic Cluster
            if validation_result['low_data_mode']:
                st.write("🧬 Synthetic Cluster: Generating synthetic users...")
                user_data = synthetic_cluster_agent(validation_result, product_context)
                st.session_state.data['user_data'] = user_data
                st.write(f"Generated {len(user_data)} synthetic users.")
            else:
                st.session_state.data['user_data'] = validation_result['dataframe']
                
            status.update(label="Phase 1 Complete", state="complete", expanded=False)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            status.update(label="Error", state="error", expanded=True)
            st.stop()
    
    if st.session_state.step == 1:
        st.session_state.step = 2
        time.sleep(1)
        st.rerun()

# --- Phase 2: The Creation Loop ---
if st.session_state.step >= 2:
    st.header("Phase 2: Persona Discovery")
    
    with st.status("Discovering & Validating Personas...", expanded=True) as status:
        # 4. Persona Discovery
        st.write("🕵️ Persona Discovery: Segmenting users...")
        personas = persona_discovery_agent(st.session_state.data['user_data'], st.session_state.data['product_context'], primary_goal, anti_personality, geography)
        st.session_state.data['personas'] = personas
        
        # 5. Persona Validator Loop
        st.write("⚖️ Persona Validator: Scoring personas...")
        validation = persona_validator_agent(personas, primary_goal)
        st.session_state.data['persona_validation'] = validation
        
        st.write(f"Score: {validation.get('score', 0)}/100")
        if validation.get('score', 0) < 70:
            st.warning(f"Low Score: {validation.get('feedback')}")
            # In a real loop, we would retry here. For MVP, we proceed with warning.
        else:
            st.success("Personas Approved!")
            
        status.update(label="Phase 2 Complete", state="complete", expanded=False)

    if st.session_state.step == 2:
        st.session_state.step = 3
        time.sleep(1)
        st.rerun()

# --- Phase 3 & 4: Strategy & Output ---
if st.session_state.step >= 3:
    st.header("Phase 3 & 4: Strategy & Deliverables")
    
    personas = st.session_state.data.get('personas', {})
    
    # Process each persona
    cols = st.columns(4)
    persona_types = ["cash_cow", "growth_a", "growth_b", "negative_persona"]
    
    for idx, p_type in enumerate(persona_types):
        p_data = personas.get(p_type)
        if not p_data:
            continue
            
        with cols[idx]:
            st.subheader(f"{p_type.replace('_', ' ').title()}")
            
            # Handle new keys
            real_name = p_data.get('real_name', 'N/A')
            persona_info = p_data.get('persona_info', '')
            demographics = p_data.get('demographics', {})
            
            st.markdown(f"### {real_name}")
            if persona_info:
                st.caption(f"**{persona_info}**")
            
            # Display Demographics
            st.markdown("#### 👤 Demographics")
            st.write(f"**Age:** {demographics.get('age_range', 'N/A')}")
            st.write(f"**Occupation:** {demographics.get('occupation', 'N/A')}")
            st.write(f"**Income:** {demographics.get('income', 'N/A')}")
            st.write(f"**Location:** {demographics.get('location', 'N/A')}")
            
            if p_type == "negative_persona":
                st.error("🚫 Do Not Target")
                psychographics = p_data.get('psychographics', {})
                st.write(f"**Why:** {psychographics.get('why_they_wont_buy', 'N/A')}")
                st.write(f"**Misalignment:** {psychographics.get('misalignment_reason', 'N/A')}")
                continue
            
            with st.spinner("Generating Strategy..."):
                # 6. JTBD
                jtbd = jtbd_extraction_agent(p_data)
                st.markdown("**🧠 JTBD**")
                st.write(f"Functional: {jtbd.get('functional_job')}")
                st.write(f"Emotional: {jtbd.get('emotional_job')}")
                
                # 7. Objection
                objection = objection_intelligence_agent(jtbd, anti_personality)
                st.markdown("**🛑 Objection**")
                st.write(f"Primary: {objection.get('primary_objection')}")
                st.write(f"Reason: {objection.get('reasoning')}")
                
                # 8. Channel
                # Handle demographics key
                demographics = p_data.get('demographics') or p_data.get('Demographics')
                channels = channel_affinity_agent(geography, category, demographics)
                st.markdown("**📢 Channels**")
                for c in channels.get('channels', [])[:2]:
                    st.write(f"- {c.get('name')}")
                
                # 9. Content
                content = content_persona_agent(jtbd, brand_voice, demographics)
                st.markdown("**✍️ Content Hook**")
                if content.get('hooks'):
                    st.write(f"\"{content['hooks'][0]}\"")
                
                # 10. Offer
                offer = offer_strategy_agent(primary_goal, objection.get('primary_objection'), real_name)
                st.markdown("**💰 Offer Strategy**")
                st.write(f"**{offer.get('offer_name')}**")
                st.write(offer.get('objection_handling'))

    if st.session_state.step == 3:
        st.success("Strategy Generation Complete!")
        st.session_state.step = 4
