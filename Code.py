import pandas as pd
import matplotlib.pyplot as plt
import calmap

# Import Data
df = pd.read_csv("DATA.csv", parse_dates=['date'])
df.set_index('date', inplace=True)

# Plot
plt.figure(figsize=(16,10), dpi= 80)
calmap.calendarplot(df['2012']['Soybean'], fig_kws={'figsize': (16,10)}, yearlabel_kws={'color':'black', 'fontsize':14}, subplot_kws={'title':'Stock Prices'})
plt.show()
