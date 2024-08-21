#python program to Remove the legend border in Matplotlib?
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y1, label='Series 1')
plt.plot(x, y2, label='Series 2')

# Add a legend and remove its border
plt.legend(frameon=False)  # frameon=False removes the border

# Display the plot
plt.show()
