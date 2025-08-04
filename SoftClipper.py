import numpy as np

gain_multiplier = 5

def soft_clip(x):
        return np.tanh(gain_multiplier * x) / np.tanh(gain_multiplier)

x = np.linspace(-1, 1, 100)
y = soft_clip(x)