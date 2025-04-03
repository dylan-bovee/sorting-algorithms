def merge_sort(tab):
    if len(tab) <= 1:
        return tab
    milieu = len(tab) // 2
    gauche = merge_sort(tab[:milieu])
    droite = merge_sort(tab[milieu:])
    return fusionner(gauche, droite)

def fusionner(gauche, droite):
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat

# Lire les nombres depuis le fichier input.py
def lire_nombres(fichier):
    try:
        with open(fichier, "r") as f:
            # Extraire les nombres en ignorant les lignes vides ou incorrectes
            nombres = [int(x) for x in f.read().split() if x.strip().isdigit()]
        return nombres
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{fichier}' est introuvable.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []

# Nom du fichier contenant les nombres
nom_fichier = "input.txt"

# Lire et trier les nombres
nombres = lire_nombres(nom_fichier)

if nombres:
    nombres_tries = merge_sort(nombres)
    print("Nombres triés :", nombres_tries)
else:
    print("Aucun nombre valide trouvé dans le fichier.")
