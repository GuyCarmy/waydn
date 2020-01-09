import tkinter as tk
from tkinter import simpledialog
import os.path
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

application_window = tk.Tk()

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1oL__HQpIYCSWp4la8bdVdxb012g_0BN4WspMuMsiwIE").sheet1


def add_to_sheet(s):
    now = datetime.now()  # current date and time
    date = now.strftime("%m/%d/%Y, %H:%M:%S")
    sheet.insert_row([date, s], 1)


answer = simpledialog.askstring("Input", "What are you doing now?",
                                parent=application_window)
if answer is not None:
    add_to_sheet(answer)
else:
    print("You are lazy")
