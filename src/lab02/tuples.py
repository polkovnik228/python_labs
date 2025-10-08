def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует запись о студенте.
    
    Параметры:
        rec: кортеж (fio: str, group: str, gpa: float)
    
    Возвращает:
        Строку формата "Фамилия И.И., гр. GROUP, GPA X.XX"
    
    Правила:
    - ФИО может содержать 2 или 3 части, лишние пробелы убираются.
    - Инициалы берутся из имени и (при наличии) отчества.
    - GPA округляется и выводится с 2 знаками после запятой.
    
    Исключения:
    - ValueError — если ФИО или группа пустые.
    - TypeError — если GPA не число.
    """
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError("Ожидается кортеж из 3 элементов: (fio, group, gpa)")

    fio, group, gpa = rec

    # Проверяем типы
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("fio и group должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    # Убираем лишние пробелы
    fio = " ".join(fio.strip().split())
    group = group.strip()
    if not fio or not group:
        raise ValueError("ФИО и группа не могут быть пустыми")

    parts = fio.split()
    if len(parts) < 2 or len(parts) > 3:
        raise ValueError("ФИО должно содержать 2 или 3 слова")

    surname = parts[0].capitalize()
    initials = "".join(p[0].upper() + "." for p in parts[1:])

    # Форматируем строку GPA
    gpa_str = f"{gpa:.2f}"

    return f"{surname} {initials}, гр. {group}, GPA {gpa_str}"
