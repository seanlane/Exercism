from datetime import date

card_ref = {
    '1st': 0,
    '2nd': 1,
    '3rd': 2,
    '4th': 3,
    '5th': 4,
    'teenth': 'teenth',
    'last': 'last'
}

day_ref = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

class MeetupDayException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def meetup_day(year, month, day, cardinality):
    card_value = card_ref[cardinality]
    day_value = day_ref[day]

    date_val = date(year, month, 1)
    dow = date_val.weekday()
    date_val = date(year, month, 1 + (day_value - dow) % 7)

    if isinstance(card_value, int):
        count = 0
        while count < card_value:
            try:
                date_val = date(year, month, date_val.day + 7)
            except ValueError:
                raise MeetupDayException
            count += 1
        return date_val

    if card_value == 'teenth':

        while date_val.day < 13:
            try:
                date_val = date(year, month, date_val.day + 7)
            except ValueError:
                raise MeetupDayException
        return date_val

    assert card_value == 'last'
    while True:
        last_date = date_val
        try:
            date_val = date(year, month, date_val.day + 7)
        except ValueError:
            return last_date
    raise MeetupDayException