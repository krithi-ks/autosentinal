import joblib
import numpy as np

# Load models
isolation = joblib.load("model/isolation.pkl")
rf = joblib.load("model/rf_classifier.pkl")
lr = joblib.load("model/lr_classifier.pkl")

feature_names = [
    "engine_temp",
    "oil_pressure",
    "battery_voltage",
    "brake_status",
    "speed"
]

def analyze_ai(data):

    X = np.array([[ 
        data.engine_temp,
        data.oil_pressure,
        data.battery_voltage,
        data.brake_status,
        data.speed
    ]])

    # -------- Anomaly Detection --------
    anomaly_score = abs(isolation.decision_function(X)[0])

    # Normalize anomaly score (prevent always HIGH)
    normalized_anomaly = min(1.0, anomaly_score / 0.5)

    # -------- Fault Classification --------
    rf_pred = rf.predict(X)[0]
    rf_prob = max(rf.predict_proba(X)[0])
    lr_prob = max(lr.predict_proba(X)[0])

    fault_prob = (rf_prob + lr_prob) / 2

    # -------- Priority Logic (Balanced) --------
    priority_score = round((fault_prob * 0.6) + (normalized_anomaly * 0.4), 4)

    if priority_score >= 0.85:
        severity = "CRITICAL"
    elif priority_score >= 0.65:
        severity = "HIGH"
    elif priority_score >= 0.4:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    # -------- Recommended Actions --------
    actions_map = {
        "LOW_OIL": [
            "Stop vehicle immediately.",
            "Check oil levels.",
            "Inspect oil leakage.",
            "Visit service center."
        ],
        "OVERHEAT": [
            "Turn off engine.",
            "Allow engine to cool.",
            "Check coolant level.",
            "Avoid driving until resolved."
        ],
        "BATTERY_FAULT": [
            "Inspect battery voltage.",
            "Check alternator output.",
            "Avoid electrical overload."
        ]
    }

    recommended_actions = actions_map.get(str(rf_pred), ["Perform full diagnostic check."])

    # -------- Explainability (Safe Version) --------
    importances = rf.feature_importances_

    explanation = {}

    for i, feature in enumerate(feature_names):
        contribution = importances[i] * X[0][i]
        explanation[feature] = float(round(contribution, 4))

    # -------- Debug Print (REMOVE LATER) --------
    print("Fault Prob:", fault_prob)
    print("Anomaly Score:", anomaly_score)
    print("Priority Score:", priority_score)
    print("Severity:", severity)
    print("-----------------------------------")

    return {
        "prediction": str(rf_pred),
        "anomaly_score": float(round(anomaly_score, 4)),
        "fault_probability": float(round(fault_prob, 4)),
        "priority_score": priority_score,
        "severity": severity,
        "feature_contributions": explanation,
        "recommended_actions": recommended_actions
    }