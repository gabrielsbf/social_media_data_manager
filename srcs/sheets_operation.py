from srcs.classes.social_man import *
from utils import *
import gspread

ct = gspread.service_account('./utils/credentials.json')
sh = ct.open_by_key("1TVN77nxIF3jmfhJIg5f2qvJa-p8I-nVAoMtk426t_Io")
worksheet = sh.worksheet('Mar')

account = Social_Manager('section_m')
file = account.getJsonFile("facebook", file_folder="test_sheets")


def input_data():
    """
        ----
        Description:
        ----
        function that extracts data from a json file and
        transforms it into arrays so that they have
        access to be added to spreadsheets

        ----
        Package Contents:
        ----
        gspread.

    """
    message, url, sr_time = [],[],[]
    for data in file:
        message.append([data['message']])
        url.append([data['permalink_url']])
        sr_time.append([data['created_time']])
    worksheet.update(message, 'B3')
    worksheet.update(url, 'H3')
    worksheet.update(sr_time, 'E3')
