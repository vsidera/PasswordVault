#!/usr/bin/env python3.8

from locker import User
from locker import Credentials

def create_user(login,loginkey):
        '''
        Function to create a new user
        '''
        new_user = User(login,loginkey)
        return new_user

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
