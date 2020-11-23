from models.userModel import UserModel  
from sqlite3 import IntegrityError
from libs.mongo import gen_chart

# fuction to register the user
def register(data):
    chart_id = gen_chart()
    user = UserModel(data, chart_id)
    try:
        user.save()
        return user
    except IntegrityError as err:
        print("That username is already taken try another.")
        return None
