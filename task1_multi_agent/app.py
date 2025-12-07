# app.py

import streamlit as st
from orchestrator import run_orchestrator


st.set_page_config(page_title="Company Intelligence Agentic System", layout="wide")

st.title("🏢 Company Intelligence Agentic System")
st.write("Multi-agent system using LangChain: Data Collector + Analyst + Orchestrator.")

# Initialize history in session state
if "history" not in st.session_state:
    st.session_state["history"] = []

company_name = st.text_input("Enter a company / organization name", value="Harman")

if st.button("Analyze"):
    if not company_name.strip():
        st.warning("Please enter a valid company name.")
    else:
        with st.spinner("Running multi-agent workflow..."):
            analysis, updated_history = run_orchestrator(
                company_name.strip(),
                st.session_state["history"]
            )
            st.session_state["history"] = updated_history

        st.success(f"Analysis complete for: {analysis.get('company_name', company_name)}")

        # Display analysis
        st.subheader("📌 Summary")
        st.write(analysis.get("summary", "No summary available."))

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Strengths")
            strengths = analysis.get("strengths", [])
            if strengths:
                for s in strengths:
                    st.markdown(f"- {s}")
            else:
                st.write("No strengths identified.")

        with col2:
            st.subheader("⚠️ Risks")
            risks = analysis.get("risks", [])
            if risks:
                for r in risks:
                    st.markdown(f"- {r}")
            else:
                st.write("No risks identified.")

        st.subheader("📊 Other Details")
        st.write(f"**Industry:** {analysis.get('industry', 'Unknown')}")
        st.write(f"**Sentiment:** {analysis.get('sentiment', 'Unknown')}")

# History section
st.sidebar.header("History (Memory)")
if st.session_state["history"]:
    for item in reversed(st.session_state["history"]):
        st.sidebar.markdown(f"- {item['company_name']}")
else:
    st.sidebar.write("No companies analyzed yet.")
