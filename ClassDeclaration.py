
from types import NoneType
from typing import List
from JavaParser.ClassDeclarationIf import ClassDeclarationIf
from JavaParser.ClassOrInterfaceDeclaration import ClassOrInterfaceDeclaration
from JavaParser.FieldDeclarationIf import FieldDeclarationIf
from JavaParser.JavaParserContextIf import JavaParserContextIf
from JavaParser.JavaTreeElementIf import JavaTreeElementIf
from JavaParser.antlr.JavaParser import JavaParser
from PythonLib.JOptional import JOptional
from PythonLib.Stream import Stream
from PythonLib.TreeStream import TreeElement, TreeStream


class ClassDeclaration(ClassOrInterfaceDeclaration, ClassDeclarationIf):
    def __init__(self, classDeclarationContext: JavaParser.ClassDeclarationContext,
                 javadocContext: JavaParser.JavadocContext, parent: JavaTreeElementIf, context: JavaParserContextIf) -> None:

        ClassOrInterfaceDeclaration.__init__(self, classDeclarationContext, javadocContext, parent, context)

        self.classDeclarationContext = classDeclarationContext
        self.superClass: str = None
        self.fields: List[FieldDeclarationIf] = []
        self.parse()

    def parse(self) -> None:

        ClassOrInterfaceDeclaration.parse(self)

        self.superClass = JOptional(self.classDeclarationContext.typeType()) \
            .map(lambda t: t.classOrInterfaceType()) \
            .map(lambda i: i.getText()) \
            .orElse(None)

        memberDeclarationWithJavaDocContexts: List[JavaParser.MemberDeclarationWithJavaDocContext] = JOptional(self.classDeclarationContext).toStream() \
            .map(lambda classDeclarationContext: classDeclarationContext.classBody()) \
            .flatMap(lambda classBodyContext: Stream(classBodyContext.classBodyDeclaration())) \
            .map(lambda classBodyDeclarationContext: classBodyDeclarationContext.memberDeclarationWithJavaDoc()) \
            .collectToList()

        for memberDeclarationWithJavaDocContext in memberDeclarationWithJavaDocContexts:
            javaDocContext: JavaParser.JavadocContext = memberDeclarationWithJavaDocContext.javadoc()

            self.methods = self.methods + Stream.of(memberDeclarationWithJavaDocContext) \
                .map(lambda memberDeclarationWithJavaDocContext: memberDeclarationWithJavaDocContext.memberDeclaration()) \
                .map(lambda memberDeclarationContext: memberDeclarationContext.methodDeclaration()) \
                .map(lambda methodDeclarationContext: self.context.createClassMethodDeclaration(methodDeclarationContext, javaDocContext, self)) \
                .collectToList()

            self.methods = self.methods + Stream.of(memberDeclarationWithJavaDocContext) \
                .map(lambda memberDeclarationWithJavaDocContext: memberDeclarationWithJavaDocContext.memberDeclaration()) \
                .map(lambda memberDeclarationContext: memberDeclarationContext.genericMethodDeclaration()) \
                .map(lambda genericMethodDeclarationContext: genericMethodDeclarationContext.methodDeclaration()) \
                .map(lambda methodDeclarationContext: self.context.createClassMethodDeclaration(methodDeclarationContext, javaDocContext, self)) \
                .collectToList()

            self.fields = self.fields + Stream.of(memberDeclarationWithJavaDocContext) \
                .map(lambda memberDeclarationWithJavaDocContext: memberDeclarationWithJavaDocContext.memberDeclaration()) \
                .map(lambda memberDeclarationContext: memberDeclarationContext.fieldDeclaration()) \
                .map(lambda fieldDeclarationContext: self.context.createFieldDeclaration(fieldDeclarationContext, javaDocContext, self)) \
                .collectToList()

            # self.methods1 = self.methods1 + Stream(memberDeclarationWithJavaDocContexts) \
            #     .map(lambda memberDeclarationWithJavaDocContext: (memberDeclarationWithJavaDocContext.memberDeclaration(), memberDeclarationWithJavaDocContext.javadoc())) \
            #     .filter(lambda memDecContJavadocCont: not isinstance(memDecContJavadocCont[0], NoneType)) \
            #     .map(lambda memDecContJavadocCont: (memDecContJavadocCont[0].methodDeclaration(), memDecContJavadocCont[1])) \
            #     .filter(lambda methDecContextJavadocCont: not isinstance(methDecContextJavadocCont[0], NoneType)) \
            #     .map(lambda methDecContextJavadocCont: self.context.createCassMethodDeclaration(methDecContextJavadocCont[0], methDecContextJavadocCont[1], self)) \
            #     .collectToList()

            # self.methods1 = self.methods1 + Stream(memberDeclarationWithJavaDocContexts) \
            #     .map(lambda memberDeclarationWithJavaDocContext: (memberDeclarationWithJavaDocContext.memberDeclaration(), memberDeclarationWithJavaDocContext.javadoc())) \
            #     .filter(lambda memDecContJavadocCont: not isinstance(memDecContJavadocCont[0], NoneType)) \
            #     .map(lambda memDecContJavadocCont: (memDecContJavadocCont[0].genericMethodDeclaration(), memDecContJavadocCont[1])) \
            #     .filter(lambda genMethDecContextJavadocCont: not isinstance(genMethDecContextJavadocCont[0], NoneType)) \
            #     .map(lambda genMethDecContextJavadocCont: (genMethDecContextJavadocCont[0].methodDeclaration(), genMethDecContextJavadocCont[1])) \
            #     .filter(lambda methDecContextJavadocCont: not isinstance(methDecContextJavadocCont[0], NoneType)) \
            #     .map(lambda methDecContextJavadocCont: self.context.createCassMethodDeclaration(methDecContextJavadocCont[0], methDecContextJavadocCont[1], self)) \
            #     .collectToList()

        Stream(self.methods).foreach(lambda method: method.parse())
        Stream(self.fields).foreach(lambda field: field.parse())

    def getSuperClass(self) -> str:
        return self.getFullQualifiedNameByShortNames([self.superClass])[0]

    def getFields(self) -> List[FieldDeclarationIf]:
        return self.fields
