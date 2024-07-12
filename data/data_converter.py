import pandas as pd

def convert_xlsx_to_list(file_path):
    """
    Convierte el contenido de un archivo .xlsx a una lista de números.
    """
    try:
        df = pd.read_excel(file_path)
        data = df.iloc[:, 0].dropna().tolist()
        return data
    except Exception as e:
        print(f"Error al convertir archivo .xlsx: {e}")
        return []

def convert_txt_to_list(file_path):
    """
    Convierte el contenido de un archivo .txt a una lista de números.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            data_list = list(map(int, data.split(',')))
            return data_list
    except Exception as e:
        print(f"Error al convertir archivo .txt: {e}")
        return []
