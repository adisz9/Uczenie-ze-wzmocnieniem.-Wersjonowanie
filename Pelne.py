import numpy as np
import pyswarms as ps

# Parametry
N = 100  # Liczba jednorękich bandytów
M = 50   # Liczba gości
Tmax = 10000  # Liczba iteracji

# Rozkłady prawdopodobieństwa wygranej dla każdej maszyny
m = np.random.uniform(0, 1, size=N)  # Średnie
s = np.random.uniform(0.1, 0.5, size=N)  # Odchylenia standardowe

# Inicjalizacja statystyk dla każdej maszyny
a = np.zeros((N, M))  # Suma wygranych
b = np.zeros((N, M))  # Liczba gier

# Funkcja celu
def funkcja_celu(pozycje):
    wygrane = np.zeros(M)
    for gosc in range(M):
        maszyna = int(pozycje[gosc][0])  # Wybór maszyny przez gościa
        maszyna = np.clip(maszyna, 0, N - 1)  # Upewnienie się, że indeks mieści się w zakresie
        wygrane[gosc] = np.random.normal(m[maszyna], s[maszyna])  # Symulacja gry na wybranej maszynie
        a[maszyna, gosc] += wygrane[gosc]  # Aktualizacja statystyk
        b[maszyna, gosc] += 1
    # Obliczenie wspólnej wygranej całej hordy
    return -np.sum(np.mean(a / (b + 1e-5), axis=1))  # Uwaga: funkcja celu jest minimalizowana, więc zwracamy negatywną wartość

# Inicjalizacja optymalizatora PSO
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=M, dimensions=M, options=options)

# Uruchomienie optymalizacji
best_position, _ = optimizer.optimize(funkcja_celu, iters=Tmax)

# Wypisanie wyników
print("Najlepsza pozycja globalna:", best_position)