import pandas as pd
from srcs.classes.social_man import Social_Manager
from srcs.export_xlsx import *

marica = Social_Manager("section_m")
face_json = marica.face_post_metrics(file_name='feb_month_face')
insta_json = marica.insta_metrics(file_name="feb_month_insta")
marica.writeJsonFile('metrics_face', face_json, JSFILES_PATH)
marica.writeJsonFile('metrics_insta', insta_json, JSFILES_PATH)

convertXlsx()
