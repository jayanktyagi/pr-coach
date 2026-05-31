from langgraph.graph import StateGraph
from app.graphs.nodes.load_history import load_history_node
from app.graphs.state import CoachState
from app.graphs.nodes.analyse import analyze_node
from app.graphs.nodes.respond import respond_node

graph = StateGraph(CoachState)
graph.add_node("load_history", load_history_node)
graph.add_node("analyze", analyze_node)
graph.add_node("respond", respond_node)

graph.set_entry_point("load_history")
graph.add_edge("load_history", "analyze")
graph.add_edge("analyze", "respond")
graph.set_finish_point("respond")

coach_graph = graph.compile()