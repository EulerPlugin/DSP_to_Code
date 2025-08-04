## lowpass filter with cutoff frequency at 200Hz
## at 48000Hz sampling rate

import numpy as np

def butter(cutoff_frequency_hz, sampling_rate, q, normalized=False):
    """
    Calculates the numerator and denominator coeffcients of the
    2nd-order Butterworth lowpass
    based on manual digitization via the bilinear transformation.
    :param cutoff_frequency_hz: cutoff frequency of the filter in hertz
    :param sampling_rate: sampling rate in hertz
    :param q: the Q-factor of the filter
    :param normalized: if True, then filter coefficients will be normalized by a0 so that a0 = 1.
    :return: b, a numerator and denominator coefficients respectively of a digital transfer function
    (see scipy.signal.butter for 'ba' output)
    """
    k = np.tan(np.pi * cutoff_frequency_hz / sampling_rate)
    b0 = k ** 2
    b1 = 2 * k ** 2
    b2 = k ** 2
    a0 = 1 + k / q + k ** 2
    a1 = 2 * k ** 2 - 2
    a2 = 1 - k / q + k ** 2
    b = [b0, b1, b2]
    a = [a0, a1, a2]

    if normalized:
        b /= a0
        a /= a0
    return b, a

# b = [0.00016822, 0.00033645, 0.00016822]
# a = [1., -1.96298009, 0.96365298]

b, a = butter(200, 48000, 1/np.sqrt(2), normalized = True)

s_1 = 0
s_2 = 0

def IIR_filter(x, y):

    global s_1, s_2

    for i in range(len(x)):
        y_0 = x[i] * b[0] + s_1
        s_1 = x[i] * b[1] - y_0 * a[1] + s_2
        s_2 = x[i] * b[2] - y_0 * a[2]

        y[i] = y_0