import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("data/creds.json",scope)

client = gspread.authorize(creds)

sheet = client.open('userbase').sheet1

# data = sheet.get_all_records()
# newmember = ['Salimov','Hakim', 'erkak',"1999",10415465,'maktab o\'quvchisi','web']
# sheet.append_row(newmember)
# print(data)
