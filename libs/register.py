from models.userModel import UserModel  
import sqlite3

# fuction to register the user
def register(data):
    user = UserModel(data)
    try:
        user.save()
        return True
    except sqlite3.IntegrityError as err:
        print("That username is already taken try another.")
        return False
