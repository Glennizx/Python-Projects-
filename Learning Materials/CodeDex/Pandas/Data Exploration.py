
import pandas as pd

data = {
  'city': ['Brooklyn', 'Seoul', 'Barcelona', 'Mexico City'],
  'country': ['US', 'South Korea', 'Spain', 'Mexico'],
  'population': [2646000, 9411000, 1636000, 9209944]
}

df = pd.DataFrame(data)

df.head()     # Displays the first 5 rows
df.tail()     # Displays the last 5 rows
df.info()  # can be used to gain a quick understanding of the data types stored
df.describe() #   to get a printout of summary statistics (mean, min, max, standard deviation, etc.) for every numeric column