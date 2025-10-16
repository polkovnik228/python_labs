# Лабораторная работа №3 — Тексты и частоты слов

## Задание A (normalize)

```python
import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    for ch in ['\n', '\r', '\t']:
        text = text.replace(ch, ' ')
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = ' '.join(text.split())
    return text

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld")) 
print(normalize("  двойные   пробелы  ")) 
```
![image3.1](./images/lab03/normalize.png)

## Задание A (tokenize)

```python
def tokenize(text: str) -> list[str]:
    return re.findall(r'\b[\w]+(?:-[\w]+)*\b', text)

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
![image3.2](./images/lab03/tokenize.png)

## Задание A (count_freq и top_n) 

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

tokens = ["a", "b", "a", "c", "b", "a"]
print(count_freq(tokens))
print(top_n(count_freq(tokens), 2))
```
![image3.34](./images/lab03/top_n-count_freq.png)

## Задание B

```python
import sys
import os
from pathlib import Path

lib_path = Path(__file__).resolve().parent.parent / 'lib'
sys.path.insert(0, str(lib_path))

from text import normalize, tokenize, count_freq, top_n


def analyze_text(text):
    normalized = normalize(text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)
    return len(tokens), len(freq), top_words


def print_stats(total, unique, top_words, table=False):
    print(f"Всего слов: {total}")
    print(f"Уникальных слов: {unique}")
    
    print("Топ-5:")
    if table:
        print_table(top_words)
    else:
        for word, count in top_words:
            print(f"{word}:{count}")


def print_table(top_words):
    if not top_words:
        return
    
    word_width = max(len("слово"), max(len(w) for w, _ in top_words))
    freq_width = max(len("частота"), max(len(str(c)) for _, c in top_words))
    
    print(f"{'слово':<{word_width}} | {'частота':<{freq_width}}")
    print("-" * (word_width + freq_width + 3))
    
    for word, count in top_words:
        print(f"{word:<{word_width}} | {count:<{freq_width}}")


def main():
    try:
        text = sys.stdin.read()
    except KeyboardInterrupt:
        print("\nПрервано", file=sys.stderr)
        return
    
    if not text.strip():
        print("Ошибка: пустой ввод", file=sys.stderr)
        return
    
    total, unique, top = analyze_text(text)
    table_format = os.environ.get('TABLE_FORMAT', '0') == '1'
    print_stats(total, unique, top, table_format)


if __name__ == "__main__":
    main()
```
![image3.5](./images/lab03/text_status.png)



