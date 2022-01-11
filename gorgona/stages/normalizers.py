from unicodedata import normalize

from gorgona.stages.base.base_stage import BaseStage
from gorgona.stages.base.replacer import Replacer


class UnicodeNormalizer(BaseStage):
    def __init__(
        self,
        name: str,
        form: str,
    ) -> None:
        super().__init__(name)
        self._form = form.upper()

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
