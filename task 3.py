#Python program to  Add Title to Subplots in Matplotlib?


import matplotlib.pyplot as plt

# Create a figure and a grid of subplots
fig, axs = plt.subplots(2, 2)  # 2x2 grid of subplots

# Plot data and add titles to each subplot
axs[0, 0].plot([1, 2, 3], [4, 5, 6])
axs[0, 0].set_title('Top Left')

axs[0, 1].plot([1, 2, 3], [6, 5, 4])
axs[0, 1].set_title('Top Right')

axs[1, 0].plot([1, 2, 3], [4, 6, 5])
axs[1, 0].set_title('Bottom Left')

axs[1, 1].plot([1, 2, 3], [5, 4, 6])
axs[1, 1].set_title('Bottom Right')

# Automatically adjust subplot parameters for a nicer layout
plt.tight_layout()

# Display the plot
plt.show()
