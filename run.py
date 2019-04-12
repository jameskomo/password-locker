#!/usr/bin/env python3.6
from user import User
from credential import Credential
import string
import random


def create_user(user_name, user_password):
    '''
    Function to create a new user account
    '''
    new_user = User(user_name, user_password)
    return new_user


def save_user(user):
    '''
    Function to save a new user account
    '''
    return User.save_user(user)


def verify_user(user_name, user_password):
    '''
    Function that verifies the existance of the user before creating credential
    '''
    checking_user = User.check_user(user_name, user_password)
    return checking_user


def generate_password():
    '''
    # Function to generate a password automatically
    '''
    gen_pass = Credential.password_generator()
    print("Your generated password is "+gen_pass+"")
    return gen_pass


def create_credential(account_name, account_username, account_password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(
        account_name, account_username, account_password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    return Credential.save_credential(credential)


def display_credential(account_name):
    '''
    Function to display credential saved by a user
    '''
    return Credential.display_credential(account_name)


def delete_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()


def copy_credential(account_username):
    '''
    Function to copy a credential details to the clipboard
    '''
    return Credential.copy_account_username(account_username)


def main():
    print(' ')
    print('Hello! Welcome to Password Vault.')
    while True:
        print(' ')
        print("*"*100)
        print(
            'Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("*"*100)
            print(' ')
            print('To create a new account:')
            user_name = input('Enter your user name - ').strip()
            user_password = input('Enter your user password - ').strip()
            save_user(create_user(user_name, user_password))
            print(" ")
            print(
                f'New Account Created for: {user_name} using password: {user_password}')
        elif short_code == 'li':
            print("*"*100)
            print(' ')
            print('Enter your account credentials to login:')
            user_name = input('Enter your username --- ').strip()
            user_password = str(input('Enter your password --- '))
            user_exists = verify_user(user_name, user_password)
            if user_exists == user_name:
                print(" ")
                print(
                    f'Welcome {user_name}. Please choose an option to continue.')
                print(' ')
                while True:
                    print("-"*60)
                    print(
                        'Navigation codes: \n cc-Create an account Credential \n dc-Display credential \n cp-Copy Account Username\n del-Delete Credential \n ex-Exit')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Thank you {user_name}. Have a nice time!')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your credential details:')
                        account_name = input(
                            'Enter the Account\'s name- ').strip()
                        account_username = input(
                            'Enter your account\'s username - ').strip()
                        while True:
                            print(' ')
                            print("-"*60)
                            print(
                                'Please choose an option for entering a password: \n ep-create your own password \n gp-generate a password \n ex-exit')
                            password_choice = input(
                                'Enter an option: ').lower().strip()
                            print("-"*60)
                            if password_choice == 'ep':
                                print(" ")
                                account_password = input(
                                    'Enter your preferred password: ').strip()
                                break
                            elif password_choice == 'gp':
                                account_password = generate_password()
                                save_credential(create_credential(
                                    account_name, account_username, account_password))
                                return account_password
                            elif password_choice == 'ex':
                                break
                            else:
                                print('Oops! Wrong option entered. Try again.')
                                save_credential(create_credential(
                                    account_name, account_username, account_password))
                                print(' ')
                                print(
                                    f'Credential Created: Account Name: {account_name} - Account Name: {account_username} - Password: {account_password}')
                                print(' ')
                    elif short_code == 'dc':
                        print(' ')
                        if display_credential(user_name):
                            print('Here is a list of all your credential')
                            print(' ')
                            for credential in display_credential(user_name):
                                print(
                                    f'account Name: {credential.account_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print(' ')
                        else:
                            print(' ')
                            print("You don't seem to have any credential saved yet")
                            print(' ')
                    elif short_code == 'cp':
                        print(' ')
                        chosen_account = input(
                            'Enter the account name for the credential username to copy: ')
                        copy_credential(chosen_account)
                        print('')

                    elif short_code == 'del':
                        print(
                            "Enter the Account name of the credential you want to delete")
                        find_credential_by_name = input()
                        delete_credential = find_credential_by_name(
                            account_name)
                        delete_credential(delete_credential)
                    else:
                        print('Oops! Wrong option entered. Try again.')

            else:
                print(' ')
                print('Oops! Wrong details entered. Try again or Create an Account.')

        else:
            print("-"*60)
            print(' ')
            print('Oops! Wrong option entered. Try again.')


if __name__ == '__main__':
    main()
