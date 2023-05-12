from typing import Final

# A special typing construct to indicate to type checkers that a name cannot be re-assigned or overridden in a subclass.
# New in version 3.8.

some_value: Final[int] = 5
some_value += 5  # type checker error

class Connection:
    TIMEOUT: Final[int] = 10

class FastConnector(Connection):
    TIMEOUT = 1  # Error reported by type checker
