import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


def logistic_map(x0, r, n):
    i = 1
    y = []
    while i <= n:
        xn=r*x0*(1-x0)
        x0=xn        
        y.append(abs(xn))
        i += 1
    return sns.scatterplot(x=range(n),y=y)


def bifurcation_diagram(r_min, r_max, r_step, n):
    x_values = np.linspace(r_min, r_max, int((r_max-r_min)/r_step))
    X = []
    Y = []
    for r in x_values:
        X.append(r)
        x = np.random.random()
        for i in range(n):
            x = x*r*(1-x)
        Y.append(x)
    return plt.plot(X, Y, ls='', marker=',')

