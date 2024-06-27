# import models
import customtkinter
from PIL import Image
from customtkinter import filedialog   
import CTkMessagebox
import os
from PIL import Image
from BtnInfo import btn_info

# Function to save a fig
def save_fig(image:Image.open):
    try:

        # Get a path to save from user
        path = filedialog.asksaveasfile(initialfile="Untitled.jpeg",
                                        defaultextension=".jpeg",
                                        filetypes=(("JPEG files",".jpeg"),("JPG files",".jpg"))
                                        )
        
        image.save(path)

        CTkMessagebox.CTkMessagebox(
        message=f"Your image was saved correctly.",
        icon="check",
        title="Mr.Doctor",
        option_1="Ok"
    )

    except:
        pass



def return_lung_plot(master:customtkinter.CTk,predicts:list) -> customtkinter.CTk :

    # set som setting of customtkinter
    customtkinter.set_appearance_mode("System")  
    customtkinter.set_default_color_theme("blue")  

    # Defind login app (type : top level)
    app = customtkinter.CTkToplevel(master) # master
    # app = customtkinter.CTk()
    app.geometry("1110x540")
    app.resizable(0,0)
    app.title("Mr.Doctor - Lung Mask")

    _bg = app._apply_appearance_mode(customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"])


    # Defind the frame just for a titles [text:str] 
    title_frame = customtkinter.CTkFrame(app,height=60,fg_color=_bg)
    title_frame.pack_propagate(False)
    title_frame.pack(fill = "both",expand=1,padx=10,pady=(10,0))

    # Defind the frame just for a images [inage:PIL.Image] 
    image_frame = customtkinter.CTkFrame(app,height=370)
    image_frame.pack_propagate(False)
    image_frame.pack(fill="x",padx=10,pady=(10,0))


    # Defind 3 frame for 3 different text image
    _frame1 = customtkinter.CTkFrame(title_frame,width=350,height=100,fg_color=_bg)
    _frame1.pack_propagate(False)
    _frame1.pack(side="left",padx=(10,0))

    _frame2 = customtkinter.CTkFrame(title_frame,width=350,height=100,fg_color=_bg)
    _frame2.pack_propagate(False)
    _frame2.pack(side="left",padx=(10,0))

    _frame3 = customtkinter.CTkFrame(title_frame,width=350,height=100,fg_color=_bg)
    _frame3.pack_propagate(False)
    _frame3.pack(side="left",padx=(10,0))


    # The 3 names for 3 images
    customtkinter.CTkLabel(_frame1,text="Original",font=("calibri",50,"bold"),text_color=("#408cd4","skyblue")).pack(anchor="center")
    customtkinter.CTkLabel(_frame2,text="Segmented",font=("calibri",50,"bold"),text_color=("#408cd4","skyblue")).pack(anchor="center")
    customtkinter.CTkLabel(_frame3,text="Masked",font=("calibri",50,"bold"),text_color=("#408cd4","skyblue")).pack(anchor="center")



    # Defind 3 frame for 3 image
    frame1 = customtkinter.CTkFrame(image_frame,width=350,height=350)
    frame1.pack_propagate(False)
    frame1.pack(side="left",pady=10,padx=(10,0))

    frame2 = customtkinter.CTkFrame(image_frame,width=350,height=350)
    frame2.pack_propagate(False)
    frame2.pack(side="left",pady=10,padx=10)

    frame3 = customtkinter.CTkFrame(image_frame,width=350,height=350)
    frame3.pack_propagate(False)
    frame3.pack(side="left",pady=10,padx=(0,10))



    # Defind and load images
    image1 = customtkinter.CTkImage(light_image=predicts[0],
                                dark_image=predicts[0],
                                size=(300, 300))
    
    image2 = customtkinter.CTkImage(light_image=predicts[1],
                                dark_image=predicts[1],
                                size=(300, 300))
    
    image3 = customtkinter.CTkImage(light_image=predicts[2],
                                dark_image=predicts[2],
                                size=(300, 300))

    
    customtkinter.CTkLabel(frame1,text="",image=image1).pack(fill="both",expand=1)
    customtkinter.CTkLabel(frame2,text="",image=image2).pack(fill="both",expand=1)
    customtkinter.CTkLabel(frame3,text="",image=image3).pack(fill="both",expand=1)

    # Load base image for design
    path = os.path.join(os.getcwd(),"App\\images\\save as.png")

    image = customtkinter.CTkImage(light_image=Image.open(path),
                                    dark_image=Image.open(path),
                                    size=(30,30))


    # `Save image` button 
    btn = customtkinter.CTkButton(app,text="Save image",font=("calibri",15,"bold"),command=lambda : save_fig(predicts[1]),height=50,image=image)
    btn.pack(fill="both",padx=10,pady=10,expand=1)

    btn_info(btn,"Save the segmented image of the lung.")

    # return app for .mainloop()
    return app
