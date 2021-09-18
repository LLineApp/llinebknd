from datetime import date
from django.test import TestCase
from llinebknd.functions.date_utils import monthsBetween


class monthsBetweenTests(TestCase):
    def test_months_between_two_dates_at_the_same_year(self):
        """
        monthsBetween returns months between two dates at the same year.
        """
        expected = 6
        found = monthsBetween(startDate=date(2021, 5, 31),
                              endDate=date(2021, 11, 12))
        self.assertEquals(found, expected)

    def test_months_between_two_dates_at_different_years(self):
        """
        monthsBetween returns months between two dates at different years.
        """
        expected = 60
        found = monthsBetween(startDate=date(2020, 1, 1),
                              endDate=date(2025, 1, 1))
        self.assertEquals(found, expected)

    def test_months_between_two_dates_when_startDate_is_bigger_than_endDate(self):
        """
        monthsBetween returns months between two dates when startDate is bigger than endDate.
        """
        expected = 24
        found = monthsBetween(startDate=date(2021, 1, 1),
                              endDate=date(2019, 1, 1))
        self.assertEquals(found, expected)

    def test_months_between_the_same_date(self):
        """
        monthsBetween returns months between the same date.
        """
        expected = 0
        found = monthsBetween(startDate=date(2021, 1, 1),
                              endDate=date(2021, 1, 1))
        self.assertEquals(found, expected)
