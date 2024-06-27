# import models
import customtkinter
import CTkMessagebox


# show message box if user right click on right click
def btn_info(btn:customtkinter.CTkButton,
             message : str,
             scr : str = "<Button-3>"
             ):
    
    def func(event):
        CTkMessagebox.CTkMessagebox(title="Info",message=message)

    btn.bind(scr,func)

