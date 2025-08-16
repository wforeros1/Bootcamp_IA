import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

#=============================
# 1. Carga de datos
#=============================
df = pd.read_csv('clientes_supermercado.csv')
print(df)

df['Edad'] = df['Edad'].round().astype(int)
df['VisitasPorMes']=df['VisitasPorMes'].round().astype(int)
print(df)
x = df[['Edad','GastoMensual','VisitasPorMes']]
#=============================
# Metodo del codo
#=============================  
inertias = []
k_range = range(1, 10)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(x)
    inertias.append(kmeans.inertia_)
plt.figure(figsize=(6,4))
plt. plot(k_range, inertias,marker='o')
plt.xlabel('Nemero de clusters')
plt.ylabel('Inercia')
plt.title('Metodo del codo segmentacion de clientes')
plt.show()