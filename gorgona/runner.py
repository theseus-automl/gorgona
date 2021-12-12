import multiprocessing as mp
from pathlib import Path
from typing import List

from gorgona.preprocessor.preprocessor import Preprocessor


class Runner:
    def __init__(
        self,
        config_path: Path,
        num_workers: int = mp.cpu_count() - 1,
    ) -> None:
        self._preprocessor = Preprocessor(config_path)
        self._num_workers = num_workers

    def run(
        self,
        texts: List[str],
    ) -> List[str]:
        pool = mp.Pool(self._num_workers)

        return pool.map(
            self._preprocessor.__call__,
            texts,
        )
