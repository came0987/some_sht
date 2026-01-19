from nodes import csv_loader, standard_scaler, kmeans

NODE_REGISTRY = {
    "csv_loader": csv_loader,
    "standard_scaler": standard_scaler,
    "kmeans": kmeans,
    "histogram": histogram,
}
