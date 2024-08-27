from __future__ import annotations
from abc import ABC, abstractmethod


class JavaTypeIf(ABC):

    @abstractmethod
    def parse(self) -> JavaTypeIf:
        pass

    @abstractmethod
    def toString(self) -> str:
        pass

    @abstractmethod
    def getExternalType(self) -> str:
        pass

    @abstractmethod
    def getInnerType(self) -> str:
        pass
