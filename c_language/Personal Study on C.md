### Categories of C language
	1. Documentation section 
	2. Link section (this is the header file level e.g #include <stdio.h>)
	3. Definition section (#define PI 3.142, this is like constant that can be used in the program several times)
	4. Global declaration function ( this are variables declared outside a function, int a[tis is a global declaration of variable], void a [this is a global declaration of a function])
	5. the main section
	6. sub program section

### Constant in C
constant are divided into two segments
1. Numeric and 
2. characters

Numeric is sub divided into integer and floating
integer is sub divided into decimal, octal and hexadecimal
floating are real constant

Character are divided into character constant and string constants

a Decimal value ranges from 0 - 9
an octal value is written beginning from 0, e.g 01 is an octal value of 1
an hex value is written thus 0x14, 0xa4

### Character constant
character constant is written with with a single quote e.g 'a' 'c'
in ascii, the a represent 97 and capital A represents 65

in a nutshell, a - z is represented by 97 - 122
capital A - Z is represented by 65 - 90
0 - 9 is represented by 0 - 47
special character is reprented by 0 - 47, 58 - 64, 91 - 96

note this, if you print a value assumes below, 
printf("%c", 97): this is will display a because the c represents  character constant, that is to say that you wish to print the equivalent character of 97.
the same thing is noted when you print the below
printf("%d", 'a'): this will display 97 because the d represents an integer notation, this implies that your are converting the characteer a to its equivalent ascii value which is 97

### String Constant
A string is a  single character or characters enclosed in a double quote, this is to say that 'a' and "a" is not seen as the same thing because a single quote represent a character constant and a double quote represents a double quote.

## Constant declaration
a constant declaration is written as 
```c
const int a = 10;
# the above cannot be changed since it is declared as a constant value
```

## Variables in C
Variable is simply a name memory location. note that the momory of a computer has its address which we cant assume nor touch but we can create a memory location by naming them as a variable name e.g
```c
sum = a + b
```
#### Declaration of a variable
to declare you neet a datatype and a variable name as seen below
```c
int a;
# where the int is the datatype and the a is the variable name
```
note that you cannot  use the 32 C keywords to make a variable in c language nor any other languages

## Identifiers and Keywords in C
c language has 32 keywords called researved words or predefined words
Keywords are basic building words for writing programs in C language, e.g of this keywords are
int, float, goto, for, continue, while, do, switch, auto, double etc.
note that keywords in c language are all lower case letters

Identifiers are variables, functions, unions. etc. these are user defined names basically made to identify names to suit their needs
only letters, numbers and underscored are allowd, no special characters and spaces are allowed

## Data types
this is used to define the type of data to be stored in a variable and how much memory is to be allocated in the memory.
#### types of data types
1. primary data types
* int, float, char, double, void

2. Derived data type
* array
* structure union
* pointers

3. User defined
* typedef
* enumerated

the int data type can be short and long int, further classified into signed and unsigned
unsigned int should have no sign, this is to say that only positive values are allowed in an unsigned values.
The size of the datatype may differ from language and system architecture, for instance in c language, the below code can be used to fing out the size of int
```c
printf("%lu", sizeof(int))

# the lu represent long unsigned
```
if your value is short, its better to use short int instead of using the int, that is waste of memory

Float
float prints values with decimal points, the decimal point is in six places having about 4 bytes.
the float extension can be extended to double or long double.
The double is in 8 bytes with 8 bytes with the precision of 14 decimal points, the long has about 10bytes storage space. their format is seen respectively below
```c
printf("%f", float)
printf("%lu", double)
printf("%Lu", long double)
```
### More on Data types
a signed vales of int on a 16bit system will range from -32768 to +32767 and an unsigned int will take the value of 0 - 65534, this is bacause the value for the signed is divided into 2 parts. lets illustrate this in a fomat in binary notation, two bytes memory is declared with a diagram of two 8 bits registers composing of 0's and 1's
lets use a little program to further expantiate the concent
```c
#include <stdio.h>
#include <conio.h>
void main()
{
int a = 32767;
clrscr();
printf("%d",a);
getch();
}

# the clrscr() and getch() is used on the library conio.h
# if the a above is changed to 32768, the value wil be changed from positive to negative because the signed value positively stopped at 32767 but since the value 32768 is within the range of the value, it will print but negatively

# however,to print the value as it was written, the  unsigned value could be used to print the value as given because the unsigned int has no negative value hence the values wont de divided

# i.e
#include <stdio.h>
#include <conio.h>
int main()
{
int a = 32768;
clrscr();
printf("%u", a);
getch();
}
```

## Char 
```c
#include <stdio.h>
int main()
{
char a = 'a';
char b = 98;
char c = 'z';
char d = 130;
char d = -130;
char d = -129
printf("%c", b);
printf("%d", a);
}
```

## Operators
Operators are symbols that tell the computer what arithmetical or logical valuations should be carried out by the computer.
Expressions is the manipulations of operators and an operand
```c
sum = 5 + 5
# the 5 is the operand to the operator + and =
```
### Types of Operators
#### based on operands
* Unary (one operand)
* binary (two operands)
* tenary (three operands)

Unary consists of  -, ++, --, !, &, sizeof
e.g
```c
a = a + (-b)
# the - with the b is the unary operator
++x [#prefix]
x++ [#postfix]
```
```c
!(y>x) 
# where y is 10 and x is 5, looking at that values, its certain that y is greater than x but since the unary operator (not) was a attached to the value, it will return a false result from the expected output

#include <stdio.h>
int main(void)
{
int x = 10, y;
y = ++x;
printf("%d", x);
printf("%d", y);

# run the program and after try the same program with x++, x-- and --x
}
```

### Binary operator
The binary takes two operands which constitute
* Arithmetic (+, -, /, \*, %*)
```c
#include <stdio.h>
#include <conio.h>
int main(void)
{
int a = 10, b = 7;
clrscr();
printf("a + b = %d", a+b);
printf("a-b = %d", a-b);
printf("a*b = %d", a*b);
printf("a/b = %d", a/b);
printf("a%b = %d", a%b);
getch();
}
# note that modulus only takes the format specifier of %d
# arithmetic precidence is assigned from left to right LR
```
* relational (<, >, <=, >=, !=)
```c
# this operators are used to compare values
e.g
3<5 (this will return a true value because 3 is less than 5, it can return 1 as a boolean value when it is true and 0 when it is false)
a+b < b+c
# you can also compare character like
'a'>'b' 
# that should be equal to 0 because in character a is seen as 97 and b 98
# strings cannot be compared, if that is done, it will compare its memory address which is not humanly known
```
```c
#include <stdio.h>
#include <conio.h>
{
int main(void)
int a=18, b=9, c, d, e=10
clrscr();
c=b++
d=b,
printf("%d", a<b<c>d);
printf("%d", b==e);
printf("%d", c+1>e);
printf("%d", a+c==b>e<c+d);
# note that arithmetic operators have higher precidence that relational operators
# in the relational signs, <, >, >= and <= have higher precidence before == and != with its associativity of left to right
# try this
printf("%d",a+c==b>=e<c+d!=1); 
}
```
* logical (&&, ||, !)
```c
# this is used to test more than one expressions, it could be called compound relational expressions like
a<b && c<d
# the output will eithe be 1 or 0
int a = 10, b = 5
a==b && b<a
# lets evaluate the above, in other of precidency, the b<a is taken first, hence is b less than 5? the answer is 0 and for the second part, is a == b, no hence the value stored is 0, then the logical statement of 0 and 0 is 0 hence the result will be 0

# the ! is used to check negation example
!0 = 1
!6 = 0
```
```c
#include <stdio.h>
#include <conio.h>
void main()
{
int a = 4, b = 6, result, result2;
result = a>b && printf("EnGentech");
result2 = a>b && printf("EnGentech") || printf("lectures");
printf("%d", result);
printf("%d",result2);
}
```
* bitwise (&, |, <<, >>, ^, ~)
```c
# this operations is used to perform operations at bit level, remember that bit is the smallest unit of memoroy in computer. this operation can only be applied on character and integer level
& bitwise and
| bitwise or
^ bitwise xor
~ bitwise not
<< left shift
>> right shift

int a = 10, b = 5;
a & 5
# convert 10 and 5 to binary
# the above is done by performing a binary and to the values above
# that is 1 0 1 0
#       x 0 1 0 1
#       = 0 0 0 0        bitwise or will be 15, try the conversion
# in bitwise nor, the value can only true when the result has a different values, i.e  0 0 = 0, 1 1 = 0 and 1 0 = 1, 0 1 = 1

void main()
{
int a = 10, b = 6;
clrscr();
printf("%d", a & b);
printf("%d", a | b);
printf("%d", a ^ b);
printf("%d" a&b && b+1 || 0 || b++)
}

# More on bitwise
# << shift operators
# it could be written in the form of variable (var) << and a number (3)
# the above means that you should shift the values by left shift operator in bit level, lets take for instance 
 int a = 10
 c = a << 2
# from the above, convert the value into 8 bits of 10, that is |0|0|0|0|1|0|1|0|
# after that, shift the value in two bits such that the last bits will be lost, then fill in the empty front cells with 0's and the result will be |0|0|1|0|1|0|0|0|

# the short approach to validate the answer is the value given, lets say 10 multiply by 2 to the power of the values to be shifted i.e 10x2^2


# the same approach is taken in shift right with the difference of shifting it to the right instead of left, the short cut is same with the above but with division rather than multiplication. if there's any remainder from the result, ignore the fractional part.

# bitwise not
int a = 5
b=~a
# in the above, lets take a sample of 4 bits, 5 = |0|1|0|1|, applying the bitwise not, inverse every bits, hence 0 becomes 1 and 1 becomes 0 respectively 
```
* equality (\==, \!=)
* comma (,)
* assignment (=)
```c
a=b=c=d=e=5
# the above is RL (right to left assignment)
 a = a+(c*10) is the same thing as a+=c*10
```

### Ternary operator
this is more of a conditional statement written in the format below
```c
expression1 ? expression 2 : expression 3
# in the above expressions, the first expression is the condition, if true, the second expression is evaluated else the third expression 

e.g
int a = 10, b = 15;
x = a>b ? a : b;
```

## Special Operators
A comma is an operator used in seperation. It has least precident, example
```c
int a, b, c
# that is to seperate those variables
# the above sample, the comma is used as a seperator but when used like seen below
a = 5, 4;
# the comma there is used as an operator
# in the above, a will be assigned to the value of 5
a = (5,4), 
# a will be assigned the value 4
int a =5,4
# that will return an error since comma is used there as a seperator and not as an operator
int a  (5,4)
# in the above, 4 will be assigned to a because 5 will be evalueated but will be rejected 
# try this example and evaluate the answer

int a = (printf("Gentle"), 6)
b = (a++, ++a, a>>2)
```
## Table of Precidence and Associativity

## Formatted input function in c (Scanf())
```c
#include <stdio.h>
#include <conio.h>
int main()
{
int a, b, sum;
clrscr();
scanf("%d %d", &b, &a);
sum = a + b,

# the operation is don in the syntax of scanf("control string", arg1, arg2 ..... argn)
# you write %4d, it means that any value you enter will be reduced to 4 values only.
# format specifiers
	# %f   float
	# %d   integer
	# %lf  Double
	# %Ld  Long integer
	# %c   char
	# %e   exponent
}
```

### Formatted input in c (Printf())
```c
# the same syntax is undertaken in terms of the scanf, however the difference is that in the scanf, the called variable name will be attached with a & sign example scanf("%d", &variable_name) while the printf is not accompanied with the & sign. example printf("%d", variable_name)
# A printf function can be easily used to print a message
 printf("%10.2f",a);
 # the abe is formatted to take 10 digits of a real value and 2 decimal point
```

### Unformatted Input
unformatted characters consist of getchar(), getch(), getche() and gets()
```c
int main()
{
char ch;
ch = getchar();
printf("%c", ch);
}
# in the above code, the program will only print one character irrespective of how many values is entered on the screen

int main()
{
ch = getch();
printf("%c", ch);
}

# In the above program, it will allow user to enter only one value, this will take the entered value and pront immediately but the value you entered wont be displayed per input but output
int main()
{
ch = getche();
printf("%c", ch);
}
# The above have similatities with the older only that the value inputted will be displayed and immediately the cursor will jump over to the next line and display the result

int main()
{
char ch[10]
gets(ch);
printf("%s", ch);
getch();
}
# The above is used to get strings instead of single value

# The above uses no format in getting and printing its output hence why it is called unformmated inputs
```

### Unformatted Output
they include putchar(), putch(), and puts()                                                                                                                                                                                                     
```c 
void main()
{
char ch;
printf("Enter a character");
ch = getchar();
printf("\n character is = %c", ch)
getch();
}
# putchar is used to print a single character eg
putchar('n')
putch('k'), 
# the two above works in same way only that the putch is defined in conio.h while the putchar is defined in the stdio.h
puts(ch);
# the puts is used same way as printf, it can print strings just like the printf but without a format specifier, it also has a built in new line defined, hence there's not need for \n during its declaration
# what output will be received if puts('a') is inputted
```

## Control statements in C
control statements includes if, if else, if else if , switch
### If statement
syntax for writing if statement is 
```c
if(condition)
	statement
end of statement

void main()
{
printf("Enter a");
scanf("%d", &a);
if(a)
print("Inside if block");
print("Out of if block");
getch();
}
# When using an if statement with only a single statement, it is needless using a curly bracket, but if the statemtent is more than one statement, then the curly bracket should be use
# Using the semi-colon after the if statement like if(a); will not return an error but will terminate the if command and hence print the values that was within its block
Assignment: write a program using nested if to check the maximum number between three numbers
```  
### Switch case
```c
switch (expression)
{
	case value.1:
		block of statement;
		break
	case value 2:
		block of statement;
		break;
	case value n:
		block of statement;
		break;
	default:
		default statement;
# the default statement is not compulsory to be written at the end, it could be written anywhere within the program. also it is not compulsory to include default as the program will leave the switch empty if the value entered was not documented and the default was not declared
# note that only integer and character values are allowed in swtich statement. note that only integer are allowed in switch, the reason the character is allowed is because it is intepreted as a number in the ascii number system

write a simple calculator using the switch statement
}
```

## Loops in C language
Loops is simply an re-iteration of a certain task in multiple folds or times. every loops has 3 factor, the initialization stage, the termination condition and the loop sequence. 
there are two aspects of loops
1. The entry control loop 
2. The exit control loop
this can be expressed using a flowchart
do while is an exit control loop, for loop is an entry control loop
```c
syntax for a for loop
for(expression1 (initialization); expression 2(condition); expression 3(update))
{
//loop body
}

for(i=1;i<=10;i++)
{
printf("i = %d", i )
}
# the initialization can take place outside the for loop e.g
int i = 1;
for( ; i<=10; i++)

for(i=1, j=0; i<=10; i++)
# in that case the i will be continuously incrememted while the j remains 0

for(i=1, j=0; i<=10,j<5; i++)

for(i=1;  ;i++)

for(i=1,j=1; i<=5,j<3, i++,j++)

for(i=1,j=1; i<=5 && j<3, i++,j++)

for(i=1,j=1; i<=5 || j<3, i++,j++)

#printing a table of any number
#include <stdio.h>
#include <conio.h>
int main()
{
int number, i, a;
printf("Enter a number:");
scanf("%d", &number);
for(i=1;i<=10;i++)
{
a=number*i;
printf("%d\n",a);
}
getch();
}
```

## Do while loop
```c
do
{
statement block;
modify\update } while (condition);
#this is an exit loop
```

## Nested loops
lets assume  you need to print ##### in six line
that will become
```c
for(j=1; j<=6;j++)
{
	for(i=1;i<=5;i++)
	{
	printf("*");
	}
print("\n")
}
```
nested while loop
```c
while (condition)
{
	while(condition)
	{
	inner loop statement block;
	}	
outer loop statement block;
}
```
sample program
```c
int i =0, j = 1;
while(i<=3)
{
	while(j<=3)
	{
	printf("%d",j++)
	}
printf("%d",i++)

}
```

```c
#include <stdio.h>

/**
 * main - Entry point
 *
 *Return: Always 0 (Success)
 */

int main(void)
{
	char put[8] = "_putchar";
	int i;
	for(i = 0; put[i]; i++)
	{
		putchar(put[i]);
	}
putchar('\n');
return (0);
}

# the above program will print _putchar on the screen, however, the _putchar will be printed in characters per time since we are using the putchar keyword
```

highest number
```c
#include "main.h"

/**
 * largest_number - returns the largest of 3 numbers
 * @a: first integer
 * @b: second integer
 * @c: third integer
 * Return: largest number
 */

int largest_number(int a, int b, int c)
{
int largest;

if (a > b && a > c)
{
largest = a;
}
else if (b > a && b > c)
{
largest = b;
}
else
{
largest = c;
}

return (largest);
}


# OR


#include "main.h"

/**
 * largest_number - returns the largest of 3 numbers
 * @a: first integer
 * @b: second integer
 * @c: third integer
 * Return: largest number
 */

int largest_number(int a, int b, int c)
{
int largest = (a > b) ? a : b;

largest = (largest > c) ? largest : c;

return (largest);
}
```

## Validate remaining days of the year
```c
#include <stdio.h>
#include <stdbool.h>

// Function to check if a year is leap or not
bool isLeapYear(int year)
{
    // A year is a leap year if it is divisible by 4
    // but not by 100, or if it is divisible by 400
    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}

int main()
{
    // Input year
    int year = 2000;

    // Input month and day
    int month = 2;
    int day = 9;

    // Check if year is a leap year
    bool leap = isLeapYear(year);

    // Total number of days in the given year
    int totalDays = leap ? 366 : 365;

    // Calculate the number of days passed so far in the year
    int daysPassed = 0;

    // Days in each month
    int daysInMonth[] = {31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // Loop through each month before the given month and add the days in it
    for (int i = 0; i < month - 1; i++)
    {
        daysPassed += daysInMonth[i];
    }

    // Add the number of days in the given month
    daysPassed += day;

    // Calculate the number of days remaining in the year
    int daysRemaining = totalDays - daysPassed;

    printf("There are %d days remaining in the year %d", daysRemaining, year);

    return 0;
}
```
or
```c
#include <stdio.h>
#include "main.h"

/**
 * print_remaining_days - takes a date and prints how many days are
 * left in the year, taking leap years into account
 * @month: month in number format
 * @day: day of month
 * @year: year
 * Return: void
 */

void print_remaining_days(int month, int day, int year)
{
if ((year % 4 == 0 && year % 100 != 0) || (year % 4 == 0))
{
if (month > 2 && day >= 60)
{
day++;
}

printf("Day of the year: %d\n", day);
printf("Remaining days: %d\n", 366 - day);
}
else
{
if (month == 2 && day == 60)
{
printf("Invalid date: %02d/%02d/%04d\n", month, day - 31, year);
}
else
{
printf("Day of the year: %d\n", day);
printf("Remaining days: %d\n", 365 - day);
}
}
}


```

## Using putchar to print 1 to 14 was not easy
```c
#include "main.h"

/**

* more_numbers - print 0 to 14 ten times

*

* Return: always 0 (Success)

*/

void more_numbers(void)

{

int i;

int j;

for (i = 0; i <= 9; i++)

{

for (j = 0; j <= 14; j++)

{

if (j > 9)

{

_putchar((j / 10) + '0');

}

_putchar((j % 10) + '0');

}

_putchar('\n');

}

}
```
## Nested Do while loop
```c
do 
{
	outer loop statement block
	do
	{
		inner loop statement block
	}
	outer loop statement block
}
```
example
```c
int i = 1, j = 3;
do 
{
	do
	{
		printf("%d", j);
		j--;
	}while (j > 0);
	i++;
	print("%d", i);
}while(i < 4);
```

# Array in C
syntax for declaring aray
datatype variable_name[size of array]
Note that all values to be stored should be of the same data type
At compile time
```c
int a[5]
int a[] = {4,5,34,2,3,5}
int a[4] = {0}
int a[2 + 4]
int a[N] //where the N is not a variable but rather a macro
```
At run time
```c
int i;
int a[5];
printf("enter element for array);
	   for(i = 0; i < 5; i++)
	   {
		   scanf("%d", &a[i]);
	   }
```

an intance of a multitudinous array, the bellow can be used
```c
int a[100], i;
for (i = 0; i < 100; i++)
{
	if(i < 30);
		 a[i] = 1;
	else
		a[i] = 0;
}
	//the above explain on 1-D array
```

lets take in values and print same using array
```c
void main()
int a[5], i;
for (i = 0; i < 5; i++)
{
	scanf("%d", &a[i]);
}
for (i = 0; i < 5; i++)
{
	printf("%d", a[i]);
}
```
write a program to read an array of 10 integers and count the total number of even and odd numbers
```c
void main()
{
int a[10]; n;
int even = 0, off = 0;
for (n = 0; n < 10; n++)
{
scanf("%d", &a[n]);
}
for (n = 0; n < 10; n++)
{
if (a[i]%2 == 0)
even += 1;
else
odd += 1;
}
	print("even number = %d", even);
	print("Odd number = %d", odd);
}
```

Write a program to read two array of 5 variables and store the sum of the array in a third array. the last array should have the result of the first two arrays.

| 1   | 5   | 7   | 9   | 3   |
| --- | --- | --- | --- | --- |
| 3   | 8   | 2   | 8   | 2   |
| add | add | add | add | add | 
```c
void main()
{
inf arr1[5], arr2[5], sumarr[5];
int i;
for (i = 0; i < 5; i++)
	scanf("%d", arr1[i]);
for (i = 0; i < 5; i++)
	scanf ("%d", arr2[i]);
for (i = 0; i < 5; i++)
{
sumarr[i] = arr1[1] + arr2[i];
printf("sum of array of at index %d is %d\n", i, sumarr[i]);
}
}
```

## 2-D Array
One dimensional array stores multiple columns to a single row, assuming a mark for 60 students, then one variable can be used to print out the values using an array however, in the situation where marks is needed to be distrubuted accross 5 subjects i.e marks_sub1[60], marks_sub2[60] etc
that could be time consuming and memory complexity, hence we can declare thus
```c
int marks[5][60]

```
the above will give us 5 rows to 5 colums. we could also have a multidimentional array, lets say a school of 3 departments offering 5 courses with a maximum number of 60 students, that will become 
```c
int marks[3][5][60]
```
syntaxs
```c
datatype [size of rows][size of column]
```
the two dimensional array is mostly used in a matrix like evaluation. though we represent the concept of 2-D array in a matrix format, it is not represented thus in the computer memory since it stores its data in sequence. 

Lets use the table below to illustrate 

| 0,0 | 0,1 | 0,2 |
| --- | --- | --- |
| 1,0 | 1,1 | 1,2 | 

Looking at the values above, it is clar that we can store 15 elements (3 x5);
therefore the allocated memory space will be 60bytes since the integer stores in 4 bytes, hence 15 elements x 4 = 60bytes memory allocation

In addition to the above, clarify the above, we could have something like 
```c
int a[2][3] = {{0,5,2}, {5,3,8}}

or

int a[2][3] = {
				{4,6,1}
				{2,8,1}
			}
```
The curly braces is also used to explicitly specify, values in the array e.g
```c
int x[2][3] = {{3,2},{1,0}}
```
In that case, the values will be initialized as seen below. the first two values will ocupy row1 and the second will ocupy row two, however, the remaining part without values will be filled up with 0 value.
In addition, if you have initializtion of 
```c
int x[][3] = {0,0,0}

or

int x[][0] = {0}
```
the above will render teh array all 0's

Runtime
```c
int a[2][3];
int x, y;
for (x = 0; x < 2; x++)
{
	for (y = 0; y < 3; y++)
	{
		scanf("%d", &a[x][y]);
	}
}
```

find out elements that float can store and its seize if only float can be used in the aspect 
```c
float a[2][7]
```

Meanwhile, memory representation of 2-D array as described above is only but for human consumption as it is not defined thus in the computr memory allocation rather is is arranged in a straight manner having its divisions in colums as seen below
| 0   | 0   | 0   | 1   | 1   | 1   |
| --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |
where the first three values represents the first row, and the second represents the second row

To access values in the array, you use the matrix formation
```c
variablename[row][column]
example a[2][1]
```

### Transpose of a matrix using 2 dimentional array
```c
int a[2][3], j, i;
for (i=o; i<2,i++)
	{
	for (j = 0; j < 3; j++)
		{
			scanf("%d", &[i][j]);
		}
	}
for (i = 0; i < 3; i++)
	{
	for (j = 0; j < 2; j++)
	{
		printf("%d\t", a[j][i]);
	}
	}

```

## Printing the sum of indidual rows and colums considering a 3 by 3 matrixs
```c
int a[3][3], i, j, sr, sc;
for (i = 0; i < 3. i++)
	{
	for (j = 0; j < 3; j++)
		{
			scanf("%d", &a[i][j]);
			
		}
	}
for (i = 0; i < 3; i++)
	{
	 sr=sc=0;
	for (j = 0; j < 3; j++)
	{
		sr += a[i][j];
		sc += a[j][i];
	}
	printf("sr = %d, sc = %d", sr,sc);
	}

```
## A program to sum to matrices i.e 2 by 3 matrices
```c
#include <stdio.h>

void main()
{
int ar1[2][3], ar2[2][3]; 
  int i, j, sum[2][3]={0};

  printf("Please enter values for first matricx\n");
for (i = 0; i < 2; i++)
  {
    for (j = 0; j < 3; j++)
      {
        scanf("%d", &ar1[i][j]);
      }
  }

   printf("Please enter values for second matricx\n");
for (i = 0; i < 2; i++)
  {
    for (j = 0; j < 3; j++)
      {
        scanf("%d", &ar2[i][j]);
      }
    
  }

//sum of the two matrices
  
for (i = 0; i < 2; i++)
  {
    for (j = 0; j < 3; j++)
      {
        sum[i][j] = ar1[i][j] + ar2[i][j];
        printf("%d\t",sum[i][j]);
      }
    putchar('\n');
  }
  
}
```

### Product of a 3x3 matrics
```c
#include <stdio.h>

void main()
{
int ar1[3][3], ar2[3][3]; 
  int i, j, k, sum, mul[3][3];

  printf("Please enter values for first matricx\n");
for (i = 0; i < 3; i++)
  {
    for (j = 0; j < 3; j++)
      {
        scanf("%d", &ar1[i][j]);
      }
  }

   printf("Please enter values for second matricx\n");
for (i = 0; i < 3; i++)
  {
    for (j = 0; j < 3; j++)
      {
        scanf("%d", &ar2[i][j]);
      }
    
  }

//mul of the two matrices
  
for (i = 0; i < 3; i++)
  {
    
    for (j = 0; j < 3; j++)
          {
             sum = 0;
        for (k = 0; k < 3; k++)
          {
             sum += ar1[i][k] * ar2[k][j];
            mul[i][j] = sum;
         }
            printf("%d\t", mul[i][j]);
      }
    putchar('\n');
  }
  
}
```
download jenny's video on multiplication of matrics for more clarity. found on video 60 or less

## Strings
strings simply means an array of character
array can take any data type but strings can take only character data type
e.g
```c
char name[10];
```
array is considered as an internal pointer
a string ends with a nul character in the memory \\0
A string is also seen as a one dimentional character array
delcaring string in c is equivalent to 1 d array
```c
char name[] = "EnGentech Lectures"
char name[] = {'E','n','G','e','n','t','e','c','h'}
```
note that the below declaration of string is not allow in c
```c
char name[];
name = "EnGentech"

char name[] = "EnGentech"
char snam[] = "Learning"
si = sname[]
```
when you wirte a sting in c, you are not passing an addres operator "&" because we dont use a certain location for the value instead we use the first address and the compiler will automatically adjust the value of the end to fit in other values using the format specifier %s in the sample below
```c
char name[];
scanf("%s", name);
printf("%s", name);
```
Note that scanf character will not consider a white space character within the string because it sees the white space character as a null value, hence after the null character exits, it will consider all other values as a gabbage character. e.g
```c
EnGentech Lectures
```
Using scanf to get the above name will result in printing only EnGentech with no lecutres due to the white space character provided.

To resolve that, we use gets with no format specifier as shown below
```c
char name[30];
printf("enter your name");
gets(name);
printf("%s", name);
```

Drawback of gets is buffer overflow, the same overflow is seen in scanf too
what does that mean!

lets assume you entered a limit string of 5 which implies that 4 characters should be inputted and the last should be null character
```c
char name[5]
```
using gets will overwrite the value of the buffer size hence it will not consider the specifiers value of 5 hence it will print all the characters 

but the scanf can be limited using the format specifier e.g
```c
scanf("%4s", name);
//that will enable only 4 characters to be taken from user input and this is known as hard coding
```

## Printf of  a string
```c
printf("%.5", name)
printf("%10.5", name)

// in the above, the .5 will print only 5 characters from the list of characters provided and in the second option, it will print 10 white space character before the 5 characters from the list of character provided
```
puts works just like the gets with no format specifier and it will automatically add a new line at the end of the srting

one more thing
if you have a code in the sample below, the program will print the values starting from the specified index. e.g
```c
printf("%s", &name[2])
//assuming the name entered was EnGentech, the program will instead print Gentech, becasuse the addressd of index 2 is find G, then it will print from there
```

lets try a little program
```c
#include <stdio.h>
int main()
{
char name[30] = "EnGentech";
printf("%s", name);
}
```
note that if you using a char literals, you must specify your null character e.g
```c
char name[10] = 'E','n','G','\0'
```

#### Find the length of string
the predefined name is strlen in the header file string.h
```c
#inlude <string.h>
int main()
{
unsigned int count = 0;
char name[30];
printf("Enter you name");
gets(name);
count = strlen(name);
printt("String length is = %d", count);
}
```
the strlen will return an unsinged integer because the length of a string can never be negative

Lets assume we are to provide our user solution to count the string, the code below will solve that problem
```c
#include <stdio.h>
{
int main()
int count = 0, i = 0;
char name[30];
print("Enter name");
gets(name);
while (name[i] != '\0')
{
	count++;
	i++;
}
printf("%d", count);
}
```

### Concatinating strings in C
 the predifined function to concatinate strings in c is strcat
 ```c
 strcat(s1, s2)
 //the s1 is the destination string and the other is the source string where the first agurment is always the destination string
```
the strcat has a drawback of buffer overflow, same as discussed above.

the same code above can be written thus
```c
char s1[30] = "EnGentech";
char s2[8] = "Lecture";
len1 = strlen(s1);
len2 = strlen(s2);
for (i = 0; i <= len2; i++)
{
si[len1+i] = s2[i]
}
printf("%s", s1)
```

if you wish to concatenate a certain number of strings, the below command is used
```c
strncat(first string, second string, numb of characters);
//e.g strncat(s1, s2, 5)
```

### comparing String in C
the predifined command to compare string is strcmp and strncmp
syntax
```c
strcmp(const char *str1, const char *str2)
//the above code will return an integer value of either 0, +ve or -ve, lets analize that.
// the value 0 is return when the compared strings are equal to each other, it will return positive value when the first character that does not match is greater in stirng on to the string two using ASCII values else the other is considered

//e.g
int value;
char s1[] = "Hello";
char s2[] = "World";
value = strcmp(s1, s2);
if (value == 0)
{
	 printf("The compared values are the same");
}
else
{
	printf("The compared strings are not the same");
}

```
lets run the program manually
```c
int flag = 0;
int i;
char s1[] = "Hello";
char s2[] = "Helli";
for (i = 0; s1[i] != '\0' || s2[i] != '\0'; i++)
{
	if (s1[i] != s2[i])
	{
		flag = 1;
		break;
	}
	if (flag == 1)
	printf("not same");
}
```
### Reversing a string
the predefined keyword is strrev but this keyword is likely no found in some of the c compilers
syntax is written as
```c
strrev(s1)
//where the s1 is the valuable tha hold the string
```
manually writing the program
```c
int l,i;
char ch;
char s1[30] = "EnGentech"
l = strlen(s1)
for (i = 0; i < l/2; i++)
{
	ch = s1[i];
	s1[i] = s1[l-1-i];
	s1[l-1-i] = ch
}
printf("%s", s1);
```
### Converting strings to lower case
the value is strlwr or islower
```c
char s1[30] = "EnGentech"
strlwr(s1)
printf("%s", s1)

//to uppsr is strupr or isupper

```
writing manually
```c
for (i = 0; s1[i] != '\0; i++)
	 {
	 if (s1[i]>='A' && s1[i]<="Z")
		 {
		 s[i] = s[i] + 32
	 }
	 printf("%s", s1);
	 }
//the value of 32 is added to the ASCII value a upper letter A hence to be converted to lower letter a and so on.
	 ```

# Pointers in C
every variable has three things allocated to itself, the variable name, the value and the address. 
Pointers are also a variable or spacial variable which contains the address of any other variable.
we can also say that pointers are derived data types

syntax
```c
datatype * pointer variable
//the asterisk can be used either close to the pointer-name , data type or at the center
e.g
int *p
//Note that the int does not specify the data type of p. rather it means that the pointer p is containing an address of a variable whose value is of integer data type

//the size of pointer for a 32 bits machine is 2bytes
```
a pointer can be declared an initialized thus
```c
int *p = &a;
int a = 10, *p = &a;
//note that its not proper to declare a pointer before initializing a value
int *p = &a, a = 10  // this is wrong
```

### Pointer Assignment
```c
int a = 10, b = 11;
int *p, *q;
p = &a
printf("a = %d %d %d", a, *p, *q)
```

lets write a little program to illustrate tha above
```c
#include <stdio.h>
void main()
{
	int a = 10, b = b;
	int *p, *q;
	p = &a;
	q = p; 
	printf(a = %d %d %d, a, *p *q);
}
```

### Pointer to pointer or double pointer
This means a pointer pointing to another pointer
it is declared with two asterisk
```c
int a = 10;
int *p = *p = &a;
int **q = &p;
//Note that a double asterisk cannot be used on a variable, it should be strictly used on a pointer variable
```

## Pointer Arithmetics
A pointer addtion 
```c
p = p+1
```
that is not adding 1 to value of p but it is adding extra byte to the defined memory size and point to the next location of the memory location. If you call to print any value within this point, it will print a gabbage value since no value is assigned there.

the pointer arithmetics is mostly used with the array concept
lets assume the table below

| 3   | 6   | 9   | 0   | 4   | 
| --- | --- | --- | --- | --- |

from the array above we have
```c
int a[5] = {3, 6, 9, 0, 4}
int *p = &a[0]
if you have a value like
p = p + 2, 
// hence the p will point to the value 9 bing the next two bytes of the address in memory. note that this is not possible within the variable name. e.g a + 2 will not work as that of the pointer
// note that 
p + 1 //this will not print anything as it is not equall to the p value exept you use the increment concept
p++;
```

```c
void main()
{
int a[] = {10, 11, -1, 56, 67, 5, 4}
int *p, *q;
p = a;
printf("%d", *p);
printf("%d %d %d\n", (*p)++, *p++, *++p);
q = p + 3;
printf("%d", *q - 3");
printf("%d", * --p + 5);
printf("%d", *p + *q);
}
```
Note that *p + 1 implies that the value stored in the address should be imcreamented by 1 while the addres remains the same fro mthe above program but p + 1 incrase4s the memory address and hence points to the next address

Assignment
```c
void main()
{
int a[] = {10, 11, -1, 56, 67, 5, 4};
int *p, *q;
p = a;
q = &a[0];
printf("%d %d %d", (*p)++, (*p)++, (*p)++, *(++p));
printf("%d", *p);
printf("%d",(*p)++);
printf("%d",(*p)--);
q--;
printf("%d", (*(q + 2))--);
printf("%d", *(q + 2) - 2);
printf("%d", *(p++ -2) -1);

}
```

Note that the data-type of a variable shoudl be the same with the pointer
e.g
```c
void main()
{
int a = -1;
int *p =a;

const int b = 12;
cont int *q = b;
}
```

Lets evaluate the concept of pointers using the porgram below
```c
void main()
{

char str[] = "Welcome to EnGentech Lectures";
char *ptr = str;
printf("%c", *ptr);
printf("%c\n", *(ptr++ 1));
printf("%c\n", *((ptr-- +5) -1) +3);
printf("%c\n", *(++ptr + 10) -35);
printf("%c %c %c", *ptr, *++ptr, *--ptr)

//Lets explain the above
//In line one, the result will be W because the value is pointing to the first data
//In the second line, the ptr++ will be executed first since it has a higher priority in arithmetic organogram compared to the plus sign. in addition we know that the ptr++ is a post increament. assuming the memory was arranged from 100 as discussed in previous documents, hence the pointer will be moved in one place forward, implying that it will take the next memory location, lets call it 101, hence it will return the value e.

//for the third line, we solve from the inner value ptr--, this will decrement the pointer value one step backward, hence we will return to 100, however this is post increament implying that it will not be used immediately so the value remains 101 for the first time, added to the 5 (ptr-- +5), we are added 5 memory location to the value 101, hence we have 106, now we wil lhave (106 -1) + 3.   that will become *105 + 3.

//Looking at the array above, the 105 meets with the letter (m) + 3, the 3 added to the pointer does not imply that the pointer will be shifted + 3 but rather the ascci value of m + 3 will be added, hence the result will become p.

//the fourth line, we noted that the ptr at this point is having a pre-increament hence the value will be increamented and used. that will become 100 + 1 = 101 plus 10 will become 111, counting the value from the array will result to E, hence E ASCII value - 32 will give us the new value to be used.

}
```

## void Pointers
This means that the pointer is not having any associated data type. this implies that the pointer can be converted to any data type. it is declared as 
```c
void *vp;
```
it can be called a generic pointer
lets assume the below
```c
int a
float b
char c
void *vp

//now you can point the pointer to any data type you prefer
//e.g

vp = &a;
vp = &c;
// now the vp pointer has been pointed to the integer data type
```
Note that you cannot dereferece a void pointer because the copiler may not be ascertain of the memory space allocated to the data type, hence to use the void pointer, you must perform casting  in the format below.
```c
printf("%d", *(int*)vp);
printf("%d", *(char *)vp);
```
the importance of void pointer is applicable where there are variety of data type that needs pointers, hence  you can use a single pointer to cast 

## Null pointer
when you define a pointer without initializing it may result in printing gababe vaues, for instance 
```c
int *prt
printf("%d", ptr)

//printing the above will result in some characters unknown, a sort of gibridge values, hence to correct this problem, the NULL can be used to avoid printing gibrige values. as seen below

int *prt = NULL or int *prt = 0;

//with the above, the value returned will be 0, but note that you should not dereference a null pointer.

//Null pointer is used in error handling in c language
```

## Dangling pointers
```c
int *ptr = (int *) mallooc (size of (int))
//the above is allocating memory which will be discussed later, the memory size of int (4byte) is allocated to the pointer value ptr
*ptr = 10;
printf("%d", *ptr);

free(ptr);

//In the above expression, we have assigned a memory space to the pointer ptr, lets say that the pointer at level ptr is pointing to a certain memory and leter on, we dont need the memory again, we hence free the memory with the free command, now the memory is freed but the pointer still exist, that pointer is hence called dangling pointer, if we dereference the pointer, we hence might receive a sort of garbrige value or still crash the program depending on the inference of the memory and what the compiler reads.

//An illustration is a case of you storing a phone number of your friend in your phone, now that phone number serves as a pointer to your friend at each time you call him or her, but lets assume your friend looses his number someday yet you still the number in your phone, if you call such number, we may not know what will become of the number. that is a life example of a dangling pointer.

//Hence a dangling pointer is a pointer that points to a freed memory location.

//Another code example to dangling is
void ()
{
int *ptr;
{
	int a = 9;
	ptr = &a;
	printf("a = %d", *ptr)
}
printf("a = %d", *ptr)
}

//printing a outside the block will run into a dangling pointer because as soon as the control leaves the block, the a is no more visible as it was declared locally, however the pointer is still pointer to the address of a, hence it will become a dangling pointer. but for the mean time, it may print the correct output, however, in later times if the memory is allocated to another thing by the memory, it will return a false result.

//the same thing happens if you declare a function that will return a value to a pointer, however if you declare the data type with static keyword, then the program wont run into dangling pointer

e.g
int static a
```

## Wild Pointers
An uninitialised pointer is refered to as a wild pointer, you can use the null pointer to resolve this problem or you assign memory to the pointer seen below
```c
int *ptr = (int *)malloc(sizeof (int))

// if you have something as seen below, 
int *ptr;
int a = 10;
a = *ptr;

//the first line is wild pointer
```

# Functions in C
In c program or every other programming languages, functions are essential and productive, the printf, scanf, main are all function defined within the program in their respective header files to perform tasks. they are all called in-built function. 
Users can also write their own function to perform user desired task, those are called user defined functions. e.g
```c
void main()
{
int a, b, sum = 0;
printf("enter two numbers")
scanf("%d %d", &a, &b);
printf("sum = %d\n" a + b)
}
```
that is a common program that we are aware of. but this program can only run and execute once, now take an instance of wishing to calculate same program for multiple times, then a function is needed.
there are three aspects of a function in c
1. Function declaration (or function prototype)
2. Function call
3. function execution
Another name for function could be seen as sub or module.
Hence a function is a piece of code that processes a specific task on routine call.
e.g of a basic function program 
```c
#include <stdio.h>
void sum()
{
	int a, b, sum=0;
	printf("Enter two numbers:");
	scanf("%d %d", &a,&b);
	sum = a + b;
	printf("Sum of a and b = %d", sum);
}
void main()
{
	sum()
}
```

## Clarifications of Functions
Functions are of 4 categories
* No argument without return type
* No argument with return type
* with argument no return type
* with argument with return type

e.g for classification 1
```c
void fun()
{
statement;
}

or

fun(void)
{
statement
}

# Example
void sum(void)
void main()
{
sum()
}
void sum()
{
int a = 5, b = 7, sum = 0;
sum = a + b;
printf(sum = %d", sum)
}
```
Gate question 2000
```c
int incr(int i)
{
static int count = 0;
count = count + i;
return count;
}
main()
{
int i, j;
for (i = 0; i <= 4; i++)
j = incr(i);
}
```
gate question 2016
```c
void f(int *p, int m)
{
m = m + 5;
*p = *p + m;
return;
}
void main()
{
int i = 5, j = 10;
f(&i, j)
printf("%d", i + j)
}
```
Passing array as an argument
```c
int arg(int[])
void main()
{
int marks[5] = {4, 6, 3, 67, 5}
arg(marks)
}
```