from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")
class Report(ABC, Generic[T]):
    @abstractmethod
    def generate(self, rows: list[dict[str, str]]) -> list[tuple[str, T]]:
        pass