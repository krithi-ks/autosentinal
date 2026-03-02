import numpy as np
import pandas as pd

def generate_dataset(samples=6000):
    np.random.seed(42)

    engine_temp = np.clip(np.random.normal(95, 7, samples), 70, 140)
    oil_pressure = np.clip(np.random.normal(50, 12, samples), 5, 90)
    battery_voltage = np.clip(np.random.normal(13.4, 0.4, samples), 10, 15)
    speed = np.clip(np.random.normal(65, 30, samples), 0, 160)
    brake_status = np.random.choice([0,1], samples, p=[0.8,0.2])

    labels = []

    for i in range(samples):
        if engine_temp[i] > 115:
            labels.append("ENGINE_OVERHEAT")
        elif oil_pressure[i] < 15:
            labels.append("LOW_OIL")
        elif battery_voltage[i] < 11.5:
            labels.append("BATTERY_FAULT")
        elif brake_status[i] == 1 and speed[i] > 100:
            labels.append("BRAKE_RISK")
        else:
            labels.append("NORMAL")

    df = pd.DataFrame({
        "engine_temp": engine_temp,
        "oil_pressure": oil_pressure,
        "battery_voltage": battery_voltage,
        "brake_status": brake_status,
        "speed": speed,
        "label": labels
    })

    df.to_csv("data/vehicle_data.csv", index=False)

if __name__ == "__main__":
    generate_dataset()