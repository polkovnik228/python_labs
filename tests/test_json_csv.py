import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    csv_file = tmp_path / "people.csv"
    json_file = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]
    with csv_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)

    csv_to_json(str(csv_file), str(json_file))

    with json_file.open(encoding="utf-8") as f:
        loaded = json.load(f)

    assert loaded == data


@pytest.mark.parametrize("bad_file", ["", "notjson.txt"])
def test_json_to_csv_invalid_file(tmp_path: Path, bad_file):
    path = tmp_path / bad_file
    with pytest.raises((ValueError, FileNotFoundError)):
        json_to_csv(str(path), str(tmp_path / "out.csv"))


@pytest.mark.parametrize("bad_file", ["", "notcsv.txt"])
def test_csv_to_json_invalid_file(tmp_path: Path, bad_file):
    path = tmp_path / bad_file
    with pytest.raises((ValueError, FileNotFoundError)):
        csv_to_json(str(path), str(tmp_path / "out.json"))
