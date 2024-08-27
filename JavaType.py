from shlex import join
from JavaParser.JavaParserContextIf import JavaParserContextIf
from JavaParser.JavaTreeElementIf import JavaTreeElementIf
from JavaParser.JavaTypeIf import JavaTypeIf
from JavaParser.antlr.JavaParser import JavaParser
from PythonLib.Stream import Stream


class JavaType(JavaTypeIf):
    def __init__(self, typeTypeContext: JavaParser.TypeTypeContext, parent: JavaTreeElementIf, context: JavaParserContextIf) -> None:
        self.typeTypeContext = typeTypeContext
        self.parent = parent
        self.context = context
        self.externalType = None
        self.innerTypes = None

    def parse(self) -> JavaTypeIf:

        primitiveType = self.typeTypeContext.primitiveType()
        if primitiveType:
            self.externalType = primitiveType.getText()
        else:
            self.externalType = self.typeTypeContext.classOrInterfaceType().typeIdentifier()
            self.innerTypes = self.typeTypeContext.classOrInterfaceType().typeArguments()

        return self

    def toString(self) -> str:
        return self.typeTypeContext.getText()

    def getExternalType(self) -> str:
        if self.externalType:
            return self.externalType.getText()
        return ""

    def getInnerType(self) -> str:
        return "," \
            .join(Stream(self.innerTypes)
                  .map(lambda innerType: innerType.getText())
                  .collectToList()
                  )
