from typing import (
    Callable,
    Type,
)

from gorgona.stages import BaseStage
from gorgona.stages.aliases import ALIASES


def register(
    alias: str,
) -> Callable:
    def wrapper(
        cls: Type,
    ) -> Type:
        if alias in ALIASES:
            raise ValueError('duplicate aliases are not allowed')

        if not issubclass(cls, BaseStage):
            raise ValueError('you must inherit from BaseStage or it\'s subclasses')

        ALIASES[alias] = cls

        return cls

    return wrapper
