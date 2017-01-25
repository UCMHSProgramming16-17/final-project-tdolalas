import pandas as pd
df = pd.read_csv('death.csv')

print(df)

from bokeh.charts import Bar, output_file, save
output_file('death.html')
