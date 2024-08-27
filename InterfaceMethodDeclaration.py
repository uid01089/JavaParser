from typing import List
from JavaParser.CommonMethodDeclaration import CommonMethodDeclaration
from JavaParser.JavaFileIf import JavaFileIf
from JavaParser.JavaParserContextIf import JavaParserContextIf
from JavaParser.JavaTreeElementIf import JavaTreeElementIf
from JavaParser.antlr.JavaParser import JavaParser
from PythonLib.JOptional import JOptional
from PythonLib.Stream import Stream
from PythonLib.StringUtil import StringUtil


class InterfaceMethodDeclaration(CommonMethodDeclaration, JavaTreeElementIf):
    def __init__(self, methodDeclarationContext: JavaParser.InterfaceMethodDeclarationContext, javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf, context: JavaParserContextIf) -> None:
        CommonMethodDeclaration.__init__(self, methodDeclarationContext, javadocContext, parent, context)

        self.methodDeclarationContext = methodDeclarationContext

    def parse(self) -> None:

        CommonMethodDeclaration.parse(self)

        self.identifier = JOptional(self.methodDeclarationContext.interfaceCommonBodyDeclaration()) \
            .map(lambda interfaceCommonBodyDeclaration: interfaceCommonBodyDeclaration.identifier()) \
            .map(lambda identifierContext: identifierContext.getText()) \
            .orElse("")

        self.returnType = JOptional(self.methodDeclarationContext.interfaceCommonBodyDeclaration()) \
            .map(lambda interfaceCommonBodyDeclaration: interfaceCommonBodyDeclaration.typeTypeOrVoid()) \
            .map(lambda typeTypeOrVoidContext: typeTypeOrVoidContext.typeType()) \
            .map(lambda typeTypeContext: self.context.createJavaType(typeTypeContext, self).parse().toString()) \
            .orElse("void")

        JOptional(self.methodDeclarationContext.interfaceCommonBodyDeclaration()) \
            .map(lambda interfaceCommonBodyDeclaration: interfaceCommonBodyDeclaration.formalParameters()).toStream() \
            .map(lambda formalParametersContext: formalParametersContext.formalParameterList()) \
            .flatMap(lambda formalParameterListContext: Stream(formalParameterListContext.formalParameter())) \
            .foreach(lambda formalParameterContext: self._handleFormalParameter(formalParameterContext))

    def getChildren(self) -> List[JavaTreeElementIf]:
        return self.parameters

    def getJavaCode(self) -> str:

        javaCode = self.getParentElement(JavaFileIf).getJavaCode()

        start = self.methodDeclarationContext.start
        stop = self.methodDeclarationContext.stop

        return StringUtil.extractSubString(javaCode, start.line - 1, start.column, stop.line - 1, stop.column + 1)

    def getJavaCodeMethodDeclaration(self) -> str:
        return self.getJavaCode()
