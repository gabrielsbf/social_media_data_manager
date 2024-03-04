from srcs.export_xlsx import *
from srcs.cfg import *

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

def main_menu():
    is_match = True
    while is_match:
        option = input("""Selecione uma das opçoes abaixo
                    1 - Converter arquivos json para Xlxs.
                    2 - Extrair dados do meta.
                    """)
        match option:
                case "1":
                    print("Numero 1 selecionado")
                    is_match = False
                case "2":
                    print("Numero 2 selecionado")
                    is_match = False
                case _:
                    print("Selecione uma opção válida.")
            