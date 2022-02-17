# import gspread
# # connect got Google Sheets
# gspread_client = gspread.service_account(filename="service.json")
# # list all available spreadsheets
# spreadsheets = gspread_client.openall()
# if spreadsheets:
#     print("Available spreadsheets:")
#     for spreadsheet in spreadsheets:
#         print("Title:", spreadsheet.title, "URL:", spreadsheet.url)
# else:
#     print("No spreadsheets available")
#     print("Please share the spreadsheet with Service Account email")
#     print(gspread_client.auth.signer_email)




from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
gauth = GoogleAuth()
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/alegra6/nationalsociety.in/Document/gdrive_uploader/service.json', scope)
gauth.auth_method = 'service'
drive = GoogleDrive(gauth)

file_path = "build.zip"
# file_path = "package.json"
fileex = drive.CreateFile({'parents': [{'kind': 'drive#fileLink', 'id': '1lRc0pLT6PoC-W0L9F8YmwSSjt1E-XWi8'}]})
fileex.SetContentFile(file_path)
fileex.Upload()
