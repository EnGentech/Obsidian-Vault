Certainly, here is the table with an extended description column:

| Command                          | Description                                                                                                                                | Example Usage                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| use                              | Switch to a specific database. This command is used to select a database to work with.                                                     | use mydatabase                                                                                         |
| show dbs                         | Show a list of databases available on the MongoDB server.                                                                                  | show dbs                                                                                               |
| show collections                 | Display all the collections in the current database.                                                                                       | show collections                                                                                       |
| db.collection.insertOne()        | Insert a single document into a collection. This method is used to add a new document to the specified collection.                         | db.myCollection.insertOne({ key: value })                                                              |
| db.collection.find()             | Retrieve documents from a collection. This method returns documents that match the specified query criteria.                               | db.myCollection.find()                                                                                 |
| db.collection.updateOne()        | Update a single document in a collection. It modifies an existing document in the collection that matches the specified filter.            | db.myCollection.updateOne({ filter }, { update })                                                      |
| db.collection.deleteOne()        | Delete a single document from a collection. This method removes a single document from the collection that matches the specified query.    | db.myCollection.deleteOne({ filter })                                                                  |
| db.dropDatabase()                | Delete the current database. This command is used to remove the current database from the MongoDB server.                                  | db.dropDatabase()                                                                                      |
| db.collection.insertMany()       | Insert multiple documents into a collection. This method adds multiple documents to the specified collection at once.                      | db.myCollection.insertMany([{ document1 }, { document2 }])                                             |
| db.collection.find().pretty()    | Display the results of a find() operation in a formatted way. The `.pretty()` method formats the output for better readability.            | db.myCollection.find().pretty()                                                                        |
| db.collection.updateMany()       | Update multiple documents in a collection. It modifies multiple documents in the collection that match the specified filter.               | db.myCollection.updateMany({ filter }, { update })                                                     |
| db.collection.deleteMany()       | Delete multiple documents from a collection. This method removes all the documents from the collection that match the specified query.     | db.myCollection.deleteMany({ filter })                                                                 |
| db.createCollection()            | Create a new collection. This command is used to create a new collection in the current database.                                          | db.createCollection("newCollection")                                                                   |
| db.dropCollection()              | Drop a collection. It deletes the specified collection from the current database.                                                          | db.myCollection.drop()                                                                                 |
| db.createUser()                  | Create a new user. This command is used to create a new user with specified roles and privileges for a specific database.                  | db.createUser({ user: "username", pwd: "password", roles: [{ role: "readWrite", db: "myDatabase" }] }) |
| db.dropUser()                    | Drop a user. This command is used to remove a user from the database.                                                                      | db.dropUser("username")                                                                                |
| db.createIndex()                 | Create an index on a collection. This method creates an index on a specified field to improve the performance of queries.                  | db.myCollection.createIndex({ key: 1 })                                                                |
| db.collection.aggregate()        | Perform aggregation operations on a collection. This method processes data records and returns computed results.                           | db.myCollection.aggregate([{ $group: { _id: "$field", total: { $sum: 1 } } }])         g               |
| db.collection.count()            | Count the number of documents in a collection. This command returns the total count of documents in the specified collection.              | db.myCollection.count()                                                                                |
| db.collection.distinct()         | Find the distinct values for a specified field across a collection. This method returns an array of unique values for the specified field. | db.myCollection.distinct("field")                                                                      |
| db.collection.renameCollection() | Rename a collection. This command renames the specified collection to a new name.                                                          | db.myCollection.renameCollection("newCollectionName")                                                  |
| db.collection.stats()            | Retrieve statistics about a collection. This method provides various statistics regarding the collection size, storage, and index usage.   | db.myCollection.stats()                                                                                |
| db.collection.getIndexes()       | Retrieve a list of indexes for a collection. This command returns a list of all the indexes created on the specified collection.           | db.myCollection.getIndexes()                                                                           |


## Research addition
| db.collection.find().sort({value: 1}) | this will search this content in ascending order | sort({value: -1}) sorts in reverse order |
| ------------------------------------- | ------------------------------------------------ | ---------------------------------------- |


## Methods combinations
| limit function       | db.collection.find().limit(number of limit e.g 1) |                              |
| -------------------- | ------------------------------------------------- | ---------------------------- |
| sort and limit       | db.collection.find().sort({name:-1}).limit(2)     | sort and print the first two |
| find specific        | db.collection.find({key:value})                   | find if key matches          |
| in the above you can | have multiple search criteria within the function |                              |
| projection parameter | db.collection.find({},{__dict__ here})            |                              |
|                      |                                                   |                              |


## updating in mongodb.
Assuming our collection is students and we wish to update a certain student named Gentle, we could use the updateOne method with the syntax db.student.updateOne(filter, update)
then we use the $set method to update the value for instance
```mongodb
db.students.updateOne({name:'Gentle'}, {$set:{fullTime: true}})

to remove the field, use the unset keyword and set the value to empty like

db.students.updateOne({name:'Gentle'}, {$unset:{fullTime: ""}})
```

### updating many fields
its almost the same thing above
```mongodb
db.students.updateMany({}, {$set:{fulltime:false}})
```

to set a value on a criteria, lets say we want to set fulltime option to true to every student who didnt have that field validated.
```mongodb
db.students.updateMany({fulltime:{$exists}}, {$set:{fulltime:true}})
```