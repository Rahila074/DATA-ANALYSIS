
#Python program to Place Legend Outside of the Plot in Matplotlib?
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y1, label='Series 1')
plt.plot(x, y2, label='Series 2')

# Add a legend outside the plot
# loc='upper left' places the legend at the upper-left corner relative to the bbox
# bbox_to_anchor=(1, 1) moves the legend outside the plot area
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout to ensure the plot and legend do not overlap
plt.tight_layout()

# Display the plot
plt.show()
