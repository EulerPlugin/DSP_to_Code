import numpy as np

class Delay:
    def __init__(self, delay_length):
        self._delay_length = delay_length
        self._delay_buffer = np.zeros((delay_length, ))

    def process(self, x):
        y = np.zeros_like(x)
        for i in range(len(x)):
            y[i] = self._delay_buffer[self._delay_length - 1]
            for j in range(self._delay_length - 1, 0 , -1):
                self._delay_buffer[j] = self._delay_buffer[j - 1]
            self._delay_buffer[0] = x[i]
        return y

