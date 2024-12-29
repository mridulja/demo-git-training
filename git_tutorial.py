"""Module for demonstrating basic Python functionality and Git tutorial examples."""

print("Hello, World!")
print("hello")


def summation(a: int, b: int) -> int:
    """Calculate the sum of two numbers.

    Args:
        a: First number to add
        b: Second number to add

    Returns:
        The sum of a and b
    """
    return a + b


RESULT = summation(1, 2)
print(RESULT)

NAME: str = "Peter"
AGE: int = 20

print(NAME, AGE)
