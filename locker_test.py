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
        
if __name__ == '__main__':
    unittest.main()    