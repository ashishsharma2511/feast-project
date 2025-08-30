from feast import FeatureStore
from datetime import datetime
import pandas as pd

fs = FeatureStore(repo_path="feature_repo")

# Build an entity dataframe
entity_df = pd.DataFrame({
    "user_id": [1, 2, 3],
    "event_timestamp": [
        datetime(2025, 8, 1, 10, 1),
        datetime(2025, 8, 1, 10, 1),
        datetime(2025, 8, 1, 10, 4),
    ],
})

# Retrieve features as-of those timestamps
df = fs.get_historical_features(
    entity_df=entity_df,
    features=["fraud_metrics:amount", "fraud_metrics:is_fraud"],
).to_df()

print(df)
