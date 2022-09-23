import os
from typing import TextIO

ROOT_DIRECTORY = root_path = os.path.dirname(os.path.dirname(__file__))


def load_fixture(path: str) -> TextIO:
    return open(os.path.join(ROOT_DIRECTORY, "tests/files", path), encoding="utf-8")
