#coding: utf-8

import csv

fichier = "concordia1.csv"
f1 = open(fichier)

lignes = csv.reader(f1)
next(lignes)

longTitre = 0 
nbPages = 0
ligne = 0 
toute = 0 
type = ""
nbPages = ""
nom = ""
prenom = ""
titre = ""

for ligne in lignes:
    toute = ligne[2]
    longTitre +=1
    longTitre = len(ligne[2])
    
    toute = ligne[6]
    if ("Theses" in toute):
        type = "thèse"
    else:
        type = "mémoire"
        
    toute = (ligne[5])
    lentoute = toute.split(";")
    nbPages = lentoute[0]
    nbPages =nbPages.replace("leaves",'')
    nbPages =nbPages.replace(": ill.",'')
        
        
    nom = ligne[0]
    prenom = ligne[1]
    titre = ligne [2]
    
print("La" + " " + type + " de " + prenom + " " + nom + " compte", nbPages, "pages" + ". Son titre est " + titre + "(",longTitre , "caractères).")
 
    
