


import numpy as np

class IIR_LP:
    def __init__(self):
        self._a = np.zeros(3)
        self._b = np.zeros(3)

        self._s1 = 0.0
        self._s2 = 0.0
        
        self._y = None

    def process(self, x, cutoff, fs, q, normalized = True):
        self._y = np.zeros_like(x)
        k = np.tan(np.pi * cutoff / fs)

        # norm = 1 + q / k + k**2
        a = np.array([1 + q / k + k**2,  2 * k ** 2 - 2,1 - k / q + k**2])
        b = np.array([k**2, 2 * k**2, k**2])

        if normalized:
            b /= a[0]
            a /= a[0]

        self._a[:] = a
        self._b[:] = b
        
        for i in range(len(x)):
            y_0 = x[i] * b[0] + self._s1
            self._s1 = x[i] * b[1] + self._s2 - a[1] * y_0
            self._s2 = x[i] * b[2] - a[2] * y_0
            self._y[i] = y_0

        return self._y


fs = 48000
cutoff = 200
q = 1 / np.sqrt(2)  # Butterworth Q



lp = IIR_LP()
x = np.random.randn(1024)
y = lp.process(x, cutoff, fs, q, normalized=True)

print(y[:10])  # 첫 10개 출력



