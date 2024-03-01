from configparser import ConfigParser


def read_config(section):
	config = ConfigParser()
	config.read('config.ini')
	tuple_items = config.items(section)
	object = {i[0] : i[1] for i in tuple_items}
	return object

