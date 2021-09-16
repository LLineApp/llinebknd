from datetime import date

from django.test import TestCase

from llinebknd.functions.math import compoundInterest, convertYearInterestToMonthInterest
from llinebknd.functions.date_utils import monthsBetween
from llinebknd.functions.math_cpf import isCpfValid


class mathTests(TestCase):
    def test_compoundIterest(self):
        """
        compoundInterest returns future value.
        """
        expected = 5276.856753442005
        found = compoundInterest(
            principalValue=1000, interestRate=0.1, time=12, monthlyDeposit=100)
        self.assertEquals(found, expected)

    def test_convertYearInterestToMonthInterest(self):
        """
        convertYearInterestToMonthInterest returns month interest of 10%.
        """
        expected = 0.2211885503119937
        found = convertYearInterestToMonthInterest(yearInterestRate=10)
        self.assertEquals(found, expected)


class date_utilsTests(TestCase):
    def test_monthsBetween(self):
        """
        monthsBetween returns months between two dates at the same year.
        """
        expected = 6
        found = monthsBetween(startDate=date(2021, 5, 31),
                              endDate=date(2021, 11, 12))
        self.assertEquals(found, expected)

        """
        monthsBetween returns months between two dates at different years.
        """
        expected = 60
        found = monthsBetween(startDate=date(2020, 1, 1),
                              endDate=date(2025, 1, 1))
        self.assertEquals(found, expected)

        """
        monthsBetween returns months between two dates when startDate is bigger than endDate.
        """
        expected = 24
        found = monthsBetween(startDate=date(2021, 1, 1),
                              endDate=date(2019, 1, 1))
        self.assertEquals(found, expected)

        """
        monthsBetween returns months between the same date.
        """
        expected = 0
        found = monthsBetween(startDate=date(2021, 1, 1),
                              endDate=date(2021, 1, 1))
        self.assertEquals(found, expected)


class math_cpfTests(TestCase):
    def test_isCpfValid(self):
        """
        isCpfValid validates a true CPF.
        """
        found = isCpfValid(cpf='19176206831')
        self.assertTrue(found)

        """
        isCpfValid validates a BLANK_LIST CPF.
        """
        found = isCpfValid(cpf='99999999999')
        self.assertFalse(found)

        """
        isCpfValid validates a short CPF.
        """
        found = isCpfValid(cpf='123')
        self.assertFalse(found)

        """
        isCpfValid validates a long CPF.
        """
        found = isCpfValid(cpf='12345678901234')
        self.assertFalse(found)

        """
        isCpfValid validates a false CPF.
        """
        found = isCpfValid(cpf='19176216831')
        self.assertFalse(found)
