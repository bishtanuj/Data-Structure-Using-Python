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

## Data Structures
Once we get data in the variables, we need some mechanism for manipulating that data to solve problem. **Data Structure** is a particular way of storing and organizing data in computer so that it can be used efficiently. A data structure is a special format for organizing and storing data. <br>
General data structures include arrays, linked list, files, stacks, queues, trees, graphs and so on.

Depending on the organization of the elements, data structures are classified into two types:
1) **Linear data structures**: Elements are accessed in a sequential order but it is not compulsory to store all elements sequentially. Examples: Linked Lists, Stacks and Queues.
2) **Non - linear data structures**: Elements of this data structure are stored/accessed in a non-linear order. Example: Trees and Graphs.

## Abstract Data Types
We all know that, by default, all primitive data types support basic operations such as addition and subtraction. The system provides the implementations for the them. For user defined data types we also need to define operations. The impelementation for these operations can be done when we want to actually use them. That means, in general, user define data types are defined along with their operations.

To simplify the process of solving problems, we combine the data structures with their operations and we call this Abstract Data Types (ADTs). An ADT consists of two parts:
1. Declaration of data 
2. Declaration of operations

Commonly used ADTs include: Linked Lists, Stacks, Queues, Priority Queues, Binary Trees, Dictionaries, Disjoint Sets (Union and Find), Hash Tables, Graphs and many others.

While defining the ADTs do not worry about the implementation details. They come into the picture only when we want to use them. Different kinds of ADTs are suited to different kinds of appliactions, and some are highly specialized to specific tasks.

## What is an Algorithm?
An algorithm is a sequence of clear and precise step-by-step instructions for solving a problem in a finite amount of time.

NOTE: We do not have to prove each step of the algorithm.

### Properties of an Algorithm
- It should take zero or more input.
- It should produce atleast one output.
- It should terminate within finite time.
- Every step in the algorithm should be deterministic (Unambiguous).
- Every step in the algorithm should perform something (don't write unnecessary statements).
- It should be programming independent.
