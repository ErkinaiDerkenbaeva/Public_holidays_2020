from utils import holiday_announcer

def test_holiday_announcer():
    assert holiday_announcer('June') == pd.Series(['Whit Monday'])
