from srcs.export_xlsx import *
from srcs.cfg import *
from srcs.export_xlsx import convertXlsx
from srcs.classes.social_man import Social_Manager
from utils.env_p import *
from utils.date_formats import *

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
	social_media = []
	while True :
		choose_media = input("""Selecione qual rede deseja
					1 - Facebook
					2 - Instagram
					3 - Terminar:
					""")
		match choose_media:
			case '1':
				social_media.append('facebook')
			case '2':
				social_media.append('instagram')
			case _:
				if not social_media == []:
					break
				else :
					print("Você não selecionou nenhuma rede")

	date = return_period()
	return [social_media, date]

def select_metric(s_manager : Social_Manager ,media):
	metrics_ = input(''' Digite 1 para apenas descritivo
Digite 2 para apenas dados
Digite 3 para mesclado: ''')
	since_date_arch = media[1]["start_date"]["date_parsed_"]
	until_date_arch = media[1]["final_date"]["date_parsed_"]
	print(media)
	for i in media[0]:
		print(i)
		if i == 'facebook':
			face_req = s_manager.face_description([media[1]["start_date"]["date_parsed"], media[1]["final_date"]["date_parsed"]])
			face_desc = face_req[0]
			if metrics_ == '1' or metrics_ == '3':
				s_manager.writeJsonFile(f"{since_date_arch}_a_{until_date_arch}_face_description", face_desc, JSFILES_PATH)
			if metrics_ == '2' or metrics_ == '3':
				face_metrics = s_manager.face_post_metrics(face_desc)
				s_manager.writeJsonFile(f"{since_date_arch}_a_{until_date_arch}_face_metrics", face_metrics, JSFILES_PATH)
				
		if i == 'instagram':
			insta_req = s_manager.insta_description([media[1]["start_date"]["date_parsed"], media[1]["final_date"]["date_parsed"]])
			insta_desc = insta_req[0]
			if metrics_ == '1' or metrics_ == '3':
				s_manager.writeJsonFile(f"{since_date_arch}_a_{until_date_arch}_insta_description", insta_desc, JSFILES_PATH)
			if metrics_ == '2' or metrics_ == '3':
				insta_metrics = s_manager.insta_metrics(insta_desc)
				s_manager.writeJsonFile(f"{since_date_arch}_a_{until_date_arch}_insta_metrics", insta_metrics, JSFILES_PATH)
