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

#Credentials class
class Credentials :
    """
    Class that creates new instances of credentials
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,account,username,password):

        """
        __init__ method that helps us define properties for our objects.

        Args:
            username : New user username.
            password : New user password.
        """
        self.account = account
        self.username = username
        self.password = password     


    def save_credentials(self):

        """
        save_credentials method saves contact objects into contact_list
        """

        Credentials.credentials_list.append(self)   

    def delete_credentials(self):
        """
        delete_credentials method deletes contact objects from contact_list
        """
        Credentials.credentials_list.remove(self)

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