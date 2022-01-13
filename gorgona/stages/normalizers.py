from unicodedata import normalize

from gorgona.stages.base.base_stage import BaseStage
from gorgona.stages.base.replacer import Replacer

_NORMALIZATION_FORMS = {
    'NFC',
    'NFKC',
    'NFD',
    'NFKD',
}


class UnicodeNormalizer(BaseStage):
    def __init__(
        self,
        name: str,
        form: str,
    ) -> None:
        super().__init__(name)

        form = form.upper()

        if form not in _NORMALIZATION_FORMS:
            raise ValueError(f'unknown form {form}. Consider using {", ".join(sorted(_NORMALIZATION_FORMS))}')

        self._form = form

    def __call__(
        self,
        text: str,
    ) -> str:
        return normalize(
            self._form,
            text,
        )


class WhitespaceNormalizer(Replacer):
    def __init__(
        self,
        name: str,
        repl: str = ' ',
    ) -> None:
        super().__init__(
            name,
            r' +',
            repl,
        )


class Lowercaser(BaseStage):
    def __init__(
        self,
        name: str,
    ) -> None:
        super().__init__(name)

    def __call__(
        self,
        text: str,
    ) -> str:
        return text.lower()
