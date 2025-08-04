import numpy as np

delay_length = 5
delay_buffer = np.zeros((delay_length, ))

def delay(x, y):
    for i in range(len(x)):
        y[i] = delay_buffer[delay_length - 1]
        for j in range(delay_length - 1, 0 ,-1):
            delay_buffer[j] = delay_buffer[j - 1]
        delay_buffer[0] = x[i]