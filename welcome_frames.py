# Import models
import customtkinter
import webbrowser

from funcs import go_to_login_func,go_to_signup_func,is_login
from models_score import return_app
# from log_app import return_log
from DataBase import logout,test_true_false_value
from BtnInfo import btn_info

import sys
import subprocess
from PIL import Image
from user_info_app import return_user_info_page
from true_to_false_predict import return_tfp_page
from log_app import return_log_app


# from true_to_false_predict import return_tfp_page




welcome_text1 = """
We are Mr.Doctor
Welcome to our project.

We are working on 6 models :

    - Brain Tumors
    - Breast Cancer
    - Cervical Cancer
    - Kidney Stone
    - Lung Cancer
    - Lung Mask

And 2 sub model but practical :

    - To Recognize
    - To Recognize And Predict

We can said To 
'Recognize And Predict' model
is one pipeline of 'To Recognize' model 
and last 6 models.

click for more about models :
"""


# LABEL -> show some text
def option_frame_text1(master)->customtkinter.CTkFrame :
    text = customtkinter.CTkLabel(master,
                                text=welcome_text1,
                                justify='left',
                                font=("calibri",14))
    return text


# Button -> return custom btn
def more_info_btn(master)->customtkinter.CTkButton:

    btn = customtkinter.CTkButton(master,
            width=150,
            text="more info",
            command=lambda : webbrowser.open("https://github.com/parsiya-maha/SMA/blob/master/README.md"))
    
    btn_info(btn,"To explore more about our project,\nIt will take you to our GitHub repository.")

    return btn


welcome_text2 = """
Mr.Doctor tried to make our models as 
efficient as possible.

To use all 8 models, login first.
"""

# LABEL -> show some text
def option_frame_text2(master)->customtkinter.CTkFrame :
    text = customtkinter.CTkLabel(master,
                                text=welcome_text2,
                                justify='left',
                                font=("calibri",14))
    return text


# Button -> return custom btn
def go_to_login(master:customtkinter.CTkFrame,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                 text="Login",
                                 width=150,
                                 command=lambda :go_to_login_func(app))  
       
    btn_info(btn,"Go to the login page to use more features.")

    return btn

# Button -> return custom btn
def go_to_signup(master:customtkinter.CTkFrame,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                 text="Sign up",
                                 width=150,
                                 command=lambda :go_to_signup_func(app))     
    
    btn_info(btn,"If you do not have an account in the program, you can create one.")

    return btn


welcome_text3 = """
We hope you enjoy our app.    
                
- Parsiya Hassanzadeh
- Mohamad Mehdi Khodaie
"""

# LABEL -> show some text
def option_frame_text3(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=welcome_text3,
                                justify='left',
                                font=("calibri",14))
    return text


welcome_text4 = """
And to work with logs and edit them,    
press the following button:
"""

# LABEL -> show some text
def option_frame_text4(master)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=welcome_text4,
                                justify='left',
                                font=("calibri",14))
    return text


# Button -> return custom btn
def go_to_model_score(master:customtkinter.CTkFrame)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                 text="Models score",
                                 width=150,
                                 command=lambda :return_app().mainloop())     
    
    btn_info(btn,"You can get help from this section to see the accuracy of all program models.")

    return btn


# Function to run [log_app.py] python file
def log_app_lambda(app):
    if not is_login():
        ...
    else:
        app.iconify()
        # subprocess.call([sys.executable, 'log_app.py'])
        # # return_log().mainloop()
        # app.deiconify()
        return_log_app(app).mainloop()



# Button -> return custom btn
def log_app(master:customtkinter.CTkFrame,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                 text="Log",
                                 width=150,
                                 command=lambda:log_app_lambda(app))  

    btn_info(btn,"View all logs and history of AI model predictions.\nTo use, you must first log in to your account.")

    return btn


def log_out_func(app):
    if not is_login(): 
        ...
    else:
        logout()

        app.destroy() # Destroy app
        app.quit() # Quit app
        subprocess.call([sys.executable, 'main.py'])



# Button -> return custom btn
def logout_app(master:customtkinter.CTkFrame,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                 text="Log out",
                                 width=150,
                                 command=lambda:log_out_func(app))   

    btn_info(btn,"Log out from your account.")

    return btn


def log_plot_app_lambda(app:customtkinter.CTk):

    if not is_login():
        ...

    elif test_true_false_value() == []:
        ...

    else:
        app.iconify()
        # return_tfp_page().mainloop()
        # subprocess.call([sys.executable, 'true_to_false_predict.py'])
        # app.deiconify()
        return_tfp_page(app).mainloop()




# Button -> return custom btn
def log_plot_app(master:customtkinter.CTkFrame,app)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master,
                                 text="Log plot",
                                 width=150,
                                 command=lambda : log_plot_app_lambda(app))     
    
    btn_info(btn,"A pie chart of the ratio of correct to incorrect predictions.\n(specified by the user)")

    return btn



# Show user info btn
def show_user_info(app:customtkinter.CTk):
        
        app.iconify()
        # subprocess.call([sys.executable, 'user_info_app.py'])
        # app.deiconify()
        return_user_info_page(app).mainloop()


# Button -> return custom btn
def user_info_btn(master:customtkinter.CTkFrame,app)->customtkinter.CTkButton:
    path = "images\\usericon2.png"

    my_image = customtkinter.CTkImage(light_image=Image.open(path),
                                  dark_image=Image.open(path),
                                  size=(25, 25))


    btn = customtkinter.CTkButton(master,
                                 text="User account",
                                 width=270,
                                 image=my_image,
                                 height=50,
                                 command = lambda : show_user_info(app),
                                 font=("calibri",15,"bold"))     
    
    btn_info(btn,"Full details of the user account you are currently in.")

    return btn