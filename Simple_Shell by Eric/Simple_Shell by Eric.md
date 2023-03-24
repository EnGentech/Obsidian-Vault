
# Notes...

log unto youtube and search for c-simple shell to get more insight

## Taking off from file descriptors

a file descriptor is basically the value associated to the macros that defines input, output and error a file. it has the following description
		STDIN_FILENO          this represents 0 as file descriptor
		STDOUT_FILENO          this represents 1 as file descriptor
		STDERR_FILENO          this represents 2 as the file descriptor
we can use write comand to test this
```c
write(1, "EnGentech", 10)
```

in exercise 0 of file program, create the text file as described in the test page, create the main as given and define your prototype as follows

```c
#ifndef FILE_H
#define FILE_H

//paste your protoype here

#endif
```
in the main
```c
#include "main.h"
#include libraries neccesary
/**

*/

ssize_t read_textfile(const char *filename, size_t letters)
{
if (filename != NULL)
{
int fd;
char *buf
ssize_t r_bytes, w_bytes;

fd = open(filename, 0_RDONLY);
//Note that if the open fuction fails, it will return a -1, hence that should be taken care of

if(fd = -1)
return (0);

//read(fd, buf, count)
//the buf could have been define as char buf[letters] but the -wall gcc compiler will not allow such function to work since it was not in existence before now, so do it the hard way. instead of that use malloc to allocate a dynamic memory
if(buf == NULL)
return (0);
buf = malloc(letters + 1)
buf[leters] = 0;

r_bytes = read(fd, buf, letters);
if (r_bytes == -1)
return (0);

w_bytes = write(STDOUT_FILENO, buf, r_bytes)
if (w_bytes == -1)
return (0);

if (r_bytes != w_writes)
return (0);

// at this stage we need a clean up to free the memory
free(buf);
close(fd);

return (w_bytes);
}
else
return (0)
}

//compile the program and run, however to read from the text file, run the program in the followin manner, instead of using ./a.out, use ./a.textfilename
```

## Simple Shell Depth
### Understanding the potentials of simple shell

check for a youtube channel with the name hhp3. for more details

## Starting from the concept page
Everything you need to know to start coding your own shell
PID means Process ID

Every process is given an ID
e.g, every shell, like the bash shell has a process ID. if you have a shell running, like the bash shell, and you hence run your shell on the bash shell, then you have a parent process id PPID.
to oget the PID, you can use the getpid command.
The getpid returns the process ID of the calling process. e.g

```c
#include <sys/types.h>
#include <unistd.h>

int main()
{
printf("%u\n", getpid());
return (0);
}
```
in the shell command, you can use ps command to know the shell process that is currently running
you can use htop or top to view the process ID currently running in your linux system

tty command shows the terminal you are currently on, if two bash terminal are open, using ps a without the dash will list the two terminals that are open.

the process ID is needed when we are writing processes upon processes. you can import the process and apply in your process

## Get ppid
the ppid is the parent process ID which could be displayed using echo $ $ (no space in between the $) which is the bash process
the maximum value of process your machine can run can be found using the command cat /proc/sys/kernel/pid_max

### example
```c 
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <string.h>

int main()
{
  char get;
 printf("%u\n", getpid());
  get = getchar();
 return (0); 
}
```

the exercise 0 tells us to write a program that prints all the arguments without using ac, this can be done by setting the ac variable to excemption. however on a lighter path, lets use a simple code without the macros. 
```c
#include <stdio.h>

int main(int agrc, char **argv) 
{
  while(*argv != NULL)
    printf("%s\n", *argv), argv++;
}
```

the next line tells us to Write a program that prints `"$ "`, wait for the user to enter a command, prints it on the next line.
looking at the reference page, we are adviced to use or man 3 getline command. lets do that

the getline allocates memory on the heap, whether if fails or not, the programmer needs to free its memory.
the syntax for the getline is 
```c 
sssize_t(char **lineptr, size_t *n, FILE *stream)
```
in there, the  n is a size_t data type which means the it is a positive integer data type, the FILE is determined by where the source of data will come from. basically stdin but is subjected to change if deem needful. 
another interesting thing is the second paragraph of the description in the man 3 getline page, its states thus:
if * lineptr is set to NULL during initialization, and n is set to 0, the getline() function will allocate a buffer for storing thelin. this buffer should be freed by user program even if the getline fails.

Lets write a simple program to illustrate that 
```c
#include <stdio.h>

int main(int agrc, char **argv) 
{
  char *lineptr = NULL;
  size_t n = 0;
  
  printf("$ ");
  getline(&lineptr, &n, stdin);
  
  printf("%s", lineptr);
  }
```
or
```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(int agrc, char **argv) 
{
  char *lineptr = NULL;
  size_t n = 0;
  ssize_t ret;
  
  printf("$ ");
  
  ret = getline(&lineptr, &n, stdin);
  if(ret == -1)
  {
  printf("%s", strerror(errno));
    }
    else
  {
    printf("%s", lineptr);
    }
  free(lineptr);
  
  
  return (0);
  }
```
in the above program, the getline allocates memory byte for the program using the n variable, while pointer is actualy the value given by the user, and the stdin is the standard input which informt the compiler that the source is coming from the keyboard.

however the getline comes with a newline because it replicated every character is pased by the user, hence the enter key which symbolises a new line is passed into the program, hence no need for \\n while using printf function.

in the shell environment, the character typed initialy when the enter key is not pressed is saved somewhere in a buffer which is not yet sent to the bash. at this point, the characters inputted is handled by the system kernel, whose responsibility is to perform the ascii conversions of that value typed by means of input and output streams. 
eg
```sh
root$ this is typed
```
but immediately, the enter key is pressed, the values is sent to the bash system which will hence evaluate the command and where it does not meet any command in the PATH, it returns an errno message depending on the input.

Next, we are to write a function that splits a string and returns an array of each word of the string. we are adviced to use strtok in this task and also try to do same without the use of strtok.
in the man page, 

the strtok is a function of tokenization. by declaration, its syntax is 
```c
char *strtok(char *str, const char *delim)
```
it has a similar output as that of the av program we wrote above by seperating the characters pending onthe delimiter provided, in the argv, the white space character is the seperation point, where the next character pointer to the beginning of the new word to be captured

e,g
```c
#include <string.h>
#include <stdio.h>

int main()
{
  char str[] = "Hello world, this is EnGentech";
  strtok(str, " ");

  printf("%s\n", str);

  return (0);
}
```
for the above code, the str will print just once since the strtok was referenced once int he program, this  will print only hello on the stdout.
to print all, the below code is applied;
```c
#include <string.h>
#include <stdio.h>

int main()
{
  char str[] = "Hello world, this is EnGentech";

  //create an array to store the strtok values
  int i = 1;
  int j;
  char *arr[10];

  arr[0] = strtok(str, " ");
  
  while (arr[i] != NULL)
    {
      
      arr[i] = strtok(NULL, " ");
      i++;
    }

  for (j = 0; arr[j] != NULL; j++)
  printf("%s\n", arr[j]);

  return (0);
}
```

## Execve
the execve function takes up all the environment that main function possess, this means that the head, env, data and all allocated resources given to main will be given to execve as a new process.. 

when running an execve command, it can either return 0 or -1, where -1 means that the function did not find the command presented by the user through the path
lets demostrate
```c
#include <stdio.h>
#include <unistd.h>

int main(void)
{
  char *argv[] = {"/bin/ls", "-lha", NULL};

  execve(argv[0], argv, NULL);
}
```
e.g 2 with return failed errno description
```c
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

int main(void)
{
  int val;
  char *argv[] = {"/bn/ls", "-lha", NULL};

  val = execve(argv[0], argv, NULL);
  if (val == -1)
  {
    printf("%s\n", strerror(errno));
  }
 
}
```

### Working with environment vectors
this are all parameters given to a child process
e.g
```c
#include <stdio.h>

int main(int argc, char **argv, char **env)
{
  int loop;
  for(loop = 0; env[loop] != NULL; loop++)
  printf("%s\n", env[loop]);
  return (0);
}
```
by the above, it means that your parent environmet variable will be copied from the parent process to the child process when created

Note: the above double pointer is not sacrosanct as a single pointer can be applied, but that helps to speed up the typing process and safe time though the single pointer is more readable compared to the double pointer. e.g.
```c
int main(int argc, char *argv[], char *env[])
```
this and the above will produce same result, a double pointer is a format of pointer pointing to an array of strings.


# More on Simple shell
basically when we allocate memory using getline, the operating system freed the memory after use hence the need for free is not very essential, however in the case of a swap memory (a swap memory is an allocation of HDD memory to act as a RAM), this memory does not get freed by the Operating system, for instance lets wrtie an infinite loop.
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
while (1)
memset(malloc(1024), 0, 1024);
return 0;
}
```
use the shell command
```sh
btm -r 250
//this is use to load the memory chat 
```
Note: the above wont work on virtual machine as the main OS will immediately kill the infinite memory loop allcocation, hence use your local machine to prove this is need be.