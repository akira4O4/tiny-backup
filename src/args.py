from dataclasses import dataclass


@dataclass
class Args:
    input: str
    output: str
    time: int = 1
    zip: bool = False
