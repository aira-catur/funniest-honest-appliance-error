import os
from pathlib import Path

FINAL_LINE = "ERROR: Magnetron dead. I will still spin your soup, light it dramatically, and beep proudly when it is ready to still be cold."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
