# USER CLASS
class User:
    """
    Class that generates new instances of users.
    """

    user_list = []  # Empty contact list
    user_credential_list = []  # Empty user account credentials list

    @classmethod
    def check_user(cls, user_name, user_password):
        '''
        Method that checks if the name and password entered match user's credentials in the users_list
        '''
        current_user = ''
        for user in User.user_list:
            if (user.user_name == user_name and user.user_password == user_password):
                current_user = user.user_name
        return current_user

    def save_user(self):
        '''
        user method saves user objects into user_list
        '''
        User.user_list.append(self)
    # Initializing User method  here
    def __init__(self, user_name, user_password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.user_password = user_password

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_user_by_username(cls, name):
        '''
        Method that takes in a username and returns a user that matches that username
        '''

        for user in cls.user_list:
            if user.user_name == name:
                return user


# USER CLASS METHODS
