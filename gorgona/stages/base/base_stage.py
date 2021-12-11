import re
from abc import (
    ABC,
    abstractmethod,
)
from typing import Optional


class BaseStage(ABC):
    def __init__(
        self,
        name: str,
        regexp: Optional[str] = None,
    ) -> None:
        self._name = name

        if regexp is not None:
            self._regexp = re.compile(regexp)

    @abstractmethod
    def __call__(
        self,
        text: str,
        *args,
        **kwargs,
    ) -> None:
        pass
