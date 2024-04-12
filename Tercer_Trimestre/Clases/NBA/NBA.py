import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Paso 1: Leer el fichero y mostar el data frame
df=pd.read_csv("./all_seasons.csv", delimiter=";")

# ¿Cuántas filas y columnas? a través del dataframe muestra esta información
print(df.shape)

# Paso 2: Quitar valores NULL (o valores nulos)
df.dropna(inplace=True)
df.shape

# ¿Cuántas filas y columnas? a través del dataframe muestra estsa información ahora.
print(df.shape)

# Mostrar toda la información del dataframe, tipos de datos de las columnas
print(df.to_string())

# Crea un índice de la columan season
print(df.set_index("season"))

# Cuenta los valores de la columna edad. value_conts()
print(df["age"].value_counts())

# Qué jugador tiene más minutos. sort_values() => Ordena valores
df.sort_values(by="Total day minutes", ascending=False).head()

# Saca la media de minutos al día. mean()
df["Total day minutes"].mean()

# Saca la media de los jugadores estadounidenses
df[df["country"] == "USA"].mean()

# Añade alguna columna más para que ordene
df[df["player_name"] == "George"].mean()

# Paso 3: Undrafted. Jugadores que no han sido elegidos a través de este sorteo, 
# a lo largo de la historia se han desarrollado varios “robos” o jugadores que han dejado huella en la liga,
Undrafted= df_season_wise[df_season_wise['draft_year']=='Undrafted']
df_season_wise['draft_year']=df_season_wise['draft_year'].replace('Undrafted',np.NaN) 

# Realiza lo mismo para las columnas draft_round, draft_number
Undrafted= df_season_wise[df_season_wise['draft_round']=='Undrafted']
df_season_wise['draft_round']=df_season_wise['draft_round'].replace('Undrafted',np.NaN) 

Undrafted= df_season_wise[df_season_wise['draft_number']=='Undrafted']
df_season_wise['draft_number']=df_season_wise['draft_number'].replace('Undrafted',np.NaN)

# Paso 4: Muestra las estadísticas de la tabla
df.plot(kind="bar", title="Estadísticas NBA")
plt.show()

# Paso 5: Seleccionamos las columnas 
# selecting columns required for analysis
col_need=['age','player_height','player_weight','gp','pts','reb','ast','net_rating','oreb_pct','dreb_pct','usg_pct','ts_pct','ast_pct']
ana_df=df[col_need]

# quitar datos repetidos
ana_df.duplicated().values.any()

# Paso 6: Muestra tu tabla de correlación a partir del dataframe ana_df
ana_df.corr()

# ¿Qué columnas tiene mayor correlación?
ana_df.corr().max()

# Paso 7: Muestra la gráfica de la correlación
pd.plotting.scatter_matrix(ana_df,figsize=(20,20),alpha=0.5)

# Prueba esta visualización. ¿Cuál es mejor? ¿ Por qué?
#better visualization
import seaborn as sns
sns.pairplot(ana_df)