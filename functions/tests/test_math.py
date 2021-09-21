from django.test import TestCase
from llinebknd.functions.math import compoundInterest, convertYearInterestToMonthInterest


class compoundIterestTests(TestCase):
    def test_return_of_future_value(self):
        """
        compoundInterest returns future value.
        """
        expected = 5276.856753442005
        found = compoundInterest(
            principalValue=1000, interestRate=0.1, time=12, monthlyDeposit=100)
        self.assertEquals(found, expected)


class convertYearInterestToMonthInterestTests(TestCase):
    def test_return_of_month_interest(self):
        """
        convertYearInterestToMonthInterest returns month interest of 10%.
        """
        expected = 0.2211885503119937
        found = convertYearInterestToMonthInterest(yearInterestRate=10)
        self.assertEquals(found, expected)
