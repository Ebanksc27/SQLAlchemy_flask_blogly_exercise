import os
import unittest
from app import app
from models import db, User

class UserTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client and make new user."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        db.create_all()

        # Add sample user
        user = User(first_name="Test", last_name="User")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """Clean up fouled transactions."""

        db.session.rollback()
        db.drop_all()
    
    def test_user_index(self):
        with self.client:
            resp = self.client.get("/users")
            self.assertIn(b"Test User", resp.data)

    def test_create_user(self):
        with self.client:
            data = {"first_name": "John", "last_name": "Doe"}
            resp = self.client.post("/users/new", data=data, follow_redirects=True)
            self.assertIn(b"John Doe", resp.data)

    def test_user_detail(self):
        with self.client:
            resp = self.client.get(f"/users/{self.user_id}")
            self.assertIn(b"Test User", resp.data)

    def test_edit_user(self):
        with self.client:
            data = {"first_name": "Updated", "last_name": "Name"}
            resp = self.client.post(f"/users/{self.user_id}/edit", data=data, follow_redirects=True)
            self.assertIn(b"Updated Name", resp.data)




