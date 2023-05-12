#
# https://peps.python.org/pep-0585/
# https://docs.python.org/3/library/typing.html#generic-concrete-collections
#

# from __future__ import annotations  # for backward compatibility before 3.9

def foo(haystack: dict[str, list[int]]) -> None:
    pass


# Deprecated since version 3.9
from typing import Dict, List

def bar(haystack: Dict[str, List[int]]) -> None:
    pass
