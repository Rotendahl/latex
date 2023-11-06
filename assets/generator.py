import pandas as pd
import numpy as np


xs = np.linspace(0, 10, 100)
ys = [2 * x + 1 for x in xs]
pd.DataFrame({'x': xs, 'y': ys}).to_csv('assets/data.csv', index=False)
