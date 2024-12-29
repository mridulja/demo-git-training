"""Module for demonstrating basic Python functionality and Git tutorial examples."""

from typing import Final


def add_numbers(first_num: int, second_num: int) -> int:
    """Calculate the sum of two numbers.

    Args:
        first_num: First number to add
        second_num: Second number to add

    Returns:
        int: The sum of the two input numbers
    """
    return first_num + second_num


def main() -> None:
    """Run the main program logic."""
    # Constants should be defined at module level
    NAME: Final[str] = "Peter"
    AGE: Final[int] = 20

    # Group related operations together
    print("Hello, World!")
    
    result = add_numbers(1, 2)
    print(f"Sum result: {result}")
    
    print(f"Name: {NAME}, Age: {AGE}")


if __name__ == "__main__":
    main()
