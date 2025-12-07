# orchestrator.py

from typing import Dict, List, Tuple

from langchain_core.runnables import RunnableLambda

from agents.data_collector_agent import run_data_collector_agent
from agents.analyst_agent import run_analyst_agent


# Wrap your existing agents as LangChain "runnables"
collector_runnable = RunnableLambda(run_data_collector_agent)
analyst_runnable = RunnableLambda(run_analyst_agent)

# Compose them into a LangChain pipeline:
# company_name -> raw_data -> analysis
orchestrator_chain = collector_runnable | analyst_runnable


def run_orchestrator(
    company_name: str,
    history: List[Dict]
) -> Tuple[Dict, List[Dict]]:
    """
    Uses a LangChain Runnable pipeline under the hood:

        company_name
           ↓
      collector_runnable (Agent 1)
           ↓
      analyst_runnable   (Agent 2)
           ↓
        analysis
    """

    # Step 1–2: run both agents via LangChain chain
    # This internally calls:
    #   raw_data = run_data_collector_agent(company_name)
    #   analysis = run_analyst_agent(raw_data)
    analysis = orchestrator_chain.invoke(company_name)

    # If you also want raw_data in history, call collector once:
    raw_data = run_data_collector_agent(company_name)

    history_entry = {
        "company_name": company_name,
        "raw_data": raw_data,
        "analysis": analysis,
    }
    history.append(history_entry)

    return analysis, history
