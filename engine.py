import networkx as nx
from registry import NODE_REGISTRY
from schema import Pipeline
from validate import validate_types

def build_graph(pipeline: Pipeline):
    g = nx.DiGraph()

    for node in pipeline.nodes:
        g.add_node(node.id, **node.dict())

    for edge in pipeline.edges:
        g.add_edge(edge.from_, edge.to, target_handle=edge.target_handle)

    return g

def run_pipeline(dsl: dict):
    pipeline = Pipeline(**dsl)
    validate_types(pipeline)

    g = build_graph(pipeline)

    results = {}

    for node_id in nx.topological_sort(g):
        node = g.nodes[node_id]
        func = NODE_REGISTRY[node["type"]]

        inputs = {}
        for parent, _, data in g.in_edges(node_id, data=True):
            handle = data.get("target_handle")
            inputs[handle or parent] = results[parent]

        # если нода принимает **kwargs
        results[node_id] = func(**inputs, **node["params"])

    return results
