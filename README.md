# web-honeypot-ai-ids
MSc Cyber Security Project - Web Honeypot with AI-Driven Intrusion Detection System 
# Web Honeypot System with AI-Driven Intrusion Detection


---

## About This Project

This project designs and develops a web honeypot system deployed on 
live cloud infrastructure to capture real cyber attacks, analyse 
attacker behaviour, and apply machine learning to classify attacks 
and inform a prevention decision.

The system addresses a real operational challenge facing organisations 
today: intrusion detection systems trained on historical academic 
benchmarks develop blind spots for the attack types that threat actors 
are actively deploying against production infrastructure. This project 
quantifies that gap and demonstrates how incorporating live honeypot 
telemetry into the training pipeline closes it.

---

## Repository Contents

| File | Description |
|---|---|
| `project implementation.ipynb` | Full pipeline - preprocessing, threat intelligence, ML training and evaluation |
| `demo_app.py` | Streamlit prevention decision interface |
| `demo_model.joblib` | Trained CSIC classifier (Classifier 1) |
| `demo_vectorizer.joblib` | TF-IDF vectoriser for Classifier 1 |
| `demo_examples.json` | Real held-out attack samples for the demo |
| `combined_5class_model.joblib` | Combined 5-class classifier (Classifier 2) |
| `combined_5class_vectorizer.joblib` | TF-IDF vectoriser for Classifier 2 |
| `honeypot_clean.csv` | Cleaned dataset - 108,515 records, 18 features |
| `fig_*.png` | Report figures - confusion matrices and threat intelligence charts |

---

## Quick Start

**Run the demo:**
```bash
pip install streamlit joblib scikit-learn
python -m streamlit run demo_app.py
```
Open browser at **http://localhost:8501**

**Run the full notebook:**
```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter
jupyter notebook project_corrected.ipynb
```

---

## Technical Stack

T-Pot 24.04.1 · Oracle Cloud Free Tier · Ubuntu 22.04 · Python 3 · 
scikit-learn · Random Forest · TF-IDF · pandas · Streamlit · 
Elasticsearch · Kibana · MITRE ATT&CK

