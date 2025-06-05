import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0,1,2,3,4,5])
plt.show()



#diplots of another kind:
sns.displot([1,2,3,4,5,6], kind='kde')
plt.show