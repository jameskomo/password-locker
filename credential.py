# CREDENTIAL CLASS
import pyperclip
import string
import random


class Credential:
    """
    Class that generates new instances of Credentials.
    """

    credential_list = []  # Empty contact list

    def __init__(self, account_name, account_username, account_password):

        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    def save_credential(self):
        '''
        credential method saves credential objects into credential_list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes a saved credential from the credential_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def display_credential(cls, account_username):
        '''
        Class method to display the list of credentials saved
        '''
        user_credential_list = []
        for credential in cls.credential_list:
            if credential.account_username == account_username:
                user_credential_list.append(credential)
        return user_credential_list

    @classmethod
    def find_credential_by_name(cls, account_name):
        '''
        Method that takes in an account_name and returns a credential that matches that account_name.
        '''
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def copy_account_username(cls, account_username):
        '''
        Class method that copies a credential's username after the credential account name is entered
        '''
        find_credential = Credential.copy_account_username(account_username)
        return pyperclip.copy(find_credential.account_username)

    @classmethod
    def password_generator(size):
        '''
        Function to generate an 8 character password for a credential
        '''
        size = int(input("Enter the preferred password size"))
        characters = string.ascii_uppercase+string.ascii_lowercase+string.digits
        account_password = ''.join(random.choice(characters)
                                   for _ in range(8, size))
        return account_password
