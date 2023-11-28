import os

from pathlib import Path

ROOT_DIRECTORY = root_path = os.path.dirname(os.path.dirname(__file__))


def read_fixture(file: str) -> str:
    with open(
        Path(ROOT_DIRECTORY).joinpath(ROOT_DIRECTORY, "tests", "files", file).with_suffix(".json"),
        encoding="utf-8",
    ) as data_file:
        return data_file.read()
