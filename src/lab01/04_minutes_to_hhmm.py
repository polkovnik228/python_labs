def minutes_to_hhmm(m):
    hours = m // 60
    remaining_minutes = m % 60
    return f"{hours}:{remaining_minutes:02d}"


m = int(input("Минуты: "))
result = minutes_to_hhmm(m)
print(f"{result}")
