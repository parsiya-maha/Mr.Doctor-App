#Import models
import customtkinter
from CTkAnimation import AutoTextWriter

# Set some setting for appaerance in system(customtkinter)
customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

# Function to make ERROR bigger (x20)
def make_acc(n):
    n = 1-n
    n*=20
    return 1-n


# Main app (CTk)
def return_app():
    
    # Defind app var and base setting  
    app = customtkinter.CTk() 

    app.geometry("800x370")
    app.resizable(0,0)
    app.title("Mr.Doctor - Models score")

    # Defind one TabView
    tab_frame = customtkinter.CTkTabview(app)

    # Add all 5 tab to `tab view` widget
    brain_tab     = tab_frame.add("BrainTumors")
    breast_tab    = tab_frame.add("BreastCancer")
    cervical_tab  = tab_frame.add("CervicalCancer")
    kidney_tab     = tab_frame.add("KidneyStone")
    lung_tab      = tab_frame.add("LungCancer")
    lung_mask_tab = tab_frame.add("LungMask")
    recog_tab     = tab_frame.add("ToRecognize")
    recog_pre_tab = tab_frame.add("ToRecognizeAndPredict")


    tab_frame.pack(fill="both",expand=True,padx=10,pady=(0,10))
    
    # Tab[1] -> BrainTumor

    brain_frame = customtkinter.CTkFrame(brain_tab)
    brain_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(brain_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    l1 = customtkinter.CTkLabel(up_frame1,
                           text="Brain Tumors",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")



    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="99.88%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(brain_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    brain_prog = customtkinter.CTkProgressBar(down_frame1)
    brain_prog.pack(pady=5,fill="x",padx=5)

    brain_acc = make_acc(0.9988)
    brain_prog.set(brain_acc)
    
    
    # Tab[2] -> LungCancer

    lung_frame = customtkinter.CTkFrame(lung_tab)
    lung_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(lung_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    customtkinter.CTkLabel(up_frame1,
                           text="Lung Cancer",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")


    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="99.80%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(lung_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    lung_prog = customtkinter.CTkProgressBar(down_frame1)
    lung_prog.pack(pady=5,fill="x",padx=5)

    lung_acc = make_acc(0.9980)
    lung_prog.set(lung_acc)




    # Tab[3] -> KidneyStone

    kidney_frame = customtkinter.CTkFrame(kidney_tab)
    kidney_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(kidney_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    customtkinter.CTkLabel(up_frame1,
                           text="Kidney Stone",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")


    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="99.76%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(kidney_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    kidney_prog = customtkinter.CTkProgressBar(down_frame1)
    kidney_prog.pack(pady=5,fill="x",padx=5)

    kidney_acc = make_acc(0.9976)
    kidney_prog.set(kidney_acc)


    # Tab[4] -> ToRecognize

    recog_frame = customtkinter.CTkFrame(recog_tab)
    recog_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(recog_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    customtkinter.CTkLabel(up_frame1,
                           text="To Recognize",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")


    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="100.0%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(recog_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    recog_prog = customtkinter.CTkProgressBar(down_frame1)
    recog_prog.pack(pady=5,fill="x",padx=5)

    recog_acc = make_acc(1)
    recog_prog.set(recog_acc)


    # Tab[5] -> ToRecognizeAndPredict

    recog_pre_frame = customtkinter.CTkFrame(recog_pre_tab)
    recog_pre_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(recog_pre_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    customtkinter.CTkLabel(up_frame1,
                           text="To Recognize\nAnd Predict",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")


    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="99.81%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(recog_pre_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    recog_pre_prog = customtkinter.CTkProgressBar(down_frame1)
    recog_pre_prog.pack(pady=5,fill="x",padx=5)

    recog_pre_acc = make_acc(0.9981)
    recog_pre_prog.set(recog_pre_acc)


    # tab[6] -> Breast Cancer

    breast_frame = customtkinter.CTkFrame(breast_tab)
    breast_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(breast_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    customtkinter.CTkLabel(up_frame1,
                           text="Breast Cancer",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")


    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="99.47%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(breast_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    breast_prog = customtkinter.CTkProgressBar(down_frame1)
    breast_prog.pack(pady=5,fill="x",padx=5)

    breast_acc = make_acc(0.9947)
    breast_prog.set(breast_acc)


    # tab[7] -> Cervical Cancer

    cervical_frame = customtkinter.CTkFrame(cervical_tab)
    cervical_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(cervical_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    customtkinter.CTkLabel(up_frame1,
                           text="Cervical Cancer",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")


    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="99.58%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(cervical_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    cervical_prog = customtkinter.CTkProgressBar(down_frame1)
    cervical_prog.pack(pady=5,fill="x",padx=5)

    cervical_acc = make_acc(0.9958)
    cervical_prog.set(cervical_acc)



    # tab[8] - > Lung Mask


    lung_mask_frame = customtkinter.CTkFrame(lung_mask_tab)
    lung_mask_frame.pack(fill="both",expand=1)

    up_frame1  = customtkinter.CTkFrame(lung_mask_frame,height=250)
    up_frame1.pack_propagate(False)
    up_frame1.pack(fill="both",expand=1,padx=10,pady=10)

    customtkinter.CTkLabel(up_frame1,
                           text="Lung Mask",
                           font=("calibri",50,"bold")
                           ).pack(side="left",padx=(60,0),pady=20,anchor="center")


    acc_frame1 = customtkinter.CTkFrame(up_frame1,width=250)
    acc_frame1.pack_propagate(False)
    acc_frame1.pack(padx=20,pady=20,side="right")

    # Acc label
    customtkinter.CTkLabel(acc_frame1,text="94.03%",font=("calibri",50,"bold")).pack(padx=50,pady=80)

    down_frame1 = customtkinter.CTkFrame(lung_mask_frame)
    down_frame1.pack(fill="both",expand=True,padx=10,pady=(0,10))

    lung_mask_prog = customtkinter.CTkProgressBar(down_frame1)
    lung_mask_prog.pack(pady=5,fill="x",padx=5)

    # lung_mask_acc = make_acc(0.9403)
    lung_mask_acc = 0.8
    lung_mask_prog.set(lung_mask_acc)


    # Return main app
    return app
