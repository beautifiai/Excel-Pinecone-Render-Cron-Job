import pandas as pd
from openpyxl import load_workbook

class ExcelHandler:
    def __init__(self, excel_url):
        self.excel_url = excel_url

    def get_excel_data(self):
        """
        Reads the Excel data from the provided URL and returns a dictionary with namespaces as keys
        and rows (as lists) as values.
        """
        data = pd.read_excel(self.excel_url, header=None)
        data_dict = data.set_index(0).T.to_dict('list')
        return data_dict

    def compare_data(self, current_data, previous_data):
        """
        Compares the current and previous data and returns two lists:
        - 'to_add': contains rows present in current_data but not in previous_data
        - 'to_remove': contains namespaces present in previous_data but not in current_data
        """
        to_add = {namespace: row for namespace, row in current_data.items() if namespace not in previous_data}
        to_remove = [namespace for namespace in previous_data if namespace not in current_data]
        return to_add, to_remove
