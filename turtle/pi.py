import matplotlib.pyplot as plt

# Data to plot
labels = ['entertainment', 'food', 'gas', 'rent']
sizes = [35, 25, 25, 15]

# Create the pie chart
plt.pie(sizes, labels=labels)

# Display the chart
plt.show()
