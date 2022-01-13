import pytest

from gorgona.stages.cleaners import PhoneNumberCleaner


@pytest.fixture()
def setup_phone_number_cleaner():
    pnc = PhoneNumberCleaner(
        '',
        '',
    )

    return pnc


def test_no_phone_numbers(setup_phone_number_cleaner):
    assert setup_phone_number_cleaner('hello, world') == 'hello, world'


def test_old(setup_phone_number_cleaner):
    assert setup_phone_number_cleaner('346-02-31') == ''


def test_old_with_area_code(setup_phone_number_cleaner):
    assert setup_phone_number_cleaner('(383) 346-02-31') == ''


def test_conventional(setup_phone_number_cleaner):
    assert setup_phone_number_cleaner('8 (913) 456-78-90') == ''


def test_microsoft(setup_phone_number_cleaner):
    assert setup_phone_number_cleaner('+7 (913) 456-78-90') == ''


def test_conventional_mandatory_area_code(setup_phone_number_cleaner):
    assert setup_phone_number_cleaner('8 913 456-78-90') == ''


def test_e123_international(setup_phone_number_cleaner):
    assert setup_phone_number_cleaner('+7 913 456-78-90') == ''
