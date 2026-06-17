import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Exam": ["CS", "Physics", "Calculus", "Anatomy"],
    "Alice": [90, 85, 80, 88],
    "Bob": [85, 87, 82, 90],
    "Charlie": [88, 90, 84, 86],
    "Diana": [92, 88, 85, 89]
})

fig, axes = plt.subplots(4,1, figsize = (10,10), sharex=True)
axes[0].bar(df['Exam'], df['Alice'], color = 'blue')
axes[0].set_title('Alice Score')
axes[0].set_ylabel('Score')

axes[1].bar(df['Exam'], df['Bob'], color = 'green')
axes[1].set_title('Bob Score')
axes[1].set_ylabel('Score')

axes[2].bar(df['Exam'], df['Charlie'], color = 'yellow')
axes[2].set_title('Charlie Score')
axes[2].set_ylabel('Score')

axes[3].bar(df['Exam'], df['Diana'], color = 'brown')
axes[3].set_title('Diana Score')
axes[3].set_ylabel('Score')

plt.xlabel('Subjects')
plt.show()






#Example
#fig, axes = plt.subplots(2, 1, figsize=(8, 8), sharex=True)
#axes[0].bar(df['Month'], df['Sales'], color='skyblue')
#axes[0].set_title('Monthly Sales')
#axes[0].set_ylabel('Sales Amount')
#axes[1].bar(df['Month'], df['Profit'], color='lightgreen')
#axes[1].set_title('Monthly Profit')
#axes[1].set_ylabel('Profit Amount')
#plt.xlabel("Month")
#plt.show()


#Solution: This is better
axes[0, 0].bar(df['Exam'], df['Alice'], label='Alice', color='pink')
axes[0, 1].bar(df['Exam'], df['Bob'], label='Bob', color='blue')
axes[1, 0].bar(df['Exam'], df['Charlie'], label='Charlie', color='green')
axes[1, 1].bar(df['Exam'], df['Diana'], label='Diana', color='aqua')

axes[0, 0].set_xlabel('Exam')
axes[0, 0].set_ylabel('Score')

axes[0, 1].set_xlabel('Exam')
axes[0, 1].set_ylabel('Score')

axes[1, 0].set_xlabel('Exam')
axes[1, 0].set_ylabel('Score')

axes[1, 1].set_xlabel('Exam')
axes[1, 1].set_ylabel('Score')

axes[0, 0].set_title('Alice')
axes[0, 1].set_title('Bob')
axes[1, 0].set_title('Charlie')
axes[1, 1].set_title('Diana')

axes[0, 0].legend()
axes[0, 1].legend()
axes[1, 0].legend()
axes[1, 1].legend()

plt.show()