from typing import Any, Literal

# New in version 3.8.

def validate_simple(data: Any) -> Literal[True]:  # always returns True
    return True

MODE = Literal['r', 'rb', 'w', 'wb']
def open_helper(file: str, mode: MODE) -> str:
    return "test"

open_helper("something", "r")
open_helper("something", "typo")