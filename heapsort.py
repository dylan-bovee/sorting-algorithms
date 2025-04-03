def heapsort(tab):
    def entasser(tab, n, i):
        plus_grand = i
        gauche = 2 * i + 1
        droite = 2 * i + 2

        if gauche < n and tab[gauche] > tab[plus_grand]:
            plus_grand = gauche
        if droite < n and tab[droite] > tab[plus_grand]:
            plus_grand = droite

        if plus_grand != i:
            tab[i], tab[plus_grand] = tab[plus_grand], tab[i]
            entasser(tab, n, plus_grand)

    n = len(tab)

    # Construire le tas (transformer le tableau en max-heap)
    for i in range(n // 2 - 1, -1, -1):
        entasser(tab, n, i)

    # Extraire les éléments un par un
    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]  # Échange
        entasser(tab, i, 0)

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
    heapsort(nombres)
    print("Nombres triés :", nombres)
else:
    print("Aucun nombre valide trouvé dans le fichier.")
