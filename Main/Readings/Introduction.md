# INTRODUCTION

## What is Data?
Data can be defines as a raw facts and figures.

## What are variables?
A place holders for represting a data.<br>
Remember, in mathematics we solve equations like **5x + 2y = 3** since childhood.🤘Here, x and y are names that are used to hold the values (data). Similarly in Computer Science we need something to hold the data , and variable is the way to do that.

## What are data types?
The data type in programming languages, is a set of predefined values. Exapmle: integer, floating point, character, strings etc. <br>
Computer memory is all filled with zeroes and ones. If we have a problem and we want to code it, it's very difficult to provide the solution in terms of zeroes and ones. To help users, programming languages and compilers provide us with data types. For example, integer takes 2 bytes (actual value depends upon compiler) means we are combining 16 bits and calling it an integer, similarly combining 32 bits calls float. <br>
This way it helps in reducing the coding efforts. <br>

There are two types of data types: <br>
* System-defined data types (Primitive Data Type)
* User-defined Data Types

### System-defined data types (Primitive Data Types)
* Data types that are defined by system are called **primitive data types**. 
* The primitive data types provided by many programming languages are: int, float, char, double, bool, etc.
* The number of bits allocated for each primitve datat type deepnds on the programming languages, the compiler and the operating system. For the same primitive data type, different languages may use different sizes.
* Depending on the size of the data type, the total available values (domain) will also change.
* For example, `int` may take 2 bytes or 4 bytes. If it takes 2 bytes (16 bits), then total possible values are minus 32,768 to plus 32,767 **(-2<sup>15</sup> to 2<sup>15</sup>-1)**. If it takes 4 bytes (32 bits), then the possible values are between minus 2,147,483,648 to plus 2,147,483,647 **(-2<sup>31</sup> to 2<sup>31</sup>-1)**. The same is the case with other data types.

### User defined data types
* Most programming languages allow the users to define their own data types, called **user defined data types**.
* For example: Structures, Classes.
* One of the syntax for structure is as follows using structure name as "typeOne":
```md
struct typeOne {
  int data_1;
  float data_2;
  double data_3;
  ...
  ...
  ...
 };
 ```
 * This gives more flexibility and comfort in dealing with computer memory.
