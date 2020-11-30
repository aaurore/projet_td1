##Imports

import csv
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statistics as sts
from math import sqrt

from datetime import datetime as dt #on importe le module date pour pouvoir les comparer par la suite

##Ouverture du fichier

df = pd.read_csv("EIVP_KM1.csv", sep=';') #le fichier devient un dataframe, on l'affiche sans les ;


##Extractions des colonnes

identity=df['id']
noise= df['noise'] #on extrait la colonne noise
temperature = df['temp']
humidity = df['humidity']
luminosity = df['lum']
co2 = df['co2']
temps = df['sent_at'] #on extrait la colonne temps

##Affichage 

couleur=['orange','black','blue','red','magenta','forestgreen']

##Fonctions

####Traitement du temps dans les fonctions

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
    
    
new_temps_i=[new_temps1,new_temps2,new_temps3,new_temps4,new_temps5,new_temps6]


def graphique_par_capteurs(variable): 
    #on affiche les 6 capteurs sur le même graphe
    for k in range(1,7):
        plt.plot(new_temps_i[k-1],capteur(variable,k), color=couleur[k-1], label='capteur {}'.format(k))
    
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
    temps_bornes= nouveau_temps(start_date, end_date, new_temps_i[nbcapt-1]) #on prend la liste réduite entre les 2 bornes
    for i in temps_bornes:
        while new_temps_tot[j] != i: #on prend new_temps_tot pour avoir l'indice correspond sur tout le dataframe
            j = j+1 #si le temps d'indice i (compris entre les bornes de temps) correspond au numéro du capteur voulu, on l'ajoute à la nouvelle liste
        liste.append(variable[j])
        j=0
    return liste


def graphique_par_capteurs_bornes(variable, start_date, end_date, L):
    #si on met le 12/08 en date de fin, il s'arrêtera le 12/08 à 23h59
    #L est la liste des valeurs que l'on veut afficher
    for k in L:
        plt.plot(nouveau_temps(start_date, end_date, new_temps_i[k-1]), variable_bornes_capteur(variable, start_date, end_date, k), color=couleur[k-1], label='capteur {}'.format(k))
    
    #on affiche la variable raccourcie par rapport au temps avec les bornes données, les 2 listes auront la même dimension et on peut les afficher

    plt.legend(loc='upper left') #on ajoute une légende en haut à gauche
    plt.show() #on affiche le graphique

####Valeurs statistiques

def moyenne_arithm(L): #on veut la moyenne arithmétique
    somme=0
    for k in range (len(L)):
        somme+=L[k]
    return(somme/len(L))

def variance(L): #avec la méthode de König Huygens
    return moyenne_arithm([x**2 for x in L]) - moyenne_arithm([x for x in L])**2

def ecart_type(L):
    return(sqrt(variance(L)))

def mini(L):
    m=L[0]
    for x in L:
        if x < m:
            m=x
    return(m)

def maxi(L):
    m=L[0]
    for x in L:
        if x > m:
             m=x
    return(m)

def trieur(L): #Tri rapide
    n=len(L)
    if n==0:
        return([])
    pivot=[L[0]]
    Lg=[]
    Ld=[]
    for x in L[1:]:
        if x > L[0]:
            Ld.append(x)
        elif x < L[0]:
            Lg.append(x)
        else :
            pivot.append(x)
    return(trieur(Lg)+pivot+trieur(Ld)) #la fonction est recursive

def mediane(L):
    l=trieur(L)
    n=len(L)
    if n%2==0:
        return((l[1-n//2]+l[n//2])//2)
    else:
        return(l[(n-1)//2])
    

def graphique_valeur(variable, valeur):
    #on fait la même chose que dans graphique_par_capteurs
    for k in range(1,7):
         plt.plot(new_temps_i[k-1],capteur(variable,k), color=couleur[k-1], label='capteur {}'.format(k))
    a=valeur(variable)
    val = [a]*len(new_temps1) #il faut créer une liste de même taille que le temps pour pouvoir l'afficher
    plt.plot(new_temps1, val, color="cyan", linewidth=0.7, linestyle="-", label="valeur")
    plt.legend(loc='upper right') #on ajoute une légende en haut à droite
    plt.show()

def graphique_valeur_bornes(variable, valeur, start_date, end_date): #on fait la même chose que dans graphique_par_capteurs_bornes
    for k in range(1,7):
        plt.plot(nouveau_temps(start_date, end_date, new_temps_i[k-1]), variable_bornes_capteur(variable, start_date, end_date, 1), color=couleur[k-1], label='capteur {}'.format(k))
    
    new_variable= []
    for i in range(1,7): #on va mettre dans une même liste les valeurs des 6 capteurs
        new_variable = new_variable + variable_bornes_capteur(variable, start_date, end_date, i) #on crée un nouvelle variable qui contient comme éléments les valeurs de la variable choisie par l'utilisateur entre les bornes qu'il a rentrées
    a = valeur(new_variable) #on prend la valeur voulue par rapport à la nouvelle liste
    val= [a]*len(nouveau_temps(start_date, end_date, new_temps1))

    plt.plot(nouveau_temps(start_date, end_date, new_temps1), val, color = 'cyan', label= 'valeur')
    plt.legend(loc='upper left')
    plt.show()

####Indice de corrélation

def indice_correlation(var1,var2): #indice de correlation avec la méthode de pearson
    M1=moyenne_arithm(var1)
    M2=moyenne_arithm(var2)
    E1=sts.stdev(var1)
    E2=sts.stdev(var2)
    n=min(len(var1), len(var2))
    a=1/(E1*E2*(n-1))
    s=0
    for k in range(n):
        s+=(var1[k]-M1)*(var2[k]-M2)
    return(a*s)


def graph_corr(var1, var2):
    plt.plot(new_temps_tot, var1, color="blue") #ici, on affiche tous les capteurs sans les distinguer
    plt.plot(new_temps_tot,var2, color="orange")
    a=indice_correlation(var1, var2)
    plt.suptitle("l'indice de corrélation vaut {}".format(a))
    plt.show()


def graph_corr_capteur(var1, var2, numcapt):
    plt.plot(capteur(temps, numcapt), capteur(var1, numcapt), color="blue") #ici, on prend en compte un seul capteur
    plt.plot(capteur(temps, numcapt),capteur(var2, numcapt), color="orange")

    a=indice_correlation(capteur(var1, numcapt),capteur(var2, numcapt))
    plt.suptitle("l'indice de corrélation vaut {}".format(a))
    plt.show()


####Humidex

def humidex(Ta,Hr):
    #Ta = température ambiante
    #Hr = humidité relative
    x=7.5*Ta/(237.7+Ta)
    y=6.112*Hr/100
    return(Ta+(y*(10**x)-10)*5/9)

Humidex=[]
for k in range(len(temperature)): 
    Humidex.append(humidex(temperature[k],humidity[k])) #on applique la formule de l'humidex à tous les couples de variables
    

def L_humidex(i):
    L=[]
    temper= capteur(temperature, i) #on isole la colonne temperature du capteur i
    humid = capteur(humidity, i) #on isole la colonne humidity du capteur i
    for k in range(len(temper)):
        L.append(humidex(temper[k],humid[k])) #on applique la formule de l'humidex à tous les couples de variables
    return L

def graphique_humidex():
    for k in range(1,7):
        plt.plot(new_temps_i[k-1],L_humidex(k), color=couleur[k-1], label='capteur {}'.format(k))
    plt.legend()
    plt.show()


def humidex_bornes(start,end): #Entrer dates de début et de fin
    for k in range(1,7):
        plt.plot(nouveau_temps(start,end,new_temps_i[k-1]),variable_bornes_capteur(Humidex,start,end,k), color=couleur[k-1], label='capteur {}'.format(k))
    plt.legend()
    plt.show()

####simiarités
    
def mesure_similarites(start, end, variable, capteur1, capteur2): #Entrer dates de début et de fin, la variable et les capteurs à comparer
    a=indice_correlation(variable_bornes_capteur(variable,start,end,capteur1), variable_bornes_capteur(variable,start,end,capteur2))
    
    plt.plot(nouveau_temps(start,end,new_temps_i[capteur1-1]),variable_bornes_capteur(variable,start,end,capteur1), color='orange', label='capteur 1')
    plt.plot(nouveau_temps(start,end,new_temps_i[capteur2-1]),variable_bornes_capteur(variable,start,end,capteur2), color='blue', label='capteur 2')
    plt.suptitle("l'indice de corrélation vaut {}".format(a))
    plt.legend()
    plt.show()

def similarites(start, end, capteur1, capteur2, ind): #Entrer dates de début et de fin, la variable, les capteurs à comparer et l'indice de corrélation minimum
    l=[]
    L_var=[noise,temperature,humidity,luminosity,co2]
    var=['noise','temperature','humidity','luminosity','co2']
    for k in range(len(var)):
        i=indice_correlation(variable_bornes_capteur(L_var[k],start,end,capteur1), variable_bornes_capteur(L_var[k],start,end,capteur2))
        if i>=ind:
            l.append([var[k],i])
    I=ind*100
    if len(l)==0:
        print('Les capteurs {} et {} ne sont pas similaires à {} % pour ces données sur cette période'.format(capteur1,capteur2,I))
    else :
        for x in l:
            print('Pour la variable {}, les capteurs {} et {} sont similaires à {} % et la corrélation est de {}'.format(x[0],capteur1,capteur2,I,x[1]))
    
def tot_similarites_automatiques(start,end,ind): #Fin du projet
    
    couple=[[1,2],[1,3],[1,4],[1,5],[1,6],[2,3],[2,4],[2,5],[2,6],[3,4],[3,5],[3,6],[4,5],[4,6],[5,6]] #tous les couples possibles
    for c in couple:
        similarites(start,end,c[0],c[1],ind) #on donne similarites pour chaque couple de capteurs

####Horaires des bureaux 


def horaires_bureaux():
    L1 = nouveau_temps('2019-08-12', '2019-08-19', new_temps6) #on a selectionné le capteur 6
    L2 = variable_bornes_capteur(luminosity, '2019-08-12', '2019-08-19', 6) #on choisit
    n = len(L2)
    debut=[]
    fin = []
    for i in range(n-1):
        if L2[i-1] == 0 and L2[i+1] != 0: #on veut la valeur lors du changement
            if L2[i] != 0: #on veut une seule valeur donc on ajoute une condition sinon 2 sont possibles
                debut.append(L1[i]) #liste des horaires de début
        elif L2[i-1] != 0 and L2[i+1] == 0: #on fait la même chose qu'au dessus mais avec les conditions inversées
            if L2[i] == 0:
                fin.append(L1[i]) #liste des horaires de fin
    minu_debut=[] 
    minu_fin=[]
    for k in range(len(debut)): #fin et debut sont de la même taille
        a = int(debut[k].strftime('%M')) #on convertit en int
        b= int((debut[k].strftime('%H')))
        minu_debut.append(a + 60*b) #on met l'horaire de début en minutes
        c = int(fin[k].strftime('%M'))
        d = int((fin[k].strftime('%H')))
        minu_fin.append(c + 60 * d) #on met l'horaire de fin en minutes
    temps_debut = moyenne_arithm(minu_debut) #on fait la moyenne de toutes les dates
    temps_fin = moyenne_arithm(minu_fin)
    return "l'heure de début est {} h {} min et l'heure de fin est {} h {} min".format(temps_debut //60, temps_debut % 60, temps_fin //60, temps_fin % 60) 
    
    
    