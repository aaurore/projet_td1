##Imports

import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statistics as st

from datetime import datetime as dt #on importe le module date

##Ouverture du fichier

df = pd.read_csv("projet_td1/EIVP_KM1.csv", sep=';') #le fichier devient un dataframe, on l'affiche sans les ;
#print(df) #on affiche le tableau

##Extractions des colonnes

Id = df['id']
noise= df['noise'] #on extrait la colonne noise
temperature = df['temp']
humidity = df['humidity']
lum = df['lum']
co2 = df['co2']
temps = df['sent_at'] #on extrait la colonne temps

##Fonctions

def capteur(variable,nb):
    #Cette fonction a été testée et marche. Elle donne la liste variable pour le capteur nb uniquement.
    capteur_nb=[]
    x=0
    while Id[x]!=nb:
        x+=1
    k=x
    while Id[k]==nb and k<7879 : #on met une condition d'arrêt avecle nombre total d'indice pour obtenir le tps du capteur 6
        capteur_nb.append(variable[k])
        k+=1
    return(capteur_nb)

temps1=capteur(temps,1)
temps2=capteur(temps,2)
temps3=capteur(temps,3)
temps4=capteur(temps,4)
temps5=capteur(temps,5)
temps6=capteur(temps,6)


def graphique(variable):
    plt.plot(temps,variable)
    plt.show()

new_temps=[]
for k in range(len(temps)):
    new_temps.append(dt.strptime(temps[k],'%Y-%m-%d %H:%M:%S%z'))

def graphique_datetime(variable):
    plt.plot(new_temps,variable)
    plt.xlabel("temps")
    plt.ylabel("variable entrée")
    plt.show()

def nouveau_temps(start_date, end_date):
    "format YYYY-MM-DD"
    k = 0
    date_new_temps_k = new_temps[k].strftime('%Y-%m-%d') #On transforme les éléments de la liste new_temps au même format que strat_date et end_date
    while date_new_temps_k != start_date :
        k+=1
    k_start = k
    while date_new_temps_k != end_date :
        k+=1
    k_end = k
    return([new_temps[k] for k in range(k_start, k_end +1)])


def graphique2(variable, valeur):
    p1 = plt.plot(new_temps, variable, color="blue", linewidth=0.7, linestyle="-", label="variable en fonction du temps")
    a=valeur(variable)
    val = [a]*len(new_temps)
    p2 = plt.plot(new_temps, val, color="red", linewidth=0.7, linestyle="-", label="valeur")
    plt.legend(loc='upper right') #on ajoute une légende en haut à droite
    plt.show()

#le programme précédent donne la valeur voulue par rapport à liste entière et ne prend pas en compte la nouvelle liste de temps


def indice_correlation(var1,var2):
    ind= var1.corr(var2, method= 'pearson') #on choisit la méthode pearson (la plus adaptée dans le cas présent)
    print(ind)


def graph_corr(var1, var2):
    p1=plt.plot(new_temps, var1, color="blue")
    p2=plt.plot(new_temps,var2, color="orange")
    a=indice_correlation(var1, var2)
    print(len(var1))
    p3=plt.plot(new_temps, cor, color="red")
    plt.show()




