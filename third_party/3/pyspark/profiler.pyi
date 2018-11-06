# Stubs for pyspark.profiler (Python 3.5)
#

from typing import Any, Callable, List,Optional, Tuple, Type

import pstats

from pyspark.accumulators import AccumulatorParam
from pyspark.context import SparkContext

class ProfilerCollector:
    profiler_cls = ...  # type: Type[Profiler]
    profile_dump_path = ...  # type: Optional[str]
    profilers = ...  # type: List[Tuple[int, Profiler, bool]]
    def __init__(self, profiler_cls: Type[Profiler], dump_path: Optional[str] = ...) -> None: ...
    def new_profiler(self, ctx: SparkContext) -> Profiler: ...
    def add_profiler(self, id: int, profiler: Profiler) -> None: ...
    def dump_profiles(self, path: str) -> None: ...
    def show_profiles(self) -> None: ...

class Profiler:
    def __init__(self, ctx: SparkContext) -> None: ...
    def profile(self, func: Callable[[], Any]) -> None: ...
    def stats(self) -> pstats.Stats: ...
    def show(self, id: int) -> None: ...
    def dump(self, id: int, path: str) -> None: ...

class PStatsParam(AccumulatorParam):
    @staticmethod
    def zero(value: pstats.Stats) -> None: ...
    @staticmethod
    def addInPlace(value1: Optional[pstats.Stats], value2: Optional[pstats.Stats]) -> Optional[pstats.Stats]: ...

class BasicProfiler(Profiler):
    def __init__(self, ctx: SparkContext) -> None: ...
    def profile(self, func: Callable[[], Any]) -> None: ...
    def stats(self) -> pstats.Stats: ...
