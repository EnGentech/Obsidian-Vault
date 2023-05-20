run sql CLI: 
```sql
mysql -u root -p
```
creatin a user statement
```sql
CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
```
After `CREATE USER`, you specify a username. This is immediately followed by an `@` sign and then the hostname from which this user will connect. If you only plan to access this user locally from your Ubuntu server, you can specify `localhost`. Wrapping both the username and host in single quotes isn’t always necessary, but doing so can help to prevent errors.

You have several options when it comes to choosing your user’s authentication plugin. The `auth_socket` plugin mentioned previously can be convenient, as it provides strong security without requiring valid users to enter a password to access the database. But it also prevents remote connections, which can complicate things when external programs need to interact with MySQL.

As an alternative, you can leave out the `WITH authentication_plugin` portion of the syntax entirely to have the user authenticate with MySQL’s default plugin, `caching_sha2_password`. [The MySQL documentation recommends this plugin](https://dev.mysql.com/doc/refman/8.0/en/upgrading-from-previous-series.html#upgrade-caching-sha2-password) for users who want to log in with a password due to its strong security features.

Run the following command to create a user that authenticates with `caching_sha2_password`. Be sure to change `sammy` to your preferred username and `password` to a strong password of your choosing:
```sql
CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';
```
**Note**: There is a known issue with some versions of PHP that causes problems with `caching_sha2_password`. If you plan to use this database with a PHP application — phpMyAdmin, for example — you may want to create a user that will authenticate with the older, though still secure, `mysql_native_password` plugin instead:

```sql
CREATE USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```


If you aren’t sure, you can always create a user that authenticates with `caching_sha2_plugin` and then `ALTER` it later on with this command:

```sql
ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

## Granting permission for users
```sql
GRANT PRIVILEGE ON database.table TO 'username'@'host';
```
The `PRIVILEGE` value in this example syntax defines what actions the user is allowed to perform on the specified `database` and `table`. You can grant multiple privileges to the same user in one command by separating each with a comma. You can also grant a user privileges globally by entering asterisks (`*`) in place of the database and table names. In SQL, asterisks are special characters used to represent “all” databases or tables.

To illustrate, the following command grants a user global privileges to `CREATE`, `ALTER`, and `DROP` databases, tables, and users, as well as the power to `INSERT`, `UPDATE`, and `DELETE` data from any table on the server. It also grants the user the ability to query data with `SELECT`, create foreign keys with the `REFERENCES` keyword, and perform `FLUSH` operations with the `RELOAD` privilege. However, you should only grant users the permissions they need, so feel free to adjust your own user’s privileges as necessary.

You can find the full list of available privileges in [the official MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#privileges-provided-summary).

Run this `GRANT` statement, replacing `sammy` with your own MySQL user’s name, to grant these privileges to your user:

```sql
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;
```

Note that this statement also includes `WITH GRANT OPTION`. This will allow your MySQL user to grant any permissions that it has to other users on the system.
```sql
FLUSH PRIVILEGES;
```
However, according to the [official MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/privilege-changes.html), when you modify the grant tables indirectly with an account management statement like `GRANT`, the database will reload the grant tables immediately into memory, meaning that the `FLUSH PRIVILEGES` command isn’t necessary in our case. On the other hand, running it won’t have any negative effect on the system.

If you need to revoke a permission, the structure is almost identical to granting it:

```sql
REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';
```

Note that when revoking permissions, the syntax requires that you use `FROM`, instead of `TO` which you used when granting the permissions.

You can review a user’s current permissions by running the `SHOW GRANTS` command:

```sql
SHOW GRANTS FOR 'username'@'host';
```

Just as you can delete databases with `DROP`, you can use `DROP` to delete a user:

```sql
DROP USER 'username'@'localhost';
```

After creating your MySQL user and granting them privileges, you can exit the MySQL client:

```sql
exit
```

In the future, to log in as your new MySQL user, you’d use a command like the following:

```sql
mysql -u sammy -p
```

The `-p` flag will cause the MySQL client to prompt you for your MySQL user’s password in order to authenticate.

## [Conclusion](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql#conclusion)[](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql#conclusion)

By following this tutorial, you’ve learned how to add new users and grant them a variety of permissions in a MySQL database. From here, you could continue to explore and experiment with different permissions settings for your MySQL user, or you may want to learn more about some higher-level MySQL configurations.

For more information about the basics of MySQL, you can check out the following tutorials: