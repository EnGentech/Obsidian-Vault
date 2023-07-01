link: [JavaScript basics - Learn web development | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
the important keyword is used hence to avoid overwriting a line of code or styling e.g
```css
button{
background-color: red !important;
}
```
Using querySelector
```js
const name = document.querySelector("h1")
name.textContent = "Hello World"
```

|Variable|Explanation|Example|
|---|---|---|
|[String](https://developer.mozilla.org/en-US/docs/Glossary/String)|This is a sequence of text known as a string. To signify that the value is a string, enclose it in single or double quote marks.|`let myVariable = 'Bob';` or  <br>`let myVariable = "Bob";`|
|[Number](https://developer.mozilla.org/en-US/docs/Glossary/Number)|This is a number. Numbers don't have quotes around them.|`let myVariable = 10;`|
|[Boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean)|This is a True/False value. The words `true` and `false` are special keywords that don't need quote marks.|`let myVariable = true;`|
|[Array](https://developer.mozilla.org/en-US/docs/Glossary/Array)|This is a structure that allows you to store multiple values in a single reference.|`let myVariable = [1,'Bob','Steve',10];`  <br>Refer to each member of the array like this:  <br>`myVariable[0]`, `myVariable[1]`, etc.|
|[Object](https://developer.mozilla.org/en-US/docs/Glossary/Object)|This can be anything. Everything in JavaScript is an object and can be stored in a variable. Keep this in mind as you learn.|`let myVariable = document.querySelector('h1');`  <br>All of the above examples too.|

## Adding eventListener
Real interactivity on a website requires event handlers. These are code structures that listen for activity in the browser, and run code in response. The most obvious example is handling the [click event](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event), which is fired by the browser when you click on something with your mouse. To demonstrate this, enter the following into your console, then click on the current webpage:
```js
document.querySelector("h1").textContent = "lets try this"
document.querySelector("h1").addEventListener('click', function(){
    document.querySelector("h1").textContent = "another one"
})
```

## Changing image with JS
```js
const myImage = document.querySelector("img");
myImage.onclick = () => (){
	const mySrc = myImage.getAttribute("src");
	if(mySrc === "images/mine.png"){
		myImage.setAttribute("src", "images/new.png")
	}
}
```

### [Adding a personalized welcome message](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics#adding_a_personalized_welcome_message)

Next, let's change the page title to a personalized welcome message when the user first visits the site. This welcome message will persist. Should the user leave the site and return later, we will save the message using the [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API). We will also include an option to change the user, and therefore, the welcome message.

1. In `index.html`, add the following line just before the [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) element:
    
    ```js
    <button>Change user</button>
    ```
    
    Copy to Clipboard
    
2. In `main.js`, place the following code at the bottom of the file, exactly as it is written. This takes references to the new button and the heading, storing each inside variables:
    
    ```js
    let myButton = document.querySelector("button");
    let myHeading = document.querySelector("h1");
    ```
    
    Copy to Clipboard
    
3. Add the following function to set the personalized greeting. This won't do anything yet, but this will change soon.
    
    ```js
    function setUserName() {
      const myName = prompt("Please enter your name.");
      localStorage.setItem("name", myName);
      myHeading.textContent = `Mozilla is cool, ${myName}`;
    }
    ```
    
    Copy to Clipboard
    
    The `setUserName()` function contains a [`prompt()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt) function, which displays a dialog box, similar to `alert()`. This `prompt()` function does more than `alert()`, asking the user to enter data, and storing it in a variable after the user clicks _OK._ In this case, we are asking the user to enter a name. Next, the code calls on an API `localStorage`, which allows us to store data in the browser and retrieve it later. We use localStorage's `setItem()` function to create and store a data item called `'name'`, setting its value to the `myName` variable which contains the user's entry for the name. Finally, we set the `textContent` of the heading to a string, plus the user's newly stored name.
4. Add the following condition block. We could call this initialization code, as it structures the app when it first loads.
    
    ```js
    if (!localStorage.getItem("name")) {
      setUserName();
    } else {
      const storedName = localStorage.getItem("name");
      myHeading.textContent = `Mozilla is cool, ${storedName}`;
    }
    ```
    
    Copy to Clipboard
    
    This first line of this block uses the negation operator (logical NOT, represented by the `!`) to check whether the `name` data exists. If not, the `setUserName()` function runs to create it. If it exists (that is, the user set a user name during a previous visit), we retrieve the stored name using `getItem()` and set the `textContent` of the heading to a string, plus the user's name, as we did inside `setUserName()`.
5. Put this `onclick` event handler (below) on the button. When clicked, `setUserName()` runs. This allows the user to enter a different name by pressing the button.
    
    ```js
    myButton.onclick = () => {
      setUserName();
    };
    ```

## Full code
```js
let myButton = document.querySelector("button")

let myHeading = document.querySelector("h1")

  

function setUserName(){

    const myName = prompt("Enter your name. ");

    if (!myName){

        setUserName()

    }else {

    localStorage.setItem("name", myName)

    myHeading.textContent = `Edge is cool, ${myName}`

    }

}

  

if(!localStorage.getItem("name")){

    setUserName();

  

}else{

    const storedName = localStorage.getItem("name");

    myHeading.textContent = `Edge is cool, ${storedName}`

}

  

myButton.onclick = () => {

    setUserName();

}
```
## Variable
link: [JavaScript data types and data structures - JavaScript | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)

Installing npm on linus: ```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
$ sudo npm install semistandard --global```

Event processes: [Process | Node.js v20.3.0 Documentation (nodejs.org)](https://nodejs.org/api/process.html#process_process_argv)

## The Map()
this is used to convert a string to numbers within an array
```js
var strings = ["1", "2", "3", "4"]; 
var numbers = strings.map(Number); 
console.log(numbers);
```

## Exporting objects or functions
link: [51 Elliot: Simple Intro to NodeJS Module Scope](http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

JavaScript Objects: [JavaScript object basics - Learn web development | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics)

classes: [Classes in JavaScript - Learn web development | MDN (mozilla.org)](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Classes_in_JavaScript)

