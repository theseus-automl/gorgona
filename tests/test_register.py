import pytest

from gorgona.stages import (
    BaseStage,
    register,
)
from gorgona.stages.aliases import ALIASES


def test_duplicate_alias():
    with pytest.raises(ValueError):
        @register(alias=list(ALIASES.keys())[0])
        class DummyStage(BaseStage):
            def __init__(self):
                super().__init__('')

            def __call__(
                self,
                text: str,
            ) -> str:
                pass


def test_no_inheritance():
    with pytest.raises(ValueError):
        @register(alias='dummy')
        class DummyStage:
            pass


def test_normal_register():
    @register(alias='dummy')
    class DummyStage(BaseStage):
        def __init__(self):
            super().__init__('')

        def __call__(
            self,
            text: str,
        ) -> str:
            pass

    assert 'dummy' in ALIASES
