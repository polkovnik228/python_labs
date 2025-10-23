# Лабораторная работа №4 — Файлы: TXT/CSV и отчёты по текстовой статистике

## Задание A — модуль `src/lab04/io_txt_csv.py`

```python
from pathlib import Path
import csv
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    
    p = Path(path)
    rows = list(rows)
    if rows and len({len(r) for r in rows}) != 1:
        raise ValueError("Все строки должны иметь одинаковую длину")

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        for r in rows:
            writer.writerow(r)
```

## Задание B — скрипт `src/lab04/text_report.py`

```python
from collections import Counter
from pathlib import Path
from src.lib.text import normalize, tokenize, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main():
    input_path = Path("data/lab04/input.txt")
    output_path = Path("data/lab04/report.csv")

    text = read_text(input_path)

    tokens = tokenize(normalize(text))

    freq = Counter(tokens)

    top5 = top_n(freq, 5)

    sorted_rows = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    write_csv(sorted_rows, output_path, header=("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
```

## A. Один файл (база)

#### Вход: (`data/input.txt`):
![image4.2](../../images/lab04/input_txt.png)

#### Итог: `report.csv`:
![image4.3](../../images/lab04/report_csv.png)

#### Консоль:
![image4.4](../../images/lab04/console.png)


## B. Пустой файл

#### Вход: пустой (`data/input.txt`):
![image4.5](../../images/lab04/empty_input_txt.png)

#### Итог: `report.csv` содержит только заголовок:
![image4.6](../../images/lab04/report_csv_2.png)

#### Консоль:
![image4.7](../../images/lab04/console2.png)


## C. Кодировка cp1251

#### Вход: (`data/input.txt`) в cp1251 с текстом Привет:
![image4.7](../../images/lab04/input_cp1251.png)

**Действие:** `python src/lab04/text_report.py --in data/input.txt --encoding cp1251`  

#### Итог: `report.csv`:
![image4.8](../../images/lab04/report_csv_3.png)

#### Консоль:
![image4.9](../../images/lab04/console3.png)
