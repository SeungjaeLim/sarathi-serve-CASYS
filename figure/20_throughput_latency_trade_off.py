import matplotlib.pyplot as plt
import numpy as np

# Data estimation from the provided graph for both Mistral-7B and Yi-34B
x_mistral = [0.1, 0.2, 0.3, 0.4, 0.5]
y_mistral_vLLM_32 = [0.8, 1.0, 1.2, 1.38, 1.4]
y_mistral_vLLM_64 = [0.8, 1.0, 1.2, 1.4, 1.6]
y_mistral_vLLM_128 = [0.8, 1.0, 1.2, 1.4, 1.6]
y_mistral_SS_512 = [2.05, 2.0, 2.0, 2.0, 2.0]
y_mistral_SS_2048 = [0.5, 1.7, 2.3, 2.3, 2.3]

x_yi = [0.2, 0.4, 0.6, 0.8, 1.0]
y_yi_vLLM_32 = [0.3, 0.45, 0.6, 0.65, 0.8]
y_yi_vLLM_64 = [0.3, 0.45, 0.6, 0.65, 0.8]
y_yi_vLLM_128 = [0.3, 0.44, 0.59, 0.64, 0.79]
y_yi_SS_512 = [1.15, 1.15, 1.15, 1.15, 1.15]
y_yi_SS_2048 = [0.2, 0.45, 1.3, 1.3, 1.3]

# Plotting both graphs horizontally
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(26, 9))  # Increased width by 1.3x

marker_size = 20  # Increased marker size
line_width = 8  # Increased line width

# Update marker styles
marker_styles = {'vLLM-32': 'o', 'vLLM-64': 's', 'vLLM-128': 'd', 'SS-512': '^', 'SS-2048': 'p'}

def plot_graph(ax, x, y_data, labels, colors):
    for y, label, color in zip(y_data, labels, colors):
        ax.plot(
            x, y, marker=marker_styles[label], markersize=marker_size, linewidth=line_width, label=label,
            color=color, markeredgewidth=3, markeredgecolor='black'
        )

# Mistral-7B Graph
y_data_mistral = [y_mistral_vLLM_32, y_mistral_vLLM_64, y_mistral_vLLM_128, y_mistral_SS_512, y_mistral_SS_2048]
labels_mistral = ['vLLM-32', 'vLLM-64', 'vLLM-128', 'SS-512', 'SS-2048']
colors_mistral = ['#87CEEB', '#87CEEB', '#87CEEB', '#191970', '#191970']
plot_graph(ax1, x_mistral, y_data_mistral, labels_mistral, colors_mistral)
ax1.set_xlabel("P99 TBT SLO (s)", fontsize=50, labelpad=30)
ax1.set_ylabel("Max Capacity", fontsize=50, labelpad=30)
ax1.set_title("Mistral-7B", fontsize=60, pad=30)
ax1.tick_params(axis='both', labelsize=40)
ax1.set_xticks([0.1, 0.2, 0.3, 0.4, 0.5])
ax1.set_yticks([0.5, 1.5, 2.5])
ax1.grid(True, linestyle='--', linewidth=0.7)

# Yi-34B Graph
y_data_yi = [y_yi_vLLM_32, y_yi_vLLM_64, y_yi_vLLM_128, y_yi_SS_512, y_yi_SS_2048]
labels_yi = ['vLLM-32', 'vLLM-64', 'vLLM-128', 'SS-512', 'SS-2048']
colors_yi = ['#87CEEB', '#87CEEB', '#87CEEB', '#191970', '#191970']
plot_graph(ax2, x_yi, y_data_yi, labels_yi, colors_yi)
ax2.set_xlabel("P99 TBT SLO (s)", fontsize=50, labelpad=30)
ax2.set_ylabel("Max Capacity", fontsize=50, labelpad=30)
ax2.set_title("Yi-34B", fontsize=60, pad=30)
ax2.tick_params(axis='both', labelsize=40)
ax2.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0])
ax2.set_yticks([0.5, 1.0, 1.5])
ax2.grid(True, linestyle='--', linewidth=0.7)

# Add shared legend
fig.legend(labels_mistral, loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=5, fontsize=40, frameon=False)

plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()
