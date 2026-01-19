import Plot from "react-plotly.js";

function PlotNode({ data }) {
  if (!data?.figure) return <div>No plot</div>;

  return (
    <div style={{ width: 400, height: 300 }}>
      <Plot
        data={data.figure.data}
        layout={data.figure.layout}
        config={{ responsive: true }}
      />
    </div>
  );
}