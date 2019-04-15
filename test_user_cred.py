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
		



	
class TestCredentials(unittest.TestCase):
	"""
		Test class that defines test cases for the Credentials behaviour
	
		Args:
			unittest.TestCase: Class from the unittest module to create unit tests
	"""

	def test_auth_check(self):
		"""
		test_auth_check test case to test if the user provided correct information
		"""
		self.new_user = Users("komo","James","pswd002")
		self.new_user.create_user()
		another_user = Users("user2","othername","pswd003")
		another_user.create_user()
		
		for cred in Users.user_info:
			if cred.first == another_user.first and cred.password == another_user.password:
				identity = another_user.first
		return identity
		
	def test_setUp(self):
		"""
		test_setUp to create a new Credentials object to begin tests
		"""
		
		self.new_cred = Credentials("komo","james","IG","pswd001")
	
	def test_init(self):
		"""
		test_init to check if the Credentials objects are initialized correctly
		"""
		self.new_cred = Credentials("komo","james","IG","pswd001")
		self.assertEqual(self.new_cred.name, "komo")
		self.assertEqual(self.new_cred.username, "james")
		self.assertEqual(self.new_cred.platform, "IG")
		self.assertEqual(self.new_cred.pwd, "pswd001")
		
	def test_save_cred(self):
		"""
		test_save_cred to check if the initialized object is saved to credentials_info
		"""
		self.new_cred = Credentials("komo","james","IG","pswd001")
		self.new_cred.save_cred()
		self.assertEqual(len(Credentials.credentials_info),5)
		
	def tearDowm(self):
		"""
		reinitializes the credentials_info list to its empty state
		"""
		Credentials.credentials_info = []
		
	def test_show_credentials(self):
		"""
		test_show_credentials test to check if credentials saved is displayed
		"""
		self.new_cred = Credentials("komo","james","IG","pswd001")
		self.new_cred.save_cred()
		self.another_cred = Credentials("komo","james","IG","pswd001")
		self.another_cred.save_cred()
		self.assertEqual(len(Credentials.show_credentials(self.new_cred.username)),1)
	
	def test_find_platform(self):
		"""
		test_find_platform test to search credentials per account
		"""
		self.new_cred = Credentials("komo","james","IG","pswd001")
		self.new_cred.save_cred()
		IG = Credentials("komo","james","IG","pswd001")
		IG.save_cred()
		# self.assertEqual(Credentials.find_platform('IG'),IG)
		
	def test_del_cred(self):
		"""
		test_del_cred test to delete credentials from the credentials list
		"""
		Credentials.credentials_info = []
		self.new_cred = Credentials("komo","james","IG","pswd001")
		self.new_cred.save_cred()
		IG = Credentials("komo","james","IG","pswd001")
		IG.save_cred()
		del_item = Credentials.find_platform('IG')
		self.assertEqual(Credentials.del_cred(del_item),"Deleted")
	
	
if __name__ == '__main__':
	unittest.main()