from srcs.export_xlsx import *
from srcs.cfg import *
from srcs.export_xlsx import convertXlsx
from srcs.classes.social_man import Social_Manager
from utils.env_p import *

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
					1 - Converta arquivos .json para .xlsx
					2 - Extrair dados do meta (facebook e instagram)
					""")
		match option:
				case "1":
					convertXlsx()
					is_match = False
				case "2":
					s_manager = Social_Manager(select_user())
					select_metric(s_manager, select_media())
					is_match = False
				case _:
					print("Selecione uma opção válida.")

def select_media():
	face_bool, insta_bool = False, False

	while face_bool == False or insta_bool == False :
		choose_media = input("""Selecione qual rede deseja
					1 - Facebook
					2 - Instagram
					3 - Terminar:
					""")
		match choose_media:
			case '1':
				face_bool = True
			case '2':
				insta_bool = True
			case '3':
				break
			case _:
				if(face_bool or insta_bool):
					print(f"""Você escolheu :
			{"Opção 1: Facebook" if face_bool == True else ""}
			{"Opção 2: Instagram" if insta_bool == True else ""}""")
					break
				else :
					print("Você não selecionou nenhuma rede")
	return {'has_face': face_bool,
		 	'has_insta': insta_bool}

def select_metric(s_manager : Social_Manager, media):
	print(dict(media).keys())
	for i in media.keys():
		print(i)
		if media[i] == True:
			if i == 'has_face':
				face_req = s_manager.face_description()
				since_date_arch = face_req[1]["start_date"]["date_parsed"]
				until_date_arch = face_req[1]["final_date"]["date_parsed"]
				face_desc = face_req[0]
				face_metrics = s_manager.face_post_metrics(face_desc)
				s_manager.merging_objects_by_id(face_desc, face_metrics)
				s_manager.writeJsonFile(f"{since_date_arch}_a_{until_date_arch}_face_merged", face_desc)
			if i == 'has_insta':
				insta_req = s_manager.insta_description()
				since_date_arch = insta_req[1]["start_date"]["date_parsed"]
				until_date_arch = insta_req[1]["final_date"]["date_parsed"]
				insta_desc = insta_req[0]
				insta_metrics = s_manager.insta_metrics(insta_desc)
				s_manager.merging_objects_by_id(insta_desc, insta_metrics, 'id', 'id')
				s_manager.writeJsonFile(f"{since_date_arch}_a_{until_date_arch}_insta_merged", insta_desc)

