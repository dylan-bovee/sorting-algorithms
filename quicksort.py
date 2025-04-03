def quicksort(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab) // 2]
    gauche = [x for x in tab if x < pivot]
    milieu = [x for x in tab if x == pivot]
    droite = [x for x in tab if x > pivot]
    return quicksort(gauche) + milieu + quicksort(droite)

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
    nombres_tries = quicksort(nombres)
    print("Nombres triés :", nombres_tries)
else:
    print("Aucun nombre valide trouvé dans le fichier.")
