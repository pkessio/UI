import unittest
import os
import json
from app import register

import sys
import unittest

class MyTestLogin(unittest.TestCase):
    email = ""
    password = ""

    def test_logins_entered(self):
        print ('email', self.email)
        print ('password', self.password)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        MyTestLogin.email = sys.argv.pop()
        MyTestLogin.password = sys.argv.pop()
    unittest.main()