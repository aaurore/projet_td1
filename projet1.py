import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statistics as st


from datetime import datetime as dt #on importe le module date

df = pd.read_csv("projet_td1/EIVP_KM.csv", sep=';') #le fichier devient un dataframe, on l'affiche sans les ;
#print(df) #on affiche le tableau

noise= df['noise']
temperature = df['temp']
humidity = df['humidity']
lum = df['lum']
co2 = df['co2']
temps = df['sent_at'] #on extrait la colonne temps

def graphique(variable):
    plt.plot(temps,variable)
    plt.show()

new_temps=[]
for k in range(len(temps)):
    new_temps.append(dt.strptime(temps[k],'%Y-%m-%d %H:%M:%S %z'))

def graphique_datetime(variable):
    plt.plot(new_temps,variable)
    plt.show()


def trans():
    new_temps=[]
    for k in range(len(temps)):
       new_temps.append(dt.strptime(temps[k],'%Y-%m-%d %H:%M:%S %z'))


def nouveau_temps(start_date, end_date):
    new_temps=dt


def graphique_bis(variable, start_date, end_date):



#def graphique2(variable, valeur):
    p1 = plt.plot(temps, variable)
    a=valeur(variable)
    val = [a]*len(temps)
    p2 = plt.plot(temps, val)
    plt.show()

def min(liste):
    min = liste[0]
    n= len(liste)
    for i in range(n):
        if liste[i]<min:
            min=liste[i]
    return min


def max(liste):
    max = liste[0]
    n= len(liste)
    for i in range(n):
        if liste[i]>max:
            max=liste[i]
    return max

# x=df['sent_at'] #on extrait la colonne temps
# y=df['noise'] #on extrait la colonne noise
# p1=plt.plot(x,y)
# a=st.mean(y)
# z=[a]*len(x)
# p2=plt.plot(x,z)
# plt.show()
#print(x)


# p1=plt.plot(x,np.sin(x),marker='o')
# p2=plt.plot(x,np.cos(x),marker='v')
# plt.title("Fonctions trigonometriques")  # Problemes avec accents (plot_directive) !
# plt.legend([p1, p2], ["Sinus", "Cosinus"])
# plt.show()



#http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/notebooks/td2a_cenonce_session_1.html