import numpy as np
import time
import logging
from prometheus_client import start_http_server, Counter, Gauge

# Configure logging
logging.basicConfig(filename='/logs/calculation.log', level=logging.INFO)

# Create metrics
calculation_count = Counter('calculation_count', 'Number of calculations performed')
pi_estimate = Gauge('pi_estimate', 'Estimated value of π')

def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = np.random.rand(2)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_value = (inside_circle / num_samples) * 4
    pi_estimate.set(pi_value)
    calculation_count.inc()  # Increment counter after each calculation

if __name__ == "__main__":
    start_http_server(8000)  # Start metrics server on port 8000
    while True:
        monte_carlo_pi(10**7)  # Run with 10 million samples
        time.sleep(60)          # Wait before next calculation
