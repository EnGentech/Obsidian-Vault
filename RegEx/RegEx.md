### Foudation
[Rubular: a Ruby regular expression editor](https://rubular.com/)
regular expression in most cases uses /regex content/ e.g
```ruby
/ninja/

#the above searching for a matiching value ninja with case sensitive, however, it will only pick the first captured while reoccuring matches will not be applied except acted upon by a flag e.g
/ninja/g

#the g above represents global case. which implies that the regex will search the entire strings and will capture the expression given irrespective of the number of times it is required.

```
### Flags in RegEx
* g   global 
* i    case insensitivity
* gi   global and case insensitivity
* m   multiple lines
* s     single line

### Checking for character set
Assuming we are go search for a character in the nature of ginja or ninja. it is noticable that the character difference amongst those two words is g and n, hence using regex, the below code code be written
```ruby
/[gn]inja/g
#that implies that it should search for a word that either begins with g or n and has the remaining part of the content, i.e ginja or ninja. 

#However, if the the second phase is not added i.e inja, it will search for a match that correspond to any of the character set present in the square bracket

/[abc123]/g
#that will searh for a value that matches any of the above listed

/[^ab]try/g
#the above character set works like a not statement, which implies that it will match any character as preceding value to try but will negate value with either a or b. for instance atry will no match, btry will no match but any other set will match e.g utry
```

### Ranges
From the above, we may love to match all possible alphabet characters, e.g
```ruby
/[abcdefghijklmnopqrstuvwxyz]boy/g
```
that is cool, but the time taken to type all the letters of the alphabet seems too long, hence we use ranges in this aspect writen as
```ruby
/[a-z]boy/g
/[b-p]boy/g
```
The above code will only be applied to a non case sensitive character. However, if there's need to apply capital letters, this could be done in two ways. 
first
```ruby
/[a-z]boy/gi
#the gi signifies global and negated case sensitivity
```
second 
```ruby
/[a-zA-Z]boy/g

#numeric range
/[0-9]me/g
```

### Repeating Characters (Phone Number sample)
In a case where theres need to match repeating characters, e.g looking for a phone number which must be 11 digit. we could choose to do the following
```ruby
/[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]/
```
Though the above is correct but the repeatition is too much. what if we needed it a million times? thats waoooo
we can rather simplify it as seen below
```ruby
/[0-9]{11}/g
#the above will match a digit of 11 characters long which represents a phone number

#meanwhile, if we use the plus + sign, it will always match the numbers as long as it is a number i.e

/[0-9]+/g

#you can match the expression in range. for instance we can look for a word that is 3 to 5 characters long. the below code could be use

/[a-z]{3,5}/g
#note, no space in between 3, and 5

/[a-z]{5,}/g
#the above matches a character of at least 5 characters long
```
### Meta-characters
This are special characters that has special meaning in the likes of
* -\\d  match any digit character (same as [0-9])
* -\\w  match any word character (a-z, A-Z, 0-9 and _'s)
* -\\s  match a whitespace character (spaces, tabs etc)
* -\\t  match a tab character only

NOTE THAT:
d - - mathces the literal character 'd'
\\d -- matches any digit character

### Special characters
'+'     The one-or-more qualifier
'\\'     The escape character
'\[]'    The character set
'\[^]'   The negate symbol in a character set
'?'    The zero-or-one quantifier (makes a preceding char optional)
'.'    Any character whatsoever (except the newline character)
'\*'    The 0-or-more quantifier (a bit like +)

Using .+ matches anything 
```ruby
/.+/
```

### Start and End string 
Assuming we need to to check a form to validate only a certain number of strings maybe like 5 character long, we could assume to use /[a-z]{5}. 
this will not work because it will only check for the first 5 characters and match, however the form will continue capturing other letters while considering only the first 5 as a matching check.
to do that we need to use the negate symbol outside the square bracket which will give a negated meaning to the suppose meaning and the $ sign at the end to entail that the character end. i.e
```ruby
/^[a-z]{5}$/
```

### Alternate Characters
The alternate character uses the symbol | which stands for or e.g
```ruby
/p|t/
#that stands for p or t in regex

e.g 11

/(EnGen|Gentle) tech/

#the above will search for either EnGen or Gentle added to tech from a string, however, if the question mark ? is used, it then becomes optional e.g

/(EnGen|Gentle)? tech/
```

## Webpage with Regular Expression
Lets create a webpage with regular expression. First, create a form with the following inputs
1. Username
2. email
3. password
4. telephone
5. profile slug
The regular expression will be written using javascript
lets store the regular expression in a variable in js

```js
var reg = /[a-z]/;

//if you need to use the flags, it should come after the last slash
```
you can choose to write your code this way
```js
var reg2 = new RegExp(/[a-z]/,'i')
//where the 'i' is the flag for the expression
```

From the from, lets validate. To avoid using multiple variable name lets use an object to express the codes in this manner
```js
const patterns = {
telephone: /^\d{11}$/
}
```
The above defines a regular expression to check and ensure that the matching character is 11 digit long and it must be numeric. however, the above will not validate the form just yet untill the next code is carried out
```js
//validation script here
const inputs = document.querySelectorAll('input');

const patterns = {
telephone: /^\d{11}$/
};

//validation function
function validate(field, regex){
	console.log(regex.test(field.value));
}

inputs.forEach((input) =>{
	input.addEventListener('keyup', (e) => {
		validate(e.target, patterns[e.target.attributes.name.value])});
});
```
The above code check if the entered value receive a true value or not when inspected through the brower inspect option. Meanwhile we are to use the code on our web hence the below conditional statement 
```js
//validation script here
const inputs = document.querySelectorAll('input');

const patterns = {
telephone: /^\d{11}$/,
username: /^[a-z\d]{5,12}$/i,
password:/^[\w@-]{8,20}$/,
slug: /^[a-z\d-]{8,20}$/,
email: /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/
};

//validation function
function validate(field, regex){
	if(regex.test(field.value)){
		field.className = 'valid'
	}
	else{
		field.className = 'invalid'
	}
}

inputs.forEach((input) =>{
	input.addEventListener('keyup', (e) => {
		validate(e.target, patterns[e.target.attributes.name.value])});
});
```