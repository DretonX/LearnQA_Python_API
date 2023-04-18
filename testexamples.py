import pytest
class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        assert a + b == 14


    def test_check_wrong(self):
        a = 33
        b = 944
        expected_sum = 975
        assert a + b == expected_sum, f"Expected {expected_sum}, got {a + b}"