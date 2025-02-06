import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

# Data for the graph
chunk_sizes = [253, 254, 255, 256, 257, 258, 259]
prefill_times = [1.0, 1.0, 1.0, 1.0, 1.32, 1.32, 1.32]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 9))  # Reduced width of the plot

# Plot the data with customized styles
ax.plot(chunk_sizes, prefill_times, marker='o', markersize=20, linewidth=6, color='#0000CD',
        path_effects=[pe.withStroke(linewidth=10, foreground='black')], label='Prefill Time')



# Customize axes
ax.set_xlabel("Token Budget", fontsize=40, labelpad=30)
ax.set_ylabel("Prefill Time (Relative)", fontsize=40, labelpad=30)
ax.tick_params(axis='both', labelsize=30, width=3, length=10)
ax.set_xticks([254, 256, 257, 259])
ax.set_yticks([1.0, 1.1, 1.2, 1.3])
ax.grid(True, linestyle='--', linewidth=0.7)

# Add legend
ax.legend(fontsize=30, loc='upper left', frameon=False)

plt.tight_layout()
plt.show()
