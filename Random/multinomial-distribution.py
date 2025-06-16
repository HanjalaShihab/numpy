import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.multinomial(n=6, pvals=(1/6,1/6,1/6,1/6,1/6,1/6))
print(data)

sns.displot(data, kind='kde')
plt.show()
