h1 = int(input("Informe o primeiro horário: "))
m1 = int(input("Informe o primeiro minuto: "))
h2 = int(input("Infome o segundo horário': "))
m2 = int(input("Informe o segundo minuto: "))

if h1 > 12:
    h1 = h1 - 12

if h2 > 12:
    h2 = h2 -12

totalH = h1 + h2
totalMin = m1 + m2


if totalMin > 60:
    totalMin -= 60
    totalH += 1


if totalH > 12:
    totalMin -= 12
print(f"{totalH}:{totalMin}")
