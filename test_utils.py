import pandas as pd
from utils import holiday_announcer

def test_holiday_announcer():
    assert holiday_announcer('Jun') == pd.Series(['Whit Monday'])
