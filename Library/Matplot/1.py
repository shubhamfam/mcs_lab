import pandas as pd
import matplotlib.pyplot as plt  
import numpy as np

series = {'month_number': [1,2,3,4,5,6,7,8,9,10,11,12],
'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890,4780,5860,6100,8300,7300,7400],
'bathingsoap': [9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400],
'shampoo': [1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800],
'moisturizer': [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760],
'total_units': [21100,18330,22470,22270,20960,20140,29550,36140,23400,26670,41280,30020],
'total_profit': [211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]}

#1.Read face cream and facewash product sales data and show it using the bar chart

dataframe = pd.DataFrame(series)

facecream_data = dataframe['facecream'].tolist()
facewash_data = dataframe['facewash'].tolist()

x = np.arange(1,len(dataframe['month_number'])+1)
print(x)
plt.bar(x - 0.2, dataframe.facewash,width=0.5, label= 'Facewash', color = "blue" )
plt.bar(x + 0.2, dataframe.facecream,width=0.5, label='Facecream',color ='black')
plt.legend()
plt.xlabel("Months")
plt.ylabel("Sold units number ")
plt.xticks(np.arange(1, 13))
plt.show()


#2.Calculate total sale data for last year for each product and show it using a Pie chart

labels = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
sales_data = list(map(lambda label: dataframe[label].sum(), labels))
plt.axis("equal")
plt.pie(sales_data, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()

#3.Read all product sales data and show it using the stack plot

plt.stackplot(dataframe['month_number'], dataframe['facecream'], dataframe['facewash'], dataframe['toothpaste'], 
              dataframe['bathingsoap'], dataframe['shampoo'], dataframe['moisturizer'], 
              colors=['m','c','r','k','g','y'], labels=labels)

plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.title('Alll product sales data using stack plot')
plt.legend(loc='upper left')
plt.show()