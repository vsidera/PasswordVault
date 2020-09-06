#!/usr/bin/env python3.8

from locker import User
from locker import Credentials

def create_user(login,loginkey):
        '''
        Function to create a new user
        '''
        new_user = User(login,loginkey)
        return new_user

def create_credentials(account,username,password):
        """
        Function to create new credentials
        """
        new_credentials = Credentials(account,username,password)
        return new_credentials        

def save_user(user):
        '''
        Function to save credentials
        '''
        user.save_user()

def save_credentials(credentials):
        '''
        Function to save credentials
        '''
        credentials.save_credentials()

def generate_password():
    '''
    function to generate a password
    '''
    random_password = Credentials.password_generate()
    return random_password        

def del_credentials(credentials):
        '''
        Function to delete a credential
        '''
        credentials.delete_credentials()

def find_credentials(account):
        '''
        Function that finds a credential by number and returns the credential
        '''
        return Credentials.find_by_account(account)

def display_credentials():
        '''
        Function that returns all the saved credentials
        '''
        return Credentials.display_credentials()  

#MAINFUNCTION

def main() :
        print("Hi!This is Password Vault.Set a username")
        login = input()
        print("set a password")
        loginkey = input()
        
        save_user(create_user(login, loginkey))

        print(f"Great!{login}, please enter your password again to login.")
        confirm = input()
        if confirm == loginkey:
            print("\n You are successfully logged in!") 

            while True:
                        print("-"*10)
                        print("What would you like to do? \n Pick a short code : \n \t\t aa - Add an account & create your password \n \t\t ga - Generate a password for your new account \n \t\t dc - display saved accounts \n \t\t sa - Search for an account \n \t\t D - delete an account \n \t\t ex - Exit the locker room ")
                        short_code = input().lower()
        
                        if short_code == 'aa':
                            print("-"*10)
                            print("Enter account name")
                            print("Account name ....(eg: facebook)")
                            account = input()
                            print("Create username")
                            username = input()
                            print("Create password")
                            password = input()
                            save_credentials(create_credentials(account, username, password))
                            print ('\n')
                            print(f"New account: {account} added \n Username: {username} --- Password:{password}")
                            print ('\n')
                        
                        elif short_code == 'ga':
                            print("-"*10)
                            print("Ente account name")
                            account = input()
                            print("Enter username")
                            username = input()
                            print("...........")
                            password = generate_password()
                            save_credentials(create_credentials(account, username, password))
                            print ('Your account has been created successfully!\n')
                            print(f"New account: {account} \n Username: {username} --- Password:{password}")
                            print ('\n')

                        elif short_code == 'dc':

                                if display_credentials():
                                        print("Here is a list of all your accounts")
                                        print('\n')

                                        for credentials in display_credentials():
                                                print(f"{credentials.account} {credentials.username} .....{credentials.password}")

                                        print('\n')
                                else:
                                        print('\n')
                                        print("You dont seem to have any accounts saved yet")
                                        print('\n')

                        elif short_code == 'sa':

                                print("Enter the account you want to search for")

                                account = input()
                                if find_credentials(account):
                                        account = find_credentials(account)
                                        print(f"{account.username} {account.password}")
                                        print('-' * 10)
                                        
                                else:
                                        print("That contact does not exist")

                        elif short_code == 'd':
                            print("-"*10)
                            print("Enter the account you would like to delete")
                            account = input()
                            if find_credentials(account):
                                del_credentials(find_credentials(account))
                                print("-"*10)
                                print("The account has been deleted successfully")

                        elif short_code == "ex":
                                print("See you later :)")
                                break
                        else:
                                print("I really didn't get that. Please use the short codes")

        else:
                print("-"*10)
                print("\nSorry,Wrong password.Try again")                        

if __name__ == '__main__':

        main()