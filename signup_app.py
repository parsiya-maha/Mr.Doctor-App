# Import models
import customtkinter,os
from PIL import Image
from CTkMessagebox import CTkMessagebox
from DataBase import check_login_data_in_json,make_id_for_user,change_islogin_json
from DataBase import SignUp
import random
from BtnInfo import btn_info
from CTkPopupKeyboard import PopupKeyboard, PopupNumpad
from ctk_components import CTkInput



def return_signup_page(master)->customtkinter.CTk:
    # set som setting of customtkinter
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    # Defind signup app (type : top level)
    app = customtkinter.CTkToplevel(master)
    app.geometry("800x540")
    app.title("Mr.Doctor - Sign up")
    app.resizable(0,0)

    icon_path = "images\\project icon.ico"
    app.after(250,lambda:app.iconbitmap(icon_path))


    # Load base image for design
    path = os.path.join(os.getcwd(),"images\\signup1.png")

    signup_image = customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(153, 340))

    # Show image as a label
    customtkinter.CTkLabel(app,image=signup_image,text="").pack(side="right",padx=(0,15),pady=(100,0))

    # Main title text 
    customtkinter.CTkLabel(app,text="Mr.Doctor Sign up",font=("...",35,"bold")).pack(pady=(50,20))


    # Main `signup` frame
    frame = customtkinter.CTkFrame(app)
    frame.pack(side="top",fill="both",expand=1,padx=(15,25),pady=15)

    en_fname = CTkInput(master=frame,font=("calibri",15),height=50,width=266,placeholder_text="First Name")
    en_fname.grid(row=0,column=0,padx=20,pady=15)

    en_lname = CTkInput(master=frame,font=("calibri",15),height=50,width=268,placeholder_text="Last Name")
    en_lname.grid(row=0,column=1,padx=(0,20),pady=15)

    en_username = CTkInput(master=frame,font=("calibri",15),height=50,width=266,placeholder_text="Username")
    en_username.grid(row=1,column=0,padx=20,pady=15)

    en_email = CTkInput(master=frame,font=("calibri",15),height=50,width=268,placeholder_text="Email")
    en_email.grid(row=1,column=1,padx=(0,20),pady=15)

    en_password = CTkInput(master=frame,font=("calibri",15),height=50,width=266,placeholder_text="Password",show="*")
    en_password.grid(row=2,column=0,padx=20,pady=15)

    en_rpassword = CTkInput(master=frame,font=("calibri",15),height=50,width=268,placeholder_text="Retry Password",show="*")
    en_rpassword.grid(row=2,column=1,padx=(0,20),pady=15)

    random_value = [random.randint(1000,9999)]

    capture = CTkInput(master=frame,font=("calibri",15),height=50,width=268,placeholder_text=f"Type : {random_value[0]}")
    capture.grid(row=3,column=0,padx=20,pady=12)


    # Add Popup keyboards
    PopupKeyboard(en_fname)
    PopupKeyboard(en_lname)
    PopupKeyboard(en_username)
    PopupKeyboard(en_email)
    PopupNumpad(capture)





    frame3 = customtkinter.CTkFrame(frame,height=50,width=268)
    frame3.pack_propagate(False)
    frame3.grid(row=3,column=1,pady=12,padx=(0,18))

    

    man_woman_var = customtkinter.IntVar(frame3,0)
    man_radio = customtkinter.CTkRadioButton(master=frame3, text="Male",
                                             command=lambda : ..., variable= man_woman_var, value=1)
    
    woman_radio = customtkinter.CTkRadioButton(master=frame3, text="Female",
                                             command=lambda : ..., variable= man_woman_var, value=2)
    

    # man_radio.grid(row=0,column=0,pady=15,sticky="w")
    # woman_radio.grid(row=0,column=1,pady=15,sticky="w")
    man_radio.pack(side="left",padx=(25,0))
    woman_radio.pack(side="right",padx=(0,10))



    def check():
        res = SignUp.signup_in_app_json(en_fname,en_lname,en_username,en_email,en_password,en_rpassword,man_woman_var,capture,random_value[0])

        if res == True:

            app.destroy() # Destroy app
            app.quit() # Quit app
            

        elif res == "CAPTCHA is not correct":

            CTkMessagebox(message=res,
                  title="Mr.Doctor - Sign up",
                  icon="cancel", option_1="Try again")

            # Change btn text to `Try agin`
            submit_btn.configure(text="Try again")

            
            random_value[0] = random.randint(1000,9999)

            capture.delete(0,"end")
            capture.configure(placeholder_text=f"Type : {random_value[0]}")
            en_fname.configure(placeholder_text="First Name")

        else : 
            
            CTkMessagebox(message=res,
                  title="Mr.Doctor - Sign up",
                  icon="cancel", option_1="Try again")

            # Change btn text to `Try agin`
            submit_btn.configure(text="Try again")


    submit_btn = customtkinter.CTkButton(app,text="Sign up",font=("...",15,"bold"),height=50,command=check)
    submit_btn.pack(side="top",fill="x",pady=(10,20),padx=(15,25))

    app.bind_all("<Return>",lambda event:check())

    btn_info(submit_btn,"Create a new account with the entered information.")

    return app


# return_signup_page(1).mainloop()