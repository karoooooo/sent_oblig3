from src.leap_year import is_leap_year

years_that_are_leap_years = [2000, 2016, 2020]
years_that_are_not_leap_years = [2001, 1700, 1800, 1900, 2100]

test_year_1 = years_that_are_leap_years[0]
test_year_2 = years_that_are_not_leap_years[0]


def test_year_is_divisible_by_4():
    division = is_leap_year(test_year_2) % 4
    assert division, f'\n{test_year_2} was not divisible by 4'


def test_year_is_not_divisible_by_100():
    division = is_leap_year(test_year_2) % 100
    assert not division, f'\n{test_year_2} was divisible by 100'


def test_year_is_divisible_by_400():
    division = is_leap_year(test_year_2) % 400
    assert division, f'\n{test_year_2} was not divisible by 400'


def test_year_is_leap_year():
    is_it_leap_year = is_leap_year(test_year_2)
    assert is_it_leap_year, f'\n{test_year_2} is not a leap year'


def test_year_is_not_a_leap_year():
    is_it_leap_year = is_leap_year(test_year_2)
    assert not is_it_leap_year, f'\n{test_year_2} is in fact a leap year...'

