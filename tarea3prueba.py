import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#limpieza de columna de numero de ticekt
def numbers(element):
    return "".join(filter(str.isnumeric, element))

df = pd.read_csv('Titanic1.csv', header=0)
pd.read_csv

df.loc[:,'num'] = [numbers(x) for x in df.ticket]


Sobrevivio= df.groupby('Sobrevivio')['record_id'].count()
print(Sobrevivio)

y = np.array([ Sobrevivio[0], Sobrevivio[1]])

mylabels = ["No", "Si"]
plt.pie(y, labels = mylabels, shadow = True)

plt.legend(title = "Sobrevivientes:")
plt.show()

Clase= df.groupby('Clase')['Bote de Rescate'].count()
print(Clase)

plt.legend(title = "Sobrevivientes por Clase:")
Clase= Clase.plot(kind='bar');

plt.show()

grouped_sex = surveys_df[surveys_df['sex'].notnull()]

print(grouped_sex, " \n")