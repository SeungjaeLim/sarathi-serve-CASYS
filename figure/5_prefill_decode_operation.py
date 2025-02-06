import matplotlib.pyplot as plt
import numpy as np

# Data for the stacked bar graphs
sequence_lengths = [128, 256, 512, 1024, 2048]
prefill_total = [25, 30, 45, 75, 140]  # Total lengths for Prefill
prefill_attention = [2, 3, 4, 5, 6]  # Smaller attention values
prefill_others = [1, 2, 3, 5, 9]  # Adjust others to maintain total
prefill_linear = [t - a - o for t, a, o in zip(prefill_total, prefill_attention, prefill_others)]

decode_batch_sizes = [1, 8, 16, 32, 64]
decode_linear = [8, 8, 8, 8, 8]  # Decode linear remains dominant
decode_attention = [2, 2, 2, 2, 2]
decode_others = [1, 1, 1, 1, 1]

# Create positions for the bars
prefill_positions = np.arange(len(sequence_lengths))
decode_positions = np.arange(len(decode_batch_sizes))

# Create the bar graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 9), gridspec_kw={"width_ratios": [1, 1]})

# Prefill stacked bar graph
ax1.bar(prefill_positions, prefill_linear, color='#00008B', edgecolor='black', linewidth=2, width=0.6, label='linear')
ax1.bar(prefill_positions, prefill_attention, bottom=prefill_linear, color='#4682B4', edgecolor='black', linewidth=2, width=0.6, label='attention')
ax1.bar(prefill_positions, prefill_others, bottom=np.array(prefill_linear) + np.array(prefill_attention), color='#87CEEB', edgecolor='black', linewidth=2, width=0.6, label='others')
ax1.set_title("Prefill", fontsize=36)
ax1.set_xlabel("Sequence Length", fontsize=36, labelpad=10)
ax1.set_ylabel("Time (ms)", fontsize=36, labelpad=10)
ax1.set_xticks(prefill_positions)
ax1.set_xticklabels(sequence_lengths, fontsize=30)
ax1.set_yticks([0, 50, 100, 150])
ax1.set_yticklabels(["0", "50", "100", "150"], fontsize=30)
ax1.tick_params(axis='y', labelsize=30)
ax1.grid(axis='y', linestyle='--', linewidth=0.7)
ax1.legend(fontsize=24, loc='upper left')

# Decode stacked bar graph
ax2.bar(decode_positions, decode_linear, color='#00008B', edgecolor='black', linewidth=2, width=0.6, label='linear')
ax2.bar(decode_positions, decode_attention, bottom=decode_linear, color='#4682B4', edgecolor='black', linewidth=2, width=0.6, label='attention')
ax2.bar(decode_positions, decode_others, bottom=np.array(decode_linear) + np.array(decode_attention), color='#87CEEB', edgecolor='black', linewidth=2, width=0.6, label='others')
ax2.set_title("Decode", fontsize=36)
ax2.set_xlabel("Batch Size", fontsize=36, labelpad=10)
ax2.set_ylabel("Time (ms)", fontsize=36, labelpad=10)
ax2.set_xticks(decode_positions)
ax2.set_xticklabels(decode_batch_sizes, fontsize=30)
ax2.set_yticks([0, 50, 100, 150])
ax2.set_yticklabels(["0", "50", "100", "150"], fontsize=30)
ax2.tick_params(axis='y', labelsize=30)
ax2.grid(axis='y', linestyle='--', linewidth=0.7)
ax2.legend(fontsize=24, loc='upper left')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
