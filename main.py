# generate a sample of random gaussians
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(1)

# Create a dataset with numeric data.
sample = [s for s in range(0, 100000, 200)]

# Take increasingly larger samples from the dataset and generate the mean value for each sample.
meanValue = [np.mean(2 * np.random.randn(item) + 50) for item in sample]

# Display the amount by which each sample mean varies from the true population mean.
graph = sns.scatterplot(x=sample, y=(np.array(meanValue) - 50))
graph.axhline(0, color='red', linewidth=2, alpha=0.5)
graph.set(xlabel='Sample size', ylabel='sample mean - population mean')
graph.set_title('The law of large numbers')

plt.show()
