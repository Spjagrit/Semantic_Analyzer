# Semantic_Analyzer
It uses syntax tree and symbol table to check whether the given program is semantically consistent with language definition. It gathers type information and stores it in either syntax tree or symbol table. This type information is subsequently used by compiler during intermediate-code generation.

### Semantic Errors:
Errors recognized by semantic analyzer are as follows:
* Type mismatch
* Undeclared variables
* Reserved identifier misuse

### Functions of Semantic Analysis:
* Type Checking – Ensures that data types are used in a way consistent with their definition.
* Label Checking – A program should contain labels references.
* Flow Control Check – Keeps a check that control structures are used in a proper manner.(example: no break statement outside a loop)

![image](https://user-images.githubusercontent.com/97080055/235754439-c8f59f6e-211d-4bf3-ad88-378427765c82.png)


### Architectural Diagram

![image](https://user-images.githubusercontent.com/97080055/235754522-ad137423-1061-4c76-acfa-b7b2a06b616e.png)

### Static and Dynamic Semantics:
1. Static Semantics –
