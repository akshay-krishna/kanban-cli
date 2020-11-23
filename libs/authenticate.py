from models.userModel import UserModel as User
import bcrypt

def authenticate(data):
    u_name = data['u_name']
    user = User.find_one(u_name, "password, chart_id")
    if user:
        if compare_hash(user[0], data['password']):
        	return user[1]
    else:
        print("User not found :(")

def compare_hash(pw_hash, password):
    return pw_hash.encode("utf-8") == bcrypt.hashpw(password.encode("utf-8"), pw_hash.encode("utf-8"))
