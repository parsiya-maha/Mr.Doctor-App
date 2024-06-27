import customtkinter



class Panel :

    def __init__(
            self,
            frame : customtkinter.CTkFrame,
            width_cte : int|float,
            step_px : int = 10,
            step_time : int|float = 10
    ) :
        self.__X = 0
        self.__f = frame
        self.__cte = width_cte
        self.__pos = "+"
        self.__widget = []
        self.__step_px = step_px
        self.__step_ms = step_time



    def add_widget(self,widget,pack_args:dict={}):
        self.__widget.append([widget,pack_args])


    def run(self):

        first = True

        if self.__pos=="+":

            if first :
                first = False
                for i,k in self.__widget :
                    i.pack(**k)


            self.__X += self.__step_px

            if self.__X <= self.__cte:
                self.__f.configure(width=self.__X)

                self.__f.after(self.__step_ms,self.run)
            else :
                self.__pos = "-"



        else : 
            self.__X -= 10

            if self.__X >= 0 :
                self.__f.configure(width=self.__X)
                self.__f.after(self.__step_ms,self.run)

            else:
                self.__pos = "+"
                for i,_ in self.__widget:
                    i.pack_forget()