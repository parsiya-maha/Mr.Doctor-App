# import models
import customtkinter
import os
from PIL import Image
import cv2
import CTkTable
import threading



# return help window (Toplevel)
def return_help_app(master:customtkinter.CTk) -> customtkinter.CTkToplevel :
    # set som setting of customtkinter
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    # Defind login app (type : top level)
    app = customtkinter.CTkToplevel(master)
    app.geometry("550x600")
    app.minsize(550,600)
    app.title("Mr.Doctor - Help")


    frame = customtkinter.CTkScrollableFrame(app,corner_radius=0,fg_color="#272323")
    # frame = CTkXYFrame.CTkXYFrame(app,corner_radius=0,fg_color="#272323")




    PATH = r"App\images\\help.png"
    WIDTH_LIMIT = 500

    image_size = cv2.imread(PATH).shape
    ALPHA = image_size[0] / image_size [1]




    image = customtkinter.CTkImage(light_image=Image.open(PATH),
                                dark_image=Image.open(PATH),
                                size=(WIDTH_LIMIT, WIDTH_LIMIT*ALPHA))
    
    label = customtkinter.CTkLabel(frame,text="",image=image)

    # Function to resize image (help)
    def resize(value):
        _image = customtkinter.CTkImage(light_image=Image.open(PATH),
                                dark_image=Image.open(PATH),
                                size=(value, value*ALPHA))
        label.configure(image=_image)


    # Thread function to resize help image
    def th_resize(value):
        th = threading.Thread(target=resize,args=[value])
        th.start()

    
    slider = customtkinter.CTkSlider(app,from_=100,to=1000,command=th_resize,number_of_steps=50)
    slider.set(500)


    slider.pack(pady=10,padx=10,fill="x")
    frame.pack(fill="both",expand=1)
    label.pack(pady=10)


    # return app for .mainlopp() method
    return app
