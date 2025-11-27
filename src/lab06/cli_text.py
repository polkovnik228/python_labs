import argparse
from pathlib import Path
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n


def cmd_cat(args):
    path = Path(args.input)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if args.n:
                print(f"{i}: {line.rstrip()}")
            else:
                print(line.rstrip())


def cmd_stats(args):
    path = Path(args.input)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    text = path.read_text(encoding="utf-8")

    text_norm = normalize(text)
    tokens = tokenize(text_norm)
    freq = count_freq(tokens)

    top = top_n(freq, args.top)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{args.top}:")
    for w, c in top:
        print(f"{w}: {c}")


def build_parser():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для анализа текста (cat, stats)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_p = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_p.add_argument("--input", required=True, help="Путь к файлу")
    cat_p.add_argument("-n", action="store_true", help="Нумеровать строки")
    cat_p.set_defaults(func=cmd_cat)

    stats_p = subparsers.add_parser("stats", help="Частотный анализ слов")
    stats_p.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_p.add_argument(
        "--top", type=int, default=5, help="Сколько слов выводить (по умолчанию 5)"
    )
    stats_p.set_defaults(func=cmd_stats)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
