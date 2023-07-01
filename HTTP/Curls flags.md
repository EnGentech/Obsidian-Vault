link: [List of popular Curl flags with short descriptions (reqbin.com)](https://reqbin.com/req/c-skhwmiil/curl-flags-example)

## Important 20

### 20 most popular Curl flags for everyday use

The table below does not show all of the Curl options, but some of them you will use in your projects.

|Flags|Description|Syntax|
|---|---|---|
|-O|[Download](https://reqbin.com/req/c-egazzayq/curl-download-file) the file and save it under the original name|```curl<br>curl -O [URL]<br>```|
|-o|Download the file and save it with a different name|```curl<br>curl -o [file name] [URL]<br>```|
|-X|Specify the [HTTP method](https://reqbin.com/Article/HttpMethods) to be used when sending the request|```curl<br>curl -X [method] [URL]<br>```|
|-I or -head|[Print](https://reqbin.com/req/c-ea0d5rlb/curl-add-header-example) the title without the body of the document|```curl<br>curl -I [URL]<br>```|
|-d|Specify the data to send to the server|```curl<br>curl -d "key1=value1&key2=value2" [URL]<br>```|
|-k or -insecure|Ignore [SSL](https://reqbin.com/req/c-bw1fsypn/curl-ssl-request) Certificate Errors|```curl<br>curl -k [URL]<br>```|
|-u or --user|Specify the [authentication](https://reqbin.com/Article/HttpAuthentication) data by passing a pair of login-password|```curl<br>curl -u [user:password] [URL]<br>```|
|-F|Submit [form](https://reqbin.com/req/c-sma2qrvp/curl-post-form-example) data as POST request|```curl<br>curl -F @field_name=@path/to/myFile<br>```|
|--cookie|Send [HTTP cookies](https://reqbin.com/req/c-bjcj04uw/curl-send-cookies-example)|```curl<br>curl --cookie "Name=Value" [URL]<br>```|
|-x or --proxy|Use a [proxy](https://reqbin.com/req/c-ddxflki5/curl-proxy-server) server to upload files|```curl<br>curl -x "[protocol://][host][:port]" [URL] [options]<br>```|
|--limit-rate|Limit the download speed|```curl<br>curl --limit-rate [speed] -O [URL]<br>```|
|-L or --location|Follow Curl [redirect](https://reqbin.com/req/c-bvijc9he/curl-follow-redirect) using HTTP Location header|```curl<br>curl -L [URL]<br>```|
|-v|Makes Curl verbose|```curl<br>curl -v [URL]<br>```|
|-m or --max-time|[Set](https://reqbin.com/req/c-70cqyayb/curl-timeout) a limit in seconds for the entire operation|```curl<br>curl -m [SECONDS] [URL]<br>```|
|--connect-timeout|Set a limit in seconds for a connection request|```curl<br>curl --connect-timeout [SECONDS] [URL]<br>```|
|-T|Transfers the specified local file to a remote URL|```curl<br>curl -T [file name] [URL]<br>```|
|-H or --header|Add additional HTTP request [header](https://reqbin.com/req/c-ea0d5rlb/curl-add-header-example)|```curl<br>curl -H "X-Header: value" [URL]<br>```|
|-D|Save the HTTP headers that the site sends back|```curl<br>curl -D [URL]<br>```|
|-A or --user-agent|Set [User-Agent](https://reqbin.com/req/c-ekublyqq/curl-user-agent) string|```curl<br>curl -A "value" [URL]<br>```|
|-C|Resume an interrupted or intentionally stopped download|```curl<br>curl -C [OFFSET] -O [URL]<br>```|

