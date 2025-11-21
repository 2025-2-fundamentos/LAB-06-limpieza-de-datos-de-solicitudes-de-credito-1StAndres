import pandas as pd

df = pd.read_csv('files/input/solicitudes_de_credito.csv', sep=';')
print(df.estrato.value_counts().sort_index())
print('\nUnique sample values:')
print(df.estrato.astype(str).unique()[:50])
