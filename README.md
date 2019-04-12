# Python Password Vault Application

## About Application
This Python application will help you to manage your passwords and even generate new passwords. On Average, a person has at least 7 different accounts he or she has signed into, be it email, social media, entertainment or job portal accounts. It becomes really hard to remember all those passwords and even create new ones. As a user, you will be able to create a password locker account with your details, a login username and password, store already existing account credentials in the application, store already existing account username and password in the application, create new account credentials, create a credentials account and the application generates a password for you to use when you sign up for an account, have the option of putting in a password that you want to use for the new credential account, view various account credentials and their passwords in the application and delete a credentials account that you no longer need in the application.

## User Stories
These are the behaviours/features that the application implements for use by a user.
As a user, you will be able to:
- To create an account with your details - log in and password
- Store your existing login credentials
- Generate a password for a new credential/account
- Copy your credentials to the clipboard

## Set-ip/Installation Requirements
- python3.6
- pip
- pyperclip
- Terminal/Command Line Interface

## Cloning
In your terminal/CLI:
-   $ git clone https://github.com/jameskomo/password-locker/
-   $ cd Password-Locker
## Running the Application
To run the application, in your terminal:

```sh
  $ chmod +x ./run.py //To make the file executable in your machine
  OR
  $ ./run.py
  ```
  

### Technologies Used

- [Python3.6](https://www.python.org)
- [Pyperclip module](https://pypi.org/project/pyperclip/)


### Tests
Test Driven Approach has been used in this application. Python Uniittesting framework has been used in the test cases. For testing, run the following command in terminal:
```sh
    python3.6 test_password_locker.py
```



### Test & Behaviour Driven Development(BDD & TDD)

| Behaviour                                   | Input                              | Output                                                                                                |
|---------------------------------------------|------------------------------------|-------------------------------------------------------------------------------------------------------|
| Display codes for navigation                | In terminal: $./run.py | Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit                                      |
| Display prompt for creating an account      | Enter: ca                          | Enter your first name, last name and password                                                         |
| Display prompt for login in                 | Enter: li                          | Enter your account name and password                                                                  |
| Display codes for navigation                | Successful login                   | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential    | Enter: cc                          | Enter the site name, your username and password                                                       |
| Display a list of credentials               | Enter: dc                          | Prints a list of saved credentials                                                                    |
| Display prompt for which credential to copy | Enter: cp                        | Enter the site name of the credential you wish to copy.                                               |
| Exit application                            | Enter: ex                          | Exit the current navigation stage                                                                     |



### Known Bugs
There are no known bugs but in case you come across any feel free to contact me on james.komoh@gmail.com.

## LICENSE

Visit this [Link](https://github.com/jameskomo/password-locker/blob/master/LICENSE) for license information

