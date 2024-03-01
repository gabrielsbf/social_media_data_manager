import pandas as pd
from srcs.classes.social_man import Social_Manager
from srcs.export_xlsx import *
from srcs.cfg import *

if __name__ == "__main__":

    def select_user():
        
        sectionc = []
        section = read_sections()
        while sectionc == []:
            user_a = input("Digite o Nome do usuario solicitado:")
            print("input do usuário ", user_a)
            list_v = list (filter(lambda x: str(x).find("section") >= 0, section))
            print("lista antes do filtro", list_v)
            sectionc = list (filter(lambda x: str(x) == user_a, list_v))
        
        return (sectionc[0])

    user_selected = select_user()
    print("User selected is: ", user_selected)