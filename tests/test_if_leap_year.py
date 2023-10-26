import pytest
from src.leap_year import is_leap_year

# Years marked with True are leap years
test_leap_year = [
    (1912, True),
    (2000, True),
    (2016, True),
    (2020, True),
    (2152, True),
]

test_not_leap_year = [
    (2001, False),
    (1700, False),
    (1800, False),
    (1900, False),
    (2100, False),
]


# A leap year is divisible by 4 but not by 100
@pytest.mark.parametrize("year, expected_result", test_leap_year)
def test_year_is_divisible_by_4_but_not_100(year, expected_result):
    result = (is_leap_year(year) % 4) and (is_leap_year(year) % 100 != 0)
    assert result == expected_result, f'\n{year} is not divisible by 4 and is divisible by 100.'


# Therefore a leap year is divisible by 400
@pytest.mark.parametrize("year, expected_result", test_leap_year)
def test_year_is_divisible_by_400(year, expected_result):
    result = (is_leap_year(year) % 400)
    assert result == expected_result, f'\n{year} is divisible by 400.'


# A non-leap year is not divisible by 4
@pytest.mark.parametrize("year, expected_result", test_not_leap_year)
def test_year_is_not_divisible_by_4(year, expected_result):
    result = is_leap_year(year) % 4
    assert result == expected_result, f'\n{year} is not divisible by 4.'


# A year is not a leap year if it is divisble by 100 but not by 400
@pytest.mark.parametrize("year, expected_result", test_not_leap_year)
def test_year_is_not_divisible_by_100_but_not_400(year, expected_result):
    result = (is_leap_year(year) % 100 != 0) or (is_leap_year(year) % 400 == 0)
    assert not result == expected_result, f'\n{year} is not divisible by 100 '


# General tests if years are leap years
@pytest.mark.parametrize("year, expected_result", test_leap_year)
def test_year_is_leap_year(year, expected_result):
    result = is_leap_year(year)
    assert result == expected_result, f'\n{year} is in fact a leap year...'


@pytest.mark.parametrize("year, expected_result", test_not_leap_year)
def test_year_is_leap_year(year, expected_result):
    result = is_leap_year(year)
    assert result == expected_result, f'\n{year} is in fact a leap year...'
