import gspread 
import os
from dotenv import load_dotenv

load_dotenv()

gc = gspread.service_account(filename='credentials.json')
sh = gc.open("TEST")

# def receive_data(messages):
    
print(sh.sheet1.get('A1'))
print(sh.sheet1.get('B1'))

val = sh.sheet1.cell(1, 2).value
print(val)
