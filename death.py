import pandas as pd
df = pd.read_csv('death.csv')

print(df)

from bokeh.charts import Bar, output_file, save
output_file('death.html')

deathyear = Bar(df, 'Year', values='All Deaths', agg='mean', title= 'Average deaths per year' )
deathyear.plot_width=800
save(deathyear)

from bokeh.charts import Histogram, output_file, save
output_file('deathage.html')
