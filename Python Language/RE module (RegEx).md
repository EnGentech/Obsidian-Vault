In Python, "regex" refers to regular expressions, which are powerful tools for pattern matching and text manipulation. "Regex" is short for "regular expression."

Regular expressions are a sequence of characters that define a search pattern. They allow you to match and manipulate strings based on specific patterns of characters. The `re` module in Python provides functions and methods for working with regular expressions.

With regular expressions, you can perform various operations, such as searching for specific patterns in a string, extracting information from text, validating input formats, and replacing parts of a string with other text.

Python's `re` module provides several functions, including:

1. `re.compile(): creates the pattern to be matched
2. `re.match()`: Attempts to match the pattern at the beginning of the string.
3. `re.search()`: Searches the entire string for a match to the pattern.
4. `re.findall()`: Returns all non-overlapping matches of the pattern in the string as a list.
5. `re.finditer()`: Returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.
6. `re.sub()`: Replaces one or more occurrences of the pattern in the string with a replacement string.
7. `re.split()`: Splits the string by the occurrences of the pattern and returns a list.

## re.complile
In Python, the `re.compile()` function is used to compile a regular expression pattern into a regular expression object. This object can then be used for various operations, such as searching, replacing, or manipulating strings based on the specified pattern.
```python
re.compile(pattern, flags=0)
```
After compiling, the regEx could be called upon with a method to define a pattern matching
```python
x = re.compile("[abc]", re.IGNORECASE)

txt = "this is my beloved son in whom I am well pleased, hear him"
print(x.findall(txt))
```
there are two approach to define a pattern, using the raw string or using the string literals
the string literals are written without the r and opposite is the case
e.g
```python 
x = re.compile(r"\in")
```
in that case the \\ which was suppose to be used as a special character is hence ignored and seen as a literal string 

### Performing Matches[](https://docs.python.org/3/howto/regex.html#performing-matches "Permalink to this headline")

Once you have an object representing a compiled regular expression, what do you do with it? Pattern objects have several methods and attributes. Only the most significant ones will be covered here; consult the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.") docs for a complete listing.

| `match()`    | Determine if the RE matches at the beginning of the string.                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `search()`   | Scan through a string, looking for any location where this RE matches.                                                             |
| `findall()`  | Find all substrings where the RE matches, and returns them as a list.                                                              |
| `finditer()` | Find all substrings where the RE matches, and returns them as an [iterator](https://docs.python.org/3/glossary.html#term-iterator) |
| split()      | Split the strings into a list, this splits where ever the RE matches                                                               |
| sub()        | find all sub strings where RE matches and replace them with a different string                                                     |
|              |                                                                                                                                    |

In every programming language, regular expression can be used with the help of regex engine installed into such programming language. RegEx engine are simply programs written to execute regular expression rules or laws
Regular Expression contains two important components.
1. String literals: this characters carried no special meaning and hence it is applied as seen
2. Special characters known as metacharacters: this characters possess special meaning and are interpreted in a special way

The RegEx in python is compiled into a series of byte code which are then executed by a matching engine written in C language

After creating the re.compile, there are different methods provided for pattern matching as listed above

## The match method
Basically the match checks only at the beginning of a string (by default)
```python
import re  
  
pattern = re.compile("hello", re.I)  
txt = "hello this is my beloved son"  
match = pattern.match(txt)  
print(type(match))  
print(match)  
if match:  
print("found")  
else:  
print("not found")  
print(match.span())
```
In the above example, we compiled the regex with the pattern "hello", we use the match to track if hello is found at the beginning of the line, if found the print(type(match)), prints the class of the regular expression but if not found, the nonetype is printed instead. 
if found, the match have some methods that could be applied, we used the span to check for the index it was found which at the default is the 0 index and the number of characters match. in the above case the span = 0, 5

However, we could change the default 0 index to our choice of index using the pos function as seen below
```python
import re  
  
pattern = re.compile("this", re.I)  
txt = "hello this is my beloved son"  
match = pattern.match(txt, pos=6)  
print(type(match))  
print(match)  
if match:  
print("found")  
else:  
print("not found")  
print(match.span())
```
the endpos is used to determine the end of search index

## The search function
Unlike the match, it does not depend on the start index, but will search entirely on the string, for instance lets use the code below
```python
import re  
  
pattern = re.compile("[v]", re.I)  
txt = "hello this is my beloved son"  
match = pattern.search(txt)  
print(type(match))  
print(match)  
if match:  
print("found")  
else:  
print("not found")  
print(match.span())
```
The pos and endpos is applied same as match

## The findall function
Unlike the other two, the find all search for the entire string and print out a list of found pattern matching. It does not check for the span but return the list of found values on the stdout. e.g
```python
import re  
  
pattern = re.compile("[ov]", re.I)  
txt = "hello this is my beloved son"  
match = pattern.findall(txt)  
print(type(match))  
print(match)  
if match:  
print("found")  
else:  
print("not found")
```

## The finditer function
This function find all match strings in a file and returns all possible spans iteratively according to the number of times such a match is found, it uses a loop to find all matches otherwise it returns only the first found span e.g
```python
import re  
  
pattern = re.compile("[o]", re.I)  
txt = "hello this is my beloved son"  
match = pattern.finditer(txt)  
print(type(match))  
print(match)  
for i in match:  
print(i)
```

## The Module level function
Rather than compiling in different line, you can use the module level function to create you pattern matching. e.g
```python
text = "this is my beloved son"
match = match("this", text, flag=0)
```
in the above the pattern is defined within the function using the syntax
```python 
variable_name = regex(pattern, text, flag)
```
However, if you are to reuse the pattern a multilevel of time, its is hence better to use the compile version instead of a module level

given the text
```python
text = "This book cost about $15"
```
using regex search method, search for $15 in the text above

Basically there are 12 metacharacters in the regex engine and each time this is used a string literals, it should be escaped

## The raw string concept
Lets say we need to search a for a certain string from the list seen below
```python
text = """
C:\Windows
C:\Python
C:\Windows\Systems32
"""
```
from the above, lets say we need to search for the last line using search, using the normal way may not have a result except two things are done e.g
```python
pattern = re.compile("C:\Windows\Systems32")
#the above will not work because of the metacharacter present in the txt, the best way to do that is to use escape sequence or use the raw string patter like
pattern = re.compile(r"C:\\Windows\\Systems32")
pattern = re.compile("C:\\\\Windows\\\\Systems32")

search = pattern.search(text)

```
### Why such multiple slashes......
the python interpreter uses the backslash for its escape sequence as well as the regex engine, note that regex is not a core python program hence, it is interpreter differently, when the python performs its escape on the above text, it sends the result of "C:\\Windows\\Systems32" to the regex engine, at that point, the regex engine is seeing only one slash and hence will be treated as none, to avoid this, the slashes needs to be treated as if it was distributed across two levels.

However, the above can still be avoided by using the re.escape() function like
```python 
import re  
  
pattern = re.compile(re.escape('C:\Windows\Systems32'), re.I)  
text = """  
C:\Windows  
C:\Python  
C:\Windows\Systems32  
"""  
match = pattern.search(text)  
print(match)
```
Note: if you pattern matching needs a special character, it is important to know that .escape will remove all the special characters and render your pattern matching useless

## Character Classes
this is defining a pattern that check for spelling depending on language derived, e.g license and license
this can be defined as 
```python
pattern = licen[cs]e
```

## Character set range
this defines a set of character range depending on user specification e.g
```python
pattern = [0 - 9]
```
## The Negate symbol
this uses the caret symbol ^ to negate what is was stated in the square bracket e.g
```python 
pattern = [^ieo]
```

## Finding all special characters
this can be done by negating all alphanumeric characters and spaces, to do this the pattern below is used 
```python
pattern = "[^\w\s]"
#the \w indicates all alphanumeric characters otherwise known as a word while the \s represents space or white space character
```

## The Alteration
this uses the pipe | that serves as an or value
```python
pattern = "and|or|me"
#note: if you add space, then space will be included in your pattern matching
```
another example
```python
txt = """
What is in the bag
Who is in the house
"""
#Pattern expression to find what is and who is

pattern = re.compile("(what|who) is")
```

## Quantifiers
this implies repetition of characters. there are 4 basic quantifiers to include
1. ? this means it can be repeated zero or one time
2. * zero or more times
3. + one or more time
4. {m, n} between m to n times

write a pattern to search for the number below
```python 
text = """
555-555-555
555 555 555
555555555
"""
pattern = re.compile("\d{3}[\s|-]?\d{3}[\s|-]?\d{3}[\s|-]?")
```

## Greedy and Non-greedy Quantifiers
Assuming you were given a text with the below to match all html tag elements, 
```python
text = <html><head><title>Title</title></head</html>
#define a pattern to match all tags
pattern = re.compile("<.*>")
#thats sounds great to the eye but that wont work because of the greediness of * 
```
so how can we help out?
To use a non-greedy behavior, you add a question mark at the end of the greedy quantifier
using the above example, we have:
```python
pattern = re.compile("<.*?>")
#that will make each element a seperate entity
```
this is applied to all quantifiers
```python
??
*?
+?
.?
```

## Boundary Matches
In a multiple text with several values, you may wish to search for a particular word, using the word, may be problematic if the text contains a word that have similar pattern in it, for instance
```python
text = "In his holy temple, the king is the real leader, this is reacorded in his holy book according to the translation on the outer space of the traditional inspiration of the holy onction"

```
from the above text, lets say we need to search for is and on, Notice that other words do have is and on as a part to their words, if you try to search using the pattern 
```python
pattern = re.compile("is|on"),
```
the above will also select other words that has is in it hence the need for boundary ma
tch as seen below
```python
pattern = re.compile("\\b(is|on)\\b")
```
Using one \\b in the above will result to another thing as python has its own interpretation to \\b hence the need to escape it twice before passing it to the regex engine
Boundary values include
1. ^
2. $
3. \\b
4. \\A
5. \\z
Lets look at an example
```python
text = """
Name:
Age: 0
Roll No.: 12
Grade: 5

Name: Gentle
Age: 78
Roll No.: 124 Name: ABC
Grade: 19

Name: Remo
Age: -7
Roll No.: 45
Grade: G
"""

pattern = re.compile("^Name:", flags=re.M)
print(pattern.findall(text))
```
In the above, we are trying to find all values that starts with Name: , the flag is used to ensure that it is find in lines otherwise it will see all text as one word and wont find a match if use without that flag.
To grap the complete line, add .* to is
```python
pattern = re.compile("^Name:.*",flag=re.M)
```
Another example, write a regular expression to find out a line that does not end with a fullstop
```python
pattern=re.compile("^.*[^\.]$", flags=re.M)
```

## Split function()
split function is used to separate patterns, lets say we have some sentences and we need to split them into individual words, the below can be done
```python
txt = "I am a students in Heritage polytechnic Ikot Udota, I am currently learning how to code using python programming language, in computer Engineernig Department."
#to split the above into individual words

pattern = re.compile("\W")
#the capital w is used as an anti alphanumeric which implies that it will match any character that is not alpha numeric.

print(pattern.split(txt))
#the above splits them into words, but will include the spaces
#to remove it, the lambda could be employed with the filter keyword

use = list(filter(lambda x : x!=" ", pattern.split(txt)))
```
To get maybe the first three words, you can use maxsplit e.g
```python 
pattern.split(txt, maxsplit=3)
```

## Substituting
this implies substituting text that match with something else like msword find and replace
to do this, define a pattern matching and use sub function to substitute and replace them as seen below
```python
import re  
  
txt = "you are my friend and she is my friend also, replace friends with enemy"  
  
pattern = re.compile("friend")  
print(re.sub(pattern, "enemy", txt))
```
the subn is used to count number of substitution made
```python
import re  
  
txt = "you are my friend and she is my friend also, replace friends with enemy"  
  
pattern = re.compile("friend")  
print(re.subn(pattern, "enemy", txt))
```

## Compilation flags
the flags include
re.IGNORECASE or re.I 
re.MULTILINE or re.M
re.DOTALL or re.S 
re.UNICODE or re.U
re.LOCALE or re.L
re.ASCII or re.A
re.VERBOSE or re.X
re.DEBUG

Description
1. Ignore case
2. Make behind/end boundary matchers (^, $) consider each line.
3. make . match newline too
4. make {\\w, \\W, \\b, \\B} follow Unicode rules
5. make {\\w, \\W, \\b, \\B} follow locale
6. make {\\w, \\W, \\b, \\B} perform ASCII-only matching
7. allow comment in regex
8. get information about the compilation pattern 

## Groupings
this is an application of precedenting. Basically concept of parenthesis 
Outside the above, grouping could be used  to collect values in groups. lets take an instance of date 20-02-2001, we can collect those values individually.
e.g
```python
import re  
  
txt = "20-10-2018"  
pattern = re.compile("(\d{2})-(\d{2})-(\d{4})")  
  
match = pattern.match(txt)  
for i in range(3):  
print(match[i])
```
```python
import re  
  
txt = "20-10-2018"  
pattern = re.compile("(\d{2})-(\d{2})-(\d{4})")  
  
match = pattern.match(txt)  
day, month, year = match.groups()  
print(day, month, year)
```
```python
import re  
  
txt = "20-10-2018"  
pattern = re.compile("(\d{2})-(\d{2})-(\d{4})")  
  
match = pattern.match(txt)  
for i in range(len(match.groups())+1):  
print(match[i])
```

## Backreferencing
Back-referencing is used to track duplicating words done with grouping
```python
import re

txt = """
hello hello
how are you
am fine fine
"""

pattern = re.compile(r"(\w+) \1")
pattern.findall(txt)
```
another good example
```python
import re  
  
txt = """  
today is 21/01/2005  
"""  
  
pattern = re.compile(r"(\d{2})\/(\d{2})\/(\d{4})")  
print(pattern.findall(txt))  
print(pattern.sub(r"\3/\2/\1", txt))
```

## Named group
instead of using index as seen above, we can use name to get a group as seen below
```python
import re  
  
txt = "Gentle Inyang"  
  
pattern = re.compile(r"(?P<first>\w+) (?P<last>\w+)")  
  
match = pattern.match(txt)  
print(match.group('first'))
```
swapping the names using the naming convention 
```python 
import re  
  
txt = "Gentle Inyang"  
  
pattern = re.compile(r"(?P<first>\w+) (?P<last>\w+)")  
  
match = pattern.match(txt)  
print(match.group('first'))  
  
print(pattern.sub(r"\g<last> \g<first>", txt))
```

Lets find out if the first name and the second name have the same value
```python 
import re  
  
txt = "Gentle Gentle"  
  
#check if the first name and last name is the same  
patt = re.compile(r"(?P<first>\w+) (?P=first)")  
print(patt.match(txt))
```

We could also store the result as a dictionary
```python
import re  
  
txt = "Gentle Inyang"  
  
pattern = re.compile(r"(?P<first>\w+) (?P<last>\w+)")  
  
match = pattern.match(txt)  
print(match.group('first'))  
  
print(pattern.sub(r"\g<last> \g<first>", txt))  
print(match.groupdict())
```

## Non Capturing Groups
if we write a code of this nature
```python 
import re  
  
txt = "I love cats, I love dogs"  
pattern = re.compile("I love (cats|dogs)")  
  
match = pattern.findall(txt)  
print(match)
```
The above will only print cats and dogs because the findall pattern returns the content of the 1 matching group, remember that the entire pattern there is the group 0 but the cats|dogs is the group 1. therefore to make the compiler see the entire pattern as group 1, then add this key
```python 
import re  
  
txt = "I love cats, I love dogs"  
pattern = re.compile("I love (?:cats|dogs)")  
  
match = pattern.findall(txt)  
print(match)
```

## Look ahead
