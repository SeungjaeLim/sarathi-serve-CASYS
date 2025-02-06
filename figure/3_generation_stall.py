import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

# Generate random staircase pattern
def generate_staircase_data(start_x, end_x, num_points):
    np.random.seed(42)
    x = [start_x]
    y = [0]
    current_x = start_x
    current_y = 0
    flat_segments = []  # Store flat segments

    while current_x < end_x:
        if current_x < 80:
            # Ensure first 80 units of x have y = 0
            current_x += 1
            x.append(current_x)
            y.append(0)
            continue

        # Adjust slope range based on position
        if current_x < 150:
            slope = np.random.uniform(0.5, 3.0) * 275  # Higher slopes in the early phase
        else:
            slope = np.random.uniform(0.2, 1) * 275  # Lower slopes in the later phase

        duration = np.random.uniform(5, 20)  # Random duration in x-axis
        flat_duration = np.random.uniform(5, 15)  # Random flat duration

        # Increase phase
        for _ in range(int(duration)):
            current_x += 1
            current_y += slope
            x.append(current_x)
            y.append(current_y)
            if current_x >= end_x:
                break

        if current_x >= end_x:
            break

        # Flat phase
        flat_start = current_x
        for _ in range(int(flat_duration)):
            current_x += 1
            x.append(current_x)
            y.append(current_y)
            if current_x >= end_x:
                break
        flat_segments.append((flat_start, current_x))  # Store start and end of flat segment

    return np.array(x), np.array(y), flat_segments

# Generate main graph data
time, tokens_generated, flat_segments = generate_staircase_data(0, 300, 301)

# Extract inset graph data (focused on generation stall)
inset_indices = (time >= 210) & (time <= 250)
inset_time = time[inset_indices]
inset_tokens = tokens_generated[inset_indices]

# Create the main plot
fig, ax = plt.subplots(figsize=(15, 9))  # Adjust to 5:3 aspect ratio
ax.plot(time, tokens_generated, color='#0000CD', linewidth=7.5, label='vLLM', path_effects=[pe.withStroke(linewidth=10, foreground='black')])

# Highlight flat segments in red
for start, end in flat_segments:
    flat_indices = (time >= start) & (time <= end)
    ax.plot(time[flat_indices], tokens_generated[flat_indices], color='red', linewidth=7.5)

ax.set_xlabel("Time (s)", fontsize=40, labelpad=20)
ax.set_ylabel("Tokens Generated", fontsize=40, labelpad=20)
ax.set_xticks(range(0, 301, 100))  # Set x-axis ticks at 100 intervals
ax.set_yticks([0, 10000, 20000, 30000])
ax.set_yticklabels(["0k", "10k", "20k", "30k"], fontsize=36)
ax.tick_params(axis='x', which='major', labelsize=36, width=2, length=6)
ax.tick_params(axis='y', which='major', labelsize=36, width=2, length=6)
ax.grid(True, linestyle='--', linewidth=0.7)
ax.legend(fontsize=32, loc='upper left', frameon=False)

# Create inset plot
inset_ax = fig.add_axes([0.6, 0.25, 0.25, 0.25])  # Move the inset plot slightly upward
inset_ax.plot(inset_time, inset_tokens, color='#0000CD', linewidth=7.5, path_effects=[pe.withStroke(linewidth=10, foreground='black')])

# Highlight flat segments in inset plot
for start, end in flat_segments:
    flat_indices = (inset_time >= start) & (inset_time <= end)
    inset_ax.plot(inset_time[flat_indices], inset_tokens[flat_indices], color='red', linewidth=7.5)

inset_ax.set_xlim(210, 250)  # Adjust x-axis range
inset_ax.set_xticks([210, 230, 250])  # Keep only specific x-ticks
inset_ax.tick_params(axis='x', which='major', labelsize=20, width=1.5, length=4)
inset_ax.tick_params(axis='y', left=False, labelleft=False)  # Remove y-axis

# Adjust layout to prevent clipping
plt.tight_layout()

# Show plot
plt.show()
