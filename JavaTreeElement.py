from typing import List, Type, TypeVar, Optional

from antlr4 import ParserRuleContext
from JavaParser.CompilationUnitIf import CompilationUnitIf
from JavaParser.JavaTreeElementIf import T, JavaTreeElementIf
from JavaParser.antlr.JavaParser import JavaParser
from PythonLib.JOptional import JOptional
from PythonLib.Stream import Stream
from PythonLib.TreeStream import TreeElement, TreeStream

JavaGenericType = ['String', 'Class', 'Integer', 'Float']


class JavaTreeElement(JavaTreeElementIf):
    def __init__(self, this: Optional[ParserRuleContext], parent: JavaTreeElementIf) -> None:
        self.parent = parent
        self.this = this

    def getParent(self) -> JavaTreeElementIf:
        return self.parent

    def getParentElement(self, classType: Type[T]) -> Optional[T]:
        runner = self
        while runner:
            if isinstance(runner, classType):
                return runner
            try:
                runner = runner.getParent()
            except AttributeError:
                return None
        return None

    def getUsedTypes(self) -> List[str]:
        if self.this:
            treeElement = TreeElement(self.this, "getChildren")
            usedTypes: List[str] = TreeStream(treeElement) \
                .toStream() \
                .filter(lambda element: isinstance(element, JavaParser.ClassOrInterfaceTypeContext)) \
                .map(lambda element: element.typeIdentifier()) \
                .map(lambda typeIdentifierContext: typeIdentifierContext.getText()) \
                .collectToSet()

            fullQualifiedTypes = self.getFullQualifiedNameByShortNames(usedTypes)

            return fullQualifiedTypes
        return []

    def getFullQualifiedNameByShortNames(self, shortNames: List[str]) -> List[str]:

        fullQualifiedNames: List[str] = []

        compilationUnit: CompilationUnitIf = self.getParentElement(CompilationUnitIf)
        importDeclarations = compilationUnit.getImportDeclarations()

        for shortName in shortNames:

            # Check if shortname (not dot)
            if shortName is not None and "." not in shortName:

                # check if imported type
                for importDec in importDeclarations:
                    if importDec.endswith(f".{shortName}"):
                        fullQualifiedNames.append(importDec)
                        break

                else:
                    # not imported (no break), then it is declared within the execution unit or is used out from the same package
                    if shortName not in JavaGenericType:
                        fullQualifiedNames.append(f'{compilationUnit.getPackageDeclaration()}.{shortName}')
                    else:
                        fullQualifiedNames.append(shortName)
            else:
                # Not a short name
                fullQualifiedNames.append(shortName)

        return fullQualifiedNames

    def _getType(self, typeTypeContext: JavaParser.TypeTypeContext) -> str:
        return JOptional(typeTypeContext) \
            .map(lambda typeTypeContext: typeTypeContext.classOrInterfaceType()) \
            .map(lambda classOrInterfaceTypeContext: classOrInterfaceTypeContext.typeIdentifier()) \
            .map(lambda typeIdentifierContext: typeIdentifierContext.getText()) \
            .orElse(JOptional(typeTypeContext)
                    .map(lambda typeTypeContext: typeTypeContext.primitiveType())
                    .map(lambda primitiveType: primitiveType.getText())
                    .orElse("")
                    )
