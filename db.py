from connection import get_connection

def create_table():
    """
    Skapar tabellen 'weather_data' om den inte redan finns.
    Kolumner:
        - id (INT, PK, autoinkrement)
        - temp (FLOAT)
        - description (NVARCHAR)
        - timestamp (DATETIME2)
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            IF NOT EXISTS (
                SELECT * FROM sysobjects WHERE name='weather_data' AND xtype='U'
            )
            CREATE TABLE weather_data (
                id INT IDENTITY(1,1) PRIMARY KEY,
                temp FLOAT,
                description NVARCHAR(100),
                timestamp DATETIME2
            )
        """)
        conn.commit()

def insert_weather(temp: float, description: str, timestamp: str):
    """
    Infogar en ny väderrad i tabellen 'weather_data'.

    Args:
        temp (float): Temperaturen i Celsius.
        description (str): Väderbeskrivning.
        timestamp (str): ISO8601-format på UTC-tid.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weather_data (temp, description, timestamp) VALUES (?, ?, ?)",
            (temp, description, timestamp)
        )
        conn.commit()
