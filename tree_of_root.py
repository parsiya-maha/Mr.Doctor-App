import customtkinter


def tree(master:customtkinter.CTk,index=0):

    _all = master.pack_slaves()

    if _all == [] :
        p = index*"    "
        print(p+str(master.__class__.__name__))

    for res in _all :
        tree(res,index+1)
