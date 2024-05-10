import pandas as pd
import matplotlib.pyplot as plt

# Predefined datasets (replace with your actual data)
data_symmetric = [50, 52, 48, 51, 49, 53, 55, 47, 54, 50, 46, 48, 52, 51]  # Symmetrical distribution
data_skewed_right = [10, 12, 15, 18, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]  # Skewed right distribution
data_outliers = data_symmetric + [1000]  # Add outlier to symmetrical data

# Function to calculate central tendency measures
def calculate_measures(data):
  """
  This function calculates the mean, median, and mode of a given dataset.
  """
  mean = sum(data) / len(data)
  median = sorted(data)[int(len(data) / 2)] if len(data) % 2 != 0 else (sorted(data)[int(len(data) / 2) - 1] + sorted(data)[int(len(data) / 2)]) / 2  # Median for even and odd length data
  mode = max(set(data), key=data.count)  # Mode - value with highest frequency
  return mean, median, mode

# Calculate measures for each dataset
results = {}
dataset_names = ["Symmetrical", "Skewed Right", "Outliers"]
for i, data in enumerate( [data_symmetric, data_skewed_right, data_outliers]):
  mean, median, mode = calculate_measures(data)
  results[dataset_names[i]] = {"Mean": mean, "Median": median, "Mode": mode}

# Print results in a table format
print("Central Tendency Measures:")
print("{:<20} {:>10} {:>10} {:>10}".format("Dataset", "Mean", "Median", "Mode"))
for name, data in results.items():
  print("{:<20} {:>10.2f} {:>10.2f} {:>10}".format(name, data["Mean"], data["Median"], data["Mode"]))

# Visualizations with Matplotlib (basic examples)
fig, axes = plt.subplots(1, 3, figsize=(12, 4))  # Create a figure with 3 subplots

# Distribution Plots (histograms)
for i, (name, data) in enumerate(results.items()):
  axes[i].hist(data, bins=10, alpha=0.7, label=name)
  axes[i].set_title(f"{name} Distribution")
  axes[i].legend()

# Boxplots
data_frame = pd.DataFrame.from_dict(results, orient='index')
data_frame.boxplot(ax=axes[2])
axes[2].set_title("Boxplots of Central Tendency Measures")

# Display plots
plt.tight_layout()
plt.show()
