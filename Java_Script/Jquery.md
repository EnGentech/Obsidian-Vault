function list in jquery
link: **[jQuery API Documentation](https://api.jquery.com/)**

1. **Selectors:**
    
    - `$(selector)`: Selects one or more elements based on the given selector.
    - Example: `$("p")` selects all `<p>` elements on the page.
2. **DOM Manipulation:**
    
    - `.html(content)`: Gets or sets the HTML content of an element.
    - `.text(content)`: Gets or sets the text content of an element.
    - `.append(content)`: Appends content to an element.
    - `.prepend(content)`: Prepends content to an element.
    - `.remove()`: Removes selected elements from the DOM.
3. **CSS Manipulation:**
    
    - `.addClass(className)`: Adds a class to selected elements.
    - `.removeClass(className)`: Removes a class from selected elements.
    - `.css(propertyName, value)`: Gets or sets the value of a CSS property for selected elements.
4. **Event Handling:**
    
    - `.on(event, handler)`: Attaches an event handler function to selected elements.
    - `.click(handler)`: Attaches a click event handler to selected elements.
    - `.hover(handlerIn, handlerOut)`: Attaches mouseenter and mouseleave event handlers.
5. **Animations:**
    
    - `.hide()`: Hides selected elements with a sliding animation.
    - `.show()`: Shows selected elements with a sliding animation.
    - `.fadeIn()`: Fades in selected elements.
    - `.fadeOut()`: Fades out selected elements.
    - `.slideUp()`: Slides up selected elements.
    - `.slideDown()`: Slides down selected elements.
6. **AJAX and HTTP Requests:**
    
    - `.ajax(options)`: Performs an AJAX request.
    - `.get(url, data, success)`: Performs a GET request.
    - `.post(url, data, success)`: Performs a POST request.
7. **Utility:**
    
    - `$.each(collection, callback)`: Iterates over a collection and applies a function.
    - `$.trim(string)`: Removes whitespace from the beginning and end of a string.
    - `$.isArray(object)`: Checks if an object is an array.
    - `$.extend(target, object1, object2)`: Extends an object with properties from other objects.