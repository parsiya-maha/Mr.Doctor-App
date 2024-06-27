# Import model
import customtkinter,os
from PIL import Image
from funcs import choice_image
from BtnInfo import btn_info

# Default image before upload image
def upload_image_sub_frame(master)->customtkinter.CTkLabel:

    path = os.path.join(os.getcwd(),"App\\images\\upload1.png")

    img = customtkinter.CTkImage(light_image=Image.open(path),
                                dark_image=Image.open(path),
                                size=(152*1.3,100*1.3)) #200x200 - 14*12, 11*12

    l = customtkinter.CTkLabel(master,image=img,text="",width=200,height=200)
    return l




text1 = """We work on the"""


# LABEL -> show some text
def main_text1(master:customtkinter.CTk)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text1,
                                font=("calibri",30,"bold"))
    return text

# LABEL -> show some text
def main_text1_auto(master:customtkinter.CTk)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text="",
                                text_color=("#408cd4","skyblue"),
                                font=("calibri",30,"bold"))
    return text


# BUTTON -> show custom btn
def upload_image_btn(master:customtkinter.CTk,frame,conts)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master=master,
                                  text="Upload Image",
                                  font=("calibri",30),
                                  width=300,
                                  height=50,
                                  corner_radius=30,
                                  command=lambda:choice_image(frame,conts)
                                  )
    
    btn_info(btn,"Upload a related photo from your system files.")

    return btn

    
text2 = "Choice model type :"

# LABEL -> show some text
def text_choice_model_type(master:customtkinter.CTk)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text2,
    #                                justify='left',
                                font=("calibri",20,"bold"))
    return text