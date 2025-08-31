from connection import get_connection

def test_connection():
    """
    Testar att anslutningen till databasen fungerar.
    """
    conn = get_connection()
    assert conn is not None
    conn.close()
