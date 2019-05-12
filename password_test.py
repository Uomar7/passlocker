import unittest
from password import User

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: Test class that helps in creating test cases.
    '''
    user_list = []
    
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
        self.assertEqual(len(user_list),1)




if __name__ == '__main__':
    unittest.main()