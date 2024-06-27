# Import models
import customtkinter
import pandas as pd
import CTkTable
from PIL import Image
import os
import pyperclip
import CTkMessagebox
import json
import jmespath
import DataBase

from funcs2 import change_one_value_in_data,find_index_from_id,delete_log_from_data
from funcs2 import make_path_short,give_up_tabel_data_in_log

from DataBase import how_is_login_json,return_json_data_as_list
from BtnInfo import btn_info


# Base custtomtkinter setting
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

def return_log():...

# Make one frame for one log
def make_one_frame(master,log:list,main_tabel):

    log_frame = customtkinter.CTkFrame(master,height=200)

    # Show base frame in root(app)

    # tabel_frame = customtkinter.CTkFrame(log_frame,width=915)
    tabel_frame = customtkinter.CTkFrame(log_frame,width=715)

    tabel_frame.pack_propagate(False)
    tabel_frame.grid(row=0,column=0,padx=10,pady=10,sticky="ne")

    image_frame = customtkinter.CTkFrame(log_frame)
    image_frame.grid(row=0,column=1,pady=10,sticky="ne")

    info_frame = customtkinter.CTkFrame(log_frame,width=160,height=200)
    info_frame.pack_propagate(False)
    info_frame.grid(row=0,column=2,padx=10,pady=10,sticky="ne")


    tabel_data =[]

    _log = log.copy()
    
    # Make path short
    _log[4] = make_path_short(_log[4],30)
    _log[2] = make_path_short(_log[2],40)




    # Make list (`tabel_list`) for `info tabel` values
    tabel_data.append(["Id","Option","Result"])
    tabel_data.append(_log[:3])
    tabel_data.append(["Time","Path","Point"])
    tabel_data.append(_log[3:])

    # Defind `tabel` widget
    tabel = CTkTable.CTkTable(tabel_frame,row=4,column=3,values=tabel_data)
    tabel.pack(pady=20,padx=20,fill="both",expand=True,anchor="e")

    # NORMAL -> the image path is correct
    if os.path.exists(str(log[4])):
        path = str(log[4])
        
    # UNDEFIND -> the image path not defind (not correct)
    else:
        # Base path for UNDEFIND images
        path = os.path.join(os.getcwd(),"images\\no_image1.png")

    # Defind CTkImage widget
    my_image = customtkinter.CTkImage(light_image=Image.open(path),
                                dark_image=Image.open(path),
                                size=(160, 160))

    # Show image as CTkLabel
    image_label = customtkinter.CTkLabel(image_frame,image=my_image,text="")
    image_label.pack(padx=20,pady=20)

    
    # Show `BIN` btn image on widget
    bin_path = os.path.join(os.getcwd(),"images\\bin.png")

    bin_image = customtkinter.CTkImage(light_image=Image.open(bin_path),
                                dark_image=Image.open(bin_path),
                                size=(30,30))

    bin_btn = customtkinter.CTkButton(info_frame,text="",image=bin_image,height=50,width=50
                                    ,command=lambda:delete_log(log_frame,log[0],main_tabel))
    
    btn_info(bin_btn,"Delete the selected log.")
                                    
    # bin_btn.pack(padx=10,pady=17)
    bin_btn.pack(padx=10,pady=(10,0),fill="both",expand=1)


    # Show `COPY` btn image on widget
    copy_path = os.path.join(os.getcwd(),"images\\copy.png")

    copy_image = customtkinter.CTkImage(light_image=Image.open(copy_path),
                                dark_image=Image.open(copy_path),
                                size=(30, 30))

    copy_btn = customtkinter.CTkButton(info_frame,text="",image=copy_image,
                                        command=lambda:copy_path_btn(log[4]),
                                        height=50,width=50)

    btn_info(copy_btn,"copy log image path (in clipboard).")
    
    # copy_btn.pack(padx=10,pady=10)   
    copy_btn.pack(padx=10,pady=(10,0),fill="both",expand=1)   
    
    # Defind defult value of switch widget
    value_of_switch = "on" if int(log[5]) else "off"

    switch_var = customtkinter.StringVar(value=value_of_switch)
    switch = customtkinter.CTkSwitch(info_frame, text="Prediction is true", command=lambda:switch_click(switch_var,tabel,main_tabel),
                                variable=switch_var, onvalue="on", offvalue="off")

    switch.pack(padx=10,pady=10)

    return log_frame



# Update `info tabel` in log app
def update_up_log_tabel(tabel:CTkTable.CTkTable):

    c = give_up_tabel_data_in_log()

    for index in range(len(c)):
        tabel.insert(1,index,c[index])


# Delete log in log app (gui not data)
def delete_log(frame,_id,main_tabel):
    frame.destroy()

    delete_log_from_data(_id)

    update_up_log_tabel(main_tabel)


# Change switch value with click
def switch_click(s:customtkinter.StringVar,tabel:CTkTable.CTkTable,main_tabel):

    if s.get() == "on":
        
        # Change point value
        tabel.insert(row=3,column=2,value=1)
        _id = tabel.cget("values")[1][0]

        row = find_index_from_id(_id)

        change_one_value_in_data(row,6,1)

        update_up_log_tabel(main_tabel)

    else:

        # Change point value
        tabel.insert(row=3,column=2,value=0)
        _id = tabel.cget("values")[1][0]

        row = find_index_from_id(_id)

        change_one_value_in_data(row,6,0)
        update_up_log_tabel(main_tabel)



# Read data [log.json] and return data as list
def return_data_as_list():
    return return_json_data_as_list()
    
    

# Copy path in clipboard and show in massage box
def copy_path_btn(path):

    pyperclip.copy(path)

    CTkMessagebox.CTkMessagebox(
        message=f"Your address was copied correctly.",
        icon="check",
        title="Mr.Doctor",
        option_1="Ok"
    )





# Function to make main of log app
def return_log_app(master):
    
    # Defind app var and set some setting
    # app = customtkinter.CTkToplevel() 
    app = customtkinter.CTkToplevel(master)

    # app.geometry("1400x700")
    app.geometry("1200x700")
    app.resizable(0,0)
    app.title("Mr.Doctor - Logs")

    icon_path = "images\\project icon.ico"
    app.after(250,lambda:app.iconbitmap(icon_path))
    

    # Defind instance var
    data_logs = return_data_as_list()
    ns = len(data_logs)


    # Defind `mian` and `sub` frame 
    des_frame = customtkinter.CTkFrame(app,height=200)
    des_frame.pack(fill="x",padx=10,pady=10)

    prog_frame = customtkinter.CTkFrame(app)
    prog_frame.pack(fill="x",padx=10)

    # Make progress bar for design
    prog = customtkinter.CTkProgressBar(prog_frame,mode="indeterminate")
    prog.pack(fill="x")
    prog.start()

    # Defind `info tabel` values for show it
    up_tabel_data = [
        ["Count","Point (Mean)","Time (Mean)","Option (Most)","Result (Most)"],
        give_up_tabel_data_in_log()
    ]

    # Defind and show Tabel from values
    up_tabel = CTkTable.CTkTable(des_frame,row=2,column=5,values=up_tabel_data,pady=2)
    up_tabel.pack(anchor="center",pady=10,fill="x",padx=10)


    # Make scrollable frame
    _win = customtkinter.CTkScrollableFrame(app)
    _win.pack(fill="both",expand=True,padx=10,pady=(10,10))


    win = customtkinter.CTkFrame(_win)
    win.pack(fill="both",expand=True)



    # Add and show one by one log frame

    for index in range(len(data_logs)):

        log = data_logs[index]

        make_one_frame(win,log,up_tabel).pack(pady=10,padx=(10,30),anchor="ne",fill="x")

    return app


# Main loop for log app
# return_log_app().mainloop()


