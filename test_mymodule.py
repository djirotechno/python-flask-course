# Importe le module 'unittest' pour créer des tests unitaires pour votre code.
import unittest

# Importe les fonctions 'square' et 'double' du module 'mymodule'.
from mymodule import square, double

# Définit une classe de cas de test pour tester la fonction 'square'.
# Un cas de test est une unité de test unique. Il vérifie un aspect spécifique du comportement du code.
class TestSquare(unittest.TestCase): 

   # Définit la première méthode de test pour la fonction 'square'.
   def test1(self): 
       # Vérifie que l'appel de 'square(2)' renvoie 4.
       # Ceci teste si la fonction calcule correctement le carré de 2.
       self.assertEqual(square(2), 4) # teste lorsque 2 est donné en entrée, la sortie est 4.

       # Vérifie que l'appel de 'square(3.0)' renvoie 9.0.
       # Ceci teste si la fonction calcule correctement le carré de 3.0, vérifiant qu'elle gère les entrées flottantes.
       self.assertEqual(square(3.0), 9.0) # teste lorsque 3.0 est donné en entrée, la sortie est 9.0.

       # Vérifie que l'appel de 'square(-3)' ne renvoie pas -9.
       # Ceci teste que la sortie de la fonction n'est pas -9, vérifiant que le carré de -3 devrait être 9.
       self.assertNotEqual(square(-3), -9) # teste lorsque -3 est donné en entrée, la sortie n'est pas -9.

# Définit une classe de cas de test pour tester la fonction 'double'.
class TestDouble(unittest.TestCase): 

   # Définit la première méthode de test pour la fonction 'double'.
   def test1(self): 
       # Vérifie que l'appel de 'double(2)' renvoie 4.
       # Ceci teste si la fonction calcule correctement le double de 2.
       self.assertEqual(double(2), 4) # teste lorsque 2 est donné en entrée, la sortie est 4.

       # Vérifie que l'appel de 'double(-3.1)' renvoie -6.2.
       # Ceci teste si la fonction calcule correctement le double de -3.1, vérifiant qu'elle gère les entrées flottantes négatives.
       self.assertEqual(double(-3.1), -6.2) # teste lorsque -3.1 est donné en entrée, la sortie est -6.2.

       # Vérifie que l'appel de 'double(0)' renvoie 0.
       # Ceci teste si la fonction calcule correctement le double de 0, vérifiant que la fonction fonctionne pour les cas limites.
       self.assertEqual(double(0), 0) # teste lorsque 0 est donné en entrée, la sortie est 0.
    
# Exécute tous les cas de test définis dans le module lorsque le script est exécuté.
# Ceci découvrira et exécutera automatiquement tous les cas de test définis dans le module.
unittest.main()