#### Hello World
Write a script that runs a C file through the preprocessor and save the result into another file.
```c
gcc -E $file_name -o output_Name
```

Write a script that compiles a C file but does not link.
```c
gcc -s $file_name
```

Write a script that generates the assembly code of a C code and save it in an output file.
```c
gcc -S -o $file_name
```

Write a script that compiles a C file and creates an executable named `cisfun`.
```c
gcc $file_name -o outputname
```

Write a C program that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
```c
printf("\"Programming is like building a multilingual puzzle,\n")
```


Write a script that generates the assembly code (Intel syntax) of a C code and save it in an output file.
```c
gcc -S -masm=intel $CFILE
```



UNIX is basically a simple operating system, but you have to be a genius to understand the simplicity
```c
#include <stdio.h>                                                                            #include <unistd.h>                                                                                                                                                                         /**                                                                                            * main - Entry point                                                                          *                                                                                             * Return: Always 1 (Success)                                                                  */                                                                                                                                                                                         int main(void)                                                                                {                                                                                             write(2, "and that piece of art is useful\" - Dora Korpar, 2015-10-19\n", 59);                return (1);                                                                                   } 
```