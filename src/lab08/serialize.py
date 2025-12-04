import json
from pathlib import Path
from .models import Student
from typing import List


def students_to_json(students: List[Student], path: str) -> None:
    data = [s.to_dict() for s in students]
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Файл '{path}' не найден")

    with p.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    students = [Student.from_dict(item) for item in data]
    return students


if __name__ == "__main__":
    input_path = "data/lab08/students_input.json"
    output_path = "data/out/lab08/students_output.json"

    students = students_from_json(input_path)
    print("Студенты из input JSON:")
    for s in students:
        print(s)

    students_to_json(students, output_path)
    print(f"\nДанные сохранены в {output_path}")
