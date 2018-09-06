import unittest
from flask_testing import TestCase
from project import app, db
from project.models import User, BlogPost


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(BlogPost("Test post", "This is a test. Only a test."))
        db.session.add(User("admin", "ad@min.com", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
    	response = self.client.get('/login', content_type='html/text')
    	self.assertTrue(b'Please login' in response.data)


    # Ensure login behaves correctly given the correct credentials
    def test_correct_login(self):
    	response = self.client.post('/login',
    		data=dict(username="admin", password="admin"),
    		follow_redirects=True
    	)
    	self.assertIn(b'You were logged in.', response.data)

    # Ensure login behaves correctly given the incorrect credentials
    def test_incorrect_login(self):
    	response = self.client.post('/login',
    		data=dict(username ="wrong", password="wrong"),
    		follow_redirects=True
    	)
    	self.assertIn(b'Invalid username or password.', response.data)


    # Ensure logout works correctly
    def test_logout(self):
    	response = self.client.post('/login',
    		data=dict(username="admin", password="admin"),
    		follow_redirects=True
    	)
    	response = self.client.get('/logout', follow_redirects=True)
    	self.assertIn(b'You were logged out.', response.data)


    # Ensure main page requires login
    def test_main_route_requires_login(self):
    	response = self.client.get('/', follow_redirects=True)
    	self.assertTrue(b'You need to login first.' in response.data)

    # Ensure logout page requires login
    def test_logout_route_requires_login(self):
    	response = self.client.get('/logout', follow_redirects=True)
    	self.assertTrue(b'You need to login first.' in response.data)


    # Ensure posts show up on main page
    def test_post_show_up(self):
    	response = self.client.post('/login',
    		data=dict(username="admin", password="admin"),
    		follow_redirects=True
    	)
    	self.assertIn(b'This is a test. Only a test.', response.data)



if __name__ == '__main__':
    unittest.main()