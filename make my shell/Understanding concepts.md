## 1.  access()
this command is used to check whether the calling program has access to a specified file. it can also check whether a file exist or not. this check is done by calling process read UID and GID
e.g
```c
int access(const char *pathname, int mode)
```
in the above, the first argument takes the path to hte directory/file, the second argument takes flags 
R_OK, 
W_OK, 
X_OK, 
F_OK

### Description
1. F_OK used to check for exisstence of file
2. R_OK used to chek for read permission bit
3. W_OK used to check for write permission bit
4. X_OK used to check for executable permision bit
if access cannot access the file, it will return -1 else it will return 0

e.,g
```c
#include<stdio.h>
#include<unistd.h>
#include<errno.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
  
extern int errno;
  
int main(int argc, const char *argv[]){
    int fd = access("sample.txt", F_OK);
    if(fd == -1){
            printf("Error Number : %d\n", errno);
        perror("Error Description:");
    }
        else
                printf("No error\n");
    return 0;
}
```
Note: the #extern keyword is used **before the global variable declaration**, the compiler understands you want to access a variable being defined in another program or file, and hence not to allocate any memory for this one. Instead, it simply points to the global variable defined in the other file

The **errno.h** header file of the C Standard Library defines the integer variable **errno**, which is set by system calls and some library functions in the event of an error to indicate what went wrong. This macro expands to a modifiable lvalue of type int, therefore it can be both read and modified by a program.

The POSIX error function, perror, is used in C and C++ to **print an error message to stderr**, based on the error state stored in errno. It prints str and an implementation-defined error message corresponding to the global variable errno.


## 2.  chdir()
The **chdir** command is a system function (system call) which is used to change the current working directory. On some systems, this command is used as an alias for the shell command [cd](https://www.geeksforgeeks.org/cd-command-in-linux-with-examples/). chdir changes the current working directory of the calling process to the directory specified in path.

**Syntax:**
```c
int chdir(const char *path);
```
**Parameter:** Here, the _path_ is the Directory path which the user want to make the current working directory.

**Return Value:** This command returns zero (0) on success. -1 is returned on an error and errno is set appropriately.
**Note:** It is declared in `unistd.h`.

example
```c
#include<stdio.h>
  
// chdir function is declared
// inside this header
#include<unistd.h> 
int main()
{   
    char s[100];
  
    // printing current working directory
    printf("%s\n", getcwd(s, 100));
  
    // using the command
    chdir("..");
  
    // printing current working directory
    printf("%s\n", getcwd(s, 100));
  
    // after chdir is executed
    return 0;
}
```
**Note:** The above program changes the working directory of a process. But, it doesn’t change the working directory of current shell. Because when the program is executed in the shell, the shell follows fork on exec mechanism. So, it doesn’t affect the current shell.

example 2
```c
#include<stdio.h>
#include<unistd.h>
int main()
{
    //pass your path in the function
    int ch=chdir("xxx");
    /*if the change of directory was successful it will print successful otherwise it will print not successful*/
    if(ch<0)
    printf("chdir change of directory not successful\n");
    else
    printf("chdir change of directory successful");
    return 0;
}
```

example 3
```c
#include <unistd.h>
#include <stdio.h>
  
// Main Method
int main() {
  
  // changing the current 
  // working directory(cwd)
  // to /usr
  if (chdir("/usr") != 0) 
    perror("chdir() to /usr failed");
  
  // changing the cwd to /tmp
  if (chdir("/tmp") != 0) 
    perror("chdir() to /temp failed");
  
  // there is no /error 
  // directory in my pc
  if (chdir("/error") != 0) 
  
    // so chdir will return -1 
    perror("chdir() to /error failed");  
  
  return 0;
}
```

**Errors:** There can be errors which can be returned. These depend on the filesystem.

-   **EACCES:** If the search permission is denied for one of the components of path.
-   **EFAULT:** If the path points lie outside the accessible address space.
-   **EIO:** If there is an I/O error occurred.
-   **ELOOP:** If there are too many symbolic links were encountered in the resolving path.
-   **ENAMETOOLONG:** If the path is too long.
-   **ENOENT:** If the file does not exist.
-   **ENOMEM:** If there is insufficient kernel memory is available.
-   **ENOTDIR:** If the component of path is not a directory.

## 3.  getcwd()
After using the **chdir()** function we might need to verify whether out current working directory has been changed or not for this we use the **getcwd()** function.
The getcwd() function places an absolute pathname of the current working directory in the array pointed to by buf, and returns buf. The size argument is the size in bytes of the character array pointed to by the buf argument. If buf is a null pointer, the behaviour of getcwd() is undefined.The return value represent our current working directory.

Syntax
```c
char *getcwd(char *buf, size_t size);
```

**Function return** :The **getcwd()** function returns a pointer which points to a character array where the path of current working directory is stored.In case the path is not found then it returns a null pointer and the contents of the array are undefined and the errno is set to indicate the type of error.

example
```c
#include <unistd.h>
#include <stdio.h>
int main() {
  char cwd[256];


    if (getcwd(cwd, sizeof(cwd)) == NULL)
      perror("getcwd() error");
    else
      printf("current working directory is: %s\n", cwd);
   
   return 0;   
  
}
```

## Using getcwd() to check changes made by chdir():

We can use **getchd()** to check whether after using the **chdir()** function the desired changes have been made or not.We first need to make the desired changes using the chdir() function and then use the getcwd() function to see whether the current working directory is the same as desired or not.

C code to check the changes made by chdir():
```c
#include<stdio.h>
#include<unistd.h>
int main()
{
  char cwd[256];

  if (chdir("Your desired path") != 0)
    perror("chdir() error()");
  else {
    if (getcwd(cwd, sizeof(cwd)) == NULL)
      perror("getcwd() error");
    else
      printf("current working directory is: %s\n", cwd);
  }  
}
```

## the `exec` System Call in C
The `exec` system call replaces the running process with some other executable process. The address space of the running process is replaced with the address space of the new process.

It is important to note that the new program is loaded into the same address space. The process id remains the same.

The new program will run independently; that is, the starting point will be the entry point of the new program. The `exec` system call has many variants.

1.  `execl`
2.  `execle`
3.  execlp
4.  `execv`
5.  `execve`
6.  execvp

These functions use the same base `exec` followed by one or multiple letters. The detail of the extra letters is below.

1.  `e` - Here, `e` is for environment variables; this function has an array of pointers that points to environment variables. The list of environment variables is explicitly passed to the newly loaded program.
2.  `l` - Here, `l` is for command line arguments. We can give the list of command line arguments to the function.
3.  `p` - Here, `p` is for the environment variable path. In this function, the path variable helps to find the file, passed as an argument to the newly loaded process.
4.  `v` - Here, `v` is also for the command line arguments. However, in this function, command line arguments are passed to the newly loaded process as an array of pointers.

In the basic `exec` system call, the current process address space is replaced with the newly loaded program’s address space; as a result, the currently running process is terminated. The freshly loaded process is passed as an argument in this system call.

The newly loaded process has the same process id, the same environment variables, and the same set of file descriptors. However, the CPU statistics and virtual memory are affected.

### [Syntax of `exec` Calls](https://www.delftstack.com/howto/c/execve-c/#syntax-of-exec-calls)

Here, we have six system calls’ syntax, variants of basic `exec` system calls.
```c

int execl(const char* path, const char* arg, ...)
int execle(const char* path, const char* arg, ..., char* const envp[])
int execlp(const char* file, const char* arg, ...)
int execv(const char* path, const char* argv[])
int execve(const char* path, const char* argv[], char* const envp[])
int execvp(const char* file, const char* argv[])
int execvpe(const char* file, const char* argv[], char* const envp[])

```
First, all functions’ return type is `int`. However, in case of a successful operation (that is, the new program is loaded and replaced), nothing is returned because the current program is no more there to receive the return value.

In failure due to some error, the new program is not loaded, and `-1` is returned to the existing program.

In the first argument, there is a difference between path and file. The `p`, `execlp`, `execvp`, and `execvpe` have a file instead of the path.

The `path` specifies the file’s full path to be executed/loaded. The `file` specifies the path name, which helps to locate the new program’s file.

In the second argument, the difference is that functions with `v` have a two-dimensional array of type `char` with multiple strings (including file name).

In contrast, other procedures have one or more one-dimensional arrays of type `char`, where the first element of this list contains the `file` name, the second element may include some parameters, etc.

Lastly, in the case of functions having `e`, a third/last parameter has an environment variable as an array of pointers.

Here, we have saved this program (with the name `execl0.c`) in the directory of executable code. This means both source and executable code exist in the same directory.
```c
#include <stdio.h>
#include <unistd.h>
int main(void) {
	char binaryPath[] = "/bin/wc";
	char arg1[]="wc";
	char arg2[]="-w";
	char arg3[]="execl0.c";
	printf ("First line of current program\n");
	execl(binaryPath, arg1, arg2, arg3, NULL);
	printf ("Last line of current program\n");
	return 1;
}
```
The above code uses an `execl` system call, having only a few simple variables of type `char*`. The first variable contains the path and name of the new program (to be executed), and the second variable has a parameter `wc` (again, the program’s name).

The third variable has a parameter `-w` to run the command as `wc -w` to count words in the source file.

It is also important to note two additional `print` statements, first before the system call and second at the end of the program.

The output shows that our new program is successfully loaded and executed. However, note that the first `print` statement is executed (see the first line of output (`'First line of current program'`).

The last `print` statement is not run because the current program automatically ends when a new program is successfully loaded.

The second output line shows the word count in the file `execl0.c`.
## [the `execve` System Call in C](https://www.delftstack.com/howto/c/execve-c/#the-execve-system-call-in-c)

Syntax:

```c
int execve(const char* path, const char* argv[], char* const envp[])
```

Here, the first argument is the `path`; as already discussed, the `path` environment variable helps to find the program to be executed as a new program.

The second argument is a two-dimensional array of characters or a one-dimensional array of strings having a list of command line arguments.

The third argument is again a two-dimensional array of characters or a one-dimensional array of strings having a list of environment variables.

In the `exec` family, `execve` is a compelling command with three arguments path, a list of command line arguments, and a list of environment variables. Let’s see a code to execute the `echo` command from the program.

```c
#include <stdio.h>
#include <unistd.h>
int main(void) {
	char *binaryPath = "/bin/bash";
	char *args[]={binaryPath, "-c", "echo visit $HOSTNAME:Fun with your browser","",NULL};
	char *const env[]={"HOSTNAME=www.linuxhint.com","port=8080",NULL};
	execve(binaryPath, args, env);
 	return 1;
}
```

In the first line of the primary function, `/bin/bash` is the path where the command exists. In the second line, the list of command line arguments contains three parameters before `NULL` that terminates the argument.

Again, the first argument is the path, and the second parameter, `-c`, stands for `cmd`, which allows passing code as a string.

The third parameter is the command; like in the code, `echo` is the command.

The code’s third line has two strings with two environment variables, `HOSTNAME` and `port`. Finally, the output of the code is:

```c
visit www.linuxhint.com:Fun with your browser
```

In this code, we have executed a Linux command from our program. Next, we will execute an external executable program inside the current program.

First of all, see this program:

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *args[]){
	int i;
	int count = atoi(args[1]);
	for (i = 1 ; i <= count ; i++)
		printf ("[%d]", i);
	printf ("\n");
	return 0;
}
```

This program is taking command line arguments. The command line argument (passed as a string) is converted to an integer in the second line of the `main` function.

Next, we run a loop from one to `count` and print counting in square brackets. See the output of this code.

```c
$ ./test 4
[1][2][3][4]
```

We have created the executable with the name `test`. We have executed the `test` file with parameter `4` from a command prompt.

We can see counting one to four in square brackets in the output.

Next, we have to run this program `test` as an external command from another program. For this, we have to specify the path of the executable `test` program.

Here, the complete path is `/home/mateen/Documents/test`. Therefore, we will specify this path in our next program to locate the executable file.

```c
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *ar[]) {
	printf("This is the first line\n");
	char *binaryPath = "/bin/bash";
	char name[80] = "/home/mateen/Documents/test ";
	strcat(name, ar[1]);
	char *args[]={binaryPath, "-c", name, NULL};
	char *env_args[] = {"/bin/bash", (char*)0};
	execve(binaryPath, args, env_args);
	printf("This is the last line\n");
  	return 1;
}
```

We have included another library to use the function to concatenate strings. In the third line of the `main` function, we have a complete path and file name because this is not a Linux command; instead, this is user defined executable program (already discussed in detail).

In the following line, we are concatenating the command line argument passed to our current program with the new program’s name. Again, in the fifth line, we have command line arguments having a path, `-c`.

The third parameter is the variable name having path + name of executable + argument passed to the current program.

Output:

```text
$ ./a.out 5
This is the first line
[1][2][3][4][5]
```

We are running our current program with the command line parameter `5`. The first line of output has the first `print` statement.

Next, you can see our test program is executed. The counting from `1` to `5` is written in square brackets.

Finally, the conclusion is we can run both Linux commands and our executable programs using `execve`. In the case of the Linux command, we can pass the path to locate the Linux program.

In the case of some other/external executable, we can give a complete path with the file name; in this case, the program will be automatically located at the given path. In this case, the command will ignore the path variable in the third line of the `main` function.