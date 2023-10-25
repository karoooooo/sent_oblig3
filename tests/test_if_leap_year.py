import pytest

from src.leap_year import is_leap_year

years_that_are_leap_years = [2000, 2016, 2020]
years_that_are_not_leap_years = [2001, 1700, 1800, 1900, 2100]


@pytest.fixture(params=[1, 2])
def test_year_choice(request):
    return request.param


@pytest.fixture
def test_year(test_year_choice):
    if test_year_choice == 1:
        return years_that_are_leap_years[2]
    elif test_year_choice == 2:
        return years_that_are_not_leap_years[3]


def test_year_is_divisible_by_4(test_year):
    division = is_leap_year(test_year) % 4
    assert division, f'\n{test_year} was not divisible by 4'


def test_year_is_not_divisible_by_100(test_year):
    division = is_leap_year(test_year) % 100
    assert not division == 0, f'\n{test_year} was divisible by 100'


def test_year_is_divisible_by_400(test_year):
    division = is_leap_year(test_year) % 400
    assert division, f'\n{test_year} was not divisible by 400'


def test_year_is_leap_year(test_year):
    is_it_leap_year = is_leap_year(test_year)
    assert is_it_leap_year, f'\n{test_year} is not a leap year'


def test_year_is_not_a_leap_year(test_year):
    is_it_leap_year = is_leap_year(test_year)
    assert not is_it_leap_year, f'\n{test_year} is in fact a leap year...'
