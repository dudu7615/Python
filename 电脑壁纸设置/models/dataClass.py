from dataclasses import dataclass


@dataclass
class Font:
    name: str
    size: int


@dataclass
class Config:
    name: str
    size: tuple[int, int]
    font: Font
    color: tuple[int, int, int]
    place: dict[str, tuple[int, int]]
