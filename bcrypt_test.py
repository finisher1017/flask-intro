import flask
from flask_bcrypt import (Bcrypt,
                          check_password_hash,
                          generate_password_hash,
                          PY3)

def test_check_hash(self):
        pw_hash = self.bcrypt.generate_password_hash('secret')
        # check a correct password
        self.assertTrue(self.bcrypt.check_password_hash(pw_hash, 'secret'))
        # check an incorrect password
        self.assertFalse(self.bcrypt.check_password_hash(pw_hash, 'hunter2'))
        # check unicode
        pw_hash = self.bcrypt.generate_password_hash(u'\u2603')
        self.assertTrue(self.bcrypt.check_password_hash(pw_hash, u'\u2603'))
        # check helpers
        pw_hash = generate_password_hash('hunter2')
        self.assertTrue(check_password_hash(pw_hash, 'hunter2'))