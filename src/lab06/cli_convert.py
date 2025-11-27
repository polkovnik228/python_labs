import argparse
import sys
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def cmd_json2csv(args):
    try:
        json_to_csv(args.input, args.output)
        print(f"Готово: {args.input} → {args.output}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_csv2json(args):
    try:
        csv_to_json(args.input, args.output)
        print(f"Готово: {args.input} → {args.output}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_csv2xlsx(args):
    try:
        csv_to_xlsx(args.input, args.output)
        print(f"Готово: {args.input} → {args.output}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


def build_parser():
    parser = argparse.ArgumentParser(
        description="CLI-конвертеры данных (JSON, CSV, XLSX)"
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    # json -> csv
    p1 = subparsers.add_parser("json2csv", help="Конвертировать JSON → CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON-файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV-файл")
    p1.set_defaults(func=cmd_json2csv)

    # csv -> json
    p2 = subparsers.add_parser("csv2json", help="Конвертировать CSV → JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON-файл")
    p2.set_defaults(func=cmd_csv2json)

    # csv -> xlsx
    p3 = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV → XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX-файл")
    p3.set_defaults(func=cmd_csv2xlsx)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
