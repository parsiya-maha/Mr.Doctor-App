# import models
import customtkinter
from CTkMenuBar import *
import sys
import subprocess
import webbrowser
from ctk_components import CTkPopupMenu,do_popup

from menu1 import return_models_score_menu,return_log_plot_menu,return_model_layer_menu,return_contact_us
from menu1 import return_user_info,return_setting_set_color,return_all_shortcuts,return_clear_all
from funcs import go_to_login_func,go_to_signup_func,is_login
from DataBase import logout
from log_app import return_log_app
from help import return_help_app


# Defind function fot fot Buttons command param
def log_out_func(app):
    if not is_login(): 
        ...
    else:
        logout()

        app.destroy() # Destroy app
        app.quit() # Quit app
        subprocess.call([sys.executable, 'main.py'])

def log_app_lambda(app:customtkinter.CTk):
    if not is_login():
        ...
    else:
        app.iconify()
        # subprocess.call([sys.executable, 'log_app.py'])
        # # return_log().mainloop()
        # app.deiconify()
        return_log_app(app).mainloop()

def help_show(app):
    app.iconify()

    return_help_app(app).mainloop()




# return the title menu for master (main app) -> [\App\main.py->app:CTk]
def return_menu(master:customtkinter.CTk):
    # Defind title menu
    menu = CTkTitleMenu(master)

    # Add tabs to title menu
    m_account = menu.add_cascade(" Account ") # log - upload - help
    m_log     = menu.add_cascade(" History ")
    m_score   = menu.add_cascade(" Models ")
    m_setting = menu.add_cascade(" Setting ")
    m_help    = menu.add_cascade(" Help ")


    # dropdown1 -> for `account` tab
    dropdown1 = CustomDropdownMenu(widget=m_account)
    dropdown1.add_option("Login",command=lambda:go_to_login_func(master))
    dropdown1.add_option("Sign up",command=lambda:go_to_signup_func(master))
    dropdown1.add_separator()
    dropdown1.add_option("Log out",command=lambda:log_out_func(master))


    # dropdown2 -> for `History` tab
    dropdown2 = CustomDropdownMenu(widget=m_log)
    dropdown2.add_option("Log app",command=lambda:log_app_lambda(master))
    return_log_plot_menu(dropdown2)


    # dropdown4 -> for `Score` tab
    dropdown4 = CustomDropdownMenu(widget=m_score)
    return_model_layer_menu(dropdown4)
    dropdown4.add_separator()
    return_models_score_menu(dropdown4)


    # dropdown5 -> for `setting` tab
    dropdown5 = CustomDropdownMenu(widget=m_setting)
    # return_setting_set_color(dropdown5)
    return_all_shortcuts(dropdown5)
    return_clear_all(dropdown5)


    # dropdown6 -> for `Help` tab
    dropdown6 = CustomDropdownMenu(widget=m_help)
    dropdown6.add_option("Help",command=lambda:help_show(master))
    dropdown6.add_option("Github",command=lambda : webbrowser.open("https://github.com/parsiya-maha/SMA"))
    return_user_info(dropdown6)
    # return_contact_us(dropdown6)



