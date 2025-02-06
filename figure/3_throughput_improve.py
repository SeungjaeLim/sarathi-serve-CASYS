import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

# Corrected data for FasterTransformer (2021)
x_ft = [0.1, 1.5, 2]
y_ft = [0.1, 0.5, 0.9]

# Corrected data for Orca (2022)
x_orca = [0.1, 1, 1.5, 2]
y_orca = [0.1, 0.2, 0.4, 1]

# Corrected data for vLLM (2023)
x_vllm = [11, 13, 15, 17, 17.5, 18, 19]
y_vllm = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.9]

# Plotting the data
plt.figure(figsize=(12, 6))
plt.plot(x_ft, y_ft, 'o-', label='FasterTransformer (2021)', color='#87CEFA', linewidth=8, markeredgecolor='black', markeredgewidth=2, path_effects=[pe.withStroke(linewidth=10, foreground='black')])
plt.plot(x_orca, y_orca, 'x-', label='Orca (2022)', color='#4682B4', linewidth=8, markeredgecolor='black', markeredgewidth=2, path_effects=[pe.withStroke(linewidth=10, foreground='black')])
plt.plot(x_vllm, y_vllm, 'o-', label='vLLM (2023)', color='#191970', linewidth=8, markeredgecolor='black', markeredgewidth=2, path_effects=[pe.withStroke(linewidth=10, foreground='black')])

# Adding labels and modifying axes
plt.xlabel('Request rate (req/s)', fontsize=30, labelpad=20)
plt.ylabel('Normalized latency', fontsize=30, labelpad=20)
plt.xticks([5, 10, 15, 20], fontsize=26)
plt.yticks([0.4, 0.8], fontsize=26)
plt.ylim(0, 0.8)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.18), ncol=3, fontsize=22, frameon=False)
plt.grid(alpha=0.3)

# Adjust layout to prevent clipping
plt.tight_layout()

# Show plot
plt.show()
