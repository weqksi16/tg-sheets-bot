import gspread 

class GoogleSheet:
    """Класс для удобной работы с конкретной Google Таблицей."""

    def __init__(self, credentials_path: str, spreadsheet_id: str):
        """
        КОНСТРУКТОР. Срабатывает автоматически при создании объекта.
        Инициализирует (сохраняет внутри объекта) базовые данные.
        """
        # Инкапсулируем настройки подключения внутри объекта
        self.creds_path = credentials_path
        self.spreadsheet_id = spreadsheet_id
        self._client = None  # Защищенный атрибут (начинается с _)
        self.sheet = None
        
        # Автоматически подключаемся при создании
        self._connect()

    def _connect(self):
        """Внутренний (скрытый) метод для авторизации."""
        self._client = gspread.service_account(filename=self.creds_path)
        self.sheet = self._client.open_by_key(self.spreadsheet_id)
        
# import os
# from dotenv import load_dotenv

# load_dotenv()

# gc = gspread.service_account(filename='credentials.json')
# sh = gc.open("TEST")

# # def receive_data(messages):
    
# print(sh.sheet1.get('A1'))
# print(sh.sheet1.get('B1'))

# val = sh.sheet1.cell(1, 2).value
# print(val)
