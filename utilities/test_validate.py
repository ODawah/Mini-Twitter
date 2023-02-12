import unittest
import validate
import hasher


class TestUUIDValidator(unittest.TestCase):
    def test_validate_uuid(self):
        self.assertIs(validate.validate_uuid("c303282d-f2e6-46ca-a04a-35d3d873712d"), True)
        self.assertIs(validate.validate_uuid("c303282d-2e6-46ca-a04a-35d3d873712d"), False)
        self.assertIs(validate.validate_uuid(""), False)


class TestPasswordValidator(unittest.TestCase):
    def test_validate_pass(self):
        hashed = hasher.encrypt("test_password")
        self.assertIs(validate.validate_pass("test_password", hashed), True)
        self.assertIs(validate.validate_pass("not_the_ssame_password", hashed), False)
        self.assertIs(validate.validate_pass("", hashed), False)


if __name__ == '__main__':
    unittest.main()
