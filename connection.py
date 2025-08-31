import pyodbc

def get_connection():
    """
    Skapar en anslutning till MSSQL-databasen.

    Returns:
        pyodbc.Connection: En aktiv databasanslutning.
    """
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=;" #Här skriver du in din server
        "Database=;" #Och här skriver du in din server
        "Trusted_Connection=yes;"
    )
    return conn
