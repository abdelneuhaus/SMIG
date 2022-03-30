from re import findall as findall
from re import split as spplit

list_to_convert = "1, 2,3, 6-9, 14, 33-36"
a = findall('\d+', list_to_convert)
c = spplit(',|, ', list_to_convert)



"""
    Avec findall, on obtient : a = ['1', '2', '3', '6', '9', '14', '33', '36']
    Là l'idée c'est de filtrer la liste de base avec la virgule comme séparateur comme ça on obtient ça : c = ['1', ' 2', '3', ' 6-9', ' 14', ' 33-36']
    Ensuite, convertir la liste a en int
    Extraire les éléments de la list c qui contiennent un tiret
    Trouver un moyen de passer de 'X-Y' à 'X', 'Y' ou X, Y à partir de la néo-liste
    Créer un range de ces intervalles et les ajouter à la liste a
"""