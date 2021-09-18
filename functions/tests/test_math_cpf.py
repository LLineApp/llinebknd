from django.test import TestCase
from llinebknd.functions.math_cpf import isCpfValid


class isCpfValidTests(TestCase):
    def test_a_true_CPF(self):
        """
        isCpfValid validates a true CPF.
        """
        found = isCpfValid(cpf='19176206831')
        self.assertTrue(found)

    def test_a_BLANK_LIST_CPF(self):
        """
        isCpfValid validates a BLANK_LIST CPF.
        """
        found = isCpfValid(cpf='99999999999')
        self.assertFalse(found)

    def test_a_shorter_CPF(self):
        """
        isCpfValid validates a shorter CPF.
        """
        found = isCpfValid(cpf='123')
        self.assertFalse(found)

    def test_a_longer_CPF(self):
        """
        isCpfValid validates a longer CPF.
        """
        found = isCpfValid(cpf='12345678901234')
        self.assertFalse(found)

    def test_a_false_CPF(self):
        """
        isCpfValid validates a false CPF.
        """
        found = isCpfValid(cpf='19176216831')
        self.assertFalse(found)
