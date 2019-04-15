#!/usr/bin/env python3.6
from user_cred_classes import Users, Credentials



def register_user(user):
	'''
	Saves the created user's account 
	'''
	Users.create_user(user)
	
def user_check(first,pwd):
	'''
	Checks whether user exists before creating any new credentials
	'''
	return Credentials.user_check(first,pwd)

def create_cred(name,username,platform,pwd):
	'''
	Creates credentials to be saved
	'''
	create_instance = Credentials(name,username,platform,pwd)
	return create_instance
	
def save_cred(cred):
	'''
	Saves created user credentials
	'''
	Credentials.save_cred(cred)

def password_gen(size):
	'''
	Generates a random password_gen
	'''
	random = Credentials.password_gen(size)
	return random

def show_cred(username):
	'''
	Dsiplays saved credentials
	'''
	return Credentials.show_credentials(username)
	
def main():
	print("Welcome to Komo password Vault app")
	while True:
		print("**************\n"*10)
		print("Please use the following short codes to interact with this application app\n li - Login\n cu - Register\n lo - Logout")
		user_input = input("Enter input here: ")
		
		if user_input == 'cu':
			print("You have selected to register. Please enter your registration details below")
			fname = input("Enter your first name: ")
			lname = input("Enter your last name: ")
			pwd = input("Enter your desired password: ")
			register_user(create_user(fname, lname, pwd))
			print(f"Your account is registered as follows: First Name: {fname}LastName: {lname} Password: {pwd} is your password")
			
		elif user_input == 'li':
			print("Enter your first name and password to log in to your account\n")
			username = input("Enter your username here:		")
			password = input("Enter your password here:		")
			if user_check(username, password) == username:
				print(f"Welcome {username}. Your login was successful")
				
				while True:
					print("**********\n"*10)
					print("Please use the following short codes to use the Password Vault")
					user_input = input("cc - Save new credentials\n ccp - Create new credentials with Generated Password\n dc - Display credentials\n del - Delete credentials\n ex - Exit")
					
					if user_input == 'cc':
						print("Enter the account details you want saved below")
						username = input("Enter your username:		")
						platform = input("Enter the platform:		")
						pwd = input("Enter your password:		")
						create_cred(fname,username,platform,pwd)
						print(f"Your credentials for site: {platform}, with username: {username} and password: {pwd} has been saved!")
					
					elif user_input == 'ccp':
						print("Enter the account details you want saved below")
						username = input("Enter your username:		")
						platform = input("Enter the platform:		")
						len = input("Enter the length of your desired password (Numbers Only):		")
						pwd = password_gen(int(len))
						create_cred(fname,username,platform,pwd)
						print(f"Your credentials for account: {platform}, with username: {username} and password: {pwd} have been saved!")
						
					elif user_input == 'dc':
						print("Your saved credentials are as below")
						show_cred(username)
						 
					elif user_input == 'del':
						print("Enter the account name and username whose credentials you want to delete below")
						platform = input("Enter the name of the account here eg IG:		")
						username = input("Enter the username here:			")
						show_cred(username)
						print("Your credentials have been deleted!")
						
					elif user_input == 'ex':
						print("Goodbye!!")
						break
	
		elif user_input == 'lo':
			print("Thank you for using Komo Password Vault")
			break
			
		else:
			print("Wrong Input! Kindly select again")
	
if __name__ == '__main__':
	main()		