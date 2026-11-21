
from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32

# Define entity
breast_cancer_entity = Entity(
    name="breast_cancer_sample",
    join_keys=["sample_id"],
    description="Unique Wisconsin dataset sample"
)

# Define data source
breast_cancer_source = FileSource(
    name="breast_cancer_source",
    path="data/breast_cancer_features.parquet",
    timestamp_field="event_timestamp"
)

# Define feature view
breast_cancer_features = FeatureView(
    name="breast_cancer_measurements",
    entities=[breast_cancer_entity],
    ttl=timedelta(days=3650),
    schema=[
        Field(name="mean_radius", dtype=Float32),
        Field(name="mean_texture", dtype=Float32),
        Field(name="mean_perimeter", dtype=Float32),
        Field(name="mean_area", dtype=Float32),
        Field(name="mean_smoothness", dtype=Float32),
        Field(name="radius_texture_ratio", dtype=Float32),
        Field(name="perimeter_area_ratio", dtype=Float32),
    ],
    source=breast_cancer_source
)
