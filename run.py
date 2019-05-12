#!/usr/bin/env python3.6
from password import User, Credentials

def create_account(fname,lname,password,mail):
    '''
    Function to create a new user
    '''
    new_account = User(fname,lname,password,mail)
    return new_account

def save_account(account):
    '''
    function to save account user.
    '''
    account.save_user()

def delete_account(account):
    '''
    function to dekete user account
    '''
    account.delete_user()
 
 def display_accounts():
     '''
     function to display all user accounts.
     '''
     return User.display_users()
    
def account_verification(first_name,password):
    '''
    function to verify an account login.
    '''
    verified_user = Credentials.confirm_user(first_name,password)
    return verified_user
