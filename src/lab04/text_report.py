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
