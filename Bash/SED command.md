replace a line with another
```bash
sed -i "s/is coming back/" has joined the meeting
```
the above replaces the line with that line

```bash
sed -i "s/Gentle/EnGentech/" file_name

sed -i "s/Gentle/EnGentech/g" file_name
```
replace Gentle with EnGentech in the file

```bash
sed -i "5iThis is line 5" file_name
```
this add this is line line 5 in line 5 of the filename, the i stands for insert (5i). Note that in the above case, if there's anything in line 5, it will move it to line 6

```bash
sed -i "s/^/#/" file_name
```
this implies that at every line, substitute the beginning of the file with #

```bash
sed -i "s/#//" file_name
```
replace # with nothing hence it returns to where if was

```bash
sed -i "/favour/d" file_name
```
the above deletes favour from the file completely

```bash
sed -i.bak "/e/d" file_name
```
in the above, sed will perform a backup of the file  to be worked upon, this help to avoid unforeseen deletion of a file, however, the .bak can be used with other file extension for instance .txt

```bash
sed -r "s/^.+/OMG/" file_name
```
this is a regex pattern

```bash
sed "1,10{s/Ese/Big Man/g}" file_name
```
in the above case, we can find Ese to represent Big man within the range of 1 to 10 lines
another way to implement this is 
```bash
sed "s/Eze/Big Man/g; 10 q"
```
where 10 q means quit at line 10

```bash
sed "/Chidubem/s/joined/Entered/" file_name
```
in the above, fine chidubem and replace joined with Entered in the line

```bash
```

Table of details
SED [FLAG] “/search/replace/[FLAG]” FILE
Command Function
S - substitute
Sed ‘s/When/Why/’ file.text
finds First match of When in a line and replaces
it with Why
-g – global, -i (insensitive case)
sed ‘/When/Why/gi’ file.text
finds all matches of When in line and replaces
all with Why(i stands for case-insensitive, g
stands for global)
P - print
sed ‘/Where/p’ file.text
find the word Where and prints it alongside the
rest of the document
Sed -n ‘/Where/p’ filt.text
Finds the word Where and prints only the line
where it was found. The -n flag is used to
negate, implying that only the lines with
matches are returned
Pre i (inplace)
sed -i ‘s/Hello/Hi/’ file.text
Substitutes Hello with Hi in text. If post-ig is
included, it ignores case. The pre-i modified the
associated txt. It actually writes into it without
reverse
Number insert (i)
sed “1,5i Zee is the only female in Big Team”
file.text
Inserts the text from line 1 through 5
Using number ranges
sed ‘1,10{/John/p} file.text
Finds John in lines within 1 and 10 and prints it.
Note that when specifying lines, commands
should be enclosed in a curly brace
Pre i (inplace) and backup
sed -i.bak ‘s/Hello/Hi/i’ file.text
First creates a copy of the original file with .bak
extension. Modifies the specified file directly
with specified command. Here, replacing hello
with hi case insensitive
d deletes a line.
Post d
sed -i ‘1,5{/Hello/d}’ file.text
sed '1,10{/Lagos/d; s/is/this is nothing/}' textfile
Finds hello in line 1,5 and deletes it
MULTIPLE COMMANDS
Direct find and replace
Sed ‘/Lagos/s/City/Village/’ file.text Find teh line containing Lagos, replace City with
Village
Using -e extension
sed -e ‘s/Lagos/Abuja/’ -e ‘s/traffic/hold-up/’
file.text
Replaces Lagos with Abuja and traffic with
hold-up
Using semi-colon ;
Sed ‘s/road/air/; /Lagos/d’ file.text Replaces road with air and deletes the line
containing Lagos from file (first occurrence). If
we want to delete a word, we can substitute it
with nothing
Q is for quit
sed ‘/air/q’ file.text
Finds the first match of search text, prints from
the beginning to the current line and quits.
Q can be used to define search length
sed ‘/commuter/p; 20 q’ file.text
Finds commutter from beginning to line 15.
stops there and returns result
USING SOME REGEEX WITH SED
MORE WHEN WE LEARN REGEX
^$
sed ‘s/^$/ d’
Searches for lines that begins and ends with
nothing (empty lines) and deletes them