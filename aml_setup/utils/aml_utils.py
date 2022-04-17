from typing import List

def join_string_list(s: List[str],
                     joiner: str = " ") -> str:
    """This function concatenates a list of strings to a single string variable.
    The joiner string between each element is configurable and a single space by default.

    Args:
        s (List[str]): A List of string elements.
        joiner (str, optional): The joiner string. Defaults to " ".

    Returns:
        str: A single string made up of concatenated elements of the input list of strings.
    """
    string_full = joiner.join(s)
    return string_full
