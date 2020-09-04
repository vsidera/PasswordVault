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

def del_credentials(credentials):
        '''
        Function to delete a contact
        '''
        credentials.delete_credentials()

def find_credentials(account):
        '''
        Function that finds a contact by number and returns the contact
        '''
        return Credentials.find_by_account(account)

def display_credentials():
        '''
        Function that returns all the saved contacts
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
        # else:
        #     print("Sorry,wrong password")  

         
            while True:
                        print("-"*10)
                        print("What would you like to do? \n Pick a short code : \n \t\t aa - Add an account & create your password \n \t\t ga - Generate a password for your new account \n \t\t da - display saved accounts \n \t\t sa - Search for an account \n \t\t D - delete an account \n \t\t ex - Exit the locker room ")
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

if __name__ == '__main__':

        main()