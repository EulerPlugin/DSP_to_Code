b_0 = 0.128
b_1 = 0.372
b_2 = 0.372
b_3 = 0.128

x_1 = 0
x_2 = 0
x_3 = 0

def fir_filter(x, y):
    global x_1, x_2, x_3

    for i in range(len(X)):
        x_0 = x[i]
        y[i] = b_0 * x_0  + b_1 * x_1 + b_2 * x_2 + b_3 * x_3

        x_3 = x_2
        x_2 = x_1
        x_1 = x_0
        
        