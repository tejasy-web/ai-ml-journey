import numpy as np

data = np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution
print(f"Mean: {data.mean():.4f}")
print(f"Standard Deviation: {data.std():.4f}")
print(f"Minimum: {data.min():.4f}")
print(f"Maximum: {data.max():.4f}")