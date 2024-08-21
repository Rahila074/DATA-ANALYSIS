import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Create a figure
fig = plt.figure()

# Define the GridSpec layout: 2 rows x 2 columns
gs = gridspec.GridSpec(2, 2, width_ratios=[2, 1], height_ratios=[1, 2])

# Create subplots with different sizes
ax1 = plt.subplot(gs[0, 0])  # Larger subplot in the upper-left
ax2 = plt.subplot(gs[0, 1])  # Smaller subplot in the upper-right
ax3 = plt.subplot(gs[1, 0])  # Smaller subplot in the lower-left
ax4 = plt.subplot(gs[1, 1])  # Larger subplot in the lower-right

# Plot data
ax1.plot([1, 2, 3], [4, 5, 6])
ax1.set_title('Large subplot 1')

ax2.plot([1, 2, 3], [6, 5, 4])
ax2.set_title('Small subplot 1')

ax3.plot([1, 2, 3], [4, 6, 5])
ax3.set_title('Small subplot 2')

ax4.plot([1, 2, 3], [5, 4, 6])
ax4.set_title('Large subplot 2')

# Adjust layout to fit all subplots neatly
plt.tight_layout()

# Display the plot
plt.show()
