Start Sql: sudo service mysql start

## break to from beginning
sudo apt update
sudo apt upgrade
sudo apt install mysql-server
```
sudo apt install mysql-client
```
```
sudo mysql_secure_installation
```
then strat the sql

2. Enter your password and answer **`Y`** when asked if you want to continue setting up the **`VALIDATE PASSWORD`** component. The component checks to see if the new password is strong enough.

3. Choose one of the **three levels** of password validation:

-   **`0` - Low**. A password containing at least 8 characters.
-   **`1` - Medium**. A password containing at least 8 characters, including numeric, mixed case characters, and special characters.
-   **`2` - Strong**. A password containing at least 8 characters, including numeric, mixed case characters, and special characters, and compares the password to a dictionary file.

Enter **`0`**, **`1`**, or **`2`** depending on the password strength you want to set. The script then instructs you to enter your password and re-enter it afterward to confirm.

Any subsequent MySQL user passwords **need to match your selected password strength**.

The program estimates the strength of your password and requires confirmation to continue.

4. Press **`Y`** if you are happy with the password or any other key if you want a different one.

![MySQL password validation script estimates password strength.](https://phoenixnap.com/kb/wp-content/uploads/2021/06/mysql-estimates-password-strength.png)

5. The script then prompts for the following security features:

-   Remove anonymous users?
-   Disallow root login remotely?
-   Remove test database and access to it?
-   Reload privilege tables now?

details on this site:  [How to Install MySQL on Ubuntu 20.04 {5-Step Process} (phoenixnap.com)](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)

step by step explain: [SQL CREATE TABLE Statement (With Examples) (programiz.com)](https://www.programiz.com/sql/create-table)
