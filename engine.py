import json
import networkx as nx
from registry import NODE_REGISTRY

def load_pipeline(path):
    with open(path) as f:
        return json.load(f)

def build_graph(dsl):
    g = nx.DiGraph()
    for node in dsl["nodes"]:
        g.add_node(node["id"], **node)
    for edge in dsl["edges"]:
        g.add_edge(edge["from"], edge["to"])
    return g

def run_pipeline(dsl):
    g = build_graph(dsl)
    results = {}

    for node_id in nx.topological_sort(g):
        node = g.nodes[node_id]
        func = NODE_REGISTRY[node["type"]]

        parents = list(g.predecessors(node_id))
        inputs = [results[p] for p in parents]

        results[node_id] = func(*inputs, **node["params"])

    return results
