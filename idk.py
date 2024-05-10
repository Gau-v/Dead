import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Random data (replace with your actual data for more realistic analysis)
data_symmetric = np.random.normal(loc=50, scale=10, size=100)  # Symmetrical distribution
data_skewed_right = np.random.lognormal(mean=2.0, size=100) # Skewed right distribution
data_outliers = np.concatenate([data_symmetric, [1000]])  # Add outlier to symmetrical data

# Function to calculate central tendency measures
def calculate_measures(data):
  mean = np.mean(data)
  median = np.median(data)
  mode = np.stats.mode(data)[0]  # Get first mode if multiple exist
  return mean, median, mode

# Calculate measures for each dataset
data_dict = {}
dataset_names = ["Symmetrical", "Skewed Right", "Outliers"]
for i, data in enumerate( [data_symmetric, data_skewed_right, data_outliers]):
  mean, median, mode = calculate_measures(data)
  data_dict[dataset_names[i]] = {"Mean": mean, "Median": median, "Mode": mode}

# Print results in a table format
print("Central Tendency Measures:")
print("{:<20} {:>10} {:>10} {:>10}".format("Dataset", "Mean", "Median", "Mode"))
for name, data in data_dict.items():
  print("{:<20} {:>10.2f} {:>10.2f} {:>10}".format(name, data["Mean"], data["Median"], data["Mode"]))

# Visualizations with Matplotlib (basic examples)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))  # Create a figure with 3 subplots

# Distribution Plots (histograms)
for i, (name, data) in enumerate(data_dict.items()):
  axes[i].hist(data, bins=20, alpha=0.7, label=name)
  axes[i].set_title(f"{name} Distribution")
  axes[i].legend()

# Boxplots
data_frame = pd.DataFrame.from_dict(data_dict, orient='index')
data_frame.boxplot(ax=axes[2])
axes[2].set_title("Boxplots of Central Tendency Measures")

# Display plots
plt.tight_layout()
plt.show()
