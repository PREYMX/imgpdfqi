import pyodbc


class Core:
    def process(self, server: str,
                database: str,
                username: str,
                password: str,
                odbc_driver: str):
        conn: pyodbc.Connection = pyodbc.connect('DRIVER={'+odbc_driver+'};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+password)
        cursor = conn.cursor()
