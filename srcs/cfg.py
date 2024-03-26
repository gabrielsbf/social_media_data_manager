from configparser import ConfigParser
from utils.env_p import *

def read_config(section):
	config = ConfigParser()
	config.read('config.ini')
	tuple_items = config.items(section)
	object = {i[0] : i[1] for i in tuple_items}
	return object

def read_sections():
	config = ConfigParser()
	config.read(CONFIG_PATH)
	sections = config.sections()
	return sections
