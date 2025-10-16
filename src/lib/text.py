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

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld")) 
# print(normalize("  двойные   пробелы  "))  


def tokenize(text: str) -> list[str]:
    return re.findall(r'\b[\w]+(?:-[\w]+)*\b', text)

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))


def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

# tokens = ["a", "b", "a", "c", "b", "a"]
# print(count_freq(tokens))
# print(top_n(count_freq(tokens), 2))
