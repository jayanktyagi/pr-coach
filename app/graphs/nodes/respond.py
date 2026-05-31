from app.llm.groq_client import get_groq_client
import json

def respond_node(state):
    llm = get_groq_client()

    # 1️⃣ Build compact training summary (cap size to control tokens)
    summary_lines = []
    for s in state["exercise_sets"][:120]:
        summary_lines.append(
            f"{s['exercise']}: {s['weight']}kg x {s['reps']} (RPE {s['rpe']})"
        )

    training_summary = "\n".join(summary_lines) or "No recent training data."

    # 2️⃣ Interpretations (LLM-generated earlier)
    insights = state.get("insights", {})
    insights_json = json.dumps(insights, indent=2) if insights else "No insights available."

    # 3️⃣ Prompt
    messages = [
        {
            "role": "system",
            "content": (
                "You are a professional strength coach. "
                "Base recommendations strictly on the provided insights and training data."
            )
        },
        {
            "role": "user",
            "content": f"""
INTERPRETED INSIGHTS (already analyzed):
{insights_json}

RAW TRAINING SNAPSHOT (for context only):
{training_summary}

USER QUESTION:
{state['question']}

Rules:
- Use insights as the primary signal
- Reference raw data only when helpful
- Be practical and specific
"""
        }
    ]

    response = llm.chat(messages)

    return {
        **state,
        "response": response
    }