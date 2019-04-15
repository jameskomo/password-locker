import unittest
from user_cred_classes import Users, Credentials


class TestUsers(unittest.TestCase):
	"""
	Test class that defines test cases for the Users behaviour
	
	Args:
		unittest.TestCase: Class from the unittest module to create unit tests
	"""
	
	def setUp(self):
		"""
			#Function creates a new user object
		"""
		self.new_user = Users("Simon","Gatheru","W3w3n!mkenya")
		
	def test_init(self):
		"""
		#test_init test case to test if the object is the initialized properly
		"""
		
		self.assertEqual(self.new_user.first,"Simon")
		self.assertEqual(self.new_user.last,"Gatheru")
		self.assertEqual(self.new_user.password,"W3w3n!mkenya")
		

	
	
if __name__ == '__main__':
	unittest.main()