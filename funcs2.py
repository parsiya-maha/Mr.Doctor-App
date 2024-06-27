# Import models
import os,time
from login import return_login_page
import customtkinter
import subprocess
import sys
from customtkinter import filedialog   
from PIL import Image
import CTkTable
import pandas as pd
# from AI.BrainTumors import BrainTumorsPredictImage
# from AI.LungCancer import LungCancerPredictImage
# from AI.KidneyStone import KidneyStonePredictImage
# from AI.ToRecognize import ToRecognizePredictImage
# from AI import ToRecognizeAndPredictImage

from DataBase import check_login_data_in_json,islogin_json,check_login_data,change_islogin_json,make_id_for_user
from DataBase import find_last_id_json,add_log_json,how_is_login_json
from DataBase import change_one_value_in_json_data,find_index_from_id_json,delete_log_from_json_data,give_up_tabel_json_data_in_log


# Function to check login data [username , password]
def check_login_data(username,password):
    return check_login_data_in_json(username,password)


# Function to check the user is in login time or not
def is_login():
    return islogin_json()


# Function to change `is login` data when user login
def change_is_login(_bool,username):
    return change_islogin_json(_bool,username)


# Run login app after user click login btn
def go_to_login_func(app:customtkinter.CTk):
    if is_login(): ...

    else : 
        app.withdraw()
        return_login_page().mainloop()

        # app.deiconify()
        app.destroy()
        subprocess.call([sys.executable, 'main.py'])

# Run signup app after user click signup btn
def go_to_signup_func(app:customtkinter.CTk):
    if is_login(): ...

    else : 
        app.withdraw()
        return_signup_page().mainloop()

        # app.deiconify()
        app.destroy()
        subprocess.call([sys.executable, 'main.py'])        
        
# Defind base path var
PATH = None


# Function to choice image from pc (open file dialog)
def choice_image(frame:customtkinter.CTkFrame,conts:list):

    try: # Try to open file
        path = filedialog.askopenfilename(initialdir=os.getcwd,
                                        title="Please select image file:",
                                        filetypes=(("All image",['.png', '.jpeg', '.jpg']),("PNG files",".png"),("JPEG files",".jpeg"),("JPG files",".jpg"))
                                        )
        

        img = customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(200, 200))

    except: # If users click `open file` btn but they dont choice image
        return

    conts[0].destroy()
    conts.pop()

    # Show image after choice that
    l = customtkinter.CTkLabel(frame,image=img,text="")
    l.pack(padx=50,pady=50)

    conts.append(l)


    global PATH
    PATH=path

    del path
    return PATH


# Find last log image id
def last_log_id():  
    return find_last_id_json()


# Function to predict image with option menu data
def predit_from_widgets(_option:customtkinter.CTkOptionMenu,tabel:CTkTable.CTkTable,progressbar:customtkinter.CTkProgressBar):

    if PATH == None:
        return ["First Upload one image.","nan"]


    # Start timer
    START_TIME = time.time()

    # Check for OptionMenu data (what user choice)
    option = _option.get()
    
    if option == "BrainTumors":
        from AI.BrainTumors import BrainTumorsPredictImage as predict_model

    elif option == "LungCancer":
        from AI.LungCancer import LungCancerPredictImage as predict_model

    elif option == "KidneyStone":
        from AI.KidneyStone import KidneyStonePredictImage as predict_model

    elif option == "ToRecognize":
        from AI.ToRecognize import ToRecognizePredictImage as predict_model

    elif option == "ToRecognizeAndPredict":
        from AI import ToRecognizeAndPredictImage as predict_model


    # predict model
    res = predict_model(PATH)
    TIME = time.time() - START_TIME


    # Defind values for tabel
    values = [
        ["Result","Time"],
        [res,f"{TIME:.3f}"]
    ]

    # Change new data with old data in tabel
    tabel.configure(values=values)


    tf = float(f"{TIME:.3f}")
    tf *= (0.5)
    tf = float(f"{tf:.5f}")

    progressbar.set(min(1,tf))

    # Add log to log file data (.json)
    # last_log_id()+1),option,res,f"{TIME:.3f}",PATH,"1"

    add_log_json(
        last_log_id()+1,
        how_is_login_json(),
        option,
        res,
        round(TIME,3),
        PATH,
        1
    )


# Change just one value in data csv (for log) with [row,col]
def change_one_value_in_data(row,column,value):
    change_one_value_in_json_data(row,column,value)


# Find index of log from id (log data)
def find_index_from_id(_id):
    return find_index_from_id_json(int(_id))


# Delete one log from data with id
def delete_log_from_data(_id):
    delete_log_from_json_data(int(_id))


# For lung path (>60 chr) , make them short
def make_path_short(path,n):
    if len(path) <= n : 
        d =  n-len(path)
        a1 = d//2
        a2 = d - a1

        return a1*" "+path+a2*" "

    else:
        n -= 3
        return "..." + path[::-1][:n][::-1]


# Return data of `info tabel` in log app :
#   Count    (len )
#   Point    (mean)
#   Time     (mean)
#   Option   (most)
#   Result   (most)

def give_up_tabel_data_in_log():
    return give_up_tabel_json_data_in_log()


