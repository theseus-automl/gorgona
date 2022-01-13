import pytest

from gorgona.stages.cleaners import MentionCleaner


@pytest.fixture()
def setup_mention_cleaner():
    mc = MentionCleaner(
        '',
        '',
    )

    return mc


def test_no_mentions(setup_mention_cleaner):
    assert setup_mention_cleaner('hello, world!') == 'hello, world!'


def test_single_mention(setup_mention_cleaner):
    assert setup_mention_cleaner('hello @mention') == 'hello '


def test_multiple_mentions(setup_mention_cleaner):
    assert setup_mention_cleaner('hello @mention and @mention2 and @world') == 'hello  and  and '


def test_single_at(setup_mention_cleaner):
    assert setup_mention_cleaner('hello @') == 'hello @'


def test_multiple_at(setup_mention_cleaner):
    assert setup_mention_cleaner('hello @ @ and @') == 'hello @ @ and @'


def test_mention_from_whitespaces(setup_mention_cleaner):
    assert setup_mention_cleaner('@   ') == '@   '


def test_email(setup_mention_cleaner):
    assert setup_mention_cleaner('johndoe@example.com') == 'johndoe@example.com'
