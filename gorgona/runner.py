import multiprocessing as mp
from pathlib import Path
from typing import (
    List,
    Optional,
)

import ray

from gorgona.preprocessor.preprocessor import Preprocessor

_AVAILABLE_BACKENDS = {
    'ray',
    'mp',
}


class Runner:
    def __init__(
        self,
        config_path: Path,
        num_workers: int = mp.cpu_count() - 1,
        backend: str = 'mp',
        ray_cluster_address: Optional[str] = None,
    ) -> None:
        self._preprocessor = Preprocessor(config_path)
        self._num_workers = num_workers

        if backend not in _AVAILABLE_BACKENDS:
            raise ValueError(f'unknown backend {backend}. Possible backends are {", ".join(_AVAILABLE_BACKENDS)}')

        self._backend = backend

        if self._backend == 'ray':
            if ray_cluster_address is not None:
                ray.init(address=ray_cluster_address)
            else:
                ray.init()

    def run(
        self,
        texts: List[str],
    ) -> List[str]:
        if self._backend == 'mp':
            pool = mp.Pool(self._num_workers)

            return pool.map(
                self._preprocessor.__call__,
                texts,
            )
        elif self._backend == 'ray':
            return ray.get([self._ray_run.remote(self, text) for text in texts])

    @ray.remote
    def _ray_run(
        self,
        text: str,
    ) -> str:
        return self._preprocessor(text)

    def _mp_run(
        self,
        texts: List[str],
    ) -> List[str]:
        pool = mp.Pool(self._num_workers)

        return pool.map(
            self._preprocessor.__call__,
            texts,
        )
