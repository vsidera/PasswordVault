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

        '''
        save_contact method saves contact objects into contact_list
        '''

        Credentials.credentials_list.append(self)   