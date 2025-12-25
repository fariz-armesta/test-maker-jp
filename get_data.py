import pandas as pd

class GetData:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.columns = ["type", "Text", "A", "B", "C", "D"]
        self.df_excel = pd.read_excel(self.file_path)
        self.df_excel.columns = self.columns[:len(self.df_excel.columns)]
        
        
    def give_data(self):
        return self.df_excel
