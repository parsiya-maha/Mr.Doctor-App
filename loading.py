# import models
import winsound
import threading
import customtkinter
from PIL import Image
import winsound

"""
File:
    loading.py

Describtion :
    A loading page without titlebar 
    (Whene the ML models are loading)

Time:
    about 10 seconds
    (It's diffrent in another system) 

"""


def return_loading_app(master:customtkinter.CTk):

    # set som setting of customtkinter
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    # Defind login app (type : top level)
    # app = customtkinter.CTk()
    app = customtkinter.CTkToplevel(master)
    app.geometry("650x415+100+100")
    app.overrideredirect(True)


    path = r"images\loading.png"

    image =  customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(25*12, 22*12))

    image_lbl = customtkinter.CTkLabel(app,text="",image=image)
    image_lbl.place(x=309,y=65)

    path1 = r"images\loading.png"
    path2 = r"images\loading2.png"

    # Function to animate the image
    def image_animation(image_pos):
        if not image_pos :
            # print(0)
            img = customtkinter.CTkImage(light_image=Image.open(path1),
                                    dark_image=Image.open(path1),
                                    size=(25*12, 22*12))
            
            image_lbl.configure(image=img)

            image_lbl.after(1000,lambda : image_animation(1))

        else :
            # print(1)
            img = customtkinter.CTkImage(light_image=Image.open(path2),
                                    dark_image=Image.open(path2),
                                    size=(25*12, 22*12))
            
            image_lbl.configure(image=img)

            image_lbl.after(1000,lambda : image_animation(0))

    # start animate
    image_animation(0)



    # Body of loading app
    customtkinter.CTkLabel(app,text="Mr.Doctor",font=("calibri",75,"bold"),text_color=("blue","skyblue")).place(x=45,y=30)
    load_text = customtkinter.CTkLabel(app,text="...",font=("calibri",35,"italic"),padx=0)
    load_text.place(x=170,y=130)
    customtkinter.CTkLabel(app,text="Loading ",font=("calibri",35,"italic")).place(x=45,y=130)

    frame = 0

    # Animate for `...` text
    def load_texx_ooo():
        t = load_text.cget("text")

        if t == "":
            load_text.configure(text=".")

        elif t == ".":
            load_text.configure(text="..")

        elif t == "..":
            load_text.configure(text="...")

        elif t == "...":
            load_text.configure(text="")

        load_text.after(550,load_texx_ooo)

    # Start text animate
    load_texx_ooo()


    # Defind and start a progress bar
    prog = customtkinter.CTkProgressBar(app,mode="indeterminate",width=560)
    prog.place(x=43,y=360)
    prog.start()


    # Copyright text
    customtkinter.CTkLabel(app,text="© 2024 Mr.Doctor. All rights reserved.",font=("calibri",15,"italic")).place(x=42,y=375)

    # return app for .mainloop()
    return app
