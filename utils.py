import numpy as np
import pandas as pd

def serialize(obj):
    if isinstance(obj, pd.DataFrame):
        return {
            "type": "dataframe",
            "columns": list(obj.columns),
            "data": obj.head(100).to_dict(orient="records")
        }

    if isinstance(obj, np.ndarray):
        return {
            "type": "ndarray",
            "shape": obj.shape,
            "data": obj.tolist()
        }

    if isinstance(obj, (list, dict, int, float, str)):
        return obj

    return str(obj)


def serialize_results(results: dict):
    return {k: serialize(v) for k, v in results.items()}
