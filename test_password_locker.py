import unittest  # Importing the unittest module
from user import User  # Importing the user class
from credential import Credential  # Importing the credential class
import pyperclip  # Pyperclip module to allow copy pasting


# TESTING USER CLASS METHODS


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    @classmethod
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Admin", "1234",)

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name, "Admin")
        self.assertEqual(self.new_user.user_password, "1234")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user()  # saving the new contact
        self.assertEqual(len(User.user_list), 1)

        # setup and class creation up here

# setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_user.save_user()
        test_user = User("User", "0001")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("User2", "0002")  # new user
        test_user.save_user()

        self.new_user.delete_user()  # Deleting a contact object
        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("User3", "0003")  # new user
        test_user.save_user()

        found_user = User.find_user_by_username("User3")

        self.assertEqual(found_user.user_name, test_user.user_name)

# TESTING CREDENTIAL CLASS METHODS


class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    @classmethod
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("FB", "Admin", "0001")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name, "FB")
        self.assertEqual(self.new_credential.account_username, "Admin")
        self.assertEqual(self.new_credential.account_password, "0001")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
        the cerdential list
        '''
        self.new_credential.save_credential()  # saving the new contact
        self.assertEqual(len(Credential.credential_list), 7)

        # setup and class creation up here

# setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.ceredential_list = []

# other test cases here
    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("FB", "Admin", "0001")  # new user
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 9)

    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("FB", "Admin", "0001")  # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()  # Deleting a contact object
        self.assertEqual(len(Credential.credential_list), 1)

    def test_display_credential(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credential()
        test_credential1 = Credential('Snapchat', 'User5', 'pswd02')
        test_credential1.save_credential()
        test_credential2 = Credential('Skype', 'User12', 'pswd123')
        test_credential2.save_credential()
        self.assertEqual(
            len(Credential.display_credential(test_credential1.account_username)), 1)

    def test_find_credential_by_name(self):
        '''
        Test to check if the find_by_account_name method returns the correct Account
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", 'User4', 'pswd001')
        test_credential.save_credential()
        found_credential = Credential.find_credential_by_name('Twitter')
        self.assertEqual(found_credential.account_name,
                         test_credential.account_name)

    def test_copy_account_username(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_credential.save_credential()
        Credential.copy_account_username("FB")

        self.assertEqual(self.new_credential.account_username,
                         pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
