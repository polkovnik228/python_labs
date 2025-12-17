from src.lab09.group import Group
from src.lab08.models import Student


def main():
    print("Тест ЛР9")

    #__init__
    group = Group("data/lab09/students.csv")
    print("Группа инициализирована\n")

    #list()
    print("Список студентов (list):")
    for s in group.list():
        print(" ", s)
    print()

    #add()
    test_student = Student(
        fio="Сергеев Сергей Сергеевич",
        birthdate="2005-01-01",
        group="БИВТ-25-9",
        gpa=4.2
    )
    group.add(test_student)
    print("Добавлен студент:")
    print(" ", test_student)
    print()

    #после add
    print("Список после add:")
    for s in group.list():
        print(" ", s)
    print()

    #find()
    print("Поиск по подстроке 'Сергеев':")
    found = group.find("Сергеев")
    for s in found:
        print(" ", s)
    print()

    #update()
    print("Обновление GPA у 'Сергеев Сергей Сергеевич'")
    group.update("Сергеев Сергей Сергеевич", gpa=4.8)

    print("После update:")
    for s in group.list():
        print(" ", s)
    print()

    #remove()
    print("Удаление 'Сергеев Сергей Сергеевич'")
    group.remove("Сергеев Сергей Сергеевич")

    print("После remove:")
    for s in group.list():
        print(" ", s)
    print()

    print("Тест завершен")


if __name__ == "__main__":
    main()
