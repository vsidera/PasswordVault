#!/usr/bin/env python3.8

from locker import User
from locker import Credentials

def create_user(login,loginkey):
        '''
        Function to create a new user
        '''
        new_user = User(login,loginkey)
        return new_user

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
        
        # print("Great!Please proceed to login")
        # print("Enter username")

        # print(f"Great !What would you like to do { login }?")
        # print('\n')
        
        # while True:
        #             print("Choose a short code : ca - create a new credential, dc - display credentials, fc -find credential, ex -exit credential list ")

        #             short_code = input().lower()


if __name__ == '__main__':

        main()