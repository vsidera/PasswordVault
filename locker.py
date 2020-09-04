class User :
    """
    Class that creates new instances of user
    """
    user_list = [] # Empty user list

    def __init__(self,username,password):

        """
        __init__ method that helps us define properties for our objects.

        Args:
            username : New user username.
            password : New user password.
        """

        self.username = username
        self.password = password