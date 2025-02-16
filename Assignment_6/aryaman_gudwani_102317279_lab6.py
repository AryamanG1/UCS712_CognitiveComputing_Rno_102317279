# -*- coding: utf-8 -*-
"""Aryaman_Gudwani_102317279_Lab6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yxWW0qScKf4oOSGrGhH8tJhKW64UFS45
"""

# Q1. Ask the user to enter a value (e.g., M) for a mathematical function.
#  Generate x values from -10 to 10 using np.linspace().
#  Compute y values for:
# o y= M⋅x2
# o y=M⋅sin(x)
#  Plot both functions in a single figure:
# o Use different colors and line styles.
# o Add legend, grid, and title.

import numpy as np
import matplotlib.pyplot as plt

M = int(input("Please enter value for M: "))
x = np.linspace(-10,10,100)
y1 = M*(x**2)
y2 = M * np.sin(x)
plt.plot(x,y1,'g--',label="y = Mx2")
plt.plot(x,y2,'r',label="y = M*sin(x)")
plt.legend()
plt.grid()
plt.show()

# Q.2 Create a dataset of five subjects and scores.
#  Convert it into a Pandas DataFrame.
#  Plot the scores using a Seaborn bar plot with:
# o Different colors for each bar.
# o Annotations on top of each bar.
# o Title, axis labels, and grid.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subjects":["English","Maths","Science","Hindi","SST"],
    "Scores":[89,95,97,72,100]
}

df = pd.DataFrame(data);
graph = sns.barplot(x="Subjects",y="Scores",data = df,palette = 'husl')

for bar in graph.patches:
  plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height()}',ha='center', va='bottom')

graph.set_title('Subject Scores')
graph.set_xlabel('Subjects')
graph.set_ylabel('Scores')
plt.grid()
plt.show()

# Q3. Write a Python script to select your roll number as seed for NumPy and
# then generate a dataset of 50 values using np.random.randn().
#  Create a 2x2 subplot layout displaying:
# o Line plot showing cumulative sum.
# o Scatter plot with random noise.
#  Customize with titles, axis labels, and grids.
import numpy as np
import matplotlib.pyplot as plt


roll = int(input("Enter your roll number: "))
np.random.seed(roll)
dataset=np.random.randn(50)
print(dataset)

figures,axs = plt.subplots(1,2)

axs[0].plot(np.cumsum(dataset))
axs[0].set_title("Cumulative Sum")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Y")
axs[0].grid()

axs[1].scatter(np.random.rand(20),np.random.rand(20))
axs[1].set_title("Scatter")
axs[1].set_xlabel("X")
axs[1].set_ylabel("Y")
axs[1].grid()

plt.show()

# Q.4 Download Data-set from the below link
# https://github.com/AnjulaMehto/MCA/blob/main/company_sales_data.csv
# Apply ‘seaborn’ library to do the following.
# 1. Read Total profit of all months and show it using a line plot.
# 2. Read all product sales data and show it using a multiline plot.
# 3. Plot bar chart for all the features/attributes.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/AnjulaMehto/MCA/refs/heads/main/company_sales_data.csv"
dataframe = pd.read_csv(url)
dataframe.head()

graph = sns.lineplot(x="month_number", y="total_profit", data=dataframe)
graph.set_title("Net Profit")
plt.show()


for column in dataframe.columns[1:6]:
  sns.lineplot(x=dataframe["month_number"], y=dataframe[column], label=column, marker="o")

plt.show()

for column in dataframe.columns[1:6]:
    sns.barplot(x="month_number", y=column, data=dataframe, label=column, alpha=0.7)