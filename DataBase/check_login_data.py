# Import models
import json
import jmespath
from .make_hash import make_hash_from_str
from .change_password import change_password_custom_user

import random

from CTkMessagebox import CTkMessagebox

#Defind instance var
path_users_data = r"App\DataBase\users.json"
path_system_data = r"App\DataBase\system.json"
path_log_data = r"App\DataBase\log.json"


RANDOM_TEXT = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPLKJHGFDSAZXCVBNM@#$%&!+-"


# Function to check login data [ username , password ]
def check_login_data_in_json(username:str,password:str):

    with open(path_users_data) as F:
        data = json.load(F)

    usernames = jmespath.search("[*].username",data)
    passwords = jmespath.search("[*].password",data)
    
    password = make_hash_from_str(password)

    for u,p in zip(usernames,passwords):
        if [username,password] == [u,p]:
            return True
        
    return False


# Function to said user was login or not
def islogin_json():

    with open(path_system_data) as F:
        reader = json.load(F)["login_status"]

    if not reader == "f8320b26d30ab433c5a54546d21f414c":
        return True
    
    return False



def change_islogin_json(_bool:bool,username:str):

    with open(path_system_data) as F:
        reader = json.load(F)
    print(_bool)
    if not _bool:
        reader["login_status"] = make_hash_from_str("False")
    else:
        with open(path_users_data) as F:
            user_data = json.load(F)

        for item in user_data:
            if item["username"] == username:

                reader["login_status"] = item["id"]
                break

    with open(path_system_data,"w") as F:
        json.dump(reader,F,indent=4)



        
# How is login now
def how_is_login_json():
    with open(path_system_data) as F:
        reader = json.load(F)

    return reader["login_status"]


def give_username_and_fullname():
    """
    retrun -> fullname,username
    """
    how = how_is_login_json()

    with open(path_users_data) as F:
        reader = json.load(F)

    data = jmespath.search(f"[? id==`{how}`].[fname,lname,username]",reader)[0]

    return [data[0]+" "+data[1],data[2]]


# Give Base info about user
def give_base_info_user(): 
    """
    username,fname,lname,email
    """
    how = how_is_login_json()

    with open(path_users_data) as F:
        reader = json.load(F)

    return jmespath.search(f"[? id==`{how}`].[username,fname,lname,email]",reader)[0]

    
# Give the user (islogin) gender
def give_gender_islogin():
    how = how_is_login_json()

    with open(path_users_data) as F:
        reader = json.load(F)

    return jmespath.search(f"[? id==`{how}`].[gender]",reader)[0][0]


# @staticmethod
def show_message_box(sms:str):
        CTkMessagebox(message=sms,
                  title="Mr.Doctor - Forget password",
                  icon="cancel", option_1="Try again")


def check_forget_password(username:str):
    with open(path_users_data) as F:
        reader = json.load(F)

    unames = jmespath.search("[*].username",reader)


    if username not in unames :
        return ["The username entered was not found."]
    
    if username == "" :
        return ["The username is empty."]
    
    new_password = "".join([random.choice(RANDOM_TEXT) for _ in range(8)])

    change_password_custom_user(username,new_password)

    return [True,new_password,jmespath.search(f"[? username==`{username}`].[email]",reader)[0][0]]