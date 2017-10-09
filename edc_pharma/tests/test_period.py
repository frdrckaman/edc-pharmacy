import arrow

from datetime import datetime, date

from django.test import TestCase, tag

from ..constants import DAYS, WEEKS, MONTHS
from ..scheduler import Period
from dateutil.relativedelta import relativedelta
from pprint import pprint


class TestPeriod(TestCase):

    def test_of_days(self):
        period = Period(start_datetime=datetime(
            2017, 9, 25), unit=DAYS, duration=1)
        self.assertEqual(period.start_datetime.date(), date(2017, 9, 25))
        self.assertEqual(period.end_datetime.date(), date(2017, 9, 25))

    @tag('1')
    def test_of_days1(self):
        start_datetime = arrow.Arrow.fromdatetime(
            datetime(2017, 8, 24)).datetime
        period = Period(start_datetime=start_datetime, unit=DAYS, duration=2)
        self.assertEqual(period.start_datetime,
                         period.start_datetime)
        self.assertEqual(period.end_datetime,
                         period.start_datetime + relativedelta(days=2))

    @tag('1')
    def test_workdays(self):
        start_datetime = arrow.Arrow.fromdatetime(
            datetime(2017, 8, 24)).datetime
        period = Period(start_datetime=start_datetime, unit=DAYS, duration=10)
        pprint(period.workdays)

    def test_of_months(self):
        period = Period(start_datetime=datetime(
            2017, 8, 24), unit=MONTHS, duration=1)
        self.assertEqual(period.start_datetime.date(),
                         datetime(2017, 8, 24).date())
        self.assertEqual(period.end_datetime.date(),
                         datetime(2017, 9, 25).date())

    def test_of_weeks(self):
        period = Period(start_datetime=datetime(
            2017, 8, 24), unit=WEEKS, duration=1)
        self.assertEqual(period.start_datetime.date(),
                         datetime(2017, 8, 24).date())
        self.assertEqual(period.end_datetime.date(),
                         datetime(2017, 8, 31).date())
