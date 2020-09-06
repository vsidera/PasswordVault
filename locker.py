import random;

class User :
    """
    Class that creates new instances of user
    """
    user_list = [] # Empty user list

    def __init__(self,login,loginkey):

        """
        __init__ method that helps us define properties for our objects.

        Args:
            login : New user login.
            loginkey : New user loginkey.
        """

        self.login = login
        self.loginkey = loginkey

    def save_user(self):

        """
        save_credentials method saves user objects into user_list
        """

        User.user_list.append(self)    

#Credentials class
class Credentials :
    """
    Class that creates new instances of credentials
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,account,username,password=None):

        """
        __init__ method that helps us define properties for our objects.

        Args:
            username : New user username.
            password : New user password.
        """
        self.account = account
        self.username = username
        self.password = password if password else Credentials.password_generate()       

    def save_credentials(self):

        """
        save_credentials method saves credentials objects into credentials_list
        """

        Credentials.credentials_list.append(self)   

    def delete_credentials(self):
        """
        delete_credentials method deletes credential objects from credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def password_generate(cls):
        '''
        class method to generate a random password
        '''
        password_length = 6
        possible_characters = "@abcdefghijklmnopqrstuvwxyz-1234567890&ABCDEFGHIJKLMNOPQRSTUVWXYZ!" 
        random_character = [random.choice(possible_characters) for i in range(password_length)]
        auto_password = "".join(random_character)
        return auto_password    

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in account and returns a credential that matches that account.

        Args:
            account: account to search for
        Returns :
            Credential of person that matches the account.
        '''

        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials        