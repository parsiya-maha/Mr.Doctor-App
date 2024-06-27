# Import models
import customtkinter,os
import matplotlib.pyplot as plt
from PIL import Image
from tkinter import ttk
import matplotlib
import numpy as np

matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
    
from matplotlib.figure import Figure

from DataBase import true_false_value




def plot1(master:customtkinter.CTkFrame,app:customtkinter.CTk):

    # fig.add_subplot().pie(true_false_value(),["True Predict","False Predict"],colors=["blue","red"])
    _bg_color = app._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])
    
    # gray17 -> #282424
    # gray86 -> #ebebeb

    if _bg_color == "gray17" :
        bg_color = "#282424"

    else : # gray86
        bg_color = "#ebebeb"


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




def return_tfp_page(master)->customtkinter.CTkToplevel:

    # set som setting of customtkinter
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    # Defind project-part app (type : top level)
    app = customtkinter.CTkToplevel(master)
    # app.geometry("500x450")
    app.title("Mr.Doctor - true/false plot")

    customtkinter.CTkLabel(app,text="True/False plot (pie)",font=("calibri",40,"bold")).pack(pady=15)

    Frame = customtkinter.CTkFrame(app)
    Frame.pack(padx=10,pady=10)
    
    plot1(Frame,app).pack(fill="both",expand=1,padx=10,pady=10)


    app.resizable(0,0)
    return app


# return_tfp_page().mainloop()