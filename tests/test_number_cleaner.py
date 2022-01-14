import pytest

from gorgona.stages.cleaners import NumberCleaner


@pytest.fixture()
def setup_number_cleaner():
    nc = NumberCleaner(
        '',
        '',
    )

    return nc


# no numbers at all
def test_no_numbers(setup_number_cleaner):
    assert setup_number_cleaner('hello, world') == 'hello, world'


# positive integer, single digit
def test_positive_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('1') == ''


def test_left_text_positive_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('hello 1') == 'hello '


def test_right_text_positive_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('1 hello') == ' hello'


def test_both_text_positive_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('hello 1 world') == 'hello  world'


def test_inside_text_positive_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('he1llo') == 'he1llo'


# positive integer, multiple digits
def test_positive_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('1234') == ''


def test_left_text_positive_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('hello 1234') == 'hello '


def test_right_text_positive_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('1234 hello') == ' hello'


def test_both_text_positive_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('hello 1234 world') == 'hello  world'


def test_inside_text_positive_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('he1234llo') == 'he1234llo'


# negative integer, single digit
def test_negative_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('-2') == ''


def test_left_text_negative_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('hello -3') == 'hello '


def test_right_text_negative_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('-4 hello') == ' hello'


def test_both_text_negative_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('hello -7 world') == 'hello  world'


def test_inside_text_negative_integer_single_digit(setup_number_cleaner):
    assert setup_number_cleaner('he-8llo') == 'he-8llo'


# negative integer, multiple digits
def test_negative_integer_multiple(setup_number_cleaner):
    assert setup_number_cleaner('-567') == ''


def test_left_text_negative_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('hello -123') == 'hello '


def test_right_text_negative_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('-789 hello') == ' hello'


def test_both_text_negative_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('hello -1337 world') == 'hello  world'


def test_inside_text_negative_integer_multiple_digits(setup_number_cleaner):
    assert setup_number_cleaner('he-228llo') == 'he-228llo'




