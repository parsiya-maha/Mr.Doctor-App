from .make_hash import make_hash_from_str
import json
import jmespath
from CTkMessagebox import CTkMessagebox


#Defind instance var
path_users_data = r"App\DataBase\users.json"
path_system_data = r"App\DataBase\system.json"
path_log_data = r"App\DataBase\log.json"


def show_massage_box(sms:str):
        CTkMessagebox(message=sms,
                  title="Mr.Doctor - Change password",
                  icon="cancel", option_1="Try again")




def change_password(new:str):
    _id = how_is_login_json()

    with open(path_users_data) as F:
        reader = json.load(F)


    for index in range(len(reader)) :
        if reader[index]["id"] == _id :
            reader[index]["password"] = make_hash_from_str(new)

            break

    with open(path_users_data,"w") as F:
        json.dump(reader,F,indent=4)

    return True


def change_password_custom_user(username:str,new:str):

    with open(path_users_data) as F:
        reader = json.load(F)

    _id = jmespath.search(f"[? username==`{username}`].[id]",reader)[0][0]


    for index in range(len(reader)) :
        if reader[index]["id"] == _id :
            reader[index]["password"] = make_hash_from_str(new)

            break

    with open(path_users_data,"w") as F:
        json.dump(reader,F,indent=4)

    return True

# How is login now
def how_is_login_json():
    with open(path_system_data) as F:
        reader = json.load(F)

    return reader["login_status"]


def change_password_for_gui(_old,_new):

    _old.reset_default()
    _new.reset_default()
    _new.password_input()

    
    old = _old.get()
    new = _new.get()


    _id = how_is_login_json()

    with open(path_users_data) as F:
        reader = json.load(F)

    PASSWORD = None

    for index in range(len(reader)) :
        if reader[index]["id"] == _id :
            PASSWORD = reader[index]["password"]
            break

    
    if PASSWORD != make_hash_from_str(old):
        _old.show_waring()
        # _old.custom_input(icon_path=r"D:\Parsia Works\python\Project\project icon.ico", text="TestText", compound="right")
        return "The previous password was entered incorrectly."
    
    if PASSWORD == make_hash_from_str(new):
        _new.show_waring()
        _new.password_input()
        return "The previous password is the same as the new password."
    
    if new == "":
        return "The new password is empty."
    
    change_password(new)

    return True