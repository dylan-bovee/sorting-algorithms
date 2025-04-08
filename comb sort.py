import time
import tracemalloc

def tri_a_peigne(liste):
    gap = len(liste)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(liste):
            if liste[i] > liste[i + gap]:
                liste[i], liste[i + gap] = liste[i + gap], liste[i]
                sorted = False
            i += 1
    return liste

# Lecture de la liste depuis input.txt (plusieurs lignes)
with open("input4.txt", "r") as file:
    liste = [int(line.strip()) for line in file if line.strip().isdigit()]

# Mesure du temps et de la mémoire
tracemalloc.start()
start_time = time.time()
tri_a_peigne(liste)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

# Affichage des performances
print(f"Temps d'exécution : {end_time - start_time:.6f} secondes")
print(f"Mémoire utilisée : {current / 1024:.2f} Ko")
print(f"Pic de mémoire : {peak / 1024:.2f} Ko")
