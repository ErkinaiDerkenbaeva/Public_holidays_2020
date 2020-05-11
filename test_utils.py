from utils import holiday_announcer

def test_holiday_announcer(month):
         assert print(holiday_announcer(month) == holiday_announcer('Jun'))



test_holiday_announcer("Jun") # should work
test_holiday_announcer("Apr") # should return false