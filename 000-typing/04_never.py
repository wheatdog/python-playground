from typing import Never, assert_never, NoReturn

#
# typing.NoReturn
# New in version 3.5.4.
#

def never_call_me(arg: Never) -> NoReturn:
    raise Exception("Should be unreachable")

#
# typing.Never typing.assert_never
# New in version 3.11.
#

def example_1(arg: int | str) -> None:
    #never_call_me(arg)  # type checker error
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _:
            never_call_me(arg)  # ok, arg is of type Never

def example_2(arg: int | str) -> None:
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _ as unreachable:
            # At runtime, this throws an exception when called.
            assert_never(unreachable)


def example_3(arg: int | str | float) -> None:
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        #case float():
        #    print("It's a float")
        case _ as unreachable:
            assert_never(unreachable)