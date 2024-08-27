from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from JavaParser.JavaFileIf import JavaFileIf
from JavaParser.JavaTreeElementIf import JavaTreeElementIf


class JavaPackageIf(JavaTreeElementIf):

    @abstractmethod
    def addJavaFile(self, javaFile: JavaFileIf) -> None:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def getSubPackages(self) -> List[JavaPackageIf]:
        pass

    @abstractmethod
    def getJavaFiles(self) -> List[JavaFileIf]:
        pass
