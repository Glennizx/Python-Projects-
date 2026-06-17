import matplotlib.pyplot as plt
import pandas as pd



data = {
  'hours': [1, 2, 3, 4, 5, 6, 7, 8],
  'scores': [55, 30, 56, 70, 72, 81, 81, 92]
}

df = pd.DataFrame(data)
print(df)

plt.scatter(df['hours'], df['scores'])

plt.title('Study Time vs. Test Score')
plt.xlabel('Study Time (Hours)')
plt.ylabel('Test Score')

plt.show() 