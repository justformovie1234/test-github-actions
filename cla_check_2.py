from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1naQC7iEfnro5iOjTFEn7iPCxNMPaPa4YnIddjT5CTM8'
SAMPLE_RANGE_NAME = 'Usernames'

def main():
  creds = None
  creds = Credentials.from_authorized_user_file('token.json', SCOPES)

  service = build('sheets', 'v4', credentials=creds)

  # Call the Sheets API
  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                              range=SAMPLE_RANGE_NAME).execute()
  values = result.get('values', [])
  if not values:
      print('No data found.')
  else:
      print('Name, Major:')
      for row in values:
          # Print columns A and E, which correspond to indices 0 and 4.
          print('%s' % (row[0]))

if __name__ == '__main__':
    main()
