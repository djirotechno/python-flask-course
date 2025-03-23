def mean(numbers):
    """
    Cette fonction renvoie la moyenne de la liste de nombres donnée.
    La moyenne est calculée comme la somme de tous les nombres divisée par le nombre de nombres.
    """
    # Calcule la moyenne en additionnant tous les nombres et en divisant par la longueur de la liste.
    # 'sum(numbers)' calcule le total de tous les nombres dans la liste.
    # 'len(numbers)' donne le nombre de nombres dans la liste.
    # La moyenne (ou moyenne arithmétique) est le total de la somme divisée par le nombre d'éléments.
    return sum(numbers) / len(numbers)  # Renvoie la valeur moyenne.

def median(numbers):
    """
    Cette fonction renvoie la médiane de la liste de nombres donnée.
    La médiane est la valeur du milieu lorsque les nombres sont triés.
    S'il y a un nombre pair d'observations, elle renvoie la moyenne des deux nombres du milieu.
    """
    # Trie la liste de nombres par ordre croissant.
    # Le tri est nécessaire pour trouver la médiane, car la médiane dépend de l'ordre des valeurs.
    numbers.sort()

    # Vérifie si le nombre d'éléments dans la liste est pair.
    # len(numbers) % 2 == 0 est évalué à True si la liste a un nombre pair d'éléments.
    if len(numbers) % 2 == 0:
        # Si la liste a un nombre pair d'éléments, trouve les deux nombres du milieu.
        # 'len(numbers) // 2' calcule l'indice du deuxième élément du milieu dans une liste indexée à zéro.
        # 'len(numbers) // 2 - 1' calcule l'indice du premier élément du milieu.
        median1 = numbers[len(numbers) // 2]  # L'indice supérieur des deux valeurs du milieu.
        median2 = numbers[len(numbers) // 2 - 1]  # L'indice inférieur des deux valeurs du milieu.
        
        # Calcule la médiane en prenant la moyenne des deux nombres du milieu.
        # Ceci est fait en additionnant les deux valeurs du milieu et en divisant par 2.
        mymedian = (median1 + median2) / 2  # Moyenne des deux valeurs du milieu.
    else:
        # Si la liste a un nombre impair d'éléments, renvoie le nombre du milieu.
        # 'len(numbers) // 2' calcule l'indice de l'élément du milieu.
        mymedian = numbers[len(numbers) // 2]  # La valeur du milieu pour les listes avec un nombre impair d'éléments.

    # Renvoie la valeur médiane calculée.
    return mymedian