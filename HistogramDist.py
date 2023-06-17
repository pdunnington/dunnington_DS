#Patrick Dunnington orientation tasks
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

binom=np.random.binomial
psn=np.random.poisson(lam=1.0, size=None)
xisqr=np.random.chisquare
plt.hist(binom)
plt.title("Binomial Dist")
plt.hist(psn)
plt.title("Poisson Dist")
plt.hist(xisqr)
plt.title("Xi-Squared Dist")
plt.show()