def potega(a, n):
    if n == 0:
        return 1
    return a * potega(a, n - 1)

a = float(input("Podaj liczbę: "))
n = int(input("Podaj wykładnik: "))
print("Wynik:", potega(a, n))
