import numpy as np

class Delay:
    def __init__(self, delay_length):
        self._delay_length = delay_length
        self._delay_buffer = np.zeros((delay_length, ))

    def process(self, x):
        y = np.zeros_like(x)
        y[0] = self._delay_buffer[self._delay_length - 1]
        