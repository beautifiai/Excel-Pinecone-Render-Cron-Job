import pandas as pd

class ExcelHandler:
    def __init__(self, excel_url):
        self.excel_url = excel_url
    
    def get_excel_data(self):
        data = pd.read_excel(self.excel_url)
        return data

    def compare_data(self, current_data, previous_data):
        current_namespaces = set(current_data.iloc[:, 0])
        previous_namespaces = set(previous_data.iloc[:, 0])

        namespaces_to_add = current_namespaces - previous_namespaces
        namespaces_to_remove = previous_namespaces - current_namespaces

        to_add = current_data[current_data.iloc[:, 0].isin(namespaces_to_add)]
        to_remove = previous_data[previous_data.iloc[:, 0].isin(namespaces_to_remove)]

        return to_add, to_remove
