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

# Symulacja gier gości
srednie_empiryczne = np.zeros((N, M))
odchylenia_empiryczne = np.zeros((N, M))

for maszyna in range(N):
    for gosc in range(M):
        wyniki = [wygrana(maszyna, m[maszyna], s[maszyna]) for _ in range(L)]
        srednie_empiryczne[maszyna, gosc] = np.mean(wyniki)
        odchylenia_empiryczne[maszyna, gosc] = np.std(wyniki)

# Wykres rozkładu empirycznych średnich wygranych dla każdego bandyty
plt.figure(figsize=(10, 6))
for maszyna in range(N):
    plt.hist(srednie_empiryczne[maszyna], bins=30, alpha=0.5, label=f"Maszyna {maszyna}")
plt.title("Rozkład empirycznych średnich wygranych dla różnych maszyn")
plt.xlabel("Średnia wygrana")
plt.ylabel("Częstość")
plt.legend()
plt.show()

# Wykres rozkładu empirycznych odchyleń standardowych wygranych dla każdego bandyty
plt.figure(figsize=(10, 6))
for maszyna in range(N):
    plt.hist(odchylenia_empiryczne[maszyna], bins=30, alpha=0.5, label=f"Maszyna {maszyna}")
plt.title("Rozkład empirycznych odchyleń standardowych wygranych dla różnych maszyn")
plt.xlabel("Odchylenie standardowe wygranej")
plt.ylabel("Częstość")
plt.legend()
plt.show()