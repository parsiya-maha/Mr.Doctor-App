import loading
import threading
import customtkinter
from menu import return_menu
import time

# Make app root and set some property of that
app = customtkinter.CTk() 
app.geometry("1100x700+100+50")
app.resizable(0,0)
app.title("  ")

icon_path = "images\\project icon.ico"
app.iconbitmap(icon_path)


LOADING = True

loading_app = loading.return_loading_app(app)

def all_import():
    from AI.BrainTumors import BrainTumorsPredictImage
    from AI.LungCancer import LungCancerPredictImage
    from AI.KidneyStone import KidneyStonePredictImage
    from AI.ToRecognize import ToRecognizePredictImage
    from AI.BreastCancer import BreastCancerPredictImage
    from AI.CervicalCancer import CervicalCancerPredictImage
    from AI import ToRecognizeAndPredictImage

    global LOADING

    LOADING = False
    loading_app.quit()


th_load = threading.Thread(target=all_import,name="Imports")
th_load.start()

while LOADING :
    loading_app.update()

loading_app.destroy()


return_menu(app)


# Import models
import customtkinter

from welcome_frames import option_frame_text1,option_frame_text2,option_frame_text3,option_frame_text4,user_info_btn
from welcome_frames import more_info_btn,go_to_login,go_to_model_score,log_app,go_to_signup,logout_app,log_plot_app

from main_frame import brain_image_label,main_signup
from main_frame import text1_to_main_frame,text2_to_main_frame,text3_to_main_frame,text4_to_main_frame,main_login

from funcs import is_login,choice_image

from main_upload_image_frame import upload_image_sub_frame,main_text1,main_text1_auto,upload_image_btn
from main_upload_image_frame import text_choice_model_type

from choice_mode_type_frame import text_choice_model_type,option_model_widget,text_option
from choice_mode_type_frame import predict_btn

from result_predict_frame import result_tabel,predict_progressbar,n_text

from CTkAnimation import AutoTextWriter
import shortcuts


# Base customtkinter setting
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

# info frame part
frame = customtkinter.CTkFrame(app,width=300)
frame.pack(fill="y",side="left",pady=10,padx=(10,0))

customtkinter.CTkLabel(frame,
                       width=280,
                       text="Mr.Doctor",
                       font=("...",30,"bold")
                       ).pack(pady=(35,20))

if is_login():
    option_frame = customtkinter.CTkScrollableFrame(frame,height=490)
else:
    option_frame = customtkinter.CTkScrollableFrame(frame,height=700)


option_frame.pack(fill="both",padx=10,pady=10)

option_frame_text1(option_frame).pack()

more_info_btn(option_frame).pack()

go_to_model_score(option_frame).pack(pady=10)

option_frame_text2(option_frame).pack()

go_to_login(option_frame,app).pack()

go_to_signup(option_frame,app).pack(pady=10)

logout_app(option_frame,app).pack(pady=(0,10))

option_frame_text4(option_frame).pack()

log_app(option_frame,app).pack(pady=(0,10))

log_plot_app(option_frame,app).pack(pady=(0,10))

option_frame_text3(option_frame).pack(anchor="nw",padx=10)

customtkinter.CTkLabel(option_frame,text="\n\n").pack()

if is_login():
    user_info_btn(frame,app).pack(padx=10)


# Main screan

if is_login() : # When user was login

    # Defind frame var 
    main_frame = customtkinter.CTkFrame(app,height=1200)
    main_frame.pack(fill="both",padx=10,pady=10,expand=True)
    
    title_frame = customtkinter.CTkFrame(main_frame,
                                         height=80,

                    fg_color=main_frame._apply_appearance_mode(
                    customtkinter.ThemeManager.theme["CTkFrame"]["fg_color"]))
    

    title_frame.pack_propagate(False)
    title_frame.pack(fill="x",padx=10,pady=10)

    main_text1(title_frame).pack(side="left",padx=(150,15))

    # Animate text
    cancers_names_lbl = main_text1_auto(title_frame)
    cancers_names_lbl.pack(side="left")

    # All auto texts
    AutoTextWriter.MultiNamesAnimate(cancers_names_lbl,[
        "BrainTumors",
        "BreastCancer",
        "CervicalCancer",
        "KidneyStone",
        "LungCancer",
        "LungMask"

    ]).run()

    wo_frame = customtkinter.CTkFrame(main_frame)
    wo_frame.pack(fill="x",padx=10)

    main_fram_wo_text = customtkinter.CTkFrame(wo_frame)
    main_fram_wo_text.grid(row=0,column=0,padx=10,pady=10)

    model_option_frame = customtkinter.CTkFrame(wo_frame,width=395,height=405)
    model_option_frame.grid(row=0,column=1,padx=(0,10),pady=12,sticky="n")

    result_frame = customtkinter.CTkFrame(main_frame,height=140)
    result_frame.pack(fill="both",expand=True,padx=10,pady=10)

    upload_image_frame = customtkinter.CTkFrame(main_fram_wo_text)
    upload_image_frame.pack(padx=15,pady=15,anchor="nw")

    upload_image_conts = upload_image_sub_frame(upload_image_frame)
    upload_image_conts.pack(padx=50,pady=50)

    list_uploaded_image = [upload_image_conts]
    
    
    # Bind image space to open file 
    upload_image_frame.bind("<Button-1>",lambda event:choice_image(upload_image_frame,list_uploaded_image))
    upload_image_conts.bind("<Button-1>",lambda event:choice_image(upload_image_frame,list_uploaded_image))
    app.bind_all("<Control-Shift-U>",lambda event:choice_image(upload_image_frame,list_uploaded_image))


    upload_image_btn(main_fram_wo_text,upload_image_frame,list_uploaded_image).pack(anchor="w",padx=15,pady=(10,15))

    text_choice_model_type(model_option_frame).pack(pady=30,padx=(20,0),anchor="nw")
    
    option_model_conts = option_model_widget(model_option_frame)
    option_model_conts.pack(padx=(20,20),anchor="nw")

    text_option(model_option_frame).pack(pady=(10,10),padx=40,anchor="w")

    n_text(result_frame).pack(anchor="nw",padx=(10,0))

    # Add progressbar bar to predict part
    predict_progressbar_const = predict_progressbar(result_frame)
    predict_progressbar_const.pack(padx=10,pady=(0,0),fill="x")


    # Result tabel -> tabel = [ massage , time ]
    result_tabel_conts = result_tabel(result_frame)
    result_tabel_conts.pack(fill="both",expand=True,padx=10,pady=10)


    # Main predict function

    predict_btn(model_option_frame,option_model_conts,result_tabel_conts,predict_progressbar_const,app).pack(padx=20,pady=(5,14.7))


    # shortcuts
    shortcuts.bind_predict(app,option_model_conts,result_tabel_conts,predict_progressbar_const)
    shortcuts.bind_models_score(app)
    shortcuts.bind_log_app(app)
    shortcuts.bind_log_out(app)
    shortcuts.bind_user_info(app)
    shortcuts.bind_log_plot(app)


else : # Else doesn't login (first run app)

    # Defind all design widgsts
    
    main_frame = customtkinter.CTkFrame(app,height=1200)
    main_frame.pack(fill="both",padx=10,pady=10)

    # 190
    pady_value = 180
    animate_state = "+"

    brain_image = brain_image_label(main_frame)
    brain_image.pack(side="right",anchor="ne",pady=(190,0))

    def image_animate():
        # (180,200)
        global pady_value,animate_state

        if pady_value <= 180 :

            pady_value += 0.7
            animate_state = "+"
            brain_image.pack_configure(pady=(pady_value,0))

            brain_image.after(20,image_animate)


        elif pady_value >= 200 :
            pady_value -= 0.7
            animate_state = "-"
            brain_image.pack_configure(pady=(pady_value,0))

            brain_image.after(20,image_animate)

        else : 

            if animate_state == "+" :
                pady_value += 0.7
                brain_image.pack_configure(pady=(pady_value,0))
                brain_image.after(20,image_animate)

            else : 
                pady_value -= 0.7
                brain_image.pack_configure(pady=(pady_value,0))
                brain_image.after(20,image_animate)              


    image_animate()
    


    main_text_frame = customtkinter.CTkFrame(main_frame,height=900)
    main_text_frame.pack(fill="both",padx=(10,5),pady=(10,10))

    text1_to_main_frame(main_text_frame).pack()
    text2_to_main_frame(main_text_frame).pack(anchor="w",padx=(85,0))
    main_login(main_text_frame,app).pack(fill="x",padx=(80,85))
    main_signup(main_text_frame,app).pack(fill="x",padx=(80,85),pady=(20,0))

    # customtkinter.CTkLabel(main_text_frame,text="\n").pack()

    copy_right_lbl = text3_to_main_frame(main_text_frame)
    copy_right_lbl.pack(pady=(11,10),side="left",padx=(105,0))

    AutoTextWriter.MultiNamesAnimate(copy_right_lbl,
                                     ["Copyright © 2024 by Mr.Doctor | All Rights Reserved."],
                                     step_time_go_back=5,
                                     step_time_go=0.05,
                                     step_time_back=0.05
                                     ).run()

    customtkinter.CTkLabel(main_text_frame,text="\n\n").pack()


    # shortcuts
    shortcuts.bind_login(app)
    shortcuts.bind_sign_up(app)
    shortcuts.bind_models_score(app)


# import tree_of_root
# import os
# os.system("cls")
# tree_of_root.tree(app,0)

app.mainloop()