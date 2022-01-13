import pickle
from contextlib import contextmanager
from pathlib import Path
from typing import Type

import pytest

from gorgona.exceptions import UnsupportedLanguageError, InvalidLangDetectionThreshold, ModelNotFoundError
from gorgona.stages.lang_detector import (
    _FT_MODEL_PATH,
    LanguageDetector,
)

_EN_TEXT = """
    I had never seen a house on fire before, so, one evening when I heard fire engines with loud alarm bells rushing 
    past my house. I quickly ran out and, a few streets away, joined a large crowd of people. We could see the fire only
    from a distance because the police would not allow any one near the building on fire.
    What a terrible scene I saw that day! Huge flames of fire were coming out of each floor, and black and thick smoke 
    spread all around. Four fire engines were engaged and the firemen in their uniform were playing the hose on various 
    parts of the building. Then the tall ladders of the fire engine were stretched upwards. Some firemen climbed up with 
    hoses in their hands. The continuous flooding brought the fire under control but the building was completely 
    destroyed.
""".replace('\n', '').strip()


@contextmanager
def not_raises(
    expected_exception: Type[Exception],
) -> None:
    try:
        yield
    except expected_exception as error:
        raise AssertionError(f'raised exception {error} when it should not')
    except Exception as error:
        raise AssertionError(f'raised an unexpected exception {error}')


def test_unsupported_language():
    with pytest.raises(UnsupportedLanguageError):
        LanguageDetector(
            '',
            'dummy lang',
        )


def test_too_small_threshold():
    with pytest.raises(InvalidLangDetectionThreshold):
        LanguageDetector(
            '',
            'en',
            threshold=-1,
        )


def test_too_big_threshold():
    with pytest.raises(InvalidLangDetectionThreshold):
        LanguageDetector(
            '',
            'en',
            threshold=10,
        )


def test_model_path_does_not_exist():
    with pytest.raises(ModelNotFoundError):
        LanguageDetector(
            '',
            'en',
            model_path=Path(__file__).parent / 'dummy',
        )


def test_model_path_is_directory():
    with pytest.raises(ModelNotFoundError):
        LanguageDetector(
            '',
            'en',
            model_path=Path(__file__).parent,
        )


def test_model_download():
    _FT_MODEL_PATH.unlink(missing_ok=True)

    assert not _FT_MODEL_PATH.exists()

    with not_raises(Exception):
        LanguageDetector(
            '',
            'en',
        )

    assert _FT_MODEL_PATH.exists()


def test_normal_detection():
    detector = LanguageDetector(
        '',
        'en',
        threshold=0.7,
    )

    assert detector(_EN_TEXT) == _EN_TEXT


def test_non_target_lang():
    detector = LanguageDetector(
        '',
        'ru',
    )

    assert detector(_EN_TEXT) == ''


def test_pickle():
    detector = LanguageDetector(
        '',
        'en',
    )
    path = Path(__file__).parent / 'detector.pkl'

    with open(path, 'wb') as f:
        pickle.dump(
            detector,
            f,
        )

    with open(path, 'rb') as f:
        detector = pickle.load(f)

    path.unlink(missing_ok=True)

    assert detector.name == ''
    assert detector._target_lang == 'en'
