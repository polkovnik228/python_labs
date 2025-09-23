fio = input("ФИО: ")
fio_clean = " ".join(fio.split())
parts = fio_clean.split()
initials = "".join([p[0].upper() for p in parts]) + "."

print(f"Инициалы: {initials}")
print(f"Длина (символов): {len(fio_clean)}")
