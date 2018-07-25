############
'''
Instructions::

Step 1: pip install gspread oauth2client

Step 2: Generate service account file from google developers console. Also enable sheets api in Google API console.

Step 3: Create a spreadsheet and share it with the client email in the service account credentials file
'''
############

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)         

gc = gspread.authorize(credentials)

sht = gc.open_by_url('https://docs.google.com/spreadsheets/d/1d0wo8_-9q7AzUJttgIJfipUHNwpFPC1Wn5QitY7jUhw/edit#gid=0')

