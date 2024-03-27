from srcs.classes.social_man import *
from utils import *
import gspread

ct = gspread.service_account('./utils/credentials.json')
sh = ct.open_by_key("1qHsjCl9FEPiXsdjxbLJBa1-B-WAB10_NcSh24isUJmQ")
worksheet = sh.worksheet('Mar')
"""
-----------------------------------------------------------------------
Variables that receive values ​​and functions that bridge the sheets
-----------------------------------------------------------------------
"""

account = Social_Manager('section_m')
file = account.getJsonFile("facebook", file_folder="test_sheets")

def input_data():
    """
        ----
        Name:
        ----
        input_data
        
        ----
        Description: 
        ----
        function that extracts data from a json file and 
        transforms it into arrays so that they have 
        access to be added to spreadsheets

        ----
        Package Contents:
        ----
        gspread (Package)

    """
    message, url, sr_time = [],[],[]
    for data in file:
        message.append([data['message']])
        url.append([data['permalink_url']])
        sr_time.append([data['created_time']])
    worksheet.update(message, 'B3')
    worksheet.update(url, 'H3')
    worksheet.update(sr_time, 'E3')

