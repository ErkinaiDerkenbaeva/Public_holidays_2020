from utils import holiday_announcer

def test_holiday_announcer():
    assert list(holiday_announcer('Jun')) == ['Whit Monday']
