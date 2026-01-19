import { useState } from "react";
import ReactFlow from "reactflow";
import PlotNode from "./PlotNode";

const nodeTypes = {
  plot: PlotNode,
};

function App() {
  const [nodes, setNodes] = useState(initialNodes);
  const [edges, setEdges] = useState(initialEdges);

  const runPipeline = async () => {
    const dsl = {
      nodes: nodes.map(n => ({
        id: n.id,
        type: n.type,
        params: n.data?.params || {}
      })),
      edges: edges.map(e => ({
        from: e.source,
        to: e.target,
        target_handle: e.targetHandle
      }))
    };

    const res = await fetch("http://localhost:8000/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dsl),
    });

    const json = await res.json();

    // 👇 ВОТ ЗДЕСЬ ПРОКИДЫВАНИЕ
    setNodes(nodes =>
      nodes.map(n =>
        json.results[n.id]
          ? {
              ...n,
              data: {
                ...n.data,
                result: json.results[n.id]
              }
            }
          : n
      )
    );
  };

  return (
    <>
      <button onClick={runPipeline}>Run</button>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
      />
    </>
  );
}