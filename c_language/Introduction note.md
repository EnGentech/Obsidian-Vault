# Runing C programs in bash

----

## Installing the compiler gcc

### Step 0 - Check if gcc is installed

```bash
which gcc
```

### Step 1 - Installing the gcc compiler

```bash
apt-get install gcc
```

### Step 2 - Check it version (optional)

```bash
gcc --version
```

## writing a program

### Step 1 - create a c file

```bash
touch hello.c
vi hello.c
```
### Step 2 - add a header

```c
#include <stdio.h>

```

#include is a way of including a standard or user-defined file in the program 
without it we cannot run the function printf()

<stdio.h> 
stands for Standard Input Output.
It has the information related to input/output functions.



| Functions | Description |
|---|---|
| printf() | It is used to print the strings, integer, character etc on the output screen. |
| scanf() | It reads the character, string, integer etc from the keyboard. |
| getc() | It reads the character from the file. |
| putc() | It writes the character to the file. |
| fopen() | It opens the file and all file handling functions are defined in stdio.h header file. |
| fclose() | It closes the opened file. |
| remove() | It deletes the file. |
| fflush() | It flushes the file. |



## Some standard header files in C
| Header Files  | Description |
|---|---|
| stdio.h | Input/Output functions |
| conio.h | Console Input/Output functions |
| stdlib.h | General utility functions |
| math.h | Mathematics functions |
| string.h | String functions |
| ctype.h | Character handling functions |
| time.h | Date and time functions |
| float.h | Limits of float types |
| limits.h | Size of basic types |
| wctype.h | Functions to determine the type contained in wide character data |


### Step 3 - Add the starting point of execution 
```c
int main() {
  // your code here
}
```

int main(){ }: This is the starting point of the code.
All the code inside the curly braces {} runs first.

### Step 4 - Add a code inside the main function

```c
// output a line
printf("Hello World!\n");
```

This line of code prints, or outputs, the text “Hello World!” to the console.
Printing text to the console is one way for a program to communicate with the user.


// output a line: This is a comment.
It is not a line of code but a message we can add to code
to tell ourselves or others what the code does.
When the code is run this line will be ignored.

## Compile and Run Program

### Compile
gcc hello.c -o hello

#### Execute a file

## Variables and Data-types declaration
