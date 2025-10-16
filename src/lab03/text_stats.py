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