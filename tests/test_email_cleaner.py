import pytest

from gorgona.stages.cleaners import EmailCleaner


@pytest.fixture()
def setup_email_cleaner():
    ec = EmailCleaner(
        '',
        '',
    )

    return ec


@pytest.mark.parametrize('value', [
    'email@here.com',
    'weirder-email@here.and.there.com',
    # 'email@[127.0.0.1]',  TODO
    'example@valid-----hyphens.com',
    'example@valid-with-hyphens.com',
    # 'test@domain.with.idn.tld.उदाहरण.परीक्षा',  TODO
    # 'email@localhost',  TODO
    # 'email@localdomain',  TODO
])
def test_valid_email(value, setup_email_cleaner):
    assert setup_email_cleaner(value) == ''


@pytest.mark.parametrize('value', [
    'abc',
    'abc@',
    'abc@bar',
    'a @x.cz',
    'abc@.com',
    'something@@somewhere.com',
    # 'email@127.0.0.1',  TODO
    'example@invalid-.com',
    'example@-invalid.com',
    'example@inv-.alid-.com',
    'example@inv-.-alid.com',
])
def test_invalid_email(value, setup_email_cleaner):
    assert setup_email_cleaner(value) == value
