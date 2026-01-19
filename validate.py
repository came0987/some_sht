from node_specs import NODE_SPECS

class TypeMismatch(Exception):
    pass

def validate_types(pipeline):
    node_map = {n.id: n for n in pipeline.nodes}

    for edge in pipeline.edges:
        src = node_map[edge.from_]
        dst = node_map[edge.to]

        src_spec = NODE_SPECS[src.type]
        dst_spec = NODE_SPECS[dst.type]

        src_out_type = list(src_spec["outputs"].values())[0]
        dst_in_type = dst_spec["inputs"].get(edge.target_handle)

        if dst_in_type is None:
            raise TypeMismatch(
                f"Node {dst.id} has no input '{edge.target_handle}'"
            )

        if src_out_type != dst_in_type:
            raise TypeMismatch(
                f"Type mismatch: {src.type} → {dst.type} "
                f"({src_out_type} → {dst_in_type})"
            )