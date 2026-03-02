def evaluate_rules(data):
    severity = 0

    if data.engine_temp > 110:
        severity = max(severity, 3)
    if data.oil_pressure < 20:
        severity = max(severity, 2)
    if data.battery_voltage < 12:
        severity = max(severity, 2)
    if data.brake_status == 1 and data.speed > 100:
        severity = max(severity, 4)

    return severity