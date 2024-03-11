import numpy as np
import matplotlib.pyplot as plt

# Liczba jednorękich bandytów
N = 100

# Parametry rozkładu normalnego dla każdego bandyty
m = np.random.uniform(0, 1, size=N)  # Średnie
s = np.random.uniform(0.1, 0.5, size=N)  # Odchylenia standardowe

# Funkcja zwracająca wygraną dla danego bandyty
def wygrana(bandyta, m, s):
    return np.random.normal(m, s)

# Testowanie funkcji dla przykładowego bandyty
bandyta_przykladowa = 5
przykladowa_wygrana = wygrana(bandyta_przykladowa, m[bandyta_przykladowa], s[bandyta_przykladowa])
print("Przykładowa wygrana dla bandyty", bandyta_przykladowa, ":", przykladowa_wygrana)

# Wykres rozkładu prawdopodobieństwa wygranej dla wszystkich bandytów
plt.figure(figsize=(10, 6))
for i in range(N):
    plt.hist(wygrana(i, m[i], s[i]), bins=30, alpha=0.5, label=f"Bandyta {i}")
plt.title("Rozkład prawdopodobieństwa wygranej dla różnych bandytów")
plt.xlabel("Wygrana")
plt.ylabel("Częstość")
plt.legend()
plt.show()