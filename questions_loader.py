import gspread
import numpy as np
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("json_data.json")

client = gspread.authorize(creds)

sheet = client.open("Jeet Lenge Ye Jahan")
page_easy = sheet.worksheet("Easy Problems")
page_medium = sheet.worksheet("Medium Problems")
page_hard = sheet.worksheet("Hard Problems")

data_easy = np.array(page_easy.get_all_values()) 
data_medium = np.array(page_medium.get_all_values())
data_hard = np.array(page_hard.get_all_values())
data_collection = []
data_collection.append(data_easy[6:,3])
data_collection.append(data_hard[6:,3])
data_collection.append(data_medium[6:,3])

questions_list = []
file = open('questions.js','w')
string_output = "questions = ["
for data in data_collection:
    for i in range(len(data)):
        if not data[i] == "":
            string_output += f'"{data[i]}",'
            questions_list.append(data[i]) 
        elif data[i+1] == "":
            break
string_output += "]"
file.write(string_output)
