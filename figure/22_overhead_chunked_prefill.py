import matplotlib.pyplot as plt
import numpy as np

# Data for the Prefill Length bar graph
prefill_lengths = ["2K", "4K", "8K"]
overhead_512 = [1.26, 1.3, 1.25]
overhead_1024 = [1.23, 1.24, 1.2]
overhead_2048 = [1.0, 1.03, 0.99]

# Generate positions for the bars
prefill_positions = np.arange(len(prefill_lengths))
bar_width = 0.25

# Create the bar graph
fig, ax = plt.subplots(figsize=(18, 8))

# Plot the bars
ax.bar(prefill_positions - bar_width, overhead_512, color='#87CEEB', edgecolor='black', linewidth=2, width=bar_width, label='512')
ax.bar(prefill_positions, overhead_1024, color='#4682B4', edgecolor='black', linewidth=2, width=bar_width, label='1024')
ax.bar(prefill_positions + bar_width, overhead_2048, color='#191970', edgecolor='black', linewidth=2, width=bar_width, label='2048')

# Add horizontal line at y = 1.0
ax.axhline(y=1.0, color='red', linestyle='--', linewidth=2)

# Add titles and labels
ax.set_xlabel("Prefill Length", fontsize=36, labelpad=10)
ax.set_ylabel("Overhead", fontsize=36, labelpad=10)
ax.set_xticks(prefill_positions)
ax.set_xticklabels(prefill_lengths, fontsize=30)
ax.set_yticks([0, 0.5, 1.0, 1.5])
ax.set_yticklabels(["0", "0.5", "1.0", "1.5"], fontsize=30)
ax.tick_params(axis='y', labelsize=30)
ax.grid(axis='y', linestyle='--', linewidth=0.7)
ax.legend(fontsize=30, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=3, frameon=False)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
