# Comandos
```
python --version
Python 3.9.2
git --version
https://git-scm.com/
pip list
python.exe -m pip install --upgrade pip
```
## Crear entorno virtual 
python -m venv env
## Activar en torno
env\scripts\activate
si no activa ejecute en el powershell
set-ExecutionPolicy Unrestricted
y escriba S

## Estructura de datos en Pandas
| Tipo      | Contenido                                     |
| --------- | --------------------------------------------- |
| Series    | Array de una demensión                        |
| DataFrame | se corresponde con una tabla de 2 dimensiones |
| panel     | Similar a un diccionario de DataFrame         |

# Creación de objetos Series
```
import pandas as pd # pip install pandas
# Creación de objeto Serie
s= pd.Series([2,4,6,8,10])
print(s)

```
manejo de git
>git init