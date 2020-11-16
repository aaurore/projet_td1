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

id=df['id']
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
    while id[x]!=nb:
        x+=1
    k=x
    while id[k]==nb and k<7879 : #on met une condition d'arrêt avecle nombre total d'indice pour obtenir le tps du capteur 6
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
    for i in range(1,7):
        plt.plot(capteur(temps,i),capteur(variable,i))
    plt.show()


new_temps1=[]  #il faudrait peut être créer une fonction qui donne new_temps(i) je pense
for k in range(len(temps1)):
    new_temps1.append(dt.strptime(temps1[k],'%Y-%m-%d %H:%M:%S%z'))

new_temps2=[]
for k in range(len(temps2)):
    new_temps2.append(dt.strptime(temps2[k],'%Y-%m-%d %H:%M:%S%z'))

new_temps3=[]
for k in range(len(temps3)):
    new_temps3.append(dt.strptime(temps3[k],'%Y-%m-%d %H:%M:%S%z'))

new_temps4=[]
for k in range(len(temps4)):
    new_temps4.append(dt.strptime(temps4[k],'%Y-%m-%d %H:%M:%S%z'))

new_temps5=[]
for k in range(len(temps5)):
    new_temps5.append(dt.strptime(temps5[k],'%Y-%m-%d %H:%M:%S%z'))

new_temps6=[]
for k in range(len(temps6)):
    new_temps6.append(dt.strptime(temps6[k],'%Y-%m-%d %H:%M:%S%z'))


def graphique_datetime(variable,new_t):
    plt.plot(new_t,variable)
    plt.title("graphique de la {} en fonction du temps".format(variable)) #on ajoute un titre  !!!!!
    plt.xlabel("temps")
    plt.ylabel("variable entrée")
    plt.show()

def graphique_par_capteurs(variable):
    plt.plot(new_temps1,capteur(variable,1), label='capteur1')
    plt.plot(new_temps2,capteur(variable,2), label='capteur2')
    plt.plot(new_temps3,capteur(variable,3), label='capteur3')
    plt.plot(new_temps4,capteur(variable,4), label='capteur4')
    plt.plot(new_temps5,capteur(variable,5), label='capteur5')
    plt.plot(new_temps6,capteur(variable,6), label='capteur6')
    plt.legend()
    plt.show()

def nouveau_temps(start_date, end_date,new_t):
    #il faut rentrer le new_temps correspondant au capteur étudié car tous les capteurs ne commencent pas au même moment
    "format YYYY-MM-DD"
    k = 0
    date_new_temps_k = new_t[k].strftime('%Y-%m-%d') #On transforme les éléments de la liste new_temps au même format que strat_date et end_date
    while date_new_temps_k != start_date :
        k+=1
    k_start = k
    while date_new_temps_k != end_date :
        k+=1
    k_end = k
    return([new_t[k] for k in range(k_start, k_end +1)])


def graphique2(variable, valeur, new_t):
    p1 = plt.plot(new_t, variable, color="blue", linewidth=0.7, linestyle="-", label="variable en fonction du temps")
    a=valeur(variable)
    val = [a]*len(new_t)
    p2 = plt.plot(new_t, val, color="red", linewidth=0.7, linestyle="-", label="valeur")
    plt.legend(loc='upper right') #on ajoute une légende en haut à droite
    plt.show()

#le programme précédent donne la valeur voulue par rapport à liste entière et ne prend pas en compte la nouvelle liste de temps

def graphique_valeur_capteur(variable, capteur):
    plt.plot(new_temps(i), capteur(variable,i))
    plt.plot(new_temps(i),valeur)
    plt.show()


def indice_correlation(var1,var2):
    ind= var1.corr(var2, method= 'pearson') #on choisit la méthode pearson (la plus adaptée dans le cas présent)
    print(ind)


def graph_corr(var1, var2, new_t):
    p1=plt.plot(new_t, var1, color="blue")
    p2=plt.plot(new_t,var2, color="orange")
    a=indice_correlation(var1, var2)
    print(len(var1))
    p3=plt.plot(new_t, cor, color="red")
    plt.show()

def humidex(Ta,Hr): #il faut que ton programme donne une valeur sans rien entrer dedans je crois car ces valeurs là sont dans le csv

    #Ta = tampérature ambiante
    #Hr = humidité relative

    x=7.5*Ta/(237.7+Ta)
    y=6.112*Hr/100

    return(Ta+(y*(10**x)-10)*5/9)