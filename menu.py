from srcs.export_xlsx import *
from srcs.cfg import *
from srcs.export_xlsx import convertXlsx
from srcs.classes.social_man import Social_Manager
from utils.env_p import *
from utils.date_formats import *

def select_user():
	"""
	----
	Description:
	----
	Function that receives input from the user determines whether it is a valid user
=======
    Selects a user from a list of sections.

    Returns:
        str: The name of the selected user.

    Example:
        >>> select_user()
        Enter the name of the requested user: Alice
        Selected user is Alice
        'Alice'
	----
	Package contents:
	----
	Social_manager,
	read_sections.

	-----
	"""
	sectionc = []
	section = read_sections()
	while sectionc == []:
		user_a = input("Digite o Nome do usuario solicitado:")
		list_v = list (filter(lambda x: str(x).find("section") >= 0, section))
		sectionc = list (filter(lambda x: str(x) == user_a, list_v))
		if sectionc == []:
			print(f"{user_a} não é um usuário")
	print("Usuário selecionado foi ", sectionc[0])
	return (sectionc[0])

def main_menu():
	"""
	-----
	Description:
	-----
	Function that makes the user select an option in the input and determines whether it is a valid selection.

	-----
	Package contents:
	-----
	Social_manager,
	convertXlsx,
	select_mertrics,
	select_user.


=======
    Displays the main menu and executes the action corresponding to the option chosen by the user.

    Returns:
        None

    Example:
        >>> main_menu()
        Select one of the options below
        1 - Convert .json files to .xlsx
        2 - Extract meta data (Facebook and Instagram)
        1
        (Action of converting .json files to .xlsx is executed)
    """
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
	"""
	----
	Description:
	----
	Request the desired network and determine if it is valid.

	----
	Package contents:
	----
	No Packs.
=======
    Permite ao usuário selecionar as redes sociais das quais deseja extrair dados.

    Retorna:
        list: Uma lista contendo a(s) rede(s) social(is) selecionada(s) e o período desejado.

    Exemplo:
        >>> select_media()
        Selecione qual rede deseja
        1 - Facebook
        2 - Instagram
        3 - Terminar:
        1
        (Ação de selecionar a rede social Facebook é executada)
        ['facebook', período_selecionado]
    """
	social_media = []
	while True :
		print("você escolheu ->", social_media)
		if social_media == ['facebook', 'instagram']:
			break

		choose_media = input("""Selecione qual rede deseja
					1 - Facebook
					2 - Instagram
					3 - Terminar:
					""")
		match choose_media:
			case '1':
				if social_media.count("facebook") == 0:
					social_media.insert(0, 'facebook')
				else:
					print("Você já escolheu essa rede")		
			case '2':
				if social_media.count("instagram") == 0:
					social_media.insert(1, 'instagram')
				else:
					print("Você já escolheu essa rede")		
			case _:
				if not social_media == []:
					break
				else :
					print("Você não selecionou nenhuma rede\nPressione CTRL+C para sair")

	date = return_period()
	return [social_media, date]


def select_metric(s_manager : Social_Manager ,media):
	"""
	----
	Description:
	----
	Receives input from the user and delivers the desired type of data.

	----
	Package:
	----
	writeJsonFile,
	Social_media,
	face_description,
	JSFILES_PATH.

=======
    Allows the user to select the desired type of metric and generates files with the corresponding data.

    Arguments:
        s_manager (Social_Manager): An instance of the social media manager.
        media (list): A list containing the selected social media platform(s) and the desired period.

    Returns:
        None

    Example:
        >>> select_metric(s_manager, ['facebook', 'instagram'], selected_period)
        Enter 1 for descriptive only
        Enter 2 for data only
        Enter 3 for merged: 3
        (Action of selecting metric and generating corresponding files is executed)
    """
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


