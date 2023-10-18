Here is an extensive list of Redis commands, along with their descriptions and code examples:

| Command | Description | Code Example |
|---------|-------------|--------------|
| APPEND | Append a value to a key | `APPEND mykey "Hello"` |
| AUTH | Authenticate to the server | `AUTH password` |
| BGSAVE | Asynchronously save the dataset to disk | `BGSAVE` |
| BITCOUNT | Count the number of set bits in a key | `BITCOUNT mykey` |
| BITOP | Perform bitwise operations between keys and store the result in a destination key | `BITOP AND destkey key1 key2` |
| BITFIELD | Perform arbitrary bitfield integer operations on strings | `BITFIELD mykey INCRBY i5 100 1 GET u4 0` |
| BITPOS | Find first bit set or clear in a string | `BITPOS mykey 1` |
| BLPOP | Remove and get the first element in a list, or block until one is available | `BLPOP mylist 0` |
| BRPOP | Remove and get the last element in a list, or block until one is available | `BRPOP mylist 0` |
| BRPOPLPUSH | Pop a value from a list, push it to another list and return it | `BRPOPLPUSH list1 list2 0` |
| BZPOPMIN | Remove and return the member with the lowest score from one or more sorted sets, or block until one is available | `BZPOPMIN myzset 0` |
| BZPOPMAX | Remove and return the member with the highest score from one or more sorted sets, or block until one is available | `BZPOPMAX myzset 0` |
| CLIENT SETNAME | Set the connection name | `CLIENT SETNAME myconnection` |
| CLIENT GETNAME | Get the current connection name | `CLIENT GETNAME` |
| CLIENT LIST | Get the list of client connections | `CLIENT LIST` |
| CLIENT KILL | Kill the connection of a client | `CLIENT KILL ip:port` |
| CLIENT PAUSE | Stop processing commands from clients for some time | `CLIENT PAUSE timeout` |
| CLIENT REPLY | Instruct the server whether to reply to commands | `CLIENT REPLY ON` |
| CLIENT ID | Get the current connection ID | `CLIENT ID` |
| CLUSTER ADDSLOTS | Assign new hash slots to receiving node | `CLUSTER ADDSLOTS 5000` |
| CLUSTER COUNT-FAILURE-REPORTS | Return the number of failure reports active for a given node | `CLUSTER COUNT-FAILURE-REPORTS node-id` |
| CLUSTER COUNTKEYSINSLOT | Return the number of keys in the specified Redis cluster slot | `CLUSTER COUNTKEYSINSLOT 5000` |
| CLUSTER DELSLOTS | Set hash slots as unbound in receiving node | `CLUSTER DELSLOTS 5000` |
| CLUSTER FAILOVER | Forces a slave to perform a manual failover of its master | `CLUSTER FAILOVER [FORCE|TAKEOVER]` |
| CLUSTER FORGET | Remove a node from the nodes table | `CLUSTER FORGET node-id` |
| CLUSTER GETKEYSINSLOT | Return local key names in the specified Redis cluster hash slot | `CLUSTER GETKEYSINSLOT 5000 count` |
| CLUSTER INFO | Provides info about Redis Cluster node state | `CLUSTER INFO` |
| CLUSTER KEYSLOT | Returns the hash slot of the specified key | `CLUSTER KEYSLOT mykey` |
| CLUSTER MEET | Force a node cluster to handshake with another node | `CLUSTER MEET ip port` |
| CLUSTER NODES | Get Cluster config for the node | `CLUSTER NODES` |
| CLUSTER REPLICATE | Reconfigure a node as a replica of the specified master node | `CLUSTER REPLICATE node-id` |
| CLUSTER RESET | Reset a Redis Cluster node | `CLUSTER RESET [HARD|SOFT]` |
| CLUSTER SAVECONFIG | Forces the node to save cluster state on disk | `CLUSTER SAVECONFIG` |
| CLUSTER SET-CONFIG-EPOCH | Set the configuration epoch in a new node | `CLUSTER SET-CONFIG-EPOCH` |
| CLUSTER SETSLOT | Bind a hash slot to a specified node | `CLUSTER SETSLOT 5000 IMPORTING|MIGRATING|STABLE|NODE [node-id]` |
| CLUSTER SLAVES | List replica nodes of the specified master node | `CLUSTER SLAVES node-id` |
| CLUSTER REPLICAS | List replica nodes of the specified master node | `CLUSTER REPLICAS node-id` |
| CLUSTER READONLY | Enables read queries for a Redis Cluster node | `CLUSTER READONLY` |
| CLUSTER READWRITE | Disables read queries for a Redis Cluster node | `CLUSTER READWRITE` |
| COMMAND | Get array of Redis command details | `COMMAND GETKEYS SET` |
| COMMAND COUNT | Get total number of Redis commands | `COMMAND COUNT` |
| COMMAND GETKEYS | Extract keys given a full Redis command | `COMMAND GETKEYS SET mykey "Hello"` |
| COMMAND INFO | Get array of specific Redis command details | `COMMAND INFO SET` |
| CONFIG GET | Get the value of a configuration parameter | `CONFIG GET dir` |
| CONFIG REWRITE | Rewrite the configuration file with the in-memory configuration | `CONFIG REWRITE` |
| CONFIG SET | Set a configuration parameter to the given value | `CONFIG SET save 60 10000` |
| CONFIG RESETSTAT | Reset the stats returned by INFO | `CONFIG RESETSTAT` |
| DBSIZE | Return the number of keys in the selected database | `DBSIZE` |
| DEBUG OBJECT | Get debugging information about a key | `DEBUG OBJECT mykey` |
| DEBUG SEGFAULT | Make the server crash | `DEBUG SEGFAULT` |
| DECR | Decrement the integer value of a key by one | `SET mykey 10`<br>`DECR mykey` |
| DECRBY | Decrement the integer value of a key by the given number | `SET mykey 10`<br>`DECRBY mykey 5` |
| DEL | Delete a key | `DEL mykey` |
| DISCARD | Discard all commands issued after MULTI | `DISCARD` |
| DUMP | Return a serialized version of the value stored at the specified key | `DUMP mykey` |
| ECHO | Echo the given string | `ECHO "Hello World"` |
| EVAL | Execute a Lua script server-side | `EVAL "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}" 2 key1 key2 first second` |
| EVALSHA | Execute a Lua script server-side using the SHA1 hash of the script | `EVALSHA sha1 2 key1 key2 first second` |
| EXEC | Execute all commands issued after MULTI | `EXEC` |
| EXISTS | Check if a key exists | `EXISTS mykey` |
| EXPIRE | Set a key's time to live in seconds | `EXPIRE mykey 10

` |
| EXPIREAT | Set the expiration for a key as a UNIX timestamp | `EXPIREAT mykey 1293840000` |
| FLUSHALL | Remove all keys from all databases | `FLUSHALL` |
| FLUSHDB | Remove all keys from the current database | `FLUSHDB` |
| GEOADD | Add one or more geospatial items | `GEOADD mygeo 13.361389 38.115556 "Palermo" 15.087269 37.502669 "Catania"` |
| GEODIST | Return the distance between two members in the geospatial index | `GEODIST mygeo "Palermo" "Catania" km` |
| GEOHASH | Return valid Geohash strings representing the position of one or more elements in a sorted set value representing a geospatial index | `GEOHASH mygeo "Palermo" "Catania"` |
| GEOPOS | Return the positions (latitude and longitude) of all the specified members of the geospatial index | `GEOPOS mygeo "Palermo" "Catania"` |
| GEORADIUS | Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a point | `GEORADIUS mygeo 15 37 200 km WITHCOORD` |
| GEORADIUSBYMEMBER | Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a member | `GEORADIUSBYMEMBER mygeo "Palermo" 200 km WITHDIST` |
| GET | Get the value of a key | `GET mykey` |
| GETBIT | Returns the bit value at offset in the string value stored at key | `SET mykey "foobar"`<br>`GETBIT mykey 0` |
| GETRANGE | Get a substring of the string stored at a key | `SET mykey "This is a string"`<br>`GETRANGE mykey 0 3` |
| GETSET | Set the string value of a key and return its old value | `GETSET mykey "newvalue"` |
| HDEL | Delete one or more hash fields | `HDEL myhash field1` |
| HEXISTS | Determine if a hash field exists | `HEXISTS myhash field1` |
| HGET | Get the value of a hash field | `HGET myhash field1` |
| HGETALL | Get all the fields and values in a hash | `HGETALL myhash` |
| HINCRBY | Increment the integer value of a hash field by the given number | `HINCRBY myhash field1 5` |
| HINCRBYFLOAT | Increment the float value of a hash field by the given amount | `HINCRBYFLOAT myhash field1 1.5` |
| HKEYS | Get all the fields in a hash | `HKEYS myhash` |
| HLEN | Get the number of fields in a hash | `HLEN myhash` |
| HMGET | Get the values of all the given hash fields | `HMGET myhash field1 field2` |
| HMSET | Set multiple hash fields to multiple values | `HMSET myhash field1 "Hello" field2 "World"` |
| HSET | Set the string value of a hash field | `HSET myhash field1 "Hello"` |
| HSETNX | Set the value of a hash field, only if the field does not exist | `HSETNX myhash field1 "Hello"` |
| HSTRLEN | Get the length of the value of a hash field | `HSTRLEN myhash field1` |
| HVALS | Get all the values in a hash | `HVALS myhash` |
| INCR | Increment the integer value of a key by one | `SET mykey 10`<br>`INCR mykey` |
| INCRBY | Increment the integer value of a key by the given amount | `SET mykey 10`<br>`INCRBY mykey 5` |
| INCRBYFLOAT | Increment the float value of a key by the given amount | `SET mykey 10.50`<br>`INCRBYFLOAT mykey 0.1` |
| INFO | Get information and statistics about the server | `INFO` |
| KEYS | Find all keys matching the given pattern | `KEYS *` |
| LASTSAVE | Get the UNIX timestamp of the last successful save to disk | `LASTSAVE` |
| LINDEX | Get an element from a list by its index | `LINDEX mylist 0` |
| LINSERT | Insert an element before or after another element in a list | `LINSERT mylist BEFORE "World" "There"` |
| LLEN | Get the length of a list | `LLEN mylist` |
| LPOP | Remove and get the first element in a list | `LPOP mylist` |
| LPUSH | Prepend one or multiple values to a list | `LPUSH mylist "world"` |
| LPUSHX | Prepend a value to a list, only if the list exists | `LPUSHX mylist "Hello"` |
| LRANGE | Get a range of elements from a list | `LRANGE mylist 0 1` |
| LREM | Remove elements from a list | `LREM mylist 2 "Hello"` |
| LSET | Set the value of an element in a list by its index | `LSET mylist 0 "Hello"` |
| LTRIM | Trim a list to the specified range | `LTRIM mylist 0 1` |
| MEMORY DOCTOR | Outputs memory problems report | `MEMORY DOCTOR` |
| MEMORY HELP | Show helpful text about the different subcommands | `MEMORY HELP` |
| MEMORY MALLOC-STATS | Show allocator internal stats | `MEMORY MALLOC-STATS` |
| MEMORY PURGE | Ask the allocator to release memory | `MEMORY PURGE` |
| MEMORY STATS | Show memory usage details | `MEMORY STATS` |
| MEMORY USAGE | Estimate the memory usage of a key | `MEMORY USAGE mykey` |
| MGET | Get the values of all the given keys | `MGET key1 key2` |
| MIGRATE | Atomically transfer a key from a Redis instance to another one | `MIGRATE host port key 0 5000` |
| MODULE LIST | List all modules loaded by the server | `MODULE LIST` |
| MODULE LOAD | Load a module | `MODULE LOAD /path/to/module.so` |
| MODULE UNLOAD | Unload a module | `MODULE UNLOAD mymodule` |
| MONITOR | Listen for all requests received by the server in real time | `MONITOR` |
| MOVE | Move a key to another database | `MOVE mykey 1` |
| MSET | Set multiple keys to multiple values | `MSET key1 "Hello" key2 "World"` |
| MSETNX | Set multiple keys to multiple values, only if none of the keys exist | `MSETNX key1 "Hello" key2 "World"` |
| MULTI | Mark the start of a transaction block | `MULTI` |
| OBJECT | Inspect the

 internals of Redis objects | `OBJECT encoding mykey` |
| PERSIST | Remove the expiration from a key | `PERSIST mykey` |
| PEXPIRE | Set a key's time to live in milliseconds | `PEXPIRE mykey 10000` |
| PEXPIREAT | Set the expiration for a key as a UNIX timestamp specified in milliseconds | `PEXPIREAT mykey 1555555555005` |
| PFADD | Add the specified elements to the HyperLogLog data structure stored at the specified key | `PFADD hll "a" "b" "c"` |
| PFCOUNT | Return the approximated cardinality of the set(s) observed by the HyperLogLog at key(s) | `PFCOUNT hll` |
| PFMERGE | Merge N different HyperLogLogs into a single one | `PFMERGE destkey sourcekey1 sourcekey2` |
| PING | Ping the server | `PING` |
| PSETEX | Set the value and expiration in milliseconds of a key | `PSETEX mykey 1000 "Hello"` |
| PSUBSCRIBE | Listen for messages published to channels matching the given patterns | `PSUBSCRIBE news.*` |
| PUBSUB | Inspect the state of the Pub/Sub subsystem | `PUBSUB CHANNELS` |
| PTTL | Get the time to live for a key in milliseconds | `PTTL mykey` |
| PUBLISH | Post a message to a channel | `PUBLISH news "Hello"` |
| PUNSUBSCRIBE | Stop listening for messages posted to channels matching the given patterns | `PUNSUBSCRIBE news.*` |
| QUIT | Close the connection | `QUIT` |
| RANDOMKEY | Return a random key from the keyspace | `RANDOMKEY` |
| READONLY | Enables read queries for a connection to a Redis Cluster replica node | `READONLY` |
| READWRITE | Disables read queries for a connection to a Redis Cluster replica node | `READWRITE` |
| RENAME | Rename a key | `RENAME mykey myotherkey` |
| RENAMENX | Rename a key, only if the new key does not exist | `RENAMENX mykey myotherkey` |
| RESTORE | Create a key using the provided serialized value, previously obtained using DUMP | `RESTORE mykey 0 "\n\x17\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x05Hello\x00\x05\x00\x00\x00\x00"` |
| ROLE | Return the role of the instance in the context of replication | `ROLE` |
| RPOP | Remove and get the last element in a list | `RPOP mylist` |
| RPOPLPUSH | Remove the last element in a list, append it to another list, and return it | `RPOPLPUSH list1 list2` |
| RPUSH | Append one or multiple values to a list | `RPUSH mylist "world"` |
| RPUSHX | Append a value to a list, only if the list exists | `RPUSHX mylist "Hello"` |
| SADD | Add one or more members to a set | `SADD myset "Hello"` |
| SAVE | Synchronously save the dataset to disk | `SAVE` |
| SCARD | Get the number of members in a set | `SCARD myset` |
| SCRIPT DEBUG | Set the debug mode for executed scripts | `SCRIPT DEBUG YES` |
| SCRIPT EXISTS | Check existence of scripts in the script cache | `SCRIPT EXISTS sha1` |
| SCRIPT FLUSH | Remove all the scripts from the script cache | `SCRIPT FLUSH` |
| SCRIPT KILL | Kill the script currently in execution | `SCRIPT KILL` |
| SCRIPT LOAD | Load the specified Lua script into the script cache | `SCRIPT LOAD "return 1"` |
| SDIFF | Subtract multiple sets | `SDIFF set1 set2` |
| SDIFFSTORE | Subtract multiple sets and store the resulting set in a key | `SDIFFSTORE destination set1 set2` |
| SELECT | Change the selected database for the current connection | `SELECT 1` |
| SET | Set the string value of a key | `SET mykey "Hello"` |
| SETBIT | Sets or clears the bit at offset in the string value stored at key | `SETBIT mykey 7 1` |
| SETEX | Set the value and expiration of a key | `SETEX mykey 10 "Hello"` |
| SETNX | Set the value of a key, only if the key does not exist | `SETNX mykey "Hello"` |
| SETRANGE | Overwrite part of a string at key starting at the specified offset | `SET mykey "Hello World"`<br>`SETRANGE mykey 6 "Redis"` |
| SHUTDOWN | Synchronously save the dataset to disk and then shut down the server | `SHUTDOWN` |
| SINTER | Intersect multiple sets | `SINTER set1 set2` |
| SINTERSTORE | Intersect multiple sets and store the resulting set in a key | `SINTERSTORE destination set1 set2` |
| SISMEMBER | Determine if a member is in a set | `SISMEMBER myset "one"` |
| SLAVEOF | Make the server a replica of another instance, or promote it as master | `SLAVEOF host port` |
| REPLICAOF | Make the server a replica of another instance, or promote it as master | `REPLICAOF host port` |
| SLOWLOG | Manages the Redis slow queries log | `SLOWLOG GET` |
| SMEMBERS | Get all the members in a set | `SMEMBERS myset` |
| SMISMEMBER | Check existence of members in a set | `SMISMEMBER myset "one" "two"` |
| SMOVE | Move a member from one set to another | `SMOVE set1 set2 "one"` |
| SORT | Sort the elements in a list, set, or sorted set | `SORT mylist ALPHA` |
| SPOP | Remove and return one or multiple random members from a set | `SPOP myset` |
| SRANDMEMBER | Get one or multiple random members from a set | `SRANDMEMBER myset 2` |
| SREM | Remove one or more members from a set | `SREM myset "one"` |
| STRLEN | Get the length of the value stored in a key | `STRLEN mykey` |
| SUBSCRIBE | Listen for messages published to the given channels | `SUBSCRIBE channel1` |
| SUNION | Add multiple sets | `SUNION set1 set2` |
| SUNIONSTORE | Add multiple sets and store the resulting set in a key | `SUNIONSTORE destination set1 set2` |
| SWAPDB | Swaps two Redis databases | `SWAPDB index1 index2` |
| SYNC | Internal command used for replication | `SYNC` |
| TIME | Return the current server time | `TIME` |
| TOUCH | Alters the last access time of a key(s)

 | `TOUCH key1 key2` |
| TTL | Get the time to live for a key | `TTL mykey` |
| TYPE | Determine the type stored at key | `TYPE mykey` |
| UNSUBSCRIBE | Stop listening for messages posted to the given channels | `UNSUBSCRIBE channel1` |
| UNLINK | Delete a key asynchronously in another thread | `UNLINK mykey` |
| UNWATCH | Forget about all watched keys | `UNWATCH` |
| WAIT | Wait for the synchronous replication of all the write commands sent in the context of the current connection | `WAIT 2 5000` |
| WATCH | Watch the given keys to determine execution of the MULTI/EXEC block | `WATCH mykey` |
| XACK | Marks the pending messages of a stream as correctly processed | `XACK mystream mygroup 1526569498047-0 1526569499048-0` |
| XADD | Appends a new entry to a stream | `XADD mystream * field1 "value1" field2 "value2"` |
| XCLAIM | Changes the ownership of a message in a consumer group | `XCLAIM mystream mygroup Alice 3600000 1526569499048-0` |
| XDEL | Removes one or more messages from a stream | `XDEL mystream 1526569498047-0 1526569499048-0` |
| XGROUP CREATE | Creates a new consumer group | `XGROUP CREATE mystream mygroup $ mkstream` |
| XGROUP SETID | Sets the last delivered ID of a consumer group | `XGROUP SETID mystream mygroup 1526569499048-0` |
| XINFO STREAM | Returns general information about the stream stored at the specified key | `XINFO STREAM mystream` |
| XINFO GROUPS | Returns the number of consumers in a consumer group, and the pending messages | `XINFO GROUPS mystream` |
| XINFO CONSUMERS | Returns the consumers list of a specific consumer group | `XINFO CONSUMERS mystream mygroup` |
| XLEN | Returns the number of entries in a stream | `XLEN mystream` |
| XPENDING | Returns information on pending messages for a given consumer group | `XPENDING mystream mygroup` |
| XRANGE | Returns the range of elements in a stream | `XRANGE mystream - + COUNT 2` |
| XREAD | Reads data from one or multiple streams, only returning entries with an ID greater than the last received ID reported by the caller | `XREAD COUNT 2 STREAMS mystream 0` |
| XREADGROUP | Reads data from a stream for a specific consumer group, only returning entries with an ID greater than the last received ID reported by the caller | `XREADGROUP GROUP mygroup Alice COUNT 2 STREAMS mystream >` |
| XREVRANGE | Returns the range of elements in a stream, with IDs ordered from high to low | `XREVRANGE mystream + - COUNT 2` |
| XTRIM | Trims the stream to a certain size | `XTRIM mystream MAXLEN 1000` |
| ZADD | Add one or more members to a sorted set, or update its score if it already exists | `ZADD myzset 1 "one"` |
| ZCARD | Get the number of members in a sorted set | `ZCARD myzset` |
| ZCOUNT | Count the members in a sorted set with scores within the given values | `ZCOUNT myzset 0 1` |
| ZINCRBY | Increment the score of a member in a sorted set | `ZINCRBY myzset 2 "one"` |
| ZINTERSTORE | Intersect multiple sorted sets and store the resulting sorted set in a new key | `ZINTERSTORE out 2 zset1 zset2 WEIGHTS 2 3` |
| ZLEXCOUNT | Count the number of members in a sorted set between a given lexicographical range | `ZLEXCOUNT myzset - +` |
| ZPOPMAX | Remove and return members with the highest scores in a sorted set | `ZPOPMAX myzset 2` |
| ZPOPMIN | Remove and return members with the lowest scores in a sorted set | `ZPOPMIN myzset 2` |
| ZRANDMEMBER | Get one or multiple random members from a sorted set | `ZRANDMEMBER myzset 2` |
| ZRANGE | Return a range of members in a sorted set, by index | `ZRANGE myzset 0 -1 WITHSCORES` |
| ZRANGEBYLEX | Return a range of members in a sorted set, by lexicographical range | `ZRANGEBYLEX myzset [alpha [omega` |
| ZREVRANGEBYLEX | Return a range of members in a sorted set, by lexicographical range, ordered from higher to lower strings | `ZREVRANGEBYLEX myzset [omega [alpha` |
| ZRANGEBYSCORE | Return a range of members in a sorted set, by score | `ZRANGEBYSCORE myzset 0 1 WITHSCORES` |
| ZRANK | Determine the index of a member in a sorted set | `ZRANK myzset "one"` |
| ZREM | Remove one or more members from a sorted set | `ZREM myzset "two"` |
| ZREMRANGEBYLEX | Remove all members in a sorted set between the given lexicographical range | `ZREMRANGEBYLEX myzset [alpha [omega` |
| ZREMRANGEBYRANK | Remove all members in a sorted set within the given indexes | `ZREMRANGEBYRANK myzset 0 1` |
| ZREMRANGEBYSCORE | Remove all members in a sorted set within the given scores | `ZREMRANGEBYSCORE myzset 0 1` |
| ZREVRANGE | Return a range of members in a sorted set, by index, with scores ordered from high to low | `ZREVRANGE myzset 0 -1 WITHSCORES` |
| ZREVRANGEBYSCORE | Return a range of members in a sorted set, by score, with scores ordered from high to low | `ZREVRANGEBYSCORE myzset 1 0 WITHSCORES` |
| ZREVRANK | Determine the index of a member in a sorted set, with scores ordered from high to low | `ZREVRANK myzset "one"` |
| ZSCORE | Get the score associated with the given member in a sorted set | `ZSCORE myzset "one"` |
| ZUNIONSTORE | Add multiple sorted sets and store the resulting sorted set in a new key | `ZUNIONSTORE out 2 zset1 zset2 WEIGHTS 2 3` |

