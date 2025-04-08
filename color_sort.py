import pygame
import math
import random
import time
import pygame_gui

# Initialisation de Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualisation de tri en cercle")
clock = pygame.time.Clock()

# Paramètres du cercle
center = (WIDTH // 2, HEIGHT // 2)
radius = 300
num_elements = 100

# Liste de valeurs aléatoires
values = list(range(num_elements))
random.shuffle(values)

# Initialisation de pygame_gui
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Fonction pour convertir une valeur en couleur
def value_to_color(val, max_val):
    color = pygame.Color(0)
    color.hsva = (val / max_val * 360, 100, 100, 100)
    return color

# Fonction pour dessiner les points en cercle
def draw_circle(values, highlight_indices=None):
    screen.fill((0, 0, 0))
    angle_step = 2 * math.pi / len(values)

    for i, val in enumerate(values):
        angle = i * angle_step
        x = int(center[0] + radius * math.cos(angle))
        y = int(center[1] + radius * math.sin(angle))
        color = value_to_color(val, num_elements)
        
        if highlight_indices and i in highlight_indices:
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 6)
        else:
            pygame.draw.circle(screen, color, (x, y), 4)

    pygame.display.flip()

# Tri par sélection
def selection_sort(values, draw_fn):
    n = len(values)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if values[j] < values[min_index]:
                min_index = j
            draw_fn(values, highlight_indices=(i, j))
            pygame.event.pump()  # Pour que la fenêtre reste responsive
            time.sleep(0.01)
        values[i], values[min_index] = values[min_index], values[i]

# Tri rapide (QuickSort)
def quicksort(values, draw_fn, low=0, high=None):
    if high is None:
        high = len(values) - 1
    
    def partition(values, low, high):
        pivot = values[high]
        i = low - 1
        for j in range(low, high):
            if values[j] < pivot:
                i += 1
                values[i], values[j] = values[j], values[i]
            draw_fn(values, highlight_indices=(i, j))
            pygame.event.pump()  # Pour que la fenêtre reste responsive
            time.sleep(0.01)
        values[i + 1], values[high] = values[high], values[i + 1]
        return i + 1

    if low < high:
        pi = partition(values, low, high)
        quicksort(values, draw_fn, low, pi - 1)
        quicksort(values, draw_fn, pi + 1, high)

# Tri fusion (MergeSort)
def merge_sort(values, draw_fn):
    if len(values) > 1:
        mid = len(values) // 2
        left_half = values[:mid]
        right_half = values[mid:]

        merge_sort(left_half, draw_fn)
        merge_sort(right_half, draw_fn)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                values[k] = left_half[i]
                i += 1
            else:
                values[k] = right_half[j]
                j += 1
            k += 1
            draw_fn(values)
            pygame.event.pump()  # Pour que la fenêtre reste responsive
            time.sleep(0.01)

        while i < len(left_half):
            values[k] = left_half[i]
            i += 1
            k += 1
            draw_fn(values)
            pygame.event.pump()  # Pour que la fenêtre reste responsive
            time.sleep(0.01)

        while j < len(right_half):
            values[k] = right_half[j]
            j += 1
            k += 1
            draw_fn(values)
            pygame.event.pump()  # Pour que la fenêtre reste responsive
            time.sleep(0.01)

# Tri par tas (HeapSort)
def heapify(values, n, i, draw_fn):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and values[i] < values[left]:
        largest = left
    if right < n and values[largest] < values[right]:
        largest = right
    if largest != i:
        values[i], values[largest] = values[largest], values[i]
        draw_fn(values)
        pygame.event.pump()
        time.sleep(0.01)
        heapify(values, n, largest, draw_fn)

def heap_sort(values, draw_fn):
    n = len(values)
    for i in range(n // 2 - 1, -1, -1):
        heapify(values, n, i, draw_fn)
    for i in range(n - 1, 0, -1):
        values[i], values[0] = values[0], values[i]
        draw_fn(values)
        pygame.event.pump()
        time.sleep(0.01)
        heapify(values, i, 0, draw_fn)

# Tri à bulles (Bubble Sort)
def bubble_sort(values, draw_fn):
    n = len(values)
    for i in range(n):
        for j in range(0, n-i-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
            draw_fn(values, highlight_indices=(j, j+1))
            pygame.event.pump()  # Pour que la fenêtre reste responsive
            time.sleep(0.01)

# Tri par insertion (Insertion Sort)
def insertion_sort(values, draw_fn):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
        draw_fn(values, highlight_indices=(i, j+1))
        pygame.event.pump()  # Pour que la fenêtre reste responsive
        time.sleep(0.01)

# Tri Peigne (Comb Sort)
def comb_sort(values, draw_fn):
    n = len(values)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        for i in range(n - gap):
            if values[i] > values[i + gap]:
                values[i], values[i + gap] = values[i + gap], values[i]
                sorted = False
            draw_fn(values, highlight_indices=(i, i+gap))
            pygame.event.pump()  # Pour que la fenêtre reste responsive
            time.sleep(0.01)



# Création des boutons de l'interface
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (150, 40)),
                                            text="Démarrer",
                                            manager=manager)
reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 60), (150, 40)),
                                             text="Réinitialiser",
                                             manager=manager)
# Création du menu déroulant avec les nouveaux algorithmes
sort_menu = pygame_gui.elements.UIDropDownMenu(
    relative_rect=pygame.Rect((10, 110), (150, 40)),
    options_list=['Selection Sort', 'Quick Sort', 'Merge Sort', 'Heap Sort', 'Bubble Sort', 'Insertion Sort', 'Comb Sort'],
    starting_option='Selection Sort',
    manager=manager
)


# Fonction pour réinitialiser la liste des valeurs
def reset_values():
    global values
    values = list(range(num_elements))
    random.shuffle(values)

# Lancement de l'animation
running = True
draw_circle(values)

# Main loop
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

        # Gestion des boutons
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                selected_sort = sort_menu.selected_option[0]  # Extraire la première option du tuple
                print(f"Tri sélectionné: {selected_sort}")  # Débogage
                if selected_sort == 'Selection Sort':
                    selection_sort(values, draw_circle)
                elif selected_sort == 'Quick Sort':
                    quicksort(values, draw_circle)
                elif selected_sort == 'Merge Sort':
                    merge_sort(values, draw_circle)
                elif selected_sort == 'Heap Sort':
                    heap_sort(values, draw_circle)
                elif selected_sort == 'Bubble Sort':
                    bubble_sort(values, draw_circle)
                elif selected_sort == 'Insertion Sort':
                    insertion_sort(values, draw_circle)
                elif selected_sort == 'Comb Sort':
                    comb_sort(values, draw_circle)
                draw_circle(values)  # Redessiner après le tri



            elif event.ui_element == reset_button:
                reset_values()
                draw_circle(values)

    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
