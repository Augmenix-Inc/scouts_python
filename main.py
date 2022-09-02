from curses.ascii import isdigit
import os.path
from urllib.parse import unquote, urlparse

from pathlib import PurePosixPath
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']


def get_csv(url: str):
    global service

    path = urlparse(url).path
    path_segments = PurePosixPath(unquote(path)).parts
    file_id = path_segments[3]

    # Call the Drive v3 API
    file_result = service.files().export(
        fileId=file_id, mimeType="text/csv")
    csvStr: str = file_result.execute().decode("utf-8")

    rows = csvStr.splitlines()
    num_rows = len(rows)
    if num_rows == 0:
        return []
    cols_0 = rows[0].split(",")
    num_cols = len(cols_0)
    if num_cols == 0:
        return []

    table = []
    for i in range(1, num_rows):
        cols = rows[i].split(",")
        for j in range(num_cols):
            if i == 1:
                table.append([cols[j].replace("\;", ",")])
                continue
            table[j].append(cols[j].replace("\;", ","))

    return table


def validate_choice_input(choice: str, max: int):
    if not choice.isdigit():
        return False
    return 1 <= int(choice) <= max


def main():
    global service, main_table

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        print("Downloading required data...")
        main_table = get_csv(
            "https://docs.google.com/spreadsheets/d/1v9ItNHslIZbQCRPdur5u30ITOvj-QXzrAXlZMjNEpLA/edit?usp=sharing")
        get_user_input()
    except HttpError as error:
        print(f'An error occurred: {error}')


def get_user_input():
    print(
        """
Welcome to Stacked Admin Console (Python), select an action:
1. Manage members
2. Manage progress badges
3. Manage event badges
4. Manage unit achievements
""")
    choice = input("Your choice (1-4): ")
    while not validate_choice_input(choice, 4):
        choice = input("Invalid input. Re-enter your choice (1-4): ")


main()
