import math

# Funkcja do obliczania odległości do horyzontu
def oblicz_odleglosc(h):
    d = 3.57 * math.sqrt(h)  # Wzór na obliczenie odległości
    return d

# Pobranie wysokości od użytkownika
h = float(input("Podaj wysokość obserwatora nad ziemią w metrach: "))

# Obliczenie odległości
odleglosc = oblicz_odleglosc(h)

# Wyświetlenie wyniku
print(f"Odległość do horyzontu wynosi {odleglosc:.2f} km.")
