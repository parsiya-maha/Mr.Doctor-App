# Import models
import customtkinter,os
from PIL import Image
from CTkMessagebox import CTkMessagebox
from DataBase import check_login_data_in_json,make_id_for_user,change_islogin_json
from BtnInfo import btn_info
from DataBase.check_login_data import show_message_box,check_forget_password
from network import send_email,send_email_html
from CTkPopupKeyboard import PopupKeyboard, PopupNumpad

from ctk_components import CTkInput




# Function to check log in data [username , password]
def check_login_data(username,password):
    return check_login_data_in_json(username,password)


# Function to change `is login` data when user login
def change_is_login(_bool,username):
    return change_islogin_json(_bool,username)


# Return Main login page
def return_login_page(master)->customtkinter.CTk:
    
    # set som setting of customtkinter
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    # Defind login app (type : top level)
    app = customtkinter.CTkToplevel(master)
    app.geometry("700x480")
    app.title("Mr.Doctor - Login")


    # Load base image for design
    path = os.path.join(os.getcwd(),"App\\images\\login.png")

    login_image = customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(250, 250))

    # Show image as a label
    customtkinter.CTkLabel(app,image=login_image,text="").pack(side="right")

    # Main title text 
    customtkinter.CTkLabel(app,text="Mr.Doctor Login",font=("...",40,"bold")).pack(pady=(45,25))


    # Main `login` frame
    frame = customtkinter.CTkFrame(app,width=400)
    frame.pack(side="top",padx=15,pady=15,fill="both",expand=1)

    # customtkinter.CTkLabel(frame,text="username",anchor="w",font=("...",20)
    # ).grid(row=0,column=0,padx=(20,30),pady=30)


    # Username entry
    # username = customtkinter.CTkEntry(frame,font=("...",15,"bold"),height=50,placeholder_text="Username")
    username = CTkInput(frame,font=("...",15,"bold"),height=50,placeholder_text="Username")
    username.pack(padx=25,pady=25,fill="both",expand=1)


    # customtkinter.CTkLabel(frame,text="password",anchor="w",font=("...",20)
    # ).grid(row=1,column=0,padx=(20,30),pady=30)

    # Password entry
    # password = customtkinter.CTkEntry(frame,font=("...",15,"bold"),width=250,show="*",height=50,placeholder_text="Password")
    password = CTkInput(frame,icon_height=30,icon_width=30,font=("...",15,"bold"),width=250,height=50,placeholder_text="Password")
    password.password_input()
    password.pack(padx=25,pady=(0,15),fill="both",expand=1)


    PopupKeyboard(username)


    # def checkbox_event(en:customtkinter.CTkEntry):
    #     if check_var.get() == "on":
    #         en.configure(show="")

    #     else:
    #         en.configure(show="*")
            

    check_var = customtkinter.StringVar(value="off")

    # show_btn = customtkinter.CTkCheckBox(frame, text="Show password", command=lambda:checkbox_event(password),
    #                                 variable=check_var, onvalue="on", offvalue="off")
    # show_btn.pack(pady=(0,20),fill="x",padx=25)


    # Fuinction to quite if data was correct else `try agin
    def check():
        username.reset_default()

        # If input data was correct
        if check_login_data(username.get(),password.get()) :

            change_is_login(True,username.get())

            app.destroy() # Destroy app
            app.quit() # Quit app
            

        else : # When `username` or `password` was not correct -> show massage box
            
            CTkMessagebox(message="Username or Password is not correct.",
                  title="Mr.Doctor",
                  icon="cancel", option_1="Try again")

            username.show_waring()
            # password.show_waring()

            # Change btn text to `Try agin`
            submit_btn.configure(text="Try again")


    # Add Submit btn to login app
    submit_btn = customtkinter.CTkButton(app,
                                        text = "Submit",
                                        font = ("...",15,"bold"),
                                        width = 420,
                                        height=70,
                                        command = check)
    
    btn_info(submit_btn,"Validation of entered information.")


    # Forget password function
    def forget_password_func():
        _username = username.get()

        res = check_forget_password(_username)

        # If had a eeror in send a email or correct username
        if res[0] != True :
            show_message_box(res[0])
            return 

        try :
            # First try to send a email for check internet connection
            send_email("iraniparsiya@gmail.com","Mr.Doctor - User",f"The user with email = {res[2]} change password with {res[1]}")
            
        # Whene has any problem in  internet connection 
        except Exception as Ex:

            # Show message box for `error in connecting to the internet`
            CTkMessagebox(title="Network Error !",message="There is a problem connecting to the Internet.."
                ,icon=os.path.join(os.getcwd(),"App\\images\\no-net-l.png"))

        # Else all things was OK
        else:
            # Try to send a email
            try:
                send_email_html(res[2],"Mr.Doctor - Forget password",res[1])

                CTkMessagebox(title="Mr.Doctor - Forget password",message="Thank you for your partnership.\nCheck your Email for get new password.",icon="check")

            # Whene have a problem in connect to the internet 
            except:
                CTkMessagebox(title="Network Error !",message="There is a problem connecting to the Internet."
                ,icon=os.path.join(os.getcwd(),"App\\images\\no-net-l.png"))


    _bg = app._apply_appearance_mode(customtkinter.ThemeManager.theme["CTk"]["fg_color"])

    # Forget password buttom (same the label)
    forget_text = customtkinter.CTkButton(app,
                                         text="Froget password (click)",
                                         text_color = ("#408CD4","#08D4EC"),
                                         width = 420,
                                         fg_color = _bg,
                                         anchor = "w",
                                         cursor="hand2",
                                         font=("calibri",15,"underline"),
                                         command=forget_password_func
                                         )
    
    forget_text.pack(pady=5)


    # Bind app and all widget to when user click = check() function
    app.bind_all("<Return>",lambda event : check())
    

    submit_btn.pack_propagate(False)
    submit_btn.pack(pady=(10,10))

    app.resizable(0,0)

    # return app for .mainloop()
    return app


# return_login_page(1).mainloop()