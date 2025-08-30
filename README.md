# Fraud Detection Feature Store with Feast

This project demonstrates a simple **feature store** setup using [Feast](https://github.com/feast-dev/feast) for fraud detection. It uses **CSV files** for offline data, **Redis** as the online store, and a small synthetic dataset to showcase feature ingestion and retrieval.

## 📁 Project Structure

```
feast_project/
├── data/
│   └── transactions.csv         # Sample transaction data
├── feature_repo/
│   ├── example_repo.py          # Defines feature views and entities
│   ├── feature_store.yaml       # Feast configuration
│   └── ...
└── README.md
```

## 💡 Features

- **Entity**: `user_id`
- **Feature View**: `fraud_metrics`
  - `amount`
  - `is_fraud`
- **Offline store**: CSV
- **Online store**: Redis

## ⚙️ Requirements

- Python 3.8+
- Feast
- Redis

Install dependencies:

```bash
pip install feast redis pandas pyarrow
```

## 🚀 Running the Project

### 1. Initialize the Feature Store

```bash
cd feast_project/feature_repo
feast apply
```

### 2. Load data into the online store

```bash
feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")
```

### 3. Get online features

```bash
feast get-online-features \
  --features fraud_metrics:amount,fraud_metrics:is_fraud \
  --entities user_id=2
```

**Ashish Sharma**  
[GitHub](https://github.com/ashishsharma2511)
