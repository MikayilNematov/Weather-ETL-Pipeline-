from main import fetch_weather

def test_fetch_weather_structure():
    """
    Testar att fetch_weather returnerar korrekt struktur.
    """
    temp, weather, timestamp = fetch_weather()

    assert isinstance(temp, (float, int))
    assert isinstance(weather, str)
    assert isinstance(timestamp, str)

def test_fetch_weather_temp_range():
    """
    Testar att temperaturen ligger inom rimligt intervall.
    """
    temp, _, _ = fetch_weather()
    assert -50 < temp < 60, "Orimlig temperatur returnerades"
