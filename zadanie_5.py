def bmi(waga, wzrost):
    wynik = waga / (wzrost ** 2)
    print("BMI:", round(wynik, 2))

    if wynik < 18.5:
        print("Niedowaga")
    elif wynik < 25:
        print("Pożądana masa ciała")
    elif wynik < 30:
        print("Nadwaga")
    elif wynik < 35:
        print("Otyłość I stopnia")
    elif wynik < 40:
        print("Otyłość II stopnia")
    else:
        print("Otyłość III stopnia")

    return wynik

waga = float(input("Podaj wagę w kg: "))
wzrost = float(input("Podaj wzrost w metrach: "))
bmi(waga, wzrost)
