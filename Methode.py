#coding:utf-8
"""
Methode            : Fonction sur une instance (objet)
Methode de classe  : Fonction sur une classe
Methode statique   : Fonction  independant mais  lie a une classe
"""


class Humain:
  """Classe qui definit un humain"""
  lieu_habitation="terre"

  def __init__(self,nom,age):
    self.nom=nom
    self.age=age
    
  def parler(self,message):    #self Methode standart
    print("{} a dit: {}".format(self.nom, message))
    
  def changer_planete(cls, nouvelle_planete):    #cls = methode de classe
  
    Humain.lieu_habitation=nouvelle_planete
  changer_planete=classmethod(changer_planete)
#Programme principal
# h1=Humain('Mbaye Diop',26)
# h1.parler('Bonjour a tous le monde ! :)')
# h1.parler('Comment allez vous ! :)')
print("planete actuelle: {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("Planete actuelle: {}".format(Humain.lieu_habitation))

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Utilisation des méthodes statiques sans créer une instance de la classe
print(MathUtils.add(5, 3))         # Affiche 8
print(MathUtils.subtract(10, 4))   # Affiche 6
print(MathUtils.multiply(2, 7))    # Affiche 14
print(MathUtils.divide(15, 3))     # Affiche 5.0








#  Humaine_creer =0 #initialisation de l'attribut de classe

#  def __init__(self,c_prenom,c_nom,c_age):
#   self.prenom=c_prenom
#   self.nom=c_nom
#   self.age=c_age
#   Humain.Humaine_creer +=1 # incrementation de l'attribut de classe

# print("lancement du programme")
# h1=Humain('Mbaye','Diop',26)
# print('les attributs du premiers homme est :{} {} ayant {}ans'.format(h1.prenom,h1.nom,h1.age))
# print("Humaine creer est {}".format(Humain.Humaine_creer)) #affichage de l'attribut de classe
# print("----------------*************-------------")
# h2=Humain('Abdou','Faye',25)
# print('les attributs du Deuxieme homme est :{} {} ayant {}ans'.format(h2.prenom,h2.nom,h2.age))
# print("Humaine creer est {}".format(Humain.Humaine_creer))