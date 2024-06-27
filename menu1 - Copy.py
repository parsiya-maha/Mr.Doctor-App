# improt models
import customtkinter
from CTkMenuBar import *
import CTkMessagebox
from tkinter import ttk
import matplotlib
import os
import webbrowser
from PIL import Image
matplotlib.use("TkAgg")

from DataBase import clear_all_log
from funcs import is_login
from network import internet_on,send_email

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from matplotlib.figure import Figure
from DataBase import true_false_value

from funcs import is_login


"""
File:
    menu1.py

Summary:
    This file (menu1.py) helps the master menu (menu.py)
"""

# All scores for `Score` tab
def return_models_score_menu(master:CustomDropdownMenu):

    a1 = master.add_submenu("Brain Tumors")
    customtkinter.CTkLabel(a1,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a1,text="99.88%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")


    a2 = master.add_submenu("Breast Cancer")
    customtkinter.CTkLabel(a2,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a2,text="99.47%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")


    a3 = master.add_submenu("Cervical Cancer")
    customtkinter.CTkLabel(a3,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a3,text="99.58%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")


    a4 = master.add_submenu("Kidney Stone")
    customtkinter.CTkLabel(a4,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a4,text="99.76%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")

    a5 = master.add_submenu("Lung Cancer")
    customtkinter.CTkLabel(a5,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a5,text="99.80%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")

    a6 = master.add_submenu("Lung Mask")
    customtkinter.CTkLabel(a6,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a6,text="94.30%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")

    a7 = master.add_submenu("To Recognize")
    customtkinter.CTkLabel(a7,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a7,text="99.94%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")


    a8 = master.add_submenu("To Recognize And Predict")
    customtkinter.CTkLabel(a8,text="Score : ",font=("calibri",20)).pack(pady=15,padx=(10,0),side="left")
    customtkinter.CTkLabel(a8,text="99.63%",text_color=("#408cd4","skyblue"),font=("calibri",20)).pack(pady=15,padx=(0,10),side="right")

# Function for lop plot menu (true/false preadict) [just return fig]
def plot1(master:customtkinter.CTkFrame,app:customtkinter.CTk):

    # fig.add_subplot().pie(true_false_value(),["True Predict","False Predict"],colors=["blue","red"])
    _bg_color = app._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
    
    # gray17 -> #282424
    # gray86 -> #ebebeb

    if _bg_color == "gray17" :
        bg_color = "#282424"

    else : # gray86
        bg_color = "#ebebeb"

    
    if list(true_false_value()) != [0,0] :


        fig = Figure(facecolor=bg_color)

        f = fig.add_subplot()


        autotexts1, autotexts2, autotexts3 = f.pie(list(true_false_value()),labels=["True","False"],
                                                colors=["blue","red"],autopct="%1.1f%%",labeldistance=1.2
                                                ,explode=[0.05]*2
                                                )

        for autotext in autotexts2:
            if _bg_color == "gray17" :
                autotext.set_color('white')
            else :
                autotext.set_color('black')

            autotext.set_fontsize(15)

        for autotext in autotexts3:
            autotext.set_color('white')
            autotext.set_fontsize(18)

        
        canvas = FigureCanvasTkAgg(fig,master)
        canvas.draw()

        return canvas.get_tk_widget()
    

    return customtkinter.CTkLabel(master,text="No log yet.",
                         font=("calibri",30,"bold"),
                         text_color=("#408cd4","skyblue"),
                         padx=30,
                         pady=30
                         )

# Function to retrun error page whene user doesn't login or signup
def return_not_login_error(master:customtkinter.CTkFrame):
    l_path = os.path.join(os.getcwd(),"images\\lock_l.png")
    d_path = os.path.join(os.getcwd(),"images\\lock_d.png")

    image = customtkinter.CTkImage(light_image=Image.open(l_path),
                                    dark_image=Image.open(d_path),
                                    size=(200, 200))
    
    master.configure(corner_radius=15)


    customtkinter.CTkLabel(master,text="",image=image).pack(pady=(10,20),padx=10,side="right")

    customtkinter.CTkLabel(master,text="First\nLogin or Sign up !",font=("calibri",40,"bold")).pack(padx=(20,10),pady=10,side="left")

# Function for log plot menu
def return_log_plot_menu(master:CustomDropdownMenu):
    frame = master.add_submenu("Log plot")

    if not is_login():
        return_not_login_error(frame)
        return

    p = [plot1(frame,frame)]
    p[0].pack(fill="both",expand=1)

    def loop(p):
        
        p[0].pack_forget()

        p[0] = plot1(frame,frame)

        p[0].pack(fill="both",expand=1)

        frame.after(1000,lambda:loop(p))

    loop(p)

# Function for `model layers` image
def return_model_layer_menu(master:CustomDropdownMenu):
    frame = master.add_submenu("Models layer")
    path = os.path.join(os.getcwd(),"images\\model layer.png")


    image = customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(306, 500))
    
    customtkinter.CTkLabel(frame,text="",image=image).pack(fill="both",expand=1,padx=10,pady=10)


# Function to return user info frame
def return_user_info(master:CustomDropdownMenu):
    

    text3 = """
Hello, the Mr.Doctor team hopes that you have enjoyed 
our app and made full use of it.Mr.Doctor's team hopes 
that various cancers will be eradicated in the near future, 
and how great it would be if our team also participates 
in this great and global victory.Good luck

- Parsiya Hassanzadeh
- Mohamad Mehdi Khodaie
"""

    frame2 = master.add_submenu("About us")

    text_frame3 = customtkinter.CTkFrame(frame2,height=310,width=420)
    text_frame3.pack_propagate(False)
    text_frame3.grid(row=0,column=0,padx=10,pady=10,sticky="n")

    bg_color3_f = frame2._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])

    # path31 = "images\\home.png"
    # image_obj31 = customtkinter.CTkImage(light_image=Image.open(path31),
    #                               dark_image=Image.open(path31),
    #                               size=(300, 300))

    # customtkinter.CTkLabel(frame2,text="",image=image_obj31).grid(row=0,column=1,sticky="n")

    customtkinter.CTkLabel(text_frame3,text="Mr.Doctor",font=("calibri",40,"bold"),text_color=("#408cd4","skyblue")).pack(pady=(5,0))

    customtkinter.CTkLabel(text_frame3,text=text3,font=("calibri",15),justify='left').pack()

    

    more_btn_frame = customtkinter.CTkFrame(text_frame3,height=60,width=260,fg_color=bg_color3_f)
    more_btn_frame.pack_propagate(False)
    more_btn_frame.pack(side="bottom",padx=10,pady=(0,10),anchor="se")
    
    bg_color3 = more_btn_frame._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])


    path32 = "images\\github.png"
    image_obj32 = customtkinter.CTkImage(light_image=Image.open(path32),
                                  dark_image=Image.open(path32),
                                  size=(40, 40))
    
    path33 = "images\\gmail.png"
    image_obj33 = customtkinter.CTkImage(light_image=Image.open(path33),
                                  dark_image=Image.open(path33),
                                  size=(40, 40))

    path34 = "images\\linkedin.png"
    image_obj34 = customtkinter.CTkImage(light_image=Image.open(path34),
                                  dark_image=Image.open(path34),
                                  size=(40, 40))
    
    path35 = "images\\facebook.png"
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


# ERROR 404 -> [NOT use in project (for now not in fiture)]
def return_setting_set_color(master:CustomDropdownMenu):
    frame = master.add_submenu("Appearance mode")

    customtkinter.CTkLabel(frame,text="Choice the appearance mode :",font=("calibri",25,"bold")).pack(pady=(25,10),padx=25)

    def chnage_mode(mode):
        customtkinter.set_appearance_mode(mode)

    om = customtkinter.CTkOptionMenu(
        frame,
        values=["System","Light","Dark"],
        command=chnage_mode
    )


    om.pack(pady=(25,5),padx=25,fill="x")


# Function to return all shortcuts (in one frane)
def return_all_shortcuts(master:CustomDropdownMenu):

    frame = master.add_submenu("Shortcuts")

    value = [
        ["Login","Shift+L"],
        ["Login","Shift+L"],
        ["Sign up","Shift+S"],
        ["Models score","Ctrl+Shift+S"],
        ["Log app","Ctrl+Shift+L"],
        ["Log plot","Shift+P"],
        ["Log out","Shift+Down"],
        ["User info","Shift+U"],
        ["Upload image","Ctrl+Shift+U"],
        ["Predict","Enter"]
    ]


    for f,i in zip(value,range(len(value))):

        name = f[0]
        command = f[1]

        customtkinter.CTkLabel(frame,text=name,font=("calibri",20,"bold"),
                               text_color=("#408cd4","skyblue")).grid(row=i,column=0,padx=(20,5),pady=10,sticky="w")
        
        customtkinter.CTkLabel(frame,text=command,
                               font=("calibri",20)).grid(row=i,column=1,pady=10,padx=(10,20),sticky="w")
        
# Function to clear all log
def return_clear_all(master:CustomDropdownMenu):

    def func():
        if is_login():
            sms = CTkMessagebox.CTkMessagebox(
                title="Delete?",
                message="Do you want to delete all log\n(form your account)",
                icon="question",
                option_1="Yes",
                option_2="Cancel"
            )

            if sms.get() == "Yes" :
                clear_all_log()

    frame = master.add_option(option="Clear all log",command=func)


# ERROR 404 -> [NOT use in project (for now not in fiture)]
def return_contact_us(master:CustomDropdownMenu):

    _frame = master.add_submenu("Contact us")
    _frame.configure(corner_radius=15)
    frame = customtkinter.CTkFrame(_frame)
    frame.pack(fill="both",expand=1)

    if not internet_on() :
        l_path = os.path.join(os.getcwd(),"images\\no-net-l.png")
        d_path = os.path.join(os.getcwd(),"images\\no-net-d.png")

        image = customtkinter.CTkImage(light_image=Image.open(l_path),
                                        dark_image=Image.open(d_path),
                                        size=(100, 100))
        
        frame.configure(corner_radius=15)

        customtkinter.CTkLabel(frame,text="",image=image).pack(pady=(10,20),padx=10,side="right")

        customtkinter.CTkLabel(frame,text="No internet\nnetwork found !",font=("calibri",35,"bold")).pack(padx=(20,10),pady=10,side="left")

    else :
        textinput = customtkinter.CTkTextbox(frame,width=400,height=300,border_width=10,border_spacing=10)
        textinput.pack(fill="x",padx=10,pady=10)