
from feast import FeatureStore

# Initialize Feast Feature Store
store = FeatureStore(repo_path=".")

# Retrieve online features
result = store.get_online_features(
    features=[
        "breast_cancer_measurements:mean_radius",
        "breast_cancer_measurements:mean_texture",
        "breast_cancer_measurements:mean_area",
    ],
    entity_rows=[
        {"sample_id": 1},
        {"sample_id": 2},
    ],
).to_dict()

# Display retrieved features
print("Online feature retrieval completed")
print(result)

