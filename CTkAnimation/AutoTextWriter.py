import customtkinter
import time
import threading


class OneWordAnimate :

    def __init__(self , word :str , label : customtkinter.CTkLabel , step_time_go : int = 0.3 , step_time_back : int = 0.1,step_word_time : int = 0.2):
        self.__w = word
        self.__lbl = label
        self.__ms_go = step_time_go
        self.__ms_back = step_time_back
        self.__sw = step_word_time

        self.__index_back = len(word)-1


    def _run_(self):

        for ch in self.__w :
            time.sleep(self.__ms_go)
            self.__lbl.configure(text = self.__lbl.cget("text")+ch)

        time.sleep(self.__sw)

        for index in range(self.__index_back,-1,-1) :
            time.sleep(self.__ms_back)
            self.__lbl.configure(text = self.__w[:index])   


    def run(self):
        tread = threading.Thread(target=self.__run,daemon=True)
        tread.start()





class MultiNamesAnimate : 

    def __init__(
            self ,
            label : customtkinter.CTkLabel ,
            names : list[str],
            step_time_go : int = 0.3 ,
            step_time_back : int = 0.1 ,
            step_time_between : int = 0.1,
            step_time_go_back : int = 0
    ) :
        
        self.__lbl = label
        self.__ms_go = step_time_go
        self.__ms_back = step_time_back
        self.__ms_bet = step_time_between
        self.__stgb = step_time_go_back
        self.__names = names



    def __run(self):
        while True : 
            for word in self.__names :
                OneWordAnimate(word,self.__lbl,self.__ms_go,self.__ms_back,self.__stgb)._run_()
                time.sleep(self.__ms_bet)



    def run(self):
        tread = threading.Thread(target=self.__run,daemon=True)
        tread.start()