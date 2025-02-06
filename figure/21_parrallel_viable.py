import matplotlib.pyplot as plt
import numpy as np

# Data for the TBT (Batch Size) bar graph
batch_sizes = [8, 16, 32, 64, 128]
tbt_tp8 = [0.19, 0.21, 0.22, 0.25, 0.35]  # TP8
p50_tp4_pp2 = [0.08, 0.09, 0.1, 0.12, 0.15]  # TP4:PP2

# Data for the SLO bar graph
slo_categories = ["SLO-S", "SLO-R"]
slo_tp8 = [0.12, 0.14]  # vLLM TP8
slo_tp4_pp2 = [0.2, 0.5]  # vLLM TP4:PP2
slo_sarathi = [0.6, 0.75]  # Sarathi-Serve TP4:PP2

# Generate positions for the bars
batch_positions = np.arange(len(batch_sizes))
slo_positions = np.arange(len(slo_categories))
bar_width = 0.25

# Create the bar graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(27, 9))

# TBT (Batch Size) bar graph
ax1.bar(batch_positions - bar_width/2, tbt_tp8, color='#87CEEB', edgecolor='black', linewidth=2, width=bar_width, label='vLLM TP8')
ax1.bar(batch_positions + bar_width/2, p50_tp4_pp2, color='#4682B4', edgecolor='black', linewidth=2, width=bar_width, label='vLLM TP4:PP2')

ax1.set_xlabel("Batch Size", fontsize=48, labelpad=10)
ax1.set_ylabel("P50 TBT (s)", fontsize=48, labelpad=10)
ax1.set_xticks(batch_positions)
ax1.set_xticklabels(batch_sizes, fontsize=42)
ax1.set_yticks([0, 0.1, 0.2, 0.3])
ax1.set_yticklabels(["0", "0.1", "0.2", "0.3"], fontsize=42)
ax1.tick_params(axis='y', labelsize=42)
ax1.grid(axis='y', linestyle='--', linewidth=0.7)
ax1.legend(fontsize=36, loc='upper left')

# SLO bar graph
ax2.bar(slo_positions - bar_width, slo_tp8, color='#87CEEB', edgecolor='black', linewidth=2, width=bar_width, label='vLLM TP8')
ax2.bar(slo_positions, slo_tp4_pp2, color='#4682B4', edgecolor='black', linewidth=2, width=bar_width, label='vLLM TP4:PP2')
ax2.bar(slo_positions + bar_width, slo_sarathi, color='#191970', edgecolor='black', linewidth=2, width=bar_width, label='Sarathi-Serve TP4:PP2')

ax2.set_xlabel("SLO", fontsize=48, labelpad=10)
ax2.set_ylabel("Max Capacity", fontsize=48, labelpad=10)
ax2.set_xticks(slo_positions)
ax2.set_xticklabels(slo_categories, fontsize=42)
ax2.set_yticks([0, 0.5, 1.0])
ax2.set_yticklabels(["0", "0.5", "1.0"], fontsize=42)
ax2.tick_params(axis='y', labelsize=42)
ax2.grid(axis='y', linestyle='--', linewidth=0.7)
ax2.legend(fontsize=36, loc='upper left')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
