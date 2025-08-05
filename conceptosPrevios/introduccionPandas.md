# Introducción Pandas
Python 3.11

import pandas as pd # pip install pandas
## Creación de objeto Serie
s= pd.Series([2,4,6,8,10])
print(s)

# Creacion de un objeto series inicializado con un diccionario de python
altura = {"Santioago": 180, "Marcelo": 172, "Luis": 174, "Alejandra":160 }
s=pd.Series(altura)
print(s)
""""
creacion de un objeto series inicializando con algunos
de los elementos de un diccionario de pyton
"""
altura = {"Santioago": 180, "Marcelo": 172, "Luis": 174, "Alejandra":160 }
s=pd.Series(altura,index=["Marcelo","Luis"])
print(s)

#creacion de un objeto series inicializandolo con un escalar 
s=pd.series(34,{"test1", "test2","test3"})
print(s)