AutoSentinel is an AI-powered vehicle fault detection system that combines deterministic rule-based logic with machine learning anomaly detection using Isolation Forest. It prioritizes alerts using a mathematically weighted scoring model and logs all telemetry events into SQLite for fleet-level monitoring and predictive maintenance.



Attachments:
Video file: [AutoSentinel_AI.mp4](https://github.com/user-attachments/assets/c94634f2-337e-4f03-9318-e7d10715fe5d)

Drive link (PPT and Video): [PPT](https://drive.google.com/drive/folders/1OJKG6W_qIb-OAtMD9mo0cHyResqYsiWI?usp=sharing)

Vehicle external dataset: [vehicle_telemetry.csv](https://github.com/user-attachments/files/25688550/vehicle_telemetry.csv)



Project Overview – AutoSentinel AI

Concept:
AutoSentinel AI is a hybrid vehicle fault detection and alerting system designed for fleet monitoring and predictive maintenance. It ingests real-time vehicle telemetry—like engine temperature, oil pressure, battery voltage, brake status, and speed—and generates prioritized alerts in categories: LOW, MEDIUM, HIGH, CRITICAL.
It combines deterministic automotive safety rules with advanced AI models to detect abnormal behavior, predict faults, and score risk in a mathematically explainable way.


🔷 AI Models Included & Process

Isolation Forest (Unsupervised)
Detects statistical anomalies in telemetry (out-of-range or unusual patterns).
Outputs an anomaly score between 0–1 indicating deviation from normal behavior.
Effective for rare or previously unseen faults.


Random Forest Classifier (Supervised)
Classifies known fault types: ENGINE_OVERHEAT, LOW_OIL, BATTERY_FAULT, BRAKE_RISK.
Trained on 5000+ realistic synthetic samples simulating actual vehicle conditions.
Provides fault probability confidence.
Logistic Regression (Supervised, Optional Ensemble)
Provides complementary probabilistic fault prediction for robust ensemble scoring.
Helps smooth out overfitting from Random Forest.


Hybrid Scoring Logic:
Each alert gets a weighted priority score:
Priority Score=0.4×Rule Severity+0.3×Anomaly Score+0.3×Fault Probability


Rule Severity → deterministic thresholds (e.g., engine >110°C → high).
Anomaly Score → how unusual the telemetry is (from Isolation Forest).
Fault Probability → supervised classifier confidence.


Priority mapping:
Score	Category
<0.3	LOW
0.3–0.5	MEDIUM
0.5–0.75	HIGH
>0.75	CRITICAL
This hybrid approach ensures both known and unknown faults are detected, while risk scoring is explainable, mimicking real-world fleet telematics.



🔷 Backend & Logic
FastAPI backend with secure HTTPS endpoints and Swagger docs.
SQLite database stores alert logs for offline or fleet use.
JWT-based admin authentication protects system access.
Rule Engine + AI Engine is modular and allows easy extension to new sensors or models.
Minimal offline dashboard visualizes alerts and metrics.

Logic Flow:
Telemetry Input → Rule Engine → AI Engine (Isolation + RandomForest + LogisticRegression) → Priority Engine → Alert + Log



🔷 Effectiveness & Industry Edge
Hybrid Detection: Combines rule-based precision with AI anomaly detection for edge cases.
Explainable: Clear weighted formula shows exactly why an alert was triggered.
Offline-ready: Works without cloud dependency; useful for fleets with connectivity constraints.
Realistic Simulation: 5000+ accurate synthetic samples mimic real vehicle telemetry.
Extensible: Add new sensors, rules, or AI models without changing core backend.
Secure & Scalable: HTTPS + JWT + modular backend suitable for future fleet-scale deployment.

Standout Feature:

Unlike basic telemetry dashboards, AutoSentinel AI fuses rules, ensemble AI, and risk scoring into a single explainable alert priority system—ready for industry or hackathon demonstration.




