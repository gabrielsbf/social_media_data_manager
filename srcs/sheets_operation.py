from srcs.classes.social_man import *
from utils import *
import gspread

ct = gspread.service_account('./utils/credentials.json')
sh = ct.open_by_key("1qHsjCl9FEPiXsdjxbLJBa1-B-WAB10_NcSh24isUJmQ")
worksheet = sh.worksheet('Mar')


account = Social_Manager('section_m')
file = account.getJsonFile("facebook", file_folder="test_sheets")


def sheet_op():
    account = Social_Manager('section_m')
    file = account.getJsonFile("facebook", file_folder="test_sheets")
    print(file[0].keys())

def input_data():
    message, url, sr_time = [],[],[]
    for data in file:
        message.append([data['message']])
        url.append([data['permalink_url']])
        sr_time.append([data['created_time']])
    worksheet.update(message, 'B3')
    worksheet.update(url, 'H3')
    worksheet.update(sr_time, 'E3')

    
        
        # url.append(data['permalink_url'])
        # sr_time.append(data['created_time'])




    #     if "post_id" in data:
    #         insert_data.append(data)
    # print(insert_data)
    