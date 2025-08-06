import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos_estudiantes = {
    "peso": pd.Series([55, 68, 74, 60, 72], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "altura": pd.Series([162, 175, 168, 180, 170], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "promedio": pd.Series([4.5, 3.8, 4.2, 2.9, 3.5], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"]),
    "edad": pd.Series([17, 18, 17, 19, 18], index=["Ana", "Carlos", "Daniela", "Eduardo", "Fernanda"])
}

df = pd.DataFrame(datos_estudiantes)
print(df)

serie_alturas = pd.Series(df["altura"], index=df.index)
print(serie_alturas)

altura_daniela = serie_alturas["Daniela"]
print(altura_daniela)

promedio_carlos_1 = df.loc["Carlos", "promedio"]
promedio_carlos_2 = df.iloc[1, 2]
promedio_carlos_3 = df["promedio"]["Carlos"]
print(promedio_carlos_1, promedio_carlos_2, promedio_carlos_3)

buen_promedio = df[df["promedio"] >= 4.0]
print(buen_promedio)

print(buen_promedio.shape[0])

print(df.describe())

df["mayor_edad"] = df["edad"] >= 18
print(df)

df["año_nacimiento"] = 2025 - df["edad"]
print(df)

df["promedio"].plot(kind="bar", title="Promedio de estudiantes")
plt.xlabel("Estudiante")
plt.ylabel("Nota promedio")
plt.show()

altura_filtrada = df[(df["altura"] >= 165) & (df["altura"] <= 175)]
print(altura_filtrada)

df_sin_peso = df.drop(columns=["peso"])
print(df_sin_peso)

df_reducido = df[["edad", "año_nacimiento"]].copy()
df_reducido["nombre"] = df.index
print(df_reducido)
