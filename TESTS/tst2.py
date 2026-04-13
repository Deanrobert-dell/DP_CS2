import matplotlib as mpl
#linegraph test

import matplotlib.pyplot as plt
import numpy as np

# Sample data: months, incomes, and expenses

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

income_data = [5000, 5200, 4800, 5500, 5300, 5600]

expense_data = [3000, 3100, 2900, 3200, 3100, 3400]
#CHANGE LATER TO BE FROM CSV FILE


# 1. Calculate Average Income (Example: a running average or fixed point)
# For this example, we'll plot the actual income vs its overall mean
avg_income_val = np.mean(income_data)
# Create a list of the same average value for each time point to draw a horizontal line
avg_income_line = [avg_income_val] * len(months) 

# 2. Plotting
plt.figure(figsize=(10, 5))
plt.plot(months, income_data, marker='o', label='Monthly Income')
plt.plot(months, avg_income_line, linestyle='--', color='red', label='Average Income')

# 3. Customization
plt.title('Income Trends Over Time')
plt.xlabel('Time (Months)')
plt.ylabel('Amount ($)')
plt.legend()
plt.grid(True)

# 4. Show the plot
plt.show()
