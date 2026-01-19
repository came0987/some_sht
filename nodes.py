import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def csv_loader(path):
    return pd.read_csv(path)

def standard_scaler(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)

def kmeans(data, n_clusters=3):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    return model.fit_predict(data)

def concat(a, b):
    return pd.concat([a, b], axis=0)

def weighted_sum(a, b, c, w1=1, w2=1, w3=1): # 3 in
    return a*w1 + b*w2 + c*w3

import plotly.express as px

def histogram(data, column=None, bins=30):
    if isinstance(data, pd.DataFrame):
        if column is None:
            raise ValueError("column is required")
        fig = px.histogram(data, x=column, nbins=bins)
    else:
        fig = px.histogram(x=data, nbins=bins)

    return {
        "type": "plotly",
        "figure": fig.to_dict()
    }
