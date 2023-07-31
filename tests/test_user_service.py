import unittest
from unittest.mock import Mock
from app.domain.user import User
from app.application.user_service import UserService         

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_repository_mock = Mock()
        self.user_service = UserService(self.user_repository_mock)
     
    def test_create_valid_user(self):
        user = User(email='test@example.com', organization='Test Org')
        result = self.user_service.create_user(user)
        
        self.assertEqual(result, user)
        self.user_repository_mock.create_user.assert_called_once_with(user)

if __name__ == '__main__':
    unittest.main()        