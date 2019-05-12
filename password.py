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
