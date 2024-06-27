# Import models
import customtkinter
import CTkTable

# Defind base `result tabel` values
values = [
    ["Result","Time"],
    ["nan","nan"]
]

# Function to return result tabel
def result_tabel(master:customtkinter.CTk)->CTkTable.CTkTable:
    return CTkTable.CTkTable(master=master,
                            row=2,
                            column=2,
                            values=values,
                            padx=2,
                            pady=2
                            )

# Predict time progress bar 
def predict_progressbar(master:customtkinter.CTk)->customtkinter.CTkProgressBar:
    c = customtkinter.CTkProgressBar(master=master,mode="determinate",determinate_speed=1)
    c.set(1)

    return c


n_t = "0s\t\t\t\t\t\t      1s\t\t\t\t\t\t         2s"


# LABEL -> show some text
def n_text(master:customtkinter.CTk)->customtkinter.CTkLabel:
    return customtkinter.CTkLabel(master=master,text=n_t)
