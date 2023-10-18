Here is a table containing some commonly used commands in Redis, along with their descriptions and code examples:

| Command | Description | Code Example |
|---------|-------------|--------------|
| SET | Set the string value of a key | `SET mykey "Hello"` |
| GET | Get the value of a key | `GET mykey` |
| DEL | Delete a key | `DEL mykey` |
| KEYS | Find all keys matching the given pattern | `KEYS *` |
| EXISTS | Check if a key exists | `EXISTS mykey` |
| EXPIRE | Set a key's time to live in seconds | `EXPIRE mykey 10` |
| TTL | Get the time to live for a key in seconds | `TTL mykey` |
| INCR | Increment the integer value of a key by one | `SET mykey 10`<br>`INCR mykey` |
| DECR | Decrement the integer value of a key by one | `SET mykey 10`<br>`DECR mykey` |
| RPUSH | Append one or multiple values to a list | `RPUSH mylist "world"` |
| LRANGE | Get a range of elements from a list | `LRANGE mylist 0 1` |
| SADD | Add one or more members to a set | `SADD myset "Hello"` |
| SMEMBERS | Get all the members of a set | `SMEMBERS myset` |
| ZADD | Add one or more members to a sorted set, or update its score if it already exists | `ZADD myzset 1 "one"` |
| ZRANGE | Return a range of members in a sorted set, by index | `ZRANGE myzset 0 -1 WITHSCORES` |
| HSET | Set the string value of a hash field | `HSET myhash field1 "Hello"` |
| HGET | Get the value of a hash field | `HGET myhash field1` |
| HGETALL | Get all the fields and values in a hash | `HGETALL myhash` |

