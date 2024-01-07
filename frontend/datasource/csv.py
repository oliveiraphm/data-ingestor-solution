import streamlit as st
import openpyxl
import pandas as pd

class CSVCollector:
    def __init__(self, schema, aws, cell_range):
        self.schema = schema
        self._aws = aws
        self._buffer = None
        self.cell_range = cell_range
        return
    
    def start(self):
        getData = self.getData()
        if getData is not None:
            extractData = self.extractData(getData)
            return extractData

    def getData(self):
        dados_excel = st.file_uploader("Insire o arquivo Excel", type=".xlsx")
        return dados_excel

    def extractData(self, dados_excel):
        workbook = openpyxl.load_workbook(dados_excel)
        sheet = workbook.active
        range_cell = sheet[self.cell_range] #[C12:I209]
        headers = [cell.value for cell in range_cell[0]]

        data = []
        for row in range_cell[1:]:
            data.append([cell.value for cell in row])

        dataframe = pd.DataFrame(data, columns=headers)
        return dataframe
    
    def validateDate(self):
        pass

    def loadData(self):
        pass 