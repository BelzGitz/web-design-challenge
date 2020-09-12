import pandas as pd
df = pd.read_csv('cities.csv')
df.to_html('table.html', index=False, classes=['table', 'table-striped'])