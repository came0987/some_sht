NODE_SPECS = {
    "csv_loader": {
        "inputs": {},
        "outputs": {
            "out": DataType.DATAFRAME
        }
    },
    "standard_scaler": {
        "inputs": {
            "data": DataType.DATAFRAME
        },
        "outputs": {
            "out": DataType.ARRAY
        }
    },
    "kmeans": {
        "inputs": {
            "data": DataType.ARRAY
        },
        "outputs": {
            "labels": DataType.LABELS
        }
    },
    "histogram": {
        "inputs": {
            "data": DataType.DATAFRAME
        },
        "outputs": {
            "plot": DataType.PLOT
        }
    }
}