import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

data = [10, 12, 11, 13, 12, 14, 13, 15, 14, 16]

model =AutoReg(data,lags=1).fit()
pred = model.predict(start=0, end=len(data)-1)
plt.plot(data, label='Actual')
plt.plot(pred, label='Predicted')
plt.legend()
plt.show()
