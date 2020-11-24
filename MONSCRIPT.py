##Imports

import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statistics as st

from datetime import datetime as dt #on importe le module date pour pouvoir les comparer par la suite

##Ouverture du fichier

df = pd.read_csv("projet_td1/EIVP_KM1.csv", sep=';') #le fichier devient un dataframe, on l'affiche sans les ;
#print(df) #on affiche le tableau

##Extractions des colonnes

identity=df['id']
noise= df['noise'] #on extrait la colonne noise
temperature = df['temp']
humidity = df['humidity']
luminosity = df['lum']
co2 = df['co2']
temps = df['sent_at'] #on extrait la colonne temps

##Fonctions


def capteur(variable,nb):
    #Cette fonction donne la liste variable pour le capteur nb uniquement.
    capteur_nb=[]
    x=0
    while identity[x]!=nb:
        x+=1
    k=x
    while identity[k]==nb and k<7879 : #on met une condition d'arrêt avec le nombre total d'indices pour obtenir le temps du capteur 6
        capteur_nb.append(variable[k])
        k+=1
    return(capteur_nb)

temps1= capteur(temps,1)
temps2= capteur(temps,2)
temps3= capteur(temps,3)
temps4= capteur(temps,4)
temps5= capteur(temps,5)
temps6= capteur(temps,6)

new_temps1=[]
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

new_temps_tot=[]
for k in range(len(temps)):
    new_temps_tot.append(dt.strptime(temps[k],'%Y-%m-%d %H:%M:%S%z'))

def graphique_par_capteurs(variable):
    plt.plot(new_temps1,capteur(variable,1), color='orange', label='capteur 1') #on affiche les 6 capteurs sur le même graphe
    plt.plot(new_temps2,capteur(variable,2), color='black', label='capteur 2')
    plt.plot(new_temps3,capteur(variable,3), color='blue', label='capteur 3')
    plt.plot(new_temps4,capteur(variable,4), color='red', label='capteur 4')
    plt.plot(new_temps5,capteur(variable,5), color='magenta', label='capteur 5')
    plt.plot(new_temps6,capteur(variable,6), color='forestgreen', label='capteur 6')
    plt.legend(loc='upper right') #on ajoute une légende en haut à droite
    plt.show() #on affiche le graphique

def nouveau_temps(start_date, end_date, temps):
    #il faut entrer le new_temps correspondant au capteur étudié car tous les capteurs ne commencent pas au même moment
    #le format des dates doit être: YYYY-MM-DD'
    nouveau=[]
    for i in temps:
         tp = i.strftime('%Y-%m-%d') #on transforme les éléments de la liste temps au même format que start_date et end_date pour pouvoir ensuite les comparer
         if tp>=start_date and tp<= end_date:
             nouveau.append(i) #on ajoute à la liste créée les éléments compris entre les 2 dates
    return nouveau


def variable_bornes_capteur(variable,start_date, end_date, nbcapt):
    liste=[]
    j=0
    if nbcapt == 1:  #le cas par cas est obligatoire car la fonction new_temps(i) que nous avions écrite ne fonctionne pas correctement
        temps= new_temps1
    elif nbcapt == 2:
        temps = new_temps2
    elif nbcapt == 3:
        temps = new_temps3
    elif nbcapt == 4:
        temps = new_temps4
    elif nbcapt == 5:
        temps = new_temps5
    elif nbcapt == 6:
        temps = new_temps6
    temps_bornes= nouveau_temps(start_date, end_date, temps) #on prend la liste réduite entre les 2 bornes
    for i in temps_bornes:
        while new_temps_tot[j] != i: #on prend new_temps_tot pour avoir l'indice correspond sur tout le dataframe
            j = j+1 #si le temps d'indice i (compris entre les bornes de temps) correspond au numéro du capteur voulu, on l'ajoute à la nouvelle liste
        liste.append(variable[j])
        j=0
    return liste


def graphique_par_capteurs_bornes(variable, start_date, end_date):
    #si on met le 12/08 en date de fin, il s'arrêtera le 12/08 à 23h59

    plt.plot(nouveau_temps(start_date, end_date, new_temps1), variable_bornes_capteur(variable, start_date, end_date, 1), color='orange', label='capteur 1')
    #on affiche la variable raccourcie par rapport au temps avec les bornes données, les 2 listes auront la même dimension et on peut les afficher

    plt.plot(nouveau_temps(start_date, end_date, new_temps2), variable_bornes_capteur(variable, start_date, end_date, 2), color='black', label='capteur 2')

    plt.plot(nouveau_temps(start_date, end_date, new_temps3), variable_bornes_capteur(variable, start_date, end_date, 3), color='blue', label='capteur 3')

    plt.plot(nouveau_temps(start_date, end_date, new_temps4), variable_bornes_capteur(variable, start_date, end_date, 4), color='red', label='capteur 4')

    plt.plot(nouveau_temps(start_date, end_date, new_temps5), variable_bornes_capteur(variable, start_date, end_date, 5), color='magenta', label='capteur 5')

    plt.plot(nouveau_temps(start_date, end_date, new_temps6), variable_bornes_capteur(variable, start_date, end_date, 6), color='forestgreen', label='capteur 6')

    plt.legend(loc='upper left') #on ajoute une légende en haut à gauche
    plt.show() #on affiche le graphique

moyenne = st.mean #on veut la moyenne arithmétique
mediane = st.median
variance = st.variance
ecart_type = st.stdev

#######ajouter les programmes
#faire les programmes min, max, moyenne, mediane, variance et ecart_type.

def graphique_valeur(variable, valeur):
    plt.plot(new_temps1,capteur(variable,1), color='orange', label='capteur 1') #on fait la même chose que dans graphique_par_capteurs
    plt.plot(new_temps2,capteur(variable,2), color='black', label='capteur 2')
    plt.plot(new_temps3,capteur(variable,3), color='blue', label='capteur 3')
    plt.plot(new_temps4,capteur(variable,4), color='red', label='capteur 4')
    plt.plot(new_temps5,capteur(variable,5), color='magenta', label='capteur 5')
    plt.plot(new_temps6,capteur(variable,6), color='forestgreen', label='capteur 6')
    a=valeur(variable)
    val = [a]*len(new_temps1) #il faut créer une liste de même taille que le temps pour pouvoir l'afficher
    plt.plot(new_temps1, val, color="cyan", linewidth=0.7, linestyle="-", label="valeur")
    plt.legend(loc='upper right') #on ajoute une légende en haut à droite
    plt.show()

def graphique_valeur_bornes(variable, valeur, start_date, end_date):
    plt.plot(nouveau_temps(start_date, end_date, new_temps1), variable_bornes_capteur(variable, start_date, end_date, 1), color='orange', label='capteur 1') #on fait la même chose que dans graphique_par_capteurs_bornes
    plt.plot(nouveau_temps(start_date, end_date, new_temps2), variable_bornes_capteur(variable, start_date, end_date, 2), color='black', label='capteur 2')
    plt.plot(nouveau_temps(start_date, end_date, new_temps3), variable_bornes_capteur(variable, start_date, end_date, 3), color='blue', label='capteur 3')
    plt.plot(nouveau_temps(start_date, end_date, new_temps4), variable_bornes_capteur(variable, start_date, end_date, 4), color='red', label='capteur 4')
    plt.plot(nouveau_temps(start_date, end_date, new_temps5), variable_bornes_capteur(variable, start_date, end_date, 5), color='magenta', label='capteur 5')
    plt.plot(nouveau_temps(start_date, end_date, new_temps6), variable_bornes_capteur(variable, start_date, end_date, 6), color='forestgreen', label='capteur 6')

    new_variable= []
    for i in range(1,7): #on va mettre dans une même liste les valeurs des 6 capteurs
        new_variable = new_variable + variable_bornes_capteur(variable, start_date, end_date, i) #on crée un nouvelle variable qui contient comme éléments les valeurs de la variable choisie par l'utilisateur entre les bornes qu'il a rentrées
    a = valeur(new_variable) #on prend la valeur voulue par rapport à la nouvelle liste
    val= [a]*len(nouveau_temps(start_date, end_date, new_temps1))

    plt.plot(nouveau_temps(start_date, end_date, new_temps1), val, color = 'cyan', label= 'valeur')
    plt.legend(loc='upper left')
    plt.show()


def indice_correlation(var1,var2):
    ind= var1.corr(var2, method= 'pearson') #on choisit la méthode pearson (la plus adaptée dans le cas présent)
    print(ind) #on l'affiche dans la console comme demandé
    return ind #on utilise return pour pouvoir utiliser cette fonction plus tard


def graph_corr(var1, var2):
    plt.plot(new_temps_tot, var1, color="blue") #ici, on affiche tous les capteurs sans les distinguer
    plt.plot(new_temps_tot,var2, color="orange")
    a=indice_correlation(var1, var2)
    plt.suptitle("l'indice de corrélation vaut {}".format(a))
    plt.show()

def graph_corr_capteur(var1, var2, numcapt):
    plt.plot(capteur(temps, numcapt), capteur(var1, numcapt), color="blue") #ici, on prend en compte un seul capteur
    plt.plot(capteur(temps, numcapt),capteur(var2, numcapt), color="orange")
    new_df = pd.DataFrame({"col1": capteur(var1, numcapt), "col2": capteur(var2, numcapt)}) #on convertit les listes en dataframe pour pouvoir calculer l'indice de corrélation par la suite car la fonction indice_correlation prend en paramètre des élèments des colonnes de dataframe
    a=indice_correlation(new_df['col1'],new_df['col2']) #on extrait les 2 colonnes du nouveau dataframe
    plt.suptitle("l'indice de corrélation vaut {}".format(a))
    plt.show()


###humidex

def humidex(Ta,Hr):
    #Ta = température ambiante
    #Hr = humidité relative
    x=7.5*Ta/(237.7+Ta)
    y=6.112*Hr/100
    return(Ta+(y*(10**x)-10)*5/9)

def L_humidex(i):
    L=[]
    temper= capteur(temperature, i) #on isole la colonne temperature du capteur i
    humid = capteur(humidity, i) #on isole la colonne humidity du capteur i
    for k in range(len(temper)):
        L.append(humidex(temper[k],humid[k])) #on applique la formule de l'humidex à tous les couples de variables
    return L

def graphique_humidex():
    plt.plot(new_temps1,L_humidex(1), color='orange', label='capteur 1')
    plt.plot(new_temps2,L_humidex(2), color='black', label='capteur 2')
    plt.plot(new_temps3,L_humidex(3), color='blue', label='capteur 3')
    plt.plot(new_temps4,L_humidex(4), color='red', label='capteur 4')
    plt.plot(new_temps5,L_humidex(5), color='magenta', label='capteur 5')
    plt.plot(new_temps6,L_humidex(6), color='forestgreen', label='capteur 6')
    plt.legend()
    plt.show()





def listes_reduites(variable, numcapt1, numcapt2):
    n1 = len(capteur(variable, numcapt1))
    n2 = len(capteur(variable, numcapt2))
    n= min(n1,n2)
    L1 = capteur(variable, numcapt1)
    L2 = capteur(variable, numcapt2)
    plt.plot(new_temps1, L1[:n])
    plt.plot(new_temps1, L2[:n])
    plt.show()