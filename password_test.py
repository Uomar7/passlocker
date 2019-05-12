import unittest
from password import User

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
        test_user = test_user = User('code','python','errorperience','code.python@pyode.com')
        test_user.save_user()
        found_user = User.find_by_name('code.python@pyode.com')
        self.assertEqual(found_user.first_name,test_user.first_name)

if __name__ == '__main__':
    unittest.main()