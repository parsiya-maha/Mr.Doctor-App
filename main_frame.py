# Import models
import customtkinter,os
from PIL import Image
from funcs import go_to_login_func,go_to_signup_func
from CTkAnimation import AutoTextWriter
from BtnInfo import btn_info



# LABEL[IMAGE] -> brain image (that is for design)
def brain_image_label(master)->customtkinter.CTkLabel:
    path = os.path.join(os.getcwd(),"images\\home.png")

    my_image = customtkinter.CTkImage(light_image=Image.open(path),
                                  dark_image=Image.open(path),
                                  size=(300, 300))
    label = customtkinter.CTkLabel(master,image=my_image,text="")
    return label


text1 = """
Mr.Doctor Login
"""

# LABEL -> show some text
def text1_to_main_frame(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text1,
#                                justify='left',
                                font=("calibri",45,"bold"))
    return text



text2 = """
You must purchase a subscription 
to use Mr.Doctor, in order not to 
violate the rights of those who 
have purchased a subscription, 
you must first purchase a subscription 
and then enter your username and 
password in the main section of 
the program.
All features of the program are 
free for those who have purchased 
a subscription. 
"""

# LABEL -> show some text
def text2_to_main_frame(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text2,
                                justify='left',
                                font=("calibri",20))
    return text


# BUTTON -> show custom btn
def main_login(master,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                   text="Login",
                                   font=("...",15,"bold"),
                                   height=50,
                                   corner_radius=25,
                                   command=lambda: go_to_login_func(app))
    
    btn_info(btn,"Go to the login page to use more features.")

    return btn


# BUTTON -> show custom btn
def main_signup(master,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                   text="Sign up",
                                   font=("...",15,"bold"),
                                   height=50,
                                   corner_radius=25,
                                   command=lambda: go_to_signup_func(app))
    
    btn_info(btn,"If you do not have an account in the program, you can create one.")

    return btn


text3 = "\n\nCopyright © 2024 by Mr.Doctor | All Rights Reserved.\n\n"


# LABEL -> show some text
def text3_to_main_frame(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text="", # text3
#                                justify='left',
                                font=("calibri",12,"bold"))
    return text



# LABEL -> show some text
def text4_to_main_frame(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text="",
                                text_color="skyblue",
#                                justify='left',
                                font=("calibri",20,"bold"))
    return text