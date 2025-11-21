import pandas as pd

df = pd.read_csv('files/output/solicitudes_de_credito.csv', sep=';')
print('total rows:', len(df))
print('comuna > 20:', (df.comuna_ciudadano>20).sum())
print(df.comuna_ciudadano.value_counts().sort_index().head(30))
print('\nestrato value_counts:')
print(df.estrato.value_counts().to_list())
