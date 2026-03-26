import matplotlib.pyplot as plt

# Data to plot
labels = ['entertainment', 'food', 'gas', 'rent']
sizes = [35, 25, 25, 15]

# Create the pie chart
plt.pie(sizes, labels=labels)

# Display the chart
plt.show()


"""import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv('medal_data.csv')

# 2. Extract columns
labels = df["country"]
sizes = df["gold_medal"]

# 3. Create pie chart
plt.figure(figsize=(8, 8)) # Set figure size for better readability
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Gold Medal Distribution")
plt.axis('equal') # Ensure pie is circular

# 4. Display
plt.show()"""