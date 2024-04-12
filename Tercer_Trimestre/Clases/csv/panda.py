import pandas as pd
import matplotlib.pyplot as plt

df_h = pd.read_csv("./Hurricanes.csv", delimiter=";")

print(df_h.to_string())

# Seleccionar columnas del dataframe
print(df_h[['name', 'year']])

# Visualiza los primeros datos del dataframe
print(df_h.head())

# Visualiza los últimos datos del dataframe
print(df_h.tail())

# Da información estadística de los datos del dataframe
print(df_h.describe())

# Información sobre las columnas y las filas del dataframe
print(df_h.shape)

print(df_h.info())

# Configurar un index y loc, para obtener los valores de un dato de ese índice
df_h_index = df_h.set_index("name")
print(df_h_index.loc["Barbara"])

# Intercambiar valores
df_h_index.loc["Barbara"] = df_h_index.loc["Barbara"].replace(1,2)
print(df_h_index.loc["Barbara"])

# Dibujar columnas
plot = df_h.plot(x="name", y="deaths", kind="bar", title="deaths by hurricans")
plt.show()

# Seleccion
print(df_h[0:3])

plot = df_h[df_h['year'] == 2004].plot(x="year", y="deaths", kind="bar")
plt.show()