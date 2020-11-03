import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv("EIVP/EIVP_KM.csv", sep=';') #la fichier devient un dataframe, on l'affiche sans les ;
#print(df) #on affiche le tableau

from datetime import * #on importe le module date

x=df['sent_at']
print(x)



def nouveau_temps(liste,start_date, end_date):
    n=len(x)
    i=0
    while liste[0][:nb] < start_date:
        i=i+1




#a[:nb] #prend les caractères les plus à gauche avant le premier espace

x=df['sent_at'] #on extrait la colonne temps
y=df['noise'] #on extrait la colonne noise
plt.plot(x,y)
plt.show()
#print(x)




#def graph_var_fonct_temps(variable):




#http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/td2a_cenonce_session_1.html