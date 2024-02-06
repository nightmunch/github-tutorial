print("zati ada kucing namanya kopiko")
print("bukan sara punya kucing")

import numpy as np
import matplotlib.pyplot as plt

def best_fit_line(x, y):
    coefficients = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coefficients)
    line_x = np.linspace(min(x), max(x), 100)
    line_y = polynomial(line_x)
    
    plt.scatter(x, y)
    plt.plot(line_x, line_y, color='red')
    plt.show()

    # acah iler do dak data science ni
