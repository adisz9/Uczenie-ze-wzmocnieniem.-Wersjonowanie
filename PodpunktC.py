import numpy as np
import matplotlib.pyplot as plt

# Liczba jednorękich bandytów
N = 100
# Liczba gości
M = 50
# Liczba gier każdego gościa na każdej maszynie
L = 10

# Parametry rozkładu normalnego dla każdego bandyty
m = np.random.uniform(0, 1, size=N)  # Średnie
s = np.random.uniform(0.1, 0.5, size=N)  # Odchylenia standardowe

# Funkcja zwracająca wygraną dla danego bandyty
def wygrana(bandyta, m, s):
    return np.random.normal(m, s)

# Inicjalizacja tablic przechowujących wyniki
srednie_empiryczne = np.zeros((N, M))
odchylenia_empiryczne = np.zeros((N, M))

# Symulacja gier gości
for maszyna in range(N):
    for gosc in range(M):
        wyniki = [wygrana(maszyna, m[maszyna], s[maszyna]) for _ in range(L)]
        srednie_empiryczne[maszyna, gosc] = np.mean(wyniki)
        odchylenia_empiryczne[maszyna, gosc] = np.std(wyniki)

# Wybór maszyny na podstawie najlepszego wyniku własnego lub całej hordy
najlepsza_maszyne_gosci = np.argmax(srednie_empiryczne, axis=0)
najlepsza_maszyne_hordy = np.argmax(np.mean(srednie_empiryczne, axis=1))

# Wykres wyników
plt.figure(figsize=(10, 6))

# Histogramy dla najlepszych maszyn gosci
plt.subplot(2, 1, 1)
for i in range(N):
    plt.hist(srednie_empiryczne[i, najlepsza_maszyne_gosci == i], bins=30, alpha=0.5, label=f"Maszyna {i}")
plt.title("Najlepsza maszyna dla każdego gościa")
plt.xlabel("Średnia wygrana")
plt.ylabel("Częstość")
plt.legend()

# Histogram dla najlepszej maszyny całej hordy
plt.subplot(2, 1, 2)
plt.hist(srednie_empiryczne[najlepsza_maszyne_hordy], bins=30, alpha=0.5)
plt.title("Najlepsza maszyna dla całej hordy")
plt.xlabel("Średnia wygrana")
plt.ylabel("Częstość")

plt.tight_layout()
plt.show()