import numpy as np

def f(x, a, b):
    return np.sqrt((b**2*(1-(x**2)/(a**2))))

##def func(x, y, a, b):
##    return (((x**2)/(a**2))+((y**2)/(b**2)))-1

a = 2
b = 4
h=.01
xpoints = np.arange(-a, a, 0.01)
ypoints = f(xpoints, a, b)


answer = 2*np.trapz(ypoints,xpoints)
print('The 1d integral answer is', answer)

xs = np.arange(-4, 4, h)
ys = np.arange(-4, 4, h)
masked_int = 0
for x in xs:
    for y in ys:
        dx = h
        dy = h
        dA = dx*dy
        if (x**2/a**2 + y**2/b**2) <= 1:
            masked_int += dA
print('The masked integral is', masked_int)


