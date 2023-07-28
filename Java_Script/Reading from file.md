```javascript
const file = require('fs')

  
file.readFile(process.argv[2], (err, data) => {

        if (err) throw err;

            console.log(data.toString());

})
```

In javascript, a file and an API is read through the require module and the type of file to be read will be placed as an argument for instance, then reading from a file, the 'fs' is passed as an argument to the require parameter and the 'request' is used when attempting to connect to the web API.
link: [The Node.js Request Module (stackabuse.com)](https://stackabuse.com/the-node-js-request-module/)