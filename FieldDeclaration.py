from typing import List
from JavaParser.FieldDeclarationIf import FieldDeclarationIf
from JavaParser.JavaDoc.JavaDocIf import JavaDocIf
from JavaParser.JavaParserContextIf import JavaParserContextIf
from JavaParser.JavaTreeElement import JavaTreeElement
from JavaParser.JavaTreeElementIf import JavaTreeElementIf
from JavaParser.antlr.JavaParser import JavaParser
from PythonLib.JOptional import JOptional
from PythonLib.Stream import Stream


class FieldDeclaration(JavaTreeElement, FieldDeclarationIf):
    def __init__(self, fieldDeclarationContext: JavaParser.FieldDeclarationContext, javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf, context: JavaParserContextIf) -> None:
        JavaTreeElement.__init__(self, fieldDeclarationContext, parent)
        self.context = context
        self.fieldDeclarationContext = fieldDeclarationContext
        self.javaDocAsString = JOptional(javadocContext).map(lambda ctx: ctx.getText()).orElse("")

        self.type = ""
        self.identifiers: List[str] = []
        self.javaDoc: JavaDocIf = None

    def parse(self) -> None:
        self.type = JOptional(self.fieldDeclarationContext) \
            .map(lambda fieldDeclarationContext: fieldDeclarationContext.typeType()) \
            .map(lambda typeTypeContext: self._getType(typeTypeContext)) \
            .orElse("")

        self.identifiers = Stream.of(self.fieldDeclarationContext) \
            .map(lambda fieldDeclarationContext: fieldDeclarationContext.variableDeclarators()) \
            .flatMap(lambda variableDeclaratorsContext: Stream(variableDeclaratorsContext.variableDeclarator())) \
            .map(lambda variableDeclaratorContext: variableDeclaratorContext.variableDeclaratorId()) \
            .map(lambda variableDeclaratorIdContext: variableDeclaratorIdContext.identifier()) \
            .map(lambda identifierContext: identifierContext.getText()) \
            .collectToList()

        self.javaDoc = self.context.createJavaDoc(self.javaDocAsString).parse()

    def getType(self) -> str:
        return self.type

    def getIdentifiers(self) -> List[str]:
        return self.identifiers

    def getChildren(self) -> List[JavaTreeElementIf]:
        return []

    def getDescription(self) -> str:
        return self.javaDoc.getDescription()
