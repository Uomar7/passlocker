class User:
    '''
    class to creates instances of class User.
    '''
    user_list = []

    def save_user(self):
        '''
        save user method that appends objects to our user_list list.
        '''
        
        User.user_list.append(self)
    
    def delete_user(self):
        '''
        method to delete user from the user list.
        '''
        User.user_list.remove(self)
    

    def __init__(self,first_name,last_name,password,email):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
    
    @classmethod
    def find_by_name(cls,first_name):
        '''
        method to locate a user account using the users first name.
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return user
    @classmethod
    def confirm_user(cls,first_name,last_name,password):
        '''
        method to confirm the availability of user.
        '''
        for user in cls.user_list:
            if user.first_name == first_name and user.password == password and user.last_name == last_name:
                return user
        
        return False


    @classmethod
    def display_users(cls):
        '''
        method that returns the user list.
        '''
        return cls.user_list
    
    @classmethod
    def user_exists(cls,last_name):
        '''
        test to check if a user exists in our users list.
        '''
        for user in cls.user_list:
            if user.last_name == last_name:
                return True
        
        return False

class Credentials:
    '''
    class that generates new credentials objects.
    '''
    credentials_list = []
    
    def __init__(self,user_name,account_name,site_name,site_password):

        self.user_name = user_name
        self.account_name = account_name
        self.site_name = site_name
        self.site_password = site_password
    
    def save_credentials(self):
        '''
        function to save a user credentials
        '''

        Credentials.credentials_list.append(self)
    
    def delete_credentials(self):
        '''
        functions to delete credentials from the list of credentials.
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
    
    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        method to find credentials using the username.
        '''
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                return credential
    


