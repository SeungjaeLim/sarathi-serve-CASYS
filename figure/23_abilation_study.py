import matplotlib.pyplot as plt
import numpy as np

# Data for the two graphs (P50TTFT and P99TBT)
x_labels = ["sharegpt4", "arxiv"]
p50_ttft_data = [[0.53, 3.78], [1.04, 5.38], [0.76, 3.9]]  # Data for P50TTFT
p99_tbt_data = [[0.68, 1.38], [0.17, 0.2], [0.14, 0.17]]  # Data for P99TBT

# Define positions and bar width
x_positions = np.arange(len(x_labels))
bar_width = 0.25

# Create subplots for P50TTFT and P99TBT
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20.8, 8), sharey=False)  # Width increased by 1.3x

# Colors for each scheduler
colors = ['#87CEEB', '#4682B4', '#191970']
labels = ['hybrid-batching-only', 'chunked-prefills-only', 'Sarathi-Serve']

# Plot P50TTFT data
for i in range(len(p50_ttft_data)):
    ax1.bar(x_positions + (i - 1) * bar_width, p50_ttft_data[i], color=colors[i], edgecolor='black', linewidth=2, 
            width=bar_width, label=labels[i])

# Add details to P50TTFT graph
ax1.set_xticks(x_positions)
ax1.set_xticklabels(x_labels, fontsize=36)
ax1.set_ylabel("P50 TTFT (s)", fontsize=48)
ax1.set_yticks([1, 3, 5])
ax1.tick_params(axis='y', labelsize=36)
ax1.grid(axis='y', linestyle='--', linewidth=0.7)

# Plot P99TBT data
for i in range(len(p99_tbt_data)):
    ax2.bar(x_positions + (i - 1) * bar_width, p99_tbt_data[i], color=colors[i], edgecolor='black', linewidth=2, 
            width=bar_width, label=labels[i])

# Add details to P99TBT graph
ax2.set_xticks(x_positions)
ax2.set_xticklabels(x_labels, fontsize=36)
ax2.set_ylabel("P99 TBT (s)", fontsize=48)
ax2.set_yticks([0.3, 0.8, 1.3])
ax2.tick_params(axis='y', labelsize=36)
ax2.grid(axis='y', linestyle='--', linewidth=0.7)

# Add a single legend above the graphs
fig.legend(labels, loc='upper center', bbox_to_anchor=(0.5, 0.93), ncol=3, fontsize=36, frameon=False)

# Adjust layout and show the plot
plt.tight_layout(rect=[0, 0, 1, 0.8])
plt.show()
