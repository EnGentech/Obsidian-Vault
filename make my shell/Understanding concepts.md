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
