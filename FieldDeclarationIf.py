from abc import ABC, abstractmethod
from typing import List

from JavaParser.JavaTreeElementIf import JavaTreeElementIf


class FieldDeclarationIf(JavaTreeElementIf):

    @abstractmethod
    def getType(self) -> str:
        pass

    @abstractmethod
    def getIdentifiers(self) -> List[str]:
        pass

    @abstractmethod
    def getDescription(self) -> str:
        pass
