#coding:utf-8

class Humain:
 
 Humaine_creer =0 #initialisation de l'attribut de classe

 def __init__(self,c_prenom,c_nom,c_age):
  self.prenom=c_prenom
  self.nom=c_nom
  self.age=c_age
  Humain.Humaine_creer +=1 # incrementation de l'attribut de classe

print("lancement du programme")
h1=Humain('Mbaye','Diop',26)
print('les attributs du premiers homme est :{} {} ayant {}ans'.format(h1.prenom,h1.nom,h1.age))
print("Humaine creer est {}".format(Humain.Humaine_creer)) #affichage de l'attribut de classe
print("----------------*************-------------")
h2=Humain('Abdou','Faye',25)
print('les attributs du Deuxieme homme est :{} {} ayant {}ans'.format(h2.prenom,h2.nom,h2.age))
print("Humaine creer est {}".format(Humain.Humaine_creer))