printing exact line, e.g, printing exact line from a multiple lines of file
```shell
cat file_name | awk 'NR==5'
or
head -n 3 iacta | tail -n 1 # for line three only
# the above will print only the content in line 5
```

```shell
printf "Best School\n" > "\*\\\'\"Best School\"\'\\\*$\?\*\*\*\*\*:)"

# the above prints best school with a new line inside the folder as seen above
```

```shell
tail -n 1 iacta >> iacta
# duplicate the last line
```

```shell
find . -type f -name "*.js" -delete
# find all files with .js and delete same in the directory and sub directory
```
```shell
find . -type d -not -name '.' | wc -l
# counting directories and subdirectories

```

listing directories 
```shell
ls -t | head -n10
```
sorting files alongside with uniqe creation
```shell
sort | uniq -u
```

counting files with a particular content
```shell
grep -i "bin" /etc/passwd | wc -l

# wc -l is used to count the number of repeated keyword
# grep is used to find a certain file
```

manipulating files with grep
```shell
grep -i "root" -A 3 /etc/passwd
# the code above will print files in 3 lines and keep three lines after each sub directory
```

invent selection
```shell
grep -iv "bin" directory_path
```

only letters is needed
```shell
grep -i "^[a-z]" directory_path
```

replacing strings
Note that tr is used to Translate, squeeze, and/or delete characters from standard input,
writing to standard output.
(that implies that you can use the above to seperate files or squeeze files depending on certain values)
```shell
tr "A" "Z" | tr "c" "e"
```

Removing all C's and c from input files
```shell
tr -d "cC"
```

lets count a file that appears on a single line, it can be done thus
```shell
echo $PATH |tr -s ":" '\n' |wc -l
# the above means that the path is listed into tr which will seperate the files in different line immediately the : is found the wc -l will count the lines
```

displaying all users with their respective directories
```shell
cut -d ':' -f 1,6 /etc/passwd | sort
```

listing empty files in directories and sub
```shell
find . -empty | rev | cut -d '/' -f 1 | rev
```

Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
```shell
tail -n +2 | cut -f -1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f -1 | rev
```

listing all values except a specific value
```shell
echo {a..z}{a..z} | tr " " "\n" | grep -v "oo"
# the above will combine a to z in a to z exception of oo which will skip while listing, the tr is responsible for catching the blank spaces thereby sending the value to new line respectively
```

formatting numbers
```shell
print "%0.2f" $variablename
```

converting from base 10 to hex
```shell
echo $((16#348))
```

converting to hexadecimal
```shell
printf '%x\n' $DECIMAL_VALUE
```

print values that fall under odd numbers only
```shell
perl -lne 'print if $. % 2 == 1'
```
