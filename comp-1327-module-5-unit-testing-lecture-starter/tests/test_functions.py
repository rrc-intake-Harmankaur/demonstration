"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: Harman Kaur 
Date: 2025-07-07
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch
from src.functions import greet_name_age

class TestFunctions(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
        # Arrange 
        name = "joe"
        age = 25
        expected = "Hello joe, you are 25 years old!"

        #Act 
        actual = greet_name_age(name,age)

        #Assert 
        self.assertEqual(expected, actual)