"""
shortcuts :

login-------------Shift-L                *
     -------------Shift-Up             
signup------------Shift-S                *
models score------Control-Shift-S        *l
log app-----------Control-Shift-L        l
log plot----------Shift-P                l
log out-----------Shift-Down             l
user info---------Shift-U                l
upload image------Control-Shift-U        l (main.py)
predict-----------Return                 l


"""

# import models
import customtkinter
import subprocess
import sys
from funcs import go_to_login_func,go_to_signup_func,is_login
from models_score import return_app
from DataBase import logout,test_true_false_value
from funcs import predit_from_widgets
from user_info_app import return_user_info_page
from true_to_false_predict import return_tfp_page
from log_app import return_log_app



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


# Function to log out
def log_out_func(app):
    if not is_login(): 
        ...
    else:
        logout()

        app.destroy() # Destroy app
        app.quit() # Quit app
        subprocess.call([sys.executable, 'main.py'])



# Show user info btn
def show_user_info(app:customtkinter.CTk):
        
        app.iconify()
        # subprocess.call([sys.executable, 'user_info_app.py'])
        # app.deiconify()
        return_user_info_page(app).mainloop()

# Function show log plot app 
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


########################################################################################
#                                       short cut function                             #
########################################################################################


def bind_login(master:customtkinter.CTk):
    master.bind_all("<Shift-L>",lambda event:go_to_login_func(master))
    master.bind_all("<Shift-Up>",lambda event:go_to_login_func(master))


def bind_sign_up(master):
    master.bind_all("<Shift-S>",lambda event:go_to_signup_func(master))


def bind_models_score(master):
    master.bind_all("<Control-Shift-S>",lambda event:return_app().mainloop())


def bind_log_app(master):
    master.bind_all("<Control-Shift-L>",lambda event:log_app_lambda(master))            


def bind_log_out(master):
    master.bind_all("<Shift-Down>",lambda event:log_out_func(master))


def bind_user_info(master):
    master.bind_all("<Shift-U>",lambda  event:show_user_info(master))


def bind_predict(master,option,tabel,progressbar):
    master.bind_all("<Return>",lambda event:predit_from_widgets(option,tabel,progressbar,master))


def bind_log_plot(master):
    master.bind_all("<Shift-P>",lambda event:log_plot_app_lambda(master))