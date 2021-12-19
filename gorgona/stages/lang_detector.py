from pathlib import Path
from typing import Optional
from urllib.request import urlretrieve

from fasttext import (
    FastText,
    load_model,
)

from gorgona._paths import _FT_MODEL_PATH
from gorgona.exceptions import (
    InvalidLangDetectionThreshold,
    ModelNotFoundError,
    UnsupportedLanguageError,
)
from gorgona.stages.base.base_stage import BaseStage

_SUPPORTED_LANGS = {
    'af',
    'als',
    'am',
    'an',
    'ar',
    'arz',
    'as',
    'ast',
    'av',
    'az',
    'azb',
    'ba',
    'bar',
    'bcl',
    'be',
    'bg',
    'bh',
    'bn',
    'bo',
    'bpy',
    'br',
    'bs',
    'bxr',
    'ca',
    'cbk',
    'ce',
    'ceb',
    'ckb',
    'co',
    'cs',
    'cv',
    'cy',
    'da',
    'de',
    'diq',
    'dsb',
    'dty',
    'dv',
    'el',
    'eml',
    'en',
    'eo',
    'es',
    'et',
    'eu',
    'fa',
    'fi',
    'fr',
    'frr',
    'fy',
    'ga',
    'gd',
    'gl',
    'gn',
    'gom',
    'gu',
    'gv',
    'he',
    'hi',
    'hif',
    'hr',
    'hsb',
    'ht',
    'hu',
    'hy',
    'ia',
    'id',
    'ie',
    'ilo',
    'io',
    'is',
    'it',
    'ja',
    'jbo',
    'jv',
    'ka',
    'kk',
    'km',
    'kn',
    'ko',
    'krc',
    'ku',
    'kv',
    'kw',
    'ky',
    'la',
    'lb',
    'lez',
    'li',
    'lmo',
    'lo',
    'lrc',
    'lt',
    'lv',
    'mai',
    'mg',
    'mhr',
    'min',
    'mk',
    'ml',
    'mn',
    'mr',
    'mrj',
    'ms',
    'mt',
    'mwl',
    'my',
    'myv',
    'mzn',
    'nah',
    'nap',
    'nds',
    'ne',
    'new',
    'nl',
    'nn',
    'no',
    'oc',
    'or',
    'os',
    'pa',
    'pam',
    'pfl',
    'pl',
    'pms',
    'pnb',
    'ps',
    'pt',
    'qu',
    'rm',
    'ro',
    'ru',
    'rue',
    'sa',
    'sah',
    'sc',
    'scn',
    'sco',
    'sd',
    'sh',
    'si',
    'sk',
    'sl',
    'so',
    'sq',
    'sr',
    'su',
    'sv',
    'sw',
    'ta',
    'te',
    'tg',
    'th',
    'tk',
    'tl',
    'tr',
    'tt',
    'tyv',
    'ug',
    'uk',
    'ur',
    'uz',
    'vec',
    'vep',
    'vi',
    'vls',
    'vo',
    'wa',
    'war',
    'wuu',
    'xal',
    'xmf',
    'yi',
    'yo',
    'yue',
    'zh',
}

FastText.eprint = lambda x: None


class FasttextWrapper:
    def __init__(
        self,
        model_path: Path,
    ) -> None:
        self._model_path = model_path
        self._model = load_model(str(self._model_path))

    def predict(
        self,
        *args,
        **kwargs,
    ) -> str:
        return self._model.predict(
            *args,
            **kwargs,
        )

    def __getstate__(self):
        return {'path': self._model_path}

    def __setstate__(self, state):
        self._model_path = state['path']
        self._model = load_model(str(self._model_path))


class LanguageDetector(BaseStage):
    def __init__(
        self,
        name: str,
        target_lang: str,
        threshold: Optional[float] = None,
        model_path: Optional[Path] = None,
    ) -> None:
        super().__init__(name)

        if target_lang not in _SUPPORTED_LANGS:
            raise UnsupportedLanguageError(
                f'language {target_lang} is not supported.'
                f'Possible languages are {", ".join(sorted(_SUPPORTED_LANGS))}',
            )

        self._target_lang = target_lang

        if threshold is not None:
            if threshold < 0 or threshold > 1:
                raise InvalidLangDetectionThreshold('possible threshold values are from 0 to 1 inclusive')

            self._threshold = threshold
        else:
            self._threshold = 0

        if model_path is None:
            if _FT_MODEL_PATH is None:
                self._download_model()

            self._model = FasttextWrapper(_FT_MODEL_PATH)
        else:
            model_path = Path(model_path)

            if not model_path.exists() or not model_path.is_file():
                raise ModelNotFoundError('language detection model does not exist or is not a file')

            self._model = FasttextWrapper(model_path)

    def __call__(
        self,
        text: str,
    ) -> str:
        pred = self._model.predict(
            text,
            threshold=self._threshold,
            k=1,
        )

        if pred[0]:
            pred = pred[0][0].replace('__label__', '')
        else:
            return ''

        return text if pred == self._target_lang else ''

    @staticmethod
    def _download_model():
        urlretrieve(
            'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin',
            _FT_MODEL_PATH,
        )
