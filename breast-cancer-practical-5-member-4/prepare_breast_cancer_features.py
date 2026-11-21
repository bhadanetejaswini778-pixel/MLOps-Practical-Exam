
from pathlib import Path
import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load the Breast Cancer dataset
data = load_breast_cancer(as_frame=True)
df = data.frame.copy()

# Add diagnosis column
df["diagnosis"] = df["target"].map({
    0: "malignant",
    1: "benign"
})

# Add sample ID
df["sample_id"] = range(1, len(df) + 1)

# Add event timestamp
df["event_timestamp"] = pd.Timestamp.now(
    tz="UTC"
).floor("s")

# Create additional features
df["radius_texture_ratio"] = (
    df["mean radius"] /
    df["mean texture"].replace(0, 1)
)

df["perimeter_area_ratio"] = (
    df["mean perimeter"] /
    df["mean area"].replace(0, 1)
)

# Rename columns to simple Feast-safe names
df = df.rename(columns={
    "mean radius": "mean_radius",
    "mean texture": "mean_texture",
    "mean perimeter": "mean_perimeter",
    "mean area": "mean_area",
    "mean smoothness": "mean_smoothness"
})

# Convert selected columns to float32
for column in [
    "mean_radius",
    "mean_texture",
    "mean_perimeter",
    "mean_area",
    "mean_smoothness",
    "radius_texture_ratio",
    "perimeter_area_ratio"
]:
    df[column] = df[column].astype("float32")

# Create data folder
Path("data").mkdir(exist_ok=True)

# Save dataset as Parquet file
df.to_parquet(
    "data/breast_cancer_features.parquet",
    index=False
)

# Display output
print("Feature data created:", df.shape)
print("Saved to data/breast_cancer_features.parquet")

