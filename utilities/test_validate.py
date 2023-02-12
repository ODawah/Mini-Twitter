import unittest
import validate
import hasher


class TestUUIDValidator(unittest.TestCase):
    def test_validate_uuid(self):
        self.assertIs(validate.is_valid_uuid("c303282d-f2e6-46ca-a04a-35d3d873712d"), True)
        self.assertIs(validate.is_valid_uuid("c303282d-2e6-46ca-a04a-35d3d873712d"), False)
        self.assertIs(validate.is_valid_uuid(""), False)


class TestPasswordValidator(unittest.TestCase):
    def test_validate_pass(self):
        hashed = hasher.encrypt("test_password")
        self.assertIs(validate.is_valid_pass("test_password", hashed), True)
        self.assertIs(validate.is_valid_pass("not_the_ssame_password", hashed), False)
        self.assertIs(validate.is_valid_pass("", hashed), False)


class TestNameValidator(unittest.TestCase):
    def test_validate_name(self):
        long_str = "adgsakmdsakgmdfklsddmfalkdmsflkmdfklsdmffdassodfdfs"
        self.assertIs(validate.is_valid_user_name(long_str), False)
        self.assertIs(validate.is_valid_user_name(""), False)
        self.assertIs(validate.is_valid_user_name("test"), True)


class TestEmailValidator(unittest.TestCase):
    def test_validate_name(self):
        self.assertIs(validate.is_valid_email("test@gmail.com"), True)
        self.assertIs(validate.is_valid_email(""), False)
        self.assertIs(validate.is_valid_email("@sdfsd@gmil.coz"), False)


if __name__ == '__main__':
    unittest.main()
