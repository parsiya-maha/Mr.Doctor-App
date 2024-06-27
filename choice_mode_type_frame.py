# Import models
import customtkinter
from funcs import predit_from_widgets
from BtnInfo import btn_info


text1 = "Choice model type          "

# LABEL -> show label with custom text
def text_choice_model_type(master:customtkinter.CTk)->customtkinter.CTkLabel:
    text = customtkinter.CTkLabel(master,
                                text=text1,
                                font=("calibri",25,"bold"))
    return text


# OPTIONMENU -> show option menu in master(app)
def option_model_widget(master:customtkinter.CTk)->customtkinter.CTkOptionMenu:
    om = customtkinter.CTkOptionMenu(master=master,

                                       values=[
                                        "BrainTumors",
                                        "BreastCancer",
                                        "CervicalCancer",
                                        "KidneyStone",
                                        "LungCancer",
                                        "LungMask",
                                        "ToRecognize",
                                        "ToRecognizeAndPredict"
                                       ],

                                        font=("calibri",20),
                                        height=40,
                                        width=355,
                                        command=lambda x : ...
                                       )

    btn_info(om,"Choosing an artificial intelligence model to predict the selected photo.\n(BrainTumprs model is selected by default)")
    
    return om


# Defind text var:str
text_option_ = """
To see the result of the selected model, 
click on the 'Predict' button.

It takes a short time to perform 
the existing operations on the photo.

Note: Before hitting the 'Predict' button, 
you must have uploaded a photo.
"""


# LABEL -> show label with custom text
def text_option(master:customtkinter.CTk)->customtkinter.CTkLabel:
    return customtkinter.CTkLabel(master,
                                text=text_option_,
                                justify='left',
                                font=("calibri",15))
   

# Button -> show buttom in master(app)
def predict_btn(master:customtkinter.CTk,option,tabel,progressbar,master_all:customtkinter.CTk)->customtkinter.CTkButton:
    btn = customtkinter.CTkButton(master=master,
                                  text="Predict",
                                  font=("calibri",30),
                                  width=355,
                                  height=50,
                                  corner_radius=30,
                                  command=lambda:predit_from_widgets(option,tabel,progressbar,master_all)
                                  )
    

    text_info = """
Performing the prediction process by artificial intelligence models.
Of course, you must select the corresponding photo before pressing this button.
He also chose his model.
(The model defaults to BrainTumors.)
"""

    btn_info(btn,text_info)

    return btn