import unittest
import pytest
from app.domain.user import User

class TestUserModel(unittest.TestCase):
     
    def test_create_valid_user(self):
        user = User(email='test@example.com', organization='Test Org')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.organization, 'Test Org')

    def test_create_invalid_user_email(self):
        with pytest.raises(ValueError):
            User(email='invalid', organization='Invalid Org')

if __name__ == '__main__':
    unittest.main()
