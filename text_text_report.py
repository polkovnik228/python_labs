import sys
from pathlib import Path
from collections import Counter
from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize

DATA_DIR = Path("data/lab04")
DATA_DIR.mkdir(parents=True, exist_ok=True)

#не существует
missing_file = DATA_DIR / "missing.txt"
print("Проверка: файл не существует")
try:
    read_text(missing_file)
except FileNotFoundError:
    print(f"Ошибка: файл {missing_file} не найден.\n")

#Пустой вход
empty_file = DATA_DIR / "empty_input.txt"
empty_file.write_text("")

print("Проверка: пустой файл")
text = read_text(empty_file)
tokens = tokenize(normalize(text))
freq = Counter(tokens)

report_empty_csv = DATA_DIR / "report_empty.csv"
write_csv(sorted(freq.items(), key=lambda x: (-x[1], x[0])),
          report_empty_csv, header=("word", "count"))

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print(f"CSV создан: {report_empty_csv}\n")

#Нестандартная кодировка
cp1251_file = DATA_DIR / "input_cp1251.txt"
cp1251_file.write_text("Привет", encoding="cp1251")

print("Проверка: кодировка CP1251")
text = read_text(cp1251_file, encoding="cp1251")
tokens = tokenize(normalize(text))
freq = Counter(tokens)

report_cp1251_csv = DATA_DIR / "report_cp1251.csv"
write_csv(sorted(freq.items(), key=lambda x: (-x[1], x[0])),
          report_cp1251_csv, header=("word", "count"))

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print(f"CSV создан: {report_cp1251_csv}")
