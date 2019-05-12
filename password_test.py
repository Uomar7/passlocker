import unittest
from password import User, Credentials

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: Test class that helps in creating test cases.
    '''

    def tearDown(self): # tearDown method to clean up after every test has been run.

        User.user_list = []
    
    def setUp(self):
        '''
        set uf method to run before evry test.
        '''

        self.new_user = User('Uomar','Earlie','Shaaddyyy','uomar.earlie@imperial.com')

    def test_init(self):
        '''
        test init test case to test if the object is initialized properly.
        '''
        self.assertEqual(self.new_user.first_name,'Uomar')
        self.assertEqual(self.new_user.last_name,'Earlie')
        self.assertEqual(self.new_user.password,'Shaaddyyy')
        self.assertEqual(self.new_user.email,'uomar.earlie@imperial.com')
    
    def test_save_user(self):
        '''
        A test to test if the user  is saved into the list.
        '''
        self.new_user.save_user()   #saving new users to our user list.
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_user(self):
        '''
        test to check if the app saves multiple users.
        '''
        self.new_user.save_user()
        test_user = User('code','python','errorperience','code.python@pyode.com')
        
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test to check if the app can delete a user from our user list. 
        '''

        self.new_user.save_user()
        test_user = User('code','python','errorperience','code.python@pyode.com')
        test_user.save_user()
        self.new_user.delete_user() #deleting a user from our user list.
        self.assertEqual(len(User.user_list),1)

    def test_find_by_first_name(self):
        '''
        test to search and find an account using the first name.
        '''
        self.new_user.save_user()
        test_user = User('code','python','errorperience','code.python@pyode.com')
        test_user.save_user()

        found_user = User.find_by_name('code')
        self.assertEqual(found_user.first_name,test_user.first_name)
    
    def test_display_users(self):
        '''
        test to check if the app will return a list of all the user registered.
        '''
        self.assertEqual(User.display_users(),User.user_list)

    def test_user_exists(self):
        '''
        test to return a boolean whether a contact exists or not.
        '''
        self.new_user.save_user()
        test_user = User('code','python','errorperience','code.python@pyode.com')
        test_user.save_user()
        
        user_exists = User.user_exists('python')
        self.assertTrue(user_exists)

class Test_Credentials(unittest.TestCase):
    '''
    test to define all credentials class instances.
    '''
    def tearDown(self): # tearDown method to clean up after every test has been run.

        Credentials.credentials_list = []

    def setUp(self):
        '''
        function to create user account before each test
        '''
        self.new_credentials = Credentials('whaat!','Waasuup','instanglam','whaashanglam')

    def test_credentials_init(self):
        self.assertEqual(self.new_credentials.user_name,'whaat!')
        self.assertEqual(self.new_credentials.account_name,'Waasuup')
        self.assertEqual(self.new_credentials.site_name,'instanglam')
        self.assertEqual(self.new_credentials.site_password,'whaashanglam')
    
    def test_save_credentials(self):
        '''
        test to check the saving functionality of credentials instances.
        '''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_save_multiple_credentials(self):
        '''
        test to check if the app saves multiple credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials('code','python','fb','cofthon')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test to check deletion of credentials
        '''

        self.new_credentials.save_credentials()
        test_Credentials = Credentials('code','python','fb','cofthon')
        test_Credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    
    def test_display_credentials(self):
        '''
        test to display all the available credentials.
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_find_user_name(self):
        '''
        function to find user credentials using by User name
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials('code','python','fb','cofthon')
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_user_name('code')
        self.assertEqual(found_credentials,test_credentials)
    

if __name__ == '__main__':
    unittest.main()