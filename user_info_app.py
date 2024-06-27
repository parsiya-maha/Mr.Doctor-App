# Import models
import customtkinter,os
from PIL import Image
from DataBase import give_username_and_fullname,give_base_info_user,give_gender_islogin
from DataBase.change_password import change_password_for_gui,show_massage_box
import CTkTable
import webbrowser
from network import internet_on,send_email
from CTkMessagebox import CTkMessagebox
import threading
from ctk_components import CTkInput


text3 = """
Hello, the Mr.Doctor team hopes that you have enjoyed 
our app and made full use of it.Mr.Doctor's team hopes 
that various cancers will be eradicated in the near future, 
and how great it would be if our team also participates 
in this great and global victory.Good luck

- Parsiya Hassanzadeh
- Mohamad Mehdi Khodaie
"""

info_text = """
In this section, you can ask 
our administrator your 
question, problem or 
challenge in our program.
We will try to answer you
as soon as possible.
Our answer will be 
sent to your email.
Note that you must be 
connected to the Internet 
before sending your 
question.
"""


# Return user info page
def return_user_info_page(master)->customtkinter.CTk:
    
    # set som setting of customtkinter
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    # Defind login app (type : top level)
    app = customtkinter.CTkToplevel(master)
    app.geometry("750x400")
    app.title("Mr.Doctor - User account")
    app.resizable(0,0)

    # Defind one TabView
    tab_frame = customtkinter.CTkTabview(app)

    # Add all 5 tab to `tab view` widget
    user_tab     = tab_frame.add("User")
    info_tab     = tab_frame.add("Info")
    password_tab = tab_frame.add("Change password")
    contact_tab  = tab_frame.add("Contact us")
    aboutus_tab  = tab_frame.add("About us")

    tab_frame.pack(fill="both",expand=True,padx=10,pady=(0,10))


    # ------------------------------------------------------------------------------- first tab (user_tab)
    frame1 = customtkinter.CTkFrame(user_tab)
    frame1.pack(fill="both",expand=1,padx=10,pady=10)

    img_frame1 = customtkinter.CTkFrame(frame1,height=300,width=300,corner_radius=150)
    img_frame1.grid(row=0,column=0,pady=20,padx=(10,20))

    path1 = "App\\images\\man.png" if give_gender_islogin() == "male" else "App\\images\\woman.png"

    image_obj1 = customtkinter.CTkImage(light_image=Image.open(path1),
                                  dark_image=Image.open(path1),
                                  size=(200, 200))
    
    customtkinter.CTkLabel(img_frame1,text="",image=image_obj1).pack(padx=40,pady=40)

    text_frame1 = customtkinter.CTkFrame(frame1,height=280,width=380)
    text_frame1.pack_propagate(False)
    text_frame1.grid(row=0,column=1)


    username1 = customtkinter.CTkScrollableFrame(text_frame1,orientation="horizontal",width=360,height=140)
    username1.pack(padx=10,pady=10,fill="x")

    fullname1 = customtkinter.CTkScrollableFrame(text_frame1,orientation="horizontal",width=360)
    fullname1.pack(padx=10,pady=10,fill="x")


    fname1,uname1 = give_username_and_fullname()

    customtkinter.CTkLabel(username1,
                           text=uname1,
                           font=("calibri",100,"bold"),
                           text_color="#286ca4"
                           ).pack(side="left")
    
    customtkinter.CTkLabel(fullname1,
                           text=fname1,
                           font=("calibri",30)
                           ).pack(side="left")

    #-------------------------------------------------------------------------------- info_tab
    frame2 = customtkinter.CTkFrame(info_tab)
    frame2.pack(fill="both",expand=1,padx=10,pady=10)

    data2  = give_base_info_user()

    tabel_frame2 = customtkinter.CTkFrame(frame2,width=555,height=305)
    tabel_frame2.pack_propagate(False)
    tabel_frame2.grid(row=0,column=0,padx=10,pady=10,sticky="w")


    values2 = [
        ["FirstName","LastName"],
        [data2[1] , data2[2]],
        ["Username","Email"],
        [data2[0] , data2[3]]
    ]
    
    tabel2 = CTkTable.CTkTable(tabel_frame2,row=4,column=2,values=values2,
                               padx=5,pady=5,corner_radius=20,font=("calibri",15,"bold"))
    tabel2.pack(fill="both",expand=1,padx=15,pady=15)


    img_frame2 = customtkinter.CTkFrame(frame2,height=305,width=120)
    img_frame2.pack_propagate(False)
    img_frame2.grid(row=0,column=1,padx=(0,10),pady=10,sticky="e")


    path21 = "App\\images\\brain.png"
    image_obj21 = customtkinter.CTkImage(light_image=Image.open(path21),
                                  dark_image=Image.open(path21),
                                  size=(50, 50))
    
    customtkinter.CTkLabel(img_frame2,text="",image=image_obj21).pack(pady=(30,20),anchor="n")


    path22 = "App\\images\\lung.png"
    image_obj22 = customtkinter.CTkImage(light_image=Image.open(path22),
                                  dark_image=Image.open(path22),
                                  size=(60, 60))
    
    customtkinter.CTkLabel(img_frame2,text="",image=image_obj22).pack(pady=(30,15),anchor="n")


    path23 = "App\\images\\kidney.png"
    image_obj23 = customtkinter.CTkImage(light_image=Image.open(path23),
                                  dark_image=Image.open(path23),
                                  size=(60, 60))
    
    customtkinter.CTkLabel(img_frame2,text="",image=image_obj23).pack(pady=(25,10),anchor="n")


    #------------------------------------------------------------------------ about us

    frame2 = customtkinter.CTkFrame(aboutus_tab)
    frame2.pack(fill="both",expand=1,padx=10,pady=10)


    text_frame3 = customtkinter.CTkFrame(frame2,height=310,width=420)
    text_frame3.pack_propagate(False)
    text_frame3.grid(row=0,column=0,padx=(10,0),pady=10,sticky="n")

    bg_color3_f = text_frame3._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])

    path31 = "App\\images\\home.png"
    image_obj31 = customtkinter.CTkImage(light_image=Image.open(path31),
                                  dark_image=Image.open(path31),
                                  size=(300, 300))

    customtkinter.CTkLabel(frame2,text="",image=image_obj31).grid(row=0,column=1,sticky="n")

    customtkinter.CTkLabel(text_frame3,text="Mr.Doctor",font=("calibri",40,"bold"),text_color=("#408cd4","skyblue")).pack(pady=(5,0))

    customtkinter.CTkLabel(text_frame3,text=text3,font=("calibri",15),justify='left').pack()

    

    more_btn_frame = customtkinter.CTkFrame(text_frame3,height=60,width=260,fg_color=bg_color3_f)
    more_btn_frame.pack_propagate(False)
    more_btn_frame.pack(side="bottom",padx=10,pady=(0,10),anchor="se")
    
    bg_color3 = more_btn_frame._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])


    path32 = "App\\images\\github.png"
    image_obj32 = customtkinter.CTkImage(light_image=Image.open(path32),
                                  dark_image=Image.open(path32),
                                  size=(40, 40))
    
    path33 = "App\\images\\gmail.png"
    image_obj33 = customtkinter.CTkImage(light_image=Image.open(path33),
                                  dark_image=Image.open(path33),
                                  size=(40, 40))

    path34 = "App\\images\\linkedin.png"
    image_obj34 = customtkinter.CTkImage(light_image=Image.open(path34),
                                  dark_image=Image.open(path34),
                                  size=(40, 40))
    
    path35 = "App\\images\\facebook.png"
    image_obj35 = customtkinter.CTkImage(light_image=Image.open(path35),
                                  dark_image=Image.open(path35),
                                  size=(40, 40))



    customtkinter.CTkButton(more_btn_frame,width=10,height=10,text="",image=image_obj32,corner_radius=20,fg_color=bg_color3_f,
                            command = lambda : webbrowser.open("github.com/parsiya-maha/SMA")
                            ).pack(anchor="e",side="right",padx=10)
    
    customtkinter.CTkButton(more_btn_frame,width=10,height=10,text="",image=image_obj33,corner_radius=20,fg_color=bg_color3_f,
                            command = lambda : webbrowser.open("github.com/parsiya-maha/SMA")
                            ).pack(anchor="e",side="right",padx=(10,0))
    
    customtkinter.CTkButton(more_btn_frame,width=10,height=10,text="",image=image_obj34,corner_radius=20,fg_color=bg_color3_f,
                            command = lambda : webbrowser.open("github.com/parsiya-maha/SMA")
                            ).pack(anchor="e",side="right",padx=(10,0))
    
    customtkinter.CTkButton(more_btn_frame,width=10,height=10,text="",image=image_obj35,corner_radius=20,fg_color=bg_color3_f,
                            command = lambda : webbrowser.open("github.com/parsiya-maha/SMA")
                            ).pack(anchor="e",side="right",padx=(10,0))
    

    #------------------------------------------------------------------------ change password


    frame2 = customtkinter.CTkFrame(password_tab)
    frame2.pack(fill="both",expand=1,padx=10,pady=10)


    text_frame3 = customtkinter.CTkFrame(frame2,height=310,width=420)
    text_frame3.pack_propagate(False)
    text_frame3.pack(fill="both",expand=1,padx=10,pady=10,side="left")


    path_l = "App\\images\\password-l.png"
    path_d = "App\\images\\password-d.png"

    image_obj31 = customtkinter.CTkImage(light_image=Image.open(path_l),
                                  dark_image=Image.open(path_d),
                                  size=(200, 200))

    customtkinter.CTkLabel(frame2,text="",image=image_obj31,width=250).pack(pady=10,padx=10,side="right")

    ent1 = CTkInput(text_frame3,
                                  placeholder_text="Old password",
                                  height=60,
                                  font=("calibri",20,"bold")
                                  )
    
    ent2 = CTkInput(text_frame3,
                                  placeholder_text="New password",
                                #   show="*",
                                  height=60,
                                  font=("calibri",20,"bold")
                                  )
    

    ent2.password_input()
    
    # def checkbox_event(en:customtkinter.CTkEntry):
    #     if check_var.get() == "on":
    #         en.configure(show="")

    #     else:
    #         en.configure(show="*")
            

    # check_var = customtkinter.StringVar(value="off")

    # show_btn = customtkinter.CTkCheckBox(text_frame3, text="Show password", command=lambda:checkbox_event(ent2),
    #                                 variable=check_var, onvalue="on", offvalue="off")
    
    # Function to change password
    def change_password_btn_func():
        res = change_password_for_gui(ent1,ent2)

        if res == True:
            CTkMessagebox(title="Mr.Doctor - Change password",
                          message="Your password has been successfully changed.",
                          icon="check"
                          )    

        else :
            
            show_massage_box(res)        
    
    change_password_btn = customtkinter.CTkButton(text_frame3,
                                                  text="Change password",
                                                  font=("calibri",20,"bold"),
                                                  command=change_password_btn_func
                                                  )

    # app.bind_all("<Return>",lambda event : change_password_btn_func())

    ent1    .pack(fill="x",padx=25,pady=25)
    ent2    .pack(fill="x",padx=25,pady= (0,30))
    # show_btn.pack(fill="x",padx=20,pady=20)

    # customtkinter.CTkFrame(text_frame3,height=2).pack(fill="x",pady=(0,10),padx=20)

    change_password_btn.pack(fill="both",expand=1,padx=20,pady=(0,10))




    #------------------------------------------------------------------------ contact

    frame2 = customtkinter.CTkFrame(contact_tab)
    frame2.pack(fill="both",expand=1,padx=10,pady=10)


    text_frame3 = customtkinter.CTkFrame(frame2,height=310,width=450)
    text_frame3.pack_propagate(False)
    text_frame3.pack(side="left",padx=10,pady=10)

    info_frame = customtkinter.CTkFrame(frame2)
    info_frame.pack(fill="both",expand=1,padx=(0,10),pady=10)

    inputtext = customtkinter.CTkTextbox(text_frame3,height=220)
    inputtext.insert("0.0","What's your problem ?\nwrite :")
    inputtext.pack_propagate(False)
    inputtext.pack(fill="x",padx=10,pady=10)


    path = os.path.join(os.getcwd(),"App\\images\\send.png")

    send_image = customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(25, 25))


    # Function to send  `contact us` content as email
    def send_func():
        _text = inputtext.get("0.0","end")
        try:
            send_email("iraniparsiya@gmail.com","Mr.Doctor - Contact US",f"{30*'-'}\nUser Email : {give_base_info_user()[3]}\n{30*'-'}\n\n{_text}")

            CTkMessagebox(title="Mr.Doctor - Contact us",message="Thank you for your partnership.",icon="check")
        except:
            CTkMessagebox(title="Network Error !",message="There is a problem connecting to the Internet."
                ,icon=os.path.join(os.getcwd(),"App\\images\\no-net-l.png"))



    send_btn = customtkinter.CTkButton(text_frame3,text="Send",font=("calibri",20,"bold"),image=send_image,command=send_func)
    send_btn.pack(fill="both",expand=1,padx=10,pady=(0,10))

    path_l = os.path.join(os.getcwd(),"App\\images\\contact-l.png")
    path_d = os.path.join(os.getcwd(),"App\\images\\contact-d.png")

    contact_image = customtkinter.CTkImage(light_image=Image.open(path_l),
                                    dark_image=Image.open(path_d),
                                    size=(80, 80))

    customtkinter.CTkLabel(info_frame,text="",image=contact_image).pack()
    customtkinter.CTkLabel(info_frame,text=info_text,justify="left",font=("calibri",13)).pack(padx=15,pady=10)


    # return app for .mainloop()
    return app

# return_user_info_page(1).mainloop()