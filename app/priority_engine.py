def compute_priority(rule_severity, anomaly_score, fault_prob):

    norm_rule = rule_severity / 4

    score = (
        0.4 * norm_rule +
        0.3 * anomaly_score +
        0.3 * fault_prob
    )

    if score < 0.3:
        category = "LOW"
    elif score < 0.5:
        category = "MEDIUM"
    elif score < 0.75:
        category = "HIGH"
    else:
        category = "CRITICAL"

    return score, category