# Semantic_Analyzer

It uses syntax tree and symbol table to check whether the given program is semantically consistent with language definition. It gathers type information and stores it in either syntax tree or symbol table. This type information is subsequently used by compiler during intermediate-code generation.

### Semantic Errors:

Errors recognized by semantic analyzer are as follows:
* Type mismatch.
* Undeclared variables.
* Reserved identifier misuse.
* Multiple declaration of variable in a scope.
* Accessing an out of scope variable.
* Actual and formal parameter mismatch.

### Functions of Semantic Analysis:

* Type Checking – Ensures that data types are used in a way consistent with their definition.
* Label Checking – A program should contain labels references.
* Flow Control Check – Keeps a check that control structures are used in a proper manner.(example: no break statement outside a loop)

![image](https://user-images.githubusercontent.com/97080055/235754439-c8f59f6e-211d-4bf3-ad88-378427765c82.png)


### Architectural Diagram:

![image](https://user-images.githubusercontent.com/97080055/235754522-ad137423-1061-4c76-acfa-b7b2a06b616e.png)

### Static and Dynamic Semantics:
* Static Semantics – It is named so because of the fact that these are checked at compile time. The static semantics and meaning of program during execution, are indirectly related.
* Dynamic Semantic Analysis – It defines the meaning of different units of program like expressions and statements. These are checked at runtime unlike static semantics.

### Working Screenshots:

![image](https://user-images.githubusercontent.com/97080055/236691504-1bd6e717-819d-4c4b-9413-3a17132b4fe7.png)

![image](https://user-images.githubusercontent.com/97080055/236691535-14e06988-7b26-49ed-b218-d23e19d41396.png)

### Additional Screenshots:

![image](https://user-images.githubusercontent.com/97080055/236691627-f89c4997-fa62-4126-80ed-ff7a76ed5fde.png)

![image](https://user-images.githubusercontent.com/97080055/236691636-881b08f4-a23e-4838-8b9f-cbdbf009df53.png)

