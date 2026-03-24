import matplotlib.pyplot as plt

# Data to plot
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [35, 25, 25, 15]

# Create the pie chart
plt.pie(sizes, labels=labels)

# Display the chart
plt.show()
