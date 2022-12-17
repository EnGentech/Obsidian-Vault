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
