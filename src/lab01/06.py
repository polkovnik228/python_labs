n = int(input("Введите количество участников: "))
ochno = 0
zaochno = 0
for i in range(n):
    fam, name, age, form = input(
        "Введите свою фамилию, имя, возраст и форму обучения: "
    ).split()
    if form == "True":
        ochno += 1
    else:
        zaochno += 1
print("Очно: ", ochno, "Заочно: ", zaochno)
