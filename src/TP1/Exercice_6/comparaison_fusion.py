import time

import numpy as np

from .fusion import fusion_v1, fusion_v2

list1 = list(range(1, 8, 2)) + list(range(10, 21)) + list(range(32, 48, 3))
list2 = list(range(3, 12)) + list(range(13, 43, 3)) + list(range(43, 57, 2))

# Vérifie que les deux fonctions renvoient bien le même résultat
assert fusion_v1(list1, list2) == fusion_v2(list1, list2)

n_runs = 100_000

temps_fusion_v1 = []

for _ in range(n_runs):
    debut = time.time()
    fusion_v1(list1, list2)
    fin = time.time()
    temps_fusion_v1.append(fin - debut)

print(
    f"Temps d'exécution pour la fonction 'fusion_v1' : "
    f"{np.mean(temps_fusion_v1)} secondes ± {np.std(temps_fusion_v1)} secondes."
)

temps_fusion_v2 = []

for _ in range(n_runs):
    debut = time.time()
    fusion_v2(list1, list2)
    fin = time.time()
    temps_fusion_v2.append(fin - debut)

print(
    f"Temps d'exécution pour la fonction 'fusion_v2' : "
    f"{np.mean(temps_fusion_v2)} secondes ± {np.std(temps_fusion_v2)} secondes."
)
