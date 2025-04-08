import time
import tracemalloc

def tri_a_bulles(liste):
    n = len(liste)
    for i in range(n):
        echange = False
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                echange = True
        if not echange:
            break
    return liste

# Lecture de la liste depuis input.txt (plusieurs lignes)
with open("input1.txt", "r") as file:
    liste = [int(line.strip()) for line in file if line.strip().isdigit()]

# Mesure du temps et de la mémoire
tracemalloc.start()
start_time = time.time()
tri_a_bulles(liste)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Affichage des performances
print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
print(f"Mémoire utilisée : {current / 1024:.2f} Ko")
print(f"Pic de mémoire : {peak / 1024:.2f} Ko")
