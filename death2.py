import pandas as pd
df = pd.read_csv('death.csv')

print(df)

from bokeh.charts import Bar, output_file, save
output_file('death2.html')

sickdeath = Bar(df, 'Year', values='Pneumonia and Influenza Deaths', agg='mean', title= 'Average Pneumonia/Influenza deaths per year' )
sickdeath.plot_width=1000
save(sickdeath)
