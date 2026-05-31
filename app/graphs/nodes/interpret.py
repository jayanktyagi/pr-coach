from app.llm.groq_client import get_groq_client
import json

def interpret_node(state):
    llm = get_groq_client()

    messages = [
        {
            "role": "system",
            "content": "You are an expert strength coach and data analyst."
        },
        {
            "role": "user",
            "content": f"""
Here are summarized training metrics (JSON):

{json.dumps(state["metrics"], indent=2)}

Explain:
- what is going well
- what is lacking
- any imbalance or risk

Do NOT give advice yet.
Return concise insights.
"""
        }
    ]

    insights = llm.chat(messages)

    return {
        **state,
        "insights": insights
    }