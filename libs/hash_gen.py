import bcrypt

def hash_gen(password):
	byte_str = password.encode("utf-8")
	return bcrypt.hashpw(byte_str, bcrypt.gensalt())
