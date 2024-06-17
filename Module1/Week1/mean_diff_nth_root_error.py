import math 
def mean_difference(y, y_hat, n, p):
    y_root = y**(1/n)
    y_hat_root = y_hat**(1/n)
    # Compute the difference between the nth roots
    difference = y_root - y_hat_root
    # Compute the MD-nRE loss
    loss = difference**p
    return loss 

y = float(input())
y_hat = float(input())
n = int(input())
p = int(input())
print(mean_difference(y, y_hat, n, p))

