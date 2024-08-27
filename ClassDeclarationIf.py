from abc import abstractmethod
from typing import List

from JavaParser.ClassOrInterfaceDeclarationIf import ClassOrInterfaceDeclarationIf
from JavaParser.FieldDeclarationIf import FieldDeclarationIf


class ClassDeclarationIf(ClassOrInterfaceDeclarationIf):

    @abstractmethod
    def getSuperClass(self) -> str:
        pass

    @abstractmethod
    def parse(self) -> None:
        pass

    @abstractmethod
    def getFields(self) -> List[FieldDeclarationIf]:
        pass
