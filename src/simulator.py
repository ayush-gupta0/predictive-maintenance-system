import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_sensor_data(n_samples=1000):
    np.random.seed(42)
    data = []
    start_time = datetime.now()

    for i in range(n_samples):
        timestamp = start_time + timedelta(minutes=i*10)
        temp = np.random.uniform(60, 80)
        vibration = np.random.uniform(0.1, 0.5)
        pressure = np.random.uniform(90, 110)
        
        # Inject failure pattern
        label = 0
        if i % 200 > 180:
            temp += np.random.uniform(20, 40)
            vibration += np.random.uniform(0.5, 1)
            label = 1
            
        data.append([timestamp, temp, vibration, pressure, label])

    df = pd.DataFrame(data, columns=['timestamp', 'temp', 'vibration', 'pressure', 'target'])
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/sensor_data.csv', index=False)
    print("✅ Data generated successfully.")

if __name__ == "__main__":
    generate_sensor_data()