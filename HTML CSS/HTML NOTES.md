What is HTML?
In simple words, HTML is the primary building block to create and structure website content.
Let's see what HyperText Markup Language means.
•	HyperText
HyperText is a way of organizing text that allows the reader to easily navigate and access related information. It takes the reader to a different part of the same web page, or to a different web page altogether.
•	Markup language
A markup language is a computer language that is used to add structure and formatting to a text document. Markup languages use a system of tags to define the structure and content of a document. These tags are interpreted by a program or application to display the document in a specific way.

Example of HTML
Let's see a simple example of HTML.
<!DOCTYPE html>
<html>
    <head>
        <title>programiz</title>
    </head>
    <body>
        <h1>HTML Tutorial</h1>
        <p>You'll learn about HTML.</p>
    </body>
</html>
In the above program,
•	<!DOCTYPE html> - defines that this document is an HTML document
•	<html> -root element of an HTML page which encloses all other elements in the HTML page
•	<head> - contains information about the page, such as the title and metadata
•	<title> - specifies a title for the HTML page which is shown in the browser's title bar
•	<body> - defines the main content of the page and is a container for all the visible contents, such as headings, paragraphs, lists, etc
•	<h1> - defines a heading
•	<p> - defines a paragraph of HTML document

How HTML works?
HTML works by defining the structure and content of a web page using a series of tags like <h1>, <p>, etc. Each tag has a meaning and can be used to define the purpose of the content it encloses. For example,
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width">
        <title>Programiz</title>
    </head>
    <body>
        <center><h1>Programiz</h1></center>
        <h1>Learn to Code for Free</h1>
        <p>
            Learn to code with our beginner-friendly tutorials and examples.
            Read interactive tutorials, and write and test your code to learn programming.
        <p>
        <button>Join for free</button>
    </body>
</html>

As you can see, a web browser reads HTML tags and displays them on the browser by interpreting their meaning. In the above code:
•	<h1> tag - displays the content inside it as a heading
•	<p> tag - displays the content inside it as a paragraph
•	<center> tag - displays contents inside it at the center of the page


How to create and run an HTML file?
You will need a text editor and a web browser to create and run an HTML file on your computer. You can follow the following steps to create and run an HTML file on your device.
HTML Features
HTML is a text-based language used to create web pages. It has several features that make it a powerful and widely used language for creating web pages. Some of these features include:
•	HTML is a standard language used for creating and structuring web pages. It allows for the organization of content using elements such as headings, paragraphs, lists, and tables.
•	It supports a wide range of media types, including text, images, audio, and video, which makes web pages more engaging and interactive.
•	HTML is a flexible language that can be used with other technologies, such as CSS and JavaScript, to add additional features and functionality to a web page
•	Since HTML is compatible with all browsers, web pages created in HTML are displayed across a variety of platforms and devices.
•	Furthermore, it is an open and standardized language, which is constantly being updated and improved by a community of developers and experts

HTML Basics
In this tutorial, you will learn about HTML Basics and their implementation with the help of examples.
HTML (HyperText Markup Language) is a markup language used to structure and organize the content on a web page. It uses various tags to define the different elements on a page, such as headings, paragraphs, and links.
________________________________________
HTML Hierarchy
HTML elements are hierarchical, which means that they can be nested inside each other to create a tree-like structure of the content on the web page.
This hierarchical structure is called the DOM (Document Object Model), and it is used by the web browser to render the web page. For example,
<!DOCTYPE html>
<html>
    <head>
        <title>My web page</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <p>This is my first web page.</p>
        <p>It contains a 
             <strong>main heading</strong> and <em> paragraph </em>.
        </p>
    </body>
</html>

In this example, the html element is the root element of the hierarchy and contains two child elements: head and body. The head element, in turn, contains a child element called the title, and the body element contains child elements: h1 and p.
Let's see the meaning of the various elements used in the above example.
•	<html>: the root element of the DOM, and it contains all of the other elements in the code
•	<head>: contains metadata about the web page, such as the title and any linked CSS or JavaScript files
•	<title>: contains the title of the web page, which will be displayed in the web browser's title bar or tab
•	<body>: contains the main content of the web page, which will be displayed in the web browser's window
•	<p>: contains the paragraphs of text on the web page
•	<strong>, <em>: child elements of the <p> elements, they are used to mark text as important and emphasized respectively

What are HTML elements?
HTML elements consist of several parts, including the opening and closing tags, the content, and the attributes. Here is an explanation of each of these parts:
 
Here,
•	The opening tag: This consists of the element name, wrapped in angle brackets. It indicates the start of the element and the point at which the element's effects begin.
•	The closing tag: This is the same as the opening tag, but with a forward slash before the element name. It indicates the end of the element and the point at which the element's effects stop.
•	The content: This is the content of the element, which can be text, other elements, or a combination of both.
•	The element: The opening tag, the closing tag, and the content together make up the element.

What are HTML Attributes?
HTML elements can have attributes, which provide additional information about the element. They are specified in the opening tag of the element and take the form of name-value pairs. Let's see an example:
<a href="http://example.com"> Example </a>
The href is an attribute. It provides the link information about the <a> tag. In the above example,
•	href - the name of attribute
•	https://www.programiz.com - the value of attribute

HTML Syntax
We need to follow a strict syntax guidelines to write valid HTML code. This includes the use of tags, elements, and attributes, as well as the correct use of indentation and white space. Here are some key points about HTML syntax:
1. HTML tags consist of the element name, wrapped in angle brackets. For example, <h1>, <p>, <img> are some HTML tags.
2. HTML elements are created by enclosing the content of the element inside the opening and closing tags of the element. For example,
<span>Some text.</span>
is an HTML element.
3. HTML attributes are used to provide additional information about HTML elements and are specified in the opening tag of the element. For example,
<a target="www.google.com">Click Here</a> 
Here, target is an attribute.
4. HTML code should be well-formed and properly indented, with each element on its own line and each level of hierarchy indented by one level. This makes the code easier to read and understand, and can help to avoid errors. For example,

<html>
    <head>
        <title>My First HTML Page</title>
    </head>
    <body>
        <h1>My First HTML Page</h1>
        <p> Hello World!</p>
    </body>
</html>

Web Design Basics: How HTML, CSS and JavaScript Work?
In this tutorial, you will learn about Web design basics and their implementation with the help of examples.
Web design refers to the process of creating and styling the appearance of a website. There are 3 fundamental technologies to build the modern website and web applications. They are:
•	HTML
•	CSS
•	JS
These technologies work together to provide the structure, style, and interactivity of a web page.
________________________________________
HTML
HTML (HyperText Markup Language) is a markup language used to structure and organize the content on a web page. It uses various tags to define the different elements on a page, such as headings, paragraphs, and links. Let's see an example:
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h1>Programiz</h1>
        <p>We create easy to understand programming tutorials.</p>
    </body>
</html>

Here, we have an HTML document where:
•	<h1> - heading of the document
•	<p> - paragraph of the document
The heading and paragraph tag in the above code help create a webpage structure.
________________________________________
CSS
CSS (Cascading Style Sheets) is a stylesheet language. It is used to style HTML documents.
It specifies how the elements of HTML look including their layout, colors, and fonts. We use <style> tag to add CSS to HTML documents. Let's add some CSS to our previous HTML code.
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
        <style>
            h1 {
  	    color: blue;
            }
            p {
  	    color: red;
            }
        </style>
    </head>
    <body>
        <h1>Programiz</h1>
        <p>We create easy to understand programming tutorial.</p>
    </body>
</html>

In the above code, we've applied CSS to <h1> and <p> tags to change their text color. Notice the code,
 h1 {
    color: blue;
}
This CSS code turns the text color of every <h1> element into blue.
Similarly,
 p {
    color: red;
}
This CSS code turns the text color of every <p> element into red.
________________________________________
JavaScript
JavaScript (JS) is a programming language that makes websites interactive and dynamic. It is primarily used in web browsers to create dropdown menus, form validation, interactive maps, and other elements on a website.
We use JavaScript with HTML and CSS to create websites that are more dynamic and user-friendly. We use <script> tag to add JS to HTML. For example,
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <button onclick="displayAlert()">Click me!</button>

        <script>
          function displayAlert() {
            alert("Learn coding from Programiz Pro");
          }
        </script>
    </body>
</html>

In the above example we have created a button that calls displayAlert() when clicked.
Notice the code,
<script>
  function displayAlert() {
    alert("Learn coding from Programiz Pro");
  }
</script>
This function simply displays an alert box with the message Learn coding from Programiz Pro.
________________________________________
How do HTML, CSS, and JavaScript work?
Let us see an example of how HTML, CSS, and JS work together for a user-friendly web experience. Let's see an example,
<html>
    <head>
        <title>My Webpage</title>
        <style>
          body {
            text-align: center;
          }
          h1 {
            color: #333;
          }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a simple HTML, CSS, and JavaScript webpage.</p>
        <button onclick="displayAlert()">Click me!</button>
        <script>
          function displayAlert() {
    	alert('Hello World!');
          }
        </script>
    </body>
</html>
In the above example, we created a simple webpage. We can now learn more HTML, CSS, and JS to create even better websites.




HTML TAGS IN THEIR CATEGORIES
Tag Description
<!DOCTYPE> Defines the document type
<html> Defines an HTML document
<title> Defines a title for the document
<body> Defines the document's body
<h1> to <h6> Defines HTML headings
<p> Defines a paragraph
<br> Inserts a single line break
<hr> Defines a thematic change in the content
<!--...--> Defines a comment
Formatting
Tag Description
<acronym> Not supported in HTML5. Use <abbr> instead.
Defines an acronym
<abbr> Defines an abbreviation or an acronym
<address> Defines contact information for the author/owner of a document/article
<b> Defines bold text
<bdi> Isolates a part of text that might be formatted in a different direction from other text outside it
<bdo> Overrides the current text direction
<big> Not supported in HTML5. Use CSS instead.
Defines big text
<blockquote> Defines a section that is quoted from another source
<center> Not supported in HTML5. Use CSS instead.
Defines centered text
<cite> Defines the title of a work
<code> Defines a piece of computer code
<del> Defines text that has been deleted from a document
<dfn> Represents the defining instance of a term
<em> Defines emphasized text
<font> Not supported in HTML5. Use CSS instead.
Defines font, color, and size for text
<i> Defines a part of text in an alternate voice or mood
<ins> Defines a text that has been inserted into a document
<kbd> Defines keyboard input
<mark> Defines marked/highlighted text
<meter> Defines a scalar measurement within a known range (a gauge)
<pre> Defines preformatted text
<progress> Represents the progress of a task
<q> Defines a short quotation
<rp> Defines what to show in browsers that do not support ruby annotations
<rt> Defines an explanation/pronunciation of characters (for East Asian typography)
<ruby> Defines a ruby annotation (for East Asian typography)
<s> Defines text that is no longer correct
<samp> Defines sample output from a computer program
<small> Defines smaller text
<strike> Not supported in HTML5. Use <del> or <s> instead.
Defines strikethrough text
<strong> Defines important text
<sub> Defines subscripted text
<sup> Defines superscripted text
<time> Defines a date/time
<tt> Not supported in HTML5. Use CSS instead.
Defines teletype text
<u> Defines text that should be stylistically different from normal text
<var> Defines a variable
<wbr> Defines a possible line-break
Forms and Input
Tag Description
<form> Defines an HTML form for user input
<input> Defines an input control
<textarea> Defines a multiline input control (text area)
<button> Defines a clickable button
<select> Defines a drop-down list
<optgroup> Defines a group of related options in a drop-down list
<option> Defines an option in a drop-down list
<label> Defines a label for an <input> element
<fieldset> Groups related elements in a form
<legend> Defines a caption for a <fieldset> element
<datalist> Specifies a list of pre-defined options for input controls
<keygen> Defines a key-pair generator field (for forms)
<output> Defines the result of a calculation
Frames
Tag Description
<frame> Not supported in HTML5.
Defines a window (a frame) in a frameset
<frameset> Not supported in HTML5.
Defines a set of frames
<noframes> Not supported in HTML5.
Defines an alternate content for users that do not support frames
<iframe> Defines an inline frame
Images
Tag Description
<img> Defines an image
<map> Defines a client-side image-map
<area> Defines an area inside an image-map
<canvas> Used to draw graphics, on the fly, via scripting (usually JavaScript)
<figcaption> Defines a caption for a <figure> element
<figure> Specifies self-contained content
Audio / Video
Tag Description
<audio> Defines sound content
<source> Defines multiple media resources for media elements (<video> and <audio>)
<track> Defines text tracks for media elements (<video> and <audio>)
<video> Defines a video or movie
Links
Tag Description
<a> Defines a hyperlink
<link> Defines the relationship between a document and an external resource (most used to link to style sheets)
<nav> Defines navigation links
Lists
Tag Description
<ul> Defines an unordered list
<ol> Defines an ordered list
<li> Defines a list item
<dir> Not supported in HTML5. Use <ul> instead.
Defines a directory list
<dl> Defines a description list
<dt> Defines a term/name in a description list
<dd> Defines a description of a term/name in a description list
<menu> Defines a list/menu of commands
<menuitem> Defines a command/menu item that the user can invoke from a popup menu
Tables
Tag Description
<table> Defines a table
<caption> Defines a table caption
<th> Defines a header cell in a table
<tr> Defines a row in a table
<td> Defines a cell in a table
<thead> Groups the header content in a table
<tbody> Groups the body content in a table
<tfoot> Groups the footer content in a table
<col> Specifies column properties for each column within a <colgroup> element
<colgroup> Specifies a group of one or more columns in a table for formatting
Styles and Semantics
Tag Description
<style> Defines style information for a document
<div> Defines a section in a document
<span> Defines a section in a document
<header> Defines a header for a document or section
<footer> Defines a footer for a document or section
<main> Specifies the main content of a document
<section> Defines a section in a document
<article> Defines an article
<aside> Defines content aside from the page content
<details> Defines additional details that the user can view or hide
<dialog> Defines a dialog box or window
<summary> Defines a visible heading for a <details> element
Meta Info
Tag Description
<head> Defines information about the document
<meta> Defines metadata about an HTML document
<base> Specifies the base URL/target for all relative URLs in a document
<basefont> Not supported in HTML5. Use CSS instead.
Specifies a default color, size, and font for all text in a document
Programming
Tag Description
<script> Defines a client-side script
<noscript> Defines an alternate content for users that do not support client-side scripts
<applet> Not supported in HTML5. Use <embed> or <object> instead.
Defines an embedded applet
<embed> Defines a container for an external (non-HTML) application
<object> Defines an embedded object
<param> Defines a parameter for an object

HTML BASICS
Paragraphing	-    <p>, <pre> :  <strong, br, em, &nbsp>
Headings	-    <h1 to h6>
Comments	-    <!--   --> 	use ctrl + / as shortcut
Table	-    <tr> <th> <td>  <table> : border attribute  categories of table <thead> <tbody> <tfoot>  ; colspan and rowspan 
List	-    <ol> <ul> <dl>;	description list: <dd> <dt>
	Tags used in HTML lists
Tag	Explanation
<ol>	Defines an ordered list.
<ul>	Defines an unordered list.
<dl>	Defines a description list.
<li>	Defines a list item in ordered or unordered lists.
<dt>	Defines a term in description list.
<dd>	Defines the description of a term in the description list.
Nested List	-    use the above
Ordered List	-    start attribute, type attribute, reversed attribute
Pre tag	-    <pre>
Horizontal line	-    <hr>

HTML Inline and Block Elements
HTML elements can be broadly categorized into one of two categories:
•	Inline Elements: <span>, <a>, <strong>, <img> <input> <b> etc.
•	Block Elements: <p>, <div>, <h1>, <figure> etc.
HTML Inline Elements
Inline elements are displayed on the same line. They do not start on a new line and take up only as much width as their contents require. An example of an inline element is the <span> tag.
<p>This is how <span style="border: 1px solid black">span</span> works. </p>

HTML Block Elements
Block elements take up the whole horizontal space available in its container. They start on a new line and take up as much height as their contents require.
An example of a block element is the HTML Paragraph Tag.
<p style="border: 1px solid black">This is how block elements works. </p>

Css With Html Inline And Block Elements
CSS properties	Effects on Elements
	Block Elements	Inline Elements
Height			
Width			
Margin			
Padding				
Border				

HTML Links
HTML links or hyperlinks connect one resource on the web to another. The resource may be an image, a web page, a program, a video clip, an audio clip, an element within a web page, etc, or anything that can be hosted on the internet.
We use the HTML <a> tag to create hyperlinks. The syntax for the <a> tag is
<a href="URL"> Text </a>
Image Links
You can insert almost any content inside a <a> tag to make it a link. Hence, we can also use images as a link.
<img src=””, alt=””>
target Attribute
By default, any link clicked will open in the same browser window. This may lead to a bad user experience. This is where the target attribute becomes useful. For example,
<a href="https://www.google.com" target="_blank">Google</a>
Target	Description
_self	(Default) Opens the link in the same browser tab.
_blank	Opens the link in a new browser tab.
_parent	Opens the link in the parent frame.
_top	Opens the link in the current tab window (topmost parent).
download Attribute
When linking to a web resource, we can specify that the resource is to be downloaded by using the download attribute. For example,
<a href="/files/logo.png" download> Download Image </a>
To change the image default name, add the new name to the download attribute e.g <a href….. download=”new_name”>
Linking to an HTML element
As previously mentioned, along with linking to web sources, an <a> tag can also link to a respecific element within the web page. We use that by adding # to the URL followed by the id of the specific element. For example,
Link to an element in the same webpage:
<a href="#title">Go to Title</a>
Email and Call links
We can also use HTML links as email links and call links to help users contact us or someone else using their email client or call app.
Email links:
The email link opens the user's default mail client to make it easier for the user to send mail to a specific address. For example,
<a href="mailto:name@domain.com" > Send Mail </a>
Call links:
Similar to email links, we can create call links to trigger the user's call app with a phone number. For example,
<a href="tel:+9778841999999"> Call Us </a>
HTML Images
HTML images are used to embed images in HTML. 
The HTML <img> tag embeds an image within the HTML web page. For example,
<img src="logo.png">
Basic attributes for images
<img loading=”lazy”(used when images are not to be loaded until you scroll down) height width alt style title>
HTML Bold
We use the HTML <b> tag or the HTML <strong> tag to make text bold
In addition, the CSS font-weight can be applied here.
HTML Italic
We use the HTML <i> tag or the HTML <em> tag to make the text italic.
In addition, font-style can be applied using CSS
HTML Superscript and Subscript
Superscript
The HTML <sup> tag is used to create superscript text. The text inside the <sup> tag is rendered half a character above the normal line and has a smaller font size. For example,
<p> This is a <sup>Superscript</sup> text.</p>
<sub> for subscript
HTML Formatting
HTML provides us with several tags to help format text, <b> for bold, <i> for italic, <u> for underlining, etc. These tags are divided into two categories:
Physical Tags: These tags are presentational. They don't add extra meaning to the text. For example,
<p> This text is <i>italic</i>.</p>
Html formatting tags includes
<b> <i> <u> <strong> <em> <mark> <sup> <sub> <del> <ins> <big> <small>
HTML Head
The <head> section contains information about the HTML document like meta, links, styles, scripts, titles, etc.
<head>
    <title>HTML  Head Article</title>
</head>
Elements of the head tag includes
<title> <meta> <script> <link> <style> <base>
HTML <meta> tag
The HTML <meta> tag is used to add metadata (information about data) about the document. Metadata includes information like character set, page description, author name, viewport settings, etc. For example,
<head>
    <meta charset="UTF-8">
    <meta name="description" content="HTML Tutorial">
    <meta name="keywords" content="HTML, Learn, Tutorial">
    <meta name="author" content="programiz team">
</head>
To learn more about the <meta> tag, visit HTML Meta.
HTML <base> tag
The HTML <base> tag is used to define the base URL for the document. The base URL refers to the common part of the URL across all the links in the webpage. All relative links in the document will point to the URL in the base tag. For example,
<head>
    <base href="https://programiz.com" target="_blank">
</head>
<body>
    <img src="images/logo.png" alt="Logo of Programiz">
</body>
Here, the image will load from https://programiz.com/images/logo.png instead of images/logo.png. This is because the <base> tag will add https://programiz.com/ before the src of the image and any other relative links on the webpage.
HTML Title
The HTML <title> tag defines the document's title. The content of the <title> tag is shown in the browser's title bar or the page's tab. For example,
<title>My First Title</title>
HTML Style
The HTML <style> tag defines style rules for an HTML document. It defines how HTML elements are rendered in a browser. We write CSS code inside the <style> tag. For example,
<style>
    h1 {
      color: red;
    }
</style>
<h1>Heading</h1>
HTML Meta Elements
The HTML <meta> tag is used to represent metadata about the HTML document.
Metadata refers to the information about data (data about the HTML document). The metadata consists of information like charset attribute, name attribute, http-equiv attribute, etc.
The <meta> tag should always go inside the <head> element. For example,
<head>
  <meta charset="utf-8" />
</head>
Here, <meta charset = "utf-8"> tells the browser to use the UTF-8 character encoding to convert machine code into human-readable code.
________________________________________
Attributes of Metadata
The Meta tag can have the following attributes:
•	charset attribute
•	name attribute
•	http-equiv attribute
We will learn about each attribute in detail.
________________________________________
charset attribute
The charset attribute defines the character encoding for the HTML document. For example,
<meta charset="UTF-8">
It helps to display an HTML page correctly in the browser. UTF-8 is the only valid encoding for HTML5 documents.
________________________________________
name attribute
The name attribute together with the content attribute provides information in terms of name-value pairs. Where:
•	name - name of the metadata
•	content - value of the metadata
Let's see an example:
<meta name="description" content=" In this article you will learn about meta tags.">
Here, we have used the name attribute to provide the information about the description of the HTML document. The text inside the content attribute is the value of description.
Some common values for the name attribute include author, keywords, referrer, etc. For example,
<head>
    <meta name="keywords" content="Meta tag, HTML">
    <meta name="author" content="Elon Musk">
</head>
Here, we have used meta tags to provide information about keywords and the author of the HTML document.
________________________________________
http-equiv attribute
The http-equiv attribute is used to provide an HTTP header for the information of the content attribute. The list of possible values for the attribute are:
•	content-security-policy: Specifies a content policy for the document. It is used to specify allowed server URLs. For example,
<meta http-equiv="content-security-policy" content="default-src 'self';" />
Here, the above tag specifies that external resources are only allowed from self, i.e. the same host as the webpage.
•	content-type: Specifies the character encoding for the document. It is the same as using the charset attribute. It is used to set the character encoding for the HTML document. For example,
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
•	default-style: Specifies the preferred style sheet to use. For example,
<meta http-equiv="default-style" content="stylesheet-1">
Here, in case of multiple stylesheets, the stylesheet with the id of stylesheet-1 will be prioritized.
•	refresh: Defines a time interval for the document to refresh itself. For example,
<!-- To refresh the site in 3 seconds -->
<meta http-equiv="refresh" content="3" />
You can optionally redirect the user to a separate url by adding ;url= followed by the url. It should be inside the content attribute after the time interval.
<!-- To redirect to youtube after 3 seconds -->
<meta http-equiv="refresh" content="3;url=https://www.youtube.com" />
________________________________________
Uses of Metadata
The uses of Metadata are as follows:
•	Tells the browser how to display content or refresh the site.
•	Used by search engines to read the data of the HTML page.
•	Used to set the viewport. Viewport refers to the visible area of the webpage. For example,


<meta name="viewport" content="width=device-width, initial-scale=1.0">
HTML Favicon
A Favicon is a small image displayed on the left of the page title in the browser tab.
Add Favicon
We use the HTML <link> tag to attach a favicon to the document. For example,
<link rel="shortcut icon" href="/images/favicon.ico">
Let us look at how this would look on a real site. For example, programiz.com might have something like this in their code,
<head>
    <title>Programiz: Learn to Code for Free!</title>
    <link rel="shortcut icon" href="favicon.png">
</head>

HTML Form
An HTML Form is a section of the document that collects input from the user. The input from the user is generally sent to a server (Web servers, Mail clients, etc). We use the HTML <form> element to create forms in HTML.
 
Example: HTML Form
The HTML <form> element is used to create HTML forms. For example,
<form>
    <label for="firstname">First name: </label>
    <input type="text" name="firstname"  required>
    <br>
    <label for="lastname">Last name: </label>
    <input type="text" name="lastname"  required>
    <br>
    <label for="email">email: </label>
    <input type="email" name="email"  required>
    <br>
    <label for="password">password: </label>
    <input type="password" name="password"  required>
    <br>
    <input type="submit" value="Login!">
</form>
HTML Form Elements
A form contains special interactive elements that users use to send the input. They are text inputs, textarea fields, checkboxes, dropdowns, and much more. For example,
<form>
    <label for="name">Name:</label>
    <input type="text" name="name"><br><br>
    <label for="sex">Sex:</label>
    <input type="radio" name="sex" id="male" value="male">
    <label for="male">Male</label>
    <input type="radio" name="sex" id="female" value="female">
    <label for="female">Female</label> <br><br>
    <label for="country">Country: </label>
    <select name="country" id="country">
        <option>Select an option</option>
        <option value="nepal">Nepal</option>
        <option value="usa">USA</option>
        <option value="australia">Australia</option>
    </select><br><br>
    <label for="message">Message:</label><br>
    <textarea name="message" id="message" cols="30" rows="4"></textarea><br><br>
    <input type="checkbox" name="newsletter" id="newsletter">
    <label for="newsletter">Subscribe?</label><br><br>
    <input type="submit" value="Submit">
</form>
Form Attributes
The HTML <form> element contains several attributes for controlling data submission. They are as follows:
action
The action attributes define the action to be performed when the form is submitted. It is usually the url for the server where the form data is to be sent.
<form action="/login">
    <label for="email">Email:</label>
    <input type="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" name="password"><br><br>
    <input type="submit" value="Submit">
</form>
In the above example, when the form is submitted, the data from the form is sent to /login.
method
The method attribute defines the HTTP method to be used when the form is submitted. There are 3 possible values for the method attribute:
•	post - It is used to send data to a server to update a resource.
•	<form method = "post">
•	...
</form>
•	get: It is used to request data from a specified resource.


•	<form method = "get">
•	...
</form>
•	dialog: This method is used when the form is inside a <dialog> element. Using this method closes the dialog and sends a form-submit event.
To learn more about HTTP methods GET and POST, visit HTML Form Action: POST and GET.
target
It specifies where to display the response received after the form is submitted. Similar to the target attribute in <a> tags, the target attribute has four possible values.
•	_self (default): Load the response into the same browser tab.
•	<form target="_self">
•	    <label for="firstname">Enter your first name:</label>
•	    <input type="text" name="firstname">
</form>
•	_blank: Load the response into a new browser tab.
•	<form target="_blank">
•	    <label for="firstname">Enter your first name:</label>
•	    <input type="text" name="firstname">
</form>
•	_parent: Load into the parent frame of the current one. If no parent is available,it loads the response into the same tab.
•	<form target="_parent">
•	    <label for="firstname">Enter your first name:</label>
•	    <input type="text" name="firstname">
</form>
•	_top: Load the response into the top-level frame. If no parent is available, it loads the response into the same tab.
•	<form target="_top">
•	    <label for="firstname">Enter your first name:</label>
•	    <input type="text" name="firstname">
</form>
enctype
It specifies how the form data should be encoded for the request. It is only applicable if we use the POST method.
<form method="post" enctype="application/x-www-form-urlencoded">
</form>
In the above example, data from the form will be encoded in the x-www-form-urlencoded format (which is the default encoding format).
name
It specifies the name of the form. The name is used in Javascript to reference or access this form.
<form name="login_form">
    <label for="email">Email:</label>
    <input type="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" name="password"><br><br>
    <input type="submit" value="Submit">
</form>
The above form can be accessed in javascript as:
document.forms['login_form']
Although it is possible to use name to access form elements in javascript, it is recommended to use id to access the form elements.
novalidate
If the novalidate attribute is set, all validations in the form elements are skipped.
<form novalidate>
    <label for="email">Enter your email:</label>
    <input type="email" id="email" name="email"><br><br>
    <input type="submit">
</form>
In the above example, the form will be submitted even if we enter some invalid value to the email field, such as Hi.

Form elements include
<input> <label> <button> <select> <option> <optgroup> <textarea> <fieldset> <legend> <datalist> <output> 
HTML <button> tag
The HTML <button> element is an interactive element that is activated by a user with a mouse, keyboard, finger, voice command, or other assistive technology.
It performs a programmable action, such as submitting a form or opening a dialog when clicked. For example,
<button type="button">Click me</button>
Button type includes
Button	onclick	reset	
HTML <select>, <option> and <optgroup> tags
The HTML <select> tag is used to create a menu of options. Each of the options is represented by the <option> tag. For example,
<label for="pets">Pets:</label>
<select id="pets">
    <option value="dog">Dog</option>
    <option value="cat">Cat</option>
</select>
Additionally, we can also group option elements inside the <optgroup> tag to create a group of options. For example,
<label for="pets">Pets:</label>
<select id="pets">
    <optgroup label="Mammals">
        <option value="dog">Dog</option>
        <option value="cat">Cat</option>
    </optgroup>
    <optgroup label="Insects">
        <option value="spider">Spider</option>
        <option value="ants">Ants</option>
    </optgroup>
    <optgroup label="Fish">
        <option value="goldfish">Goldfish</option>
    </optgroup>
</select>
From the above, the optgroup will create the drop down list in segments to reproduce groups within a list
HTML <datalist> tag
The <datalist> tag defines a list of pre-defined options for an <input> element. It is used to provide autocomplete options to the form elements that show up as recommended options when the user fills in the form. For example,
<label for="country-choice">Choose a country:</label>
<input list="country-options" id="country-choice" name="country-choice">
<datalist id="country-options">
    <option value="Australia">
    <option value="Austria">
    <option value="America">
    <option value="Nepal">
</datalist>
HTML Input Tag
In this tutorial, we will learn about the input tag and its types in HTML with the help of examples.
The HTML <input> tag defines the field where the user can enter data. The type attribute determines what type of user input is taken.
<input type="text" name="firstname">
Here,
•	type - determines the type of input the <input> tag takes
•	name - specifies the name of the input which is what the data is named as when submitting the data to a server.
Different Input Types
The various types of input tags available in HTML5 are:
1.	text - creates a single-line text fields (default)
2.	button - creates a button with no default functionality
3.	checkbox - creates a checkbox
4.	color - creates a color picker
5.	date - creates a date picker
6.	datetime-local - creates a date and time picker
7.	email - creates an input field that allows the user to input a valid email address
8.	file - creates an input field that lets the user upload a file or multiple files
9.	hidden - creates an invisible input field
10.	image - creates a button using an image
11.	month - creates an input field that lets the user enter month and year
12.	password - creates an input field that lets the user enter information securely
13.	radio - creates a radio button
14.	range - creates a range picker from which the user can select the value
15.	reset - creates the button which clears all the form values to their default value
16.	search - allows user to enter their search queries in the text fields
17.	submit - allows user to submit form to the server
18.	tel - defines the field to enter a telephone number
19.	time - creates an input field that accepts time value
20.	url - lets the user enter and edit a URL
21.	week - lets the user pick a week and a year from a calendar

Semantic HTML
HTML tags can be categorized into two types based on semantics in HTML. They are:
•	Semantic Tag
•	Non-semantic Tag
Semantic HTML elements clearly define the purpose and meaning of code.
Semantic Tags
The tags which accurately describe their purpose and describe the type of their content are called semantic tags. For example,
<h1>Header</h1>
From the above code, we can accurately tell that the content inside the <h1> tag is a heading.
Some examples of semantic tags are 一 <h1>-<h6>, <form>, <table>, <main>, etc
Non-Semantic Tags
HTML non-semantic tags do not have a specific meaning or purpose. They are used to create general-purpose containers for content without providing any additional meaning or context. For example,
<span>Some Text</span>
From the above code, we cannot extract the meaning of the text. This code could come from any section of the document thus it adds no semantic value to the document.
Some examples of non-semantic tags are 一 <div>, <span>, etc

HTML <div> Tag
In this tutorial, we will learn about div tags in HTML with the help of examples.
The HTML <div> tag is a non-semantic tag that is used to define division in an HTML document. For example,
<div>
    <h2>This is a heading in a div element</h2>
    <p>This is some text in a div element.</p>
</div>
Usage of HTML <div>
The HTML <div> tag is generally used to group content and provide CSS styles using class or id attributes. For example,
<div class="div1">
    <h2>This is heading.</h2>
    <p>This is a paragraph</p>
</div>

<div class="div2">
    <h2>This is another heading.</h2>
    <p>This is another paragraph</p>
</div>

<style>
    .div1 {
        color: red;
    }

    .div2 {
        color: green;
    }
</style>

HTML <aside> Tag
In this tutorial, we will learn about HTML <aside> tag with the help of examples.
The HTML <aside> tag is used to represent a portion of a document that is indirectly related to the main content. It is most commonly used as a sidebar in the document. It does not render anything special in the browser. For example,
<div>
    <h1>This is a heading</h1>
    <aside>
        <p>This is a paragraph</p>
    </aside>
</div>
CSS with HTML <aside>
We use CSS to style to HTML <aside>. For example,
<aside>
    <h2>Sidebar</h2>
    <p>This is some content in the sidebar.</p>
</aside>
<main>
    <h1>Main Content</h1>
    <p>This is the main content of the page.</p>
</main>
<style>
    main {
        padding: 10px;
        margin: 10px;
    }

    aside {
        width: 200px;
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
        float: left;
    }
</style>

