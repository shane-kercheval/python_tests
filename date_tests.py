import unittest
import datetime
import calendar


class DateTests(unittest.TestCase):

    def test_dates(self):
        date = datetime.datetime(2008, 11, 22, 19, 53, 42)
        assert str(date) == "2008-11-22 19:53:42"
        strftime = date.strftime('%Y-%m-%d')
        assert strftime == "2008-11-22"

        string_date = '1/27/2016'
        converted = datetime.datetime.strptime(string_date, '%m/%d/%Y')
        assert converted.month == 1
        assert converted.day == 27
        assert converted.year == 2016

        string_date = '01/27/2016'
        converted = datetime.datetime.strptime(string_date, '%m/%d/%Y')
        assert converted.month == 1
        assert converted.day == 27
        assert converted.year == 2016

        string_date = '2015-02'
        converted = datetime.datetime.strptime(string_date, '%Y-%m')
        assert converted.month == 2
        assert converted.day == 1
        assert converted.year == 2015


        string_date = '03/21/2016'
        end_date = datetime.datetime.strptime(string_date, '%m/%d/%Y')
        difference = datetime.datetime.today() - end_date
        assert difference.days >= 1

        #assert date_is_before_today(datetime.datetime(2015,month=3, day=21))
        #assert date_is_before_today(datetime.datetime(2016,month=3, day=21))
        #assert date_is_before_today(datetime.datetime(2016,month=3, day=22)) is False
        #assert date_is_before_today(datetime.datetime(2016,month=3, day=23)) is False

    def test_last_day_of_month(self):
        string_date = '2015-02'
        start_date = datetime.datetime.strptime(string_date, '%Y-%m')
        assert start_date.month == 2
        assert start_date.day == 1
        assert start_date.year == 2015

        last_day = calendar.monthrange(start_date.year, start_date.month)[1]
        assert last_day == 28
        end_date = datetime.datetime(year=start_date.year, month=start_date.month, day=last_day)
        assert end_date.month == 2
        assert end_date.day == 28
        assert end_date.year == 2015

def date_is_before_today(date):
    difference = datetime.datetime.today() - date
    return difference.days >= 1

if __name__ == '__main__':
    unittest.main()
