#Using getpass module, so that user doesn't see the what he writes in the password field.
import getpass
#Dictionary of usernames and passwords
database = {"deepak":"123456","arjun":"654321"}
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter your password again: ")
        break
print("User Verified")
