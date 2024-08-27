from abc import ABC, abstractmethod
from typing import Optional

from JavaParser.ClassDeclarationIf import ClassDeclarationIf
from JavaParser.CompilationUnitIf import CompilationUnitIf
from JavaParser.FieldDeclarationIf import FieldDeclarationIf
from JavaParser.InterfaceDeclarationIf import InterfaceDeclarationIf
from JavaParser.JavaDoc.JavaDocContextIf import JavaDocContextIf
from JavaParser.JavaFileIf import JavaFileIf
from JavaParser.JavaPackageIf import JavaPackageIf
from JavaParser.JavaProjectIf import JavaProjectIf
from JavaParser.JavaTreeElementIf import JavaTreeElementIf
from JavaParser.JavaTypeIf import JavaTypeIf
from JavaParser.MethodDeclarationIf import MethodDeclarationIf
from JavaParser.antlr.JavaParser import JavaParser


class JavaParserContextIf(JavaDocContextIf):

    @abstractmethod
    def createJavaFile(self, parent: JavaTreeElementIf) -> JavaFileIf:
        pass

    @abstractmethod
    def createCompilationUnit(self, compilationUnitContext: JavaParser.CompilationUnitContext, parent: JavaTreeElementIf) -> CompilationUnitIf:
        pass

    @abstractmethod
    def createClassDeclaration(self, classDeclarationContext: JavaParser.ClassDeclarationContext,
                               javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf) -> ClassDeclarationIf:
        pass

    @abstractmethod
    def createInterfaceDeclaration(self, interfaceDeclarationContext: JavaParser.InterfaceDeclarationContext,
                                   javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf) -> InterfaceDeclarationIf:
        pass

    @abstractmethod
    def createClassMethodDeclaration(self, methodDeclarationContext: JavaParser.MethodDeclarationContext, javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf) -> MethodDeclarationIf:
        pass

    @abstractmethod
    def createInterfaceMethodDeclaration(self, methodDeclarationContext: JavaParser.InterfaceMethodDeclarationContext, javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf) -> MethodDeclarationIf:
        pass

    @abstractmethod
    def createJavaProject(self) -> JavaProjectIf:
        pass

    @abstractmethod
    def getJavaProject(self) -> JavaProjectIf:
        pass

    @abstractmethod
    def createJavaPackage(self, name: str, root: Optional[JavaPackageIf] = None) -> JavaPackageIf:
        pass

    @abstractmethod
    def createFieldDeclaration(self, fieldDeclarationContext: JavaParser.FieldDeclarationContext, javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf) -> FieldDeclarationIf:
        pass

    @abstractmethod
    def createJavaType(self, typeTypeContext: JavaParser.TypeTypeContext, parent: JavaTreeElementIf) -> JavaTypeIf:
        pass
