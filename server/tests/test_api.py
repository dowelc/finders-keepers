# TestAPI: Basic API Test
import unittest
from flask import Flask

app = Flask(__name__)

class MockTestCase(unittest.TestCase):
	# Tests for 'server.py' mock methods

	# This tests that the API is returning valid mock user data
	# $NOTE-yoont4: this only checks that a response is returned right now
	def test_mock_get_user(self):
		client = app.test_client()
		response = client.get('mock/api/get_user/1234')
		self.assertTrue(response is not None)

if __name__ == '__main__':
	unittest.main()
