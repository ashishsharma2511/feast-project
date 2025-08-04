from feast import FeatureView, Entity, Field, FileSource, ValueType
from feast.types import Float32, Int32
from datetime import timedelta
from feast import FileSource
from feast.data_format import FileFormat

# Entity definition
customer = Entity(name="user_id", value_type=ValueType.INT64)

# File source
transaction_source = FileSource(
    path="data/transactions.parquet",   # or .csv if you converted to parquet, as suggested
    timestamp_field="event_timestamp"  # must match the column name in your data
)

# FeatureView definition
fraud_fv = FeatureView(
    name="fraud_metrics",
    entities=[customer],  # ✅ Pass Entity object
    ttl=timedelta(days=1),
    schema=[
        Field(name="amount", dtype=Float32),
        Field(name="is_fraud", dtype=Int32),
    ],
    source=transaction_source,
)
