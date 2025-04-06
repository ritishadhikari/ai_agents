import matplotlib.pyplot as plt 
# Data to plot 
labels = ['ETFs', 'Bitcoin', 'Bonds', 'Tesla'] 
sizes = [50, 20, 20, 10] 
colors = ['gold', 'lightcoral', 'lightskyblue', 'yellowgreen'] 
# Plotting the pie chart 
plt.figure(figsize=(8, 8)) 
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140) 
plt.axis('equal') 
# Equal aspect ratio ensures that pie is drawn as a circle. 
plt.title('Investment Distribution') 
# Show the chart 
plt.show()