import csv
from pathlib import Path
from typing import List

from src.lab08.models import Student


class Group:
    HEADER = ["fio", "birthdate", "group", "gpa"]

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None: 
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(self.HEADER)

    def _read_all(self) -> list[dict]: 
        with self.path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if reader.fieldnames != self.HEADER:
            raise ValueError(f"Ожидаемые заголовки: {self.HEADER}, "
                             f"но получено: {reader.fieldnames}")

        return rows

    def _write_all(self, rows: list[dict]) -> None:
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]: 
        rows = self._read_all()
        return [Student.from_dict(r) for r in rows]

    def add(self, student: Student) -> None: 
        rows = self._read_all()

        rows.append(student.to_dict())

        self._write_all(rows)

    def find(self, substr: str) -> List[Student]:
        substr = substr.lower()
        rows = self._read_all()

        found = [
            Student.from_dict(r)
            for r in rows
            if substr in r["fio"].lower()
        ]

        return found

    def remove(self, fio: str) -> bool:
        rows = self._read_all()
        new_rows = [r for r in rows if r["fio"] != fio]

        if len(new_rows) == len(rows):
            return False  # ничего не удалили

        self._write_all(new_rows)
        return True

    def update(self, fio: str, **fields) -> bool:
        rows = self._read_all()
        updated = False

        for r in rows:
            if r["fio"] == fio:
                updated = True

                for key, value in fields.items():
                    if key not in self.HEADER:
                        raise KeyError(f"Недопустимое поле: {key}")
                    r[key] = value

                Student.from_dict(r)

                break

        if updated:
            self._write_all(rows)

        return updated