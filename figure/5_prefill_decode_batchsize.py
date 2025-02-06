import matplotlib.pyplot as plt
import numpy as np

# Data for the bar graphs
batch_sizes_prefill = [1, 2, 4, 8]
prefill_tokens_per_second = [4000, 4500, 4500, 4400]

batch_sizes_decode = [1, 8, 16, 32, 64]
decode_tokens_per_second = [10, 100, 210, 410, 810]

# Generate fixed-width x values for equal spacing
prefill_positions = np.arange(len(batch_sizes_prefill))
decode_positions = np.arange(len(batch_sizes_decode))

# Create the bar graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 9), gridspec_kw={"width_ratios": [1, 1]})

# Prefill bar graph
ax1.bar(prefill_positions, prefill_tokens_per_second, color='#191970', edgecolor='black', linewidth=2, width=0.6)
ax1.set_title("Prefill", fontsize=36)
ax1.set_xlabel("Batch Size", fontsize=36, labelpad=10)
ax1.set_ylabel("Tokens per Second", fontsize=36, labelpad=10)
ax1.set_xticks(prefill_positions)
ax1.set_xticklabels(batch_sizes_prefill, fontsize=30)
ax1.set_yticks([0, 2000, 4000])
ax1.set_yticklabels(["0", "2K", "4K"], fontsize=30)
ax1.tick_params(axis='y', labelsize=30)
ax1.grid(axis='y', linestyle='--', linewidth=0.7)

# Decode bar graph
ax2.bar(decode_positions, decode_tokens_per_second, color='#191970', edgecolor='black', linewidth=2, width=0.6)
ax2.set_title("Decode", fontsize=36)
ax2.set_xlabel("Batch Size", fontsize=36, labelpad=10)
ax2.set_ylabel("Tokens per Second", fontsize=36, labelpad=10)
ax2.set_xticks(decode_positions)
ax2.set_xticklabels(batch_sizes_decode, fontsize=30)
ax2.set_yticks([0, 200, 400, 600, 800])
ax2.set_yticklabels(["0", "200", "400", "600", "800"], fontsize=30)
ax2.tick_params(axis='y', labelsize=30)
ax2.grid(axis='y', linestyle='--', linewidth=0.7)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
