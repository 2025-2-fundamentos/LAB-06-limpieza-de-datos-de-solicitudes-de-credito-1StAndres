import pandas as pd

df = pd.read_csv('files/output/solicitudes_de_credito.csv', sep=';')
print('sexo:', df.sexo.value_counts().to_list())
print('tipo_de_emprendimiento:', df.tipo_de_emprendimiento.value_counts().to_list()[:10])
print('idea_negocio counts len:', len(df.idea_negocio.value_counts().to_list()))
print('barrio counts len:', len(df.barrio.value_counts().to_list()))
print('estrato:', df.estrato.value_counts().to_list())
print('comuna_ciudadano counts len:', len(df.comuna_ciudadano.value_counts().to_list()))
print('monto_del_credito top counts:', df.monto_del_credito.value_counts().to_list()[:10])
print('linea_credito:', df['línea_credito'].value_counts().to_list()[:10])
