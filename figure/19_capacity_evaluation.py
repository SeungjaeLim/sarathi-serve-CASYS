import matplotlib.pyplot as plt
import numpy as np

# Data for the bar graph
slo_categories = ["Strict SLO (SLO-S)", "Relaxed SLO (SLO-R)"]
mistral_data = [0.1, 0.5]  # Mistral-7B values
yi_data = [0.2, 1.0]  # Yi-34B values
orca_data = [[0.6, 0.3], [1.1, 0.45]]  # Orca values
vllm_data = [[0.65, 0.35], [1.5, 0.75]]  # vLLM values
sarathi_data = [[2.1, 1.1], [2.4, 1.2]]  # Sarathi-Serve values

# Generate positions for the bars
x_positions = np.arange(len(slo_categories))
bar_width = 0.3

fig, ax = plt.subplots(1, 2, figsize=(27, 12), sharey=True)

# Strict SLO (SLO-S)
ax[0].bar(x_positions - bar_width, orca_data[0], color='#87CEEB', edgecolor='black', linewidth=2, width=bar_width, label='Orca')
ax[0].bar(x_positions, vllm_data[0], color='#4682B4', edgecolor='black', linewidth=2, width=bar_width, label='vLLM')
ax[0].bar(x_positions + bar_width, sarathi_data[0], color='#191970', edgecolor='black', linewidth=2, width=bar_width, label='Sarathi-Serve')

# Relaxed SLO (SLO-R)
ax[1].bar(x_positions - bar_width, orca_data[1], color='#87CEEB', edgecolor='black', linewidth=2, width=bar_width, label='Orca')
ax[1].bar(x_positions, vllm_data[1], color='#4682B4', edgecolor='black', linewidth=2, width=bar_width, label='vLLM')
ax[1].bar(x_positions + bar_width, sarathi_data[1], color='#191970', edgecolor='black', linewidth=2, width=bar_width, label='Sarathi-Serve')

# Set x-axis labels
ax[0].set_xticks(x_positions)
ax[0].set_xticklabels(["Mistral-7B\n(0.1s)", "Yi-34B\n(0.2s)"], fontsize=64)
ax[0].set_xlabel("Strict SLO (SLO-S)", fontsize=64, labelpad=30)

ax[1].set_xticks(x_positions)
ax[1].set_xticklabels(["Mistral-7B\n(0.5s)", "Yi-34B\n(1.0s)"], fontsize=64)
ax[1].set_xlabel("Relaxed SLO (SLO-R)", fontsize=64, labelpad=30)

# Set shared y-axis labels and limits
ax[0].set_ylabel("Max Capacity", fontsize=64, labelpad=30)
for a in ax:
    a.set_yticks([0, 1, 2])
    a.set_yticklabels(["0", "1", "2"], fontsize=64)
    a.tick_params(axis='y', labelsize=64)
    a.grid(axis='y', linestyle='--', linewidth=1.0)

# Add legend above the plots
fig.legend(labels=["Orca", "vLLM", "Sarathi-Serve"], fontsize=64, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=3, frameon=False)

# Adjust layout to merge the subplots
plt.tight_layout(rect=[0, 0, 1, 0.9], w_pad=0.5)
plt.show()
