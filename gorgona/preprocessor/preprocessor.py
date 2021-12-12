from inspect import signature
from pathlib import Path
from typing import Generator

from yaml import safe_load

from gorgona.preprocessor.default import Defaults
from gorgona.stages.aliases import ALIASES


class Preprocessor:
    def __init__(
        self,
        config_path: Path,
    ) -> None:
        if not config_path.exists() or not config_path.is_file() or config_path.suffix not in {'.yaml', '.yml'}:
            raise ValueError('config path does not exist or is not a YAML file')

        self._stages = []
        self._default_repl = None
        self._default_join_on = None
        self._stage_num_factory = self._get_stage_number()

        with open(config_path, 'r', encoding='utf-8') as f:
            self._parse_config(safe_load(f))

    def _parse_config(
        self,
        cfg: dict,
    ) -> None:
        if 'defaults' in cfg:
            self._default_repl = cfg['defaults'].get(
                'repl',
                Defaults.repl,
            )
            self._default_join_on = cfg['defaults'].get(
                'join_on',
                Defaults.join_on,
            )

        if 'stages' not in cfg:
            raise ValueError('unable to detect stages section')

        for stage in cfg['stages']:
            cls = stage['type']

            if cls not in ALIASES:
                raise ValueError(f'unknown stage {cls}. Possible stages: {" ".join(ALIASES.keys())}')

            cls = ALIASES[cls]
            del stage['type']

            init_args = set(signature(cls.__init__).parameters.keys())
            kwargs = stage or {}

            if 'repl' in init_args and 'repl' not in kwargs:
                kwargs['repl'] = self._default_repl

            if 'join_on' in init_args and 'join_on' not in kwargs:
                kwargs['join_on'] = self._default_join_on

            if 'name' not in kwargs:
                kwargs['name'] = f'stage {next(self._stage_num_factory)}'

            self._stages.append(cls(**kwargs))

    def __call__(
        self,
        text: str,
        debug: bool = False,
    ) -> str:
        if debug:
            print('GORGONA DEBUG MODE')

        for i, stage in enumerate(self._stages):
            if debug:
                print(f'RUNNING STAGE #{i} - {type(stage)}: {stage.name}')
                print(f'BEFORE: {text}')

            text = stage(text)

            if debug:
                print(f'AFTER: {text}')
                print(f'{"-" * 100}\n')

        return text

    @staticmethod
    def _get_stage_number() -> Generator[int, None, None]:
        i = 0

        while True:
            yield i
            i += 1
