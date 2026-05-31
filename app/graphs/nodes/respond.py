from app.llm.groq_client import get_groq_client

def respond_node(state):
    llm = get_groq_client()

    summary_lines = []
    for s in state["exercise_sets"][:120]:
        summary_lines.append(
            f"{s['exercise']}: {s['weight']}kg x {s['reps']} (RPE {s['rpe']})"
        )

    training_summary = "\n".join(summary_lines) or "No recent training data."

    messages = [
        {
            "role": "system",
            "content": "You are a professional strength coach analyzing workout logs."
        },
        {
            "role": "user",
            "content": f"""
Training data:
{training_summary}

Question:
{state['question']}
"""
        }
    ]

    response = llm.chat(messages)

    return {
        **state,
        "response": response
    }