import unittest # Importing the unittest module
from locker import User #Importing the User class
from locker import Credentials #Importing the Credentials class

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("vik","P@pi") # create user object
        self.new_credentials = Credentials("facebook","sidera","Fr1day") #create credentials object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.login,"vik")
        self.assertEqual(self.new_user.loginkey,"P@pi")

        self.assertEqual(self.new_credentials.account,"facebook")
        self.assertEqual(self.new_credentials.username,"sidera")
        self.assertEqual(self.new_credentials.password,"Fr1day") 


    def test_save_credentials(self):
        """
        test_save_credentials test case to test if the credentials object is saved into
         the credential list
        """
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)    

    def test_display_credentials(self):
        """
        method that returns a list of all credentials saved
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_delete_credentials(self):
        """
        test_delete_credentials test case to test if the credentials object is deleted from
         the credential list
        """    
        self.new_credentials.save_credentials() # saving the new credentials
        self.new_credentials.delete_credentials() #deleting credentials
        self.assertEqual(len(Credentials.credentials_list),0)
         
if __name__ == '__main__':
    unittest.main()    