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

def find_account(fname):
    '''
    function to search account.
    '''
    return User.find_by_name(fname)
 
def display_accounts():
     '''
     function to display all user accounts.
     '''
     return User.display_users()
    
def account_verification(first_name,last_name,password):
    '''
    function to verify an account login.
    '''
    return User.confirm_user(first_name,last_name,password)

def create_credentials(user_name,account_name,site_name,site_password):
    '''
    function to create new credentials
    '''
    new_credentials = Credentials(user_name,account_name,site_name,site_password)
    return new_credentials

def save_credentials(credentials):
    '''
    function to save credentials
    '''
    credentials.save_credentials()

def display_credentials():
    '''
    function to display the list of credentials
    '''
    return Credentials.display_credentials()

def find_credentials(user_name):
    '''
    function to search for credentials
    '''
    return Credentials.find_by_user_name(user_name)

def main():
    print('Wellie Welcome to Password Locker. Sign up or login')
    print('\n')

    while True:
        print('use these short to navigate: ca- create a new account, li- login, du- display users, del- delete account, ep- exit password locker')

        short_code = input().lower()

        if short_code == 'ep':
            print('Bye, Humbled to serve you.')

            break
        
        elif short_code == 'ca':
            print("sign-up")
            print('-'*10)

            print('first name....')
            fname = input()

            print('last name....')
            lname = input()

            print('password...')
            password = input()

            print('email...')
            mail = input()

            save_account(create_account(fname,lname,password,mail))
            print('\n')
            print(f'New account {fname} {lname} created')

            print('\n')
        
        elif short_code == 'li':
            print('put first name and password')
            print('enter first name')
            fname = input()
            print('enter last name')
            lname = input()
            print('enter password')
            password = input()

            if account_verification(fname,lname,password):
                search_user = find_account(fname)
                
                print(f'you are logged in {search_user.first_name} {search_user.last_name}')

                while True:
                    print('use short codes to navigate: nc- create new credentials, dc- display credentials, delc- delete credentials,fn- find credentials, ex- log out')
                    short_code = input()
                    if short_code == 'nc':
                        print('create new credentials')
                        print('-'*10)

                        print('username....')
                        user_name = input()

                        print('account name...')
                        account_name = input()

                        print('site name...')
                        site_name = input()

                        print('site password...')
                        site_password = input()

                        save_credentials(create_credentials(user_name,account_name,site_name,site_password))
                        print('\n')
                        print(f'new credentials {user_name} {site_name} created!!')

                    elif short_code == 'dc':

                        if display_credentials():
                            print('Here is a list of all your credentials')

                            print('\n')
                            
                            for credential in display_credentials():
                                print(f'{credential.user_name} {credential.site_name}.......... {credential.site_password}')
                                print('\n')

                                print('\n')
                        
                        else:
                            print('No credentials made yet. type dc- to create credentials')
                        

                    elif short_code == 'delc':

                        print('Enter your credentials username')
                        delete_credential = input()

                        if find_by_user_name(delete_credential):

                            print(f'{search_cred.user_name} {search_cred.account_name} {search_cred.site_name}')
                            print('-'*20)

                            Credentials.credentials_list.remove(search_cred)
                        
                        else:
                            print('no existing credentials')

                    elif short_code == 'fn':
                        print('enter the user_name you want to search for')
                        search_credentials = input()

                        if find_by_user_name(search_credentials) == True:
                            
                            print(f'{credential.user_name} {credential.account_name}')
                            print('-'*30)
                            print(f'{credential.site_name}')
                            print(f'{credential.site_password}')
                        
                        else:
                            print('No such credentials details')

                    elif short_code == 'ex':
                        print('Am Out')
                        break

                            
            else:
                print('you dont have an account with us!')
                break
        
    else:
        print('follow protocol')


if __name__ == '__main__':
    main()
            

            
            

                

        

                