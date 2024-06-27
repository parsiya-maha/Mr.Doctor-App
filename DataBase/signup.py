# Import models
import re
import json
import jmespath
from CTkMessagebox import CTkMessagebox
import customtkinter
from .make_hash import make_hash_from_str,make_id_for_user




#Defind instance var
path_users_data = r"App\DataBase\users.json"
path_system_data = r"App\DataBase\system.json"
path_log_data = r"App\DataBase\log.json"


# Class for sign up methods
class SignUp :
    
    @staticmethod
    def email_valid(email:str):
        pattern = r".{2,20}@gmail.com"
        res = re.findall(pattern,email)

        if res == []:
            return False
        
        return True


    @staticmethod
    def username_vaid(username:str):
        with open(path_users_data) as F:
            reader = json.load(F)

        usernames = jmespath.search("[*].username",reader)

        return username not in usernames
    

    @staticmethod
    def show_massage_box(sms:str):
        CTkMessagebox(message=sms,
                  title="Mr.Doctor - Signup",
                  icon="cancel", option_1="Try again")


    @staticmethod
    def signup_in_app_json(
        en_fname:customtkinter.CTkEntry,
        en_lname:customtkinter.CTkEntry,
        en_username:customtkinter.CTkEntry,
        en_email:customtkinter.CTkEntry,
        en_password:customtkinter.CTkEntry,
        en_rpassword:customtkinter.CTkEntry,
        radio_var:customtkinter.IntVar,
        en_CAPTCHA : customtkinter.CTkEntry,
        r_value : int
    ):
        
        fname = en_fname.get()
        lname = en_lname.get()
        username = en_username.get()
        email = en_email.get()
        password = en_password.get()
        rpassword = en_rpassword.get()
        gender = radio_var.get()
        CAPTCHA = en_CAPTCHA.get()

        en_rpassword.reset_default()
        en_CAPTCHA.reset_default()
        en_email.reset_default()
        en_fname.reset_default()
        en_lname.reset_default()
        en_username.reset_default()
        en_password.reset_default()
        # radio_var.reset_default()


        if CAPTCHA == "" :
            en_CAPTCHA.show_waring(border_color="yellow")
            return "CAPTCHA field is empty !"


        if not CAPTCHA == str(r_value):
            en_CAPTCHA.show_waring(border_color="red")
            return "CAPTCHA is not correct"
        
        
        if fname == "" :
            en_fname.show_waring(border_color="yellow")
            return "First name field is empty !"

        
        if lname == "" :
            en_lname.show_waring(border_color="yellow")
            return "Last name field is empty !"


        if username == "" :
            en_username.show_waring(border_color="yellow")
            return "The username field is empty !"


        if not SignUp.username_vaid(username) :
            en_username.show_waring(border_color="red")
            return "This username exists in the system."


        if not SignUp.email_valid(email) :
            en_email.show_waring(border_color="red")
            return "The email is invalid !"


        if password == "":
            en_password.show_waring(border_color="yellow")
            return "The password field is empty !"
        

        if password != rpassword :
            en_rpassword.show_waring(border_color="red")
            return "The retry password is not equal with correct password"
        

        if gender == 0:
            # radio_var.show_waring(border_color="yellow")
            return "First select your gender !"
        
        with open(path_users_data) as F:
            reader = json.load(F)

        reader.append({
            "id" : make_id_for_user(username,password),
            "username" : username,
            "password" : make_hash_from_str(password),
            "email" : email,
            "fname" : fname,
            "lname" : lname,
            "gender" : "male" if gender == 1 else "female"
        })


        with open(path_users_data,"w") as F:
            json.dump(reader,F,indent=4)


        with open(path_system_data) as F:
            reader = json.load(F)

        reader["login_status"] = make_id_for_user(username,password)

        with open(path_system_data,"w") as F:
            json.dump(reader,F,indent=4)

        return True
